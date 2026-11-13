# StephSec Research
### Cybersecurity assurance • Cyberwarfare • Cybercrime • Intelligence

The public research workspace of **Stéphane Ikoué**: research questions, executable demonstrations, study protocols, and source-grounded analysis connecting cybersecurity to national security.

[StephSec](https://stephsec.com) · [Research agenda](research/agenda.md) · [Current landscape](research/landscape-2026-11.md) · [Platform direction](platform/README.md)

## Featured work: Mission Assurance Workbench

**Can an AI-assisted security workflow stay useful, authorized, and evidentially defensible when permissions, context, or sources change?**

The proposed workbench connects a defense reference to a local requirement, a scenario, an observed trace, and a reviewed claim. Its first implementation is an offline evaluator for hand-authored synthetic traces. It distinguishes permitted completion, correct denial, policy violations, overblocking, incomplete work, and unknown outcomes.

```bash
python scripts/evidence_workbench.py fixtures/mission-cases.json
python scripts/evidence_workbench.py fixtures/mission-cases.json --format json
python -m unittest discover -s tests -v
```

Python 3.9+; no API key, network call, or external package is required. Read the [quickstart and outcome definitions](examples/workbench-quickstart.md).

The fixture includes English and French descriptions. This demonstrates an evidence-reporting mechanism; it is **not an AI evaluation, measured defensive improvement, or multilingual benchmark**.

## Read the research

| Resource | What it contributes | Status |
| --- | --- | --- |
| [November 2026 landscape](research/landscape-2026-11.md) | AIDEFEND, evaluation tools, current institutional guidance, and a specific research opportunity | Scoped source synthesis |
| [Mission Assurance Workbench](platform/README.md) | Architecture, integration boundary, research use cases, and measurable milestones | Platform concept; offline prototype exists |
| [Agent-assisted evidence protocol](protocols/agent-assurance-evaluation.md) | Hypotheses, comparison conditions, outcomes, confounds, and publication limits | Proposed experiment |
| [Potential collaboration with Edward Lee](collaboration/lee-proposal.md) | A focused contribution and discussion plan grounded in AIDEFEND's public interface | Proposal only; no outreach or agreement |
| [Assurance evidence review](protocols/assurance-evidence-review.md) | Document-review inclusion rules and claim–evidence analysis plan | Proposed study |
| [Source notes](docs/source-notes.md) | Verified upstream identity, version, licensing boundaries, and source limitations | Inspection record |

## Six research interests, one coherent direction

| Area | Research direction |
| --- | --- |
| Cybersecurity assurance | Trace security claims to evidence and distinguish tested behavior from unsupported confidence |
| Cyberwarfare | Study authorization, uncertainty, and civilian-service continuity in defensive exercises |
| Cyber military selective service | Investigate cyber workforce readiness, demonstrated competencies, governance, and safeguards |
| Cybercrime and international cooperation | Examine evidence handoffs, provenance, and cross-organization coordination |
| Botnets in African contexts | Study measurement coverage, regional context, language, and defensive triage |
| Intelligence and national security | Separate observations, source dependencies, alternative explanations, and judgments |

The [research agenda](research/agenda.md) develops each area. These are interests and study directions, not completed findings or endorsements of a policy.

## Repository boundaries

| Repository | Owns |
| --- | --- |
| **stephsec-research** | Research questions, source synthesis, protocols, experimental evidence, and interpretation |
| [security-modeling](https://github.com/secsar/security-modeling) | Policy specifications, security properties, and executable model examples |
| [threat-modeling](https://github.com/secsar/threat-modeling) | Threat scenarios, attack paths, prioritization, and treatment analysis |

AIDEFEND is an independently maintained external reference, not a StephSec product or an established partner. Detailed upstream attribution and intended integration appear in [source notes](docs/source-notes.md).

## Research materials and limits

Use the [research method](docs/research-method.md), [note template](templates/research-note.md), and [source register](templates/source-register.csv). Proposed studies do not become findings until data are collected and analyzed under a documented method.

No live-system assessment, empirical model benchmark, peer-reviewed publication, or formal proof is claimed in this release. Public source analysis and synthetic software tests have different evidentiary limits.

Contributions follow [publication standards](docs/publication-standards.md) and [review guidance](CONTRIBUTING.md).
