# From AI defense guidance to mission assurance

**Review date:** 2026-11-13 · **Status:** scoped public-source synthesis and proposed research direction  
**Method:** inspected the primary project documentation and institutional publications linked below. This is a targeted landscape review, not an exhaustive systematic review or a vendor ranking.

## Opportunity within the broader research program

A promising direction for the AI-assurance portion of StephSec research is to investigate **whether an AI-assisted workflow remains useful, authorized, and evidentially defensible when its context, permissions, or dependencies change**. An additional control catalog would overlap substantially with existing projects. A focused assurance workbench can instead connect controls to observations and make unsupported conclusions visible.

That opportunity is an inference from the reviewed material, not a claim that nobody else is working on assurance. The proposed contribution needs to be evaluated against existing benchmarks and products before making novelty claims.

## What exists now

| Source inspected | Observed contribution | Implication for StephSec |
| --- | --- | --- |
| [AIDEFEND](https://github.com/edward-playground/aidefense-framework), source version 1.20261101 | Defensive guidance, mappings, and a versioned integration export | Reuse references and provenance; do not rebuild a second catalog |
| [AIDEFEND MCP](https://github.com/edward-playground/aidefend-mcp) | Local semantic retrieval and MCP/REST access to indexed framework content | Retrieval can assist selection; it is not evidence that a control works in a deployment |
| [AIDEFEND Discovery](https://github.com/minh-armadin/aidefend-discovery) | Existing downstream workbench for public signals, candidate gaps, and human review | Signal ingestion and gap discovery alone would not differentiate this proposal |
| [AgentDojo](https://github.com/ethz-spylab/agentdojo) | Environment for evaluating prompt-injection attacks and defenses for tool-using agents | Use as a comparator or adapter target; do not relabel a scenario suite as a novel benchmark |
| [ControlArena](https://github.com/UKGovernmentBEIS/control-arena) | Settings and protocols for AI control experiments | Learn from experiment structure and controlled comparisons |
| [garak](https://github.com/NVIDIA/garak) | LLM vulnerability probing | Model probing is complementary to workflow-level policy and evidence checks |

The assessed AIDEFEND repository was active, not archived, and exposed main commit `0508e69287ed5ad44f9b7cc9a047b381a181290d` at inspection. Its [integration manifest](https://github.com/edward-playground/aidefense-framework/blob/0508e69287ed5ad44f9b7cc9a047b381a181290d/data/integration/manifest.json) records checksums and distinguishes actionable controls from navigation families. A mapping expresses relevance; it is not an implementation attestation.

## Why the timing matters

- **Guidance is becoming more operational.** OWASP's [Securing Agentic Applications V2](https://genai.owasp.org/resource/securing-agentic-applications-v2/), dated November 10, 2026, covers architecture, identity, runtime protection, supply chains, and assurance testing. A proposal based only on a risk taxonomy would miss this progress.
- **Identity and evaluation remain active research areas.** NIST's [AI Agent Standards Initiative](https://www.nist.gov/artificial-intelligence/ai-agent-standards-initiative) explicitly includes identity infrastructure, protocols, and security evaluations. Its [May 2026 RFI-response analysis](https://www.nist.gov/publications/summary-analysis-responses-request-information-regarding-security-considerations-ai) reports stakeholder agreement that conventional security practices need adaptation for agents. The report summarizes respondents; it is not a finding that any particular product is secure.
- **Threat knowledge now includes agent behavior.** [MITRE ATLAS](https://atlas.mitre.org/) covers AI-related adversary behavior, with agent-oriented techniques such as tool and context poisoning. A static prompt-only evaluation would omit relevant workflow behavior.
- **A failed attack is not necessarily useful protection.** The October 2026 preprint [Ignored, Not Refused](https://arxiv.org/abs/2610.23254) argues for reporting legitimate task outcomes alongside attack outcomes. Its empirical claims have not been reproduced here, and its preprint status must remain visible. The methodological lesson is to measure both dimensions rather than equate inaction with success.

## Connected workstreams for this platform opportunity

| Research interest | Proposed question | Concrete study artifact | Boundary |
| --- | --- | --- | --- |
| Cybersecurity assurance | Does control-to-evidence traceability improve the correctness of assurance judgments? | Versioned evidence packets, policy checks, reviewer study | A passing fixture is not a deployment guarantee |
| Cyberwarfare | Can defensive response workflows preserve authorization and source uncertainty under manipulated incident context? | Synthetic critical-service incident and response-approval exercise | No targeting, offensive deployment, or conflict attribution engine |
| Cyber military selective service | Which demonstrated competencies are required to supervise AI-assisted cyber defense under pressure? | Task-based readiness scenarios and a comparative governance protocol | No conscription, eligibility, or employment decision system |
| Cybercrime cooperation | Can organizations exchange minimized evidence while preserving restrictions, provenance, and review responsibility? | Synthetic cross-organization evidence-handoff scenario | Technical integrity does not establish legal admissibility |
| African botnets | How do incomplete telemetry and language affect defensive triage and confidence statements? | Synthetic traffic summaries, sensor-coverage cards, English/French variants | No inference of operator nationality from IP location |
| Intelligence | Can analysts separate observations, source dependencies, hypotheses, and judgments in AI-assisted products? | Claim ledger, source graph, alternative explanations, confidence rationale | No classified sources or automatic actor attribution |

These examples connect to the platform opportunity; they are not an exhaustive list of research interests. Studies should retain their own questions and success measures rather than being forced into a single product. The [research agenda](agenda.md) and [connected research map](map.md) develop the broader program.

Connected areas include adversarial machine learning, digital forensics, privacy-preserving evidence exchange, critical-infrastructure resilience, human-agent interaction, and governance and diplomacy. A result in one workstream may change the assumptions of another: a telemetry gap can challenge an intelligence judgment, which can reveal a new evidence-sharing requirement, which can become a security-modeling question. These relationships help organize inquiry; they are not additional empirical findings from this landscape review.

## Grounding the regional and national-security dimensions

[INTERPOL's August 2026 assessment announcement](https://www.interpol.int/News-and-Events/News/2026/INTERPOL-report-finds-AI-linked-to-more-than-half-of-cybercrime-in-Africa) describes survey evidence from 36 African member countries and calls for forensic capability, cooperation, and AI literacy. Those are reasons to study evidence-handling and capacity—not to claim uniform regional conditions or generalize survey responses to every country. The announcement is not a botnet prevalence dataset.

The [ICRC's July 2026 working-paper announcement](https://www.icrc.org/en/article/icrc-working-paper-six-ict-related-threats-civilian-populations) highlights civilian consequences of ICT activity, including AI use during conflict. That supports a defensive, civilian-service continuity lens for the cyberwarfare workstream; this repository does not provide a legal analysis of operations.

The [NICE Framework](https://www.nist.gov/publications/workforce-framework-cybersecurity-nice-framework) offers a vocabulary of tasks, knowledge, and skills. It can inform a proposed readiness rubric, but it does not validate a compulsory-service policy or authorize assessment of individuals.

The [ODNI explanation of analytic standards](https://www.dni.gov/index.php/how-we-work/objectivity) emphasizes source quality, uncertainty, distinctions between information and judgment, and alternative analysis. Those concepts inform the research design; this project claims no intelligence-community affiliation or conformance certification.

## What to build first

Start with one synthetic workflow: two organizations reviewing a bilingual incident report before sharing a minimized evidence package. The assistant may summarize, classify, and recommend; an external policy boundary determines permitted actions, and a person approves sensitive release. Inject a changed permission, untrusted instruction, or stale source and observe the resulting action trace.

The first study should compare policy violations, legitimate task completion, unnecessary denials, and evidence completeness. Subsequent studies can add telemetry uncertainty, multi-agent handoffs, or human participants. Do not start with a broad autonomous national-security platform whose core claims cannot be tested.

See the [platform design](../platform/README.md), [evaluation protocol](../protocols/agent-assurance-evaluation.md), and [proposed collaboration brief](../collaboration/lee-proposal.md).
