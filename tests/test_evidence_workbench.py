import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('workbench', ROOT / 'scripts/evidence_workbench.py')
wb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wb)


class WorkbenchTests(unittest.TestCase):
    def setUp(self):
        self.data = wb.load_json(ROOT / 'fixtures/mission-cases.json')

    def test_fixture_outcomes_and_no_security_score(self):
        report = wb.evaluate(self.data)
        self.assertEqual(report['summary']['baseline']['policy_violation'], 3)
        self.assertEqual(report['summary']['baseline']['task_complete'], 2)
        self.assertEqual(report['summary']['guarded']['denied'], 3)
        self.assertEqual(report['summary']['guarded']['task_complete'], 2)
        self.assertNotIn('security_score', report)

    def test_all_failures_retained(self):
        request = self.data['scenarios'][0]['request']
        request.update(tool='shell', resource_tenant='other', claim_sources=['missing'])
        decision, failures = wb.decide(request, self.data['policy'])
        self.assertEqual(decision, 'deny')
        self.assertEqual(set(failures), {'LOCAL-ALLOWLIST', 'LOCAL-TENANT', 'LOCAL-PROVENANCE'})

    def test_unknown_is_not_denied_or_complete(self):
        trace = self.data['scenarios'][0]['traces'][1]
        trace.update(decision='unknown', task_completed=False)
        report = wb.evaluate(self.data)
        self.assertEqual(report['results'][1]['outcome'], 'unknown')

    def test_deny_all_is_overblocking(self):
        self.data['scenarios'][0]['traces'][1].update(decision='deny', task_completed=False)
        self.assertEqual(wb.evaluate(self.data)['results'][1]['outcome'], 'overblocked')

    def test_allowed_but_unfinished_is_not_success(self):
        self.data['scenarios'][0]['traces'][1]['task_completed'] = False
        self.assertEqual(wb.evaluate(self.data)['results'][1]['outcome'], 'incomplete')

    def test_canonical_hash_order_invariance_and_content_sensitivity(self):
        original = wb.evaluate(self.data)['fixture_sha256']
        reordered = {key:self.data[key] for key in reversed(list(self.data))}
        self.assertEqual(original, wb.evaluate(reordered)['fixture_sha256'])
        self.data['scenarios'][0]['description'] += ' revision'
        self.assertNotEqual(original, wb.evaluate(self.data)['fixture_sha256'])

    def test_invalid_inputs(self):
        mutations = [lambda d:d.update(schema_version=True),
                     lambda d:d['policy'].update(version='unsupported'),
                     lambda d:d.update(kind='production'),
                     lambda d:d.update(extra='field'),
                     lambda d:d['scenarios'].append(copy.deepcopy(d['scenarios'][0])),
                     lambda d:d['scenarios'][0]['request'].update(claim_sources=[]),
                     lambda d:d['scenarios'][0]['request'].update(evidence_refs='E-01'),
                     lambda d:d['scenarios'][0]['traces'][0].update(task_completed='true'),
                     lambda d:d['scenarios'][0]['traces'][0].update(decision='deny'),
                     lambda d:d['policy']['controls'][0].update(origin='official'),
                     lambda d:d['policy'].update(allowed_tools=['read_evidence','read_evidence'])]
        for mutate in mutations:
            with self.subTest(mutation=mutate):
                data=copy.deepcopy(self.data)
                mutate(data)
                with self.assertRaises(wb.ValidationError):
                    wb.evaluate(data)

    def test_duplicate_json_keys_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'bad.json'
            path.write_text('{"x":1,"x":2}')
            with self.assertRaises(wb.ValidationError):
                wb.load_json(path)

    def test_markdown_escapes_cell_injection(self):
        self.data['scenarios'][0]['id'] = 'S|X\nnew<script>'
        output = wb.markdown(wb.evaluate(self.data))
        self.assertIn('S\\|X new', output)
        self.assertNotIn('<script>', output)

    def test_cli_json_and_invalid_exit(self):
        command=[sys.executable,str(ROOT/'scripts/evidence_workbench.py')]
        result=subprocess.run(command+[str(ROOT/'fixtures/mission-cases.json'),'--format','json'],capture_output=True,text=True)
        self.assertEqual(result.returncode,0)
        self.assertEqual(json.loads(result.stdout)['evidence_kind'],'synthetic_trace_consistency')
        result=subprocess.run(command+['/nonexistent/fixture.json'],capture_output=True,text=True)
        self.assertEqual(result.returncode,2)
        self.assertIn('Invalid fixture:',result.stderr)


if __name__ == '__main__':
    unittest.main()
