# Mission Assurance Workbench: offline prototype

This prototype evaluates **hand-authored synthetic action traces** against three explicit local rules. It does not call an AI model, execute tools, probe services, or claim that a deployed defense works.

## Run

Python 3.9+ and its standard library are sufficient. From the repository root:

```bash
python scripts/evidence_workbench.py fixtures/mission-cases.json
python scripts/evidence_workbench.py fixtures/mission-cases.json --format json
python -m unittest discover -s tests -v
```

Optional: redirect either report to a local file. Successful evaluation exits 0 even when a fixture contains policy violations; 0 means the report was computed, not that a system passed a security assessment. Malformed input exits 2.

## What is connected

Each fixture declares a versioned local policy, control IDs, property descriptions, scenario IDs, language, a proposed action, and supplied baseline/guarded traces. Reports retain those links and a SHA-256 digest of the canonical input. This supports reproducible comparisons of the same input, not provenance authentication.

| Local experimental rule | Checked behavior | Important limitation |
| --- | --- | --- |
| LOCAL-ALLOWLIST | Requested tool belongs to the declared allowlist | Does not validate arguments, tool behavior, or the identity provider |
| LOCAL-TENANT | Actor and resource tenant fields match | Assumes those fields came from authoritative state |
| LOCAL-PROVENANCE | Every claim reference appears in the supplied evidence manifest | Does not establish that a source is genuine or that it supports the claim |

These IDs are local, not AIDEFEND identifiers. No framework mapping or endorsement is asserted. External catalog relevance should be reviewed separately from a result about observed behavior.

## Example cases

The fixture contains five scenarios, each with a baseline and guarded trace: two permitted operations, an unapproved tool request, a cross-tenant request, and an untraceable citation. Descriptions include English and French. This is bilingual fixture text, not a multilingual model benchmark.

The intentionally permissive baseline contains three policy violations. The guarded fixture contains three denials and two completed permitted tasks. These outcomes were authored into the fixture to demonstrate the evaluator; they are not measurements of a baseline agent versus a defended agent.

## Interpret outcomes carefully

| Outcome | Meaning |
| --- | --- |
| task_complete | Allowed by the local policy and reported completed |
| denied | Forbidden by the policy and denied in the trace |
| policy_violation | Forbidden by the policy but allowed in the trace, regardless of completion |
| overblocked | Permitted by the policy but denied in the trace |
| incomplete | Permitted and allowed, but not completed |
| unknown | The trace cannot establish an action decision |

There is deliberately no composite security percentage. Denying every request would produce overblocking, not useful success. A human still needs to judge whether the policy expresses the mission's real requirements and whether trace collection is trustworthy.

## Extend toward a real experiment

1. Freeze a policy and scenario revision before collecting outcomes.
2. Build a separately reviewed adapter that records actual tool decisions and completion evidence from an isolated system.
3. Preserve the raw trace and collector version; do not relabel it as synthetic input to this evaluator.
4. Introduce a separately versioned observed-trace schema and evaluate data authenticity, privacy, and missingness.
5. Run paired baseline/defended experiments and report denominators, uncertainty, repeatability, false denials, and execution limits.

The current strict schema accepts only synthetic fixtures to keep that boundary explicit. JSON unknown fields, duplicate keys/IDs, malformed types, unsupported modes, and contradictory completion assertions are rejected. The validator does not impose a size limit; use trusted local files, not an exposed network service.
