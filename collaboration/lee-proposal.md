# Proposed collaboration with Edward Lee

**Status:** discussion proposal only. No outreach has been sent, no agreement exists, and no contribution or endorsement is attributed to Edward Lee or AIDEFEND Labs.

## The proposition

Build a small, reproducible bridge from defensive knowledge to assurance evidence: a workflow-specific test packet that links an AIDEFEND control reference to a local security requirement, controlled scenario, observed actions, and explicit limits on the resulting claim.

The first demonstration would use a synthetic English/French incident-evidence handoff between two organizations. It would test authorization and provenance while measuring whether useful work still gets done.

## Why Lee is a relevant prospective collaborator

The [official AIDEFEND Labs profile](https://aidefendlabs.com/en/about/) identifies Edward Lee as its founder and describes work on open frameworks, analysis, and implementation guidance. The [framework repository](https://github.com/edward-playground/aidefense-framework) supplies a concrete public integration surface. This makes a focused technical contribution more credible than proposing a new catalog or assuming access to private work.

## Proposed responsibilities, subject to agreement

| Contribution | Proposed lead | Concrete artifact |
| --- | --- | --- |
| Research questions, domain assumptions, measurement limits | Stéphane Ikoué | Protocol and claim-evidence rubric |
| Scenario and policy specification | StephSec contributors | Synthetic handoff cases and expected outcomes |
| Upstream mapping and integration review | Invite Lee or a willing maintainer | Reviewed version/ID mapping contract |
| Runner and result format | Joint or independent contributors | Reproducible fixture and evidence packet |
| Publication and credit | All actual contributors | Agreed authorship, attribution, and release scope |

The table is a suggested division of work, not a commitment by anyone else.

## A useful first contribution

Prepare one independently runnable example with:

1. A pinned upstream commit and integrity-checked metadata.
2. A small set of reviewed control references with reasons for relevance.
3. One required security property and one legitimate business task.
4. Benign, policy-violating, and incomplete-evidence traces.
5. A report that does not equate framework coverage with effectiveness.
6. Tests for schema errors, stale mappings, and ambiguous outcomes.
7. Clear attribution and an unofficial downstream identity.

Then ask whether the maintainer prefers an upstream example, a separate adapter, or an independent research companion. Do not open an unsolicited large pull request containing a new platform architecture before discussing fit.

## Questions for an initial discussion

- Is the integration export the preferred stable boundary for this experiment?
- Which control references are appropriate for a narrowly scoped evidence-handoff example?
- How should version migration and retired identifiers be represented?
- Would an evidence-packet example fill a useful documentation gap?
- What contribution, attribution, and maintenance expectations would apply?
- Would a bilingual scenario help, and who could independently review its equivalence?

## Collaboration options

| Option | Benefit | Commitment |
| --- | --- | --- |
| Independent downstream research | Can proceed using public interfaces and license terms | No participation assumed |
| Focused maintainer review | Checks mapping accuracy and integration fit | Small review request if accepted |
| Joint pilot | Shared protocol and publication | Explicit scope, responsibilities, data rules, and authorship agreement |

The independent path remains valuable if Lee has no time or prefers another direction. A fork is a technical starting point, not a partnership.

## Decision gate

Before broader development, require a working small example, meaningful negative tests, a reviewed evaluation protocol, and a clear account of overlap with existing tools. Treat an affirmative response from a collaborator as an additional input, not as a condition for honest independent research.
