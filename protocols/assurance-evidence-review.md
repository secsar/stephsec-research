# Protocol: Reporting evidence for cybersecurity assurance claims

**Protocol ID:** SR-P01  
**Version:** 0.1  
**Status:** Proposed; collection and analysis have not begun  
**Review type:** bounded exploratory document review, not a completed systematic review

## Research question

How do publicly accessible technical documents connect a defined cybersecurity claim to evidence, assumptions, and limitations?

## Scope

Unit of analysis: a claim–evidence pair within a technical document.

Initial sample target: 10–15 eligible documents, with no claim of representativeness. Start with documents published from 2020 through 2026; record the actual search date and exclude material published after that date. The proposed English-language restriction must be reported as a limitation.

Relevant claims concern access control, tenant isolation, information flow, or security-state integrity.

## Planned search

Search primary publication repositories such as NIST publications and publisher or institutional research repositories. Record the exact repository, query, date, result limits, and screening decisions.

Candidate query strings:
- "security assurance" "evidence"
- "access control" "verification"
- "tenant isolation" "evaluation"
- "information flow" "security proof"

These are proposed queries, not a search log. Amend the strategy after a documented pilot if it fails to retrieve relevant material.

## Eligibility

Include a document when:
- Full text is legitimately accessible.
- It identifies a system, model, or mechanism.
- It makes at least one relevant security claim.
- It describes supporting evidence or explicitly identifies evidence still needed.
- Authorship, publication date, and provenance can be recorded.

Exclude sales-only claims without a technical basis, duplicate versions unless analyzing changes, and sources requiring confidential access.

A preprint may be included, but its review status must be recorded. Do not treat preprint availability as peer review.

## Extraction fields

For each pair record document ID, location, claim, claimed scope, evidence type, model/system version, assumptions, evaluation conditions, limitations, and whether the evidence directly supports the claim.

Evidence categories:
- Explanatory argument.
- Formal proof.
- Bounded model checking.
- Test or experiment.
- Configuration or implementation inspection.
- Operational observation.
- Evidence proposed but not supplied.

Multiple categories may apply. The reviewer records what is actually described, not an inferred level of rigor.

## Coding procedure

1. Pilot on three eligible documents.
2. Clarify ambiguous categories and log changes.
3. Recode the pilot with the revised definitions.
4. Extract the remaining sample.
5. Recheck every consequential claim against its source location.

No independent second review is currently arranged. Report that limitation if the study proceeds without one.

## Analysis plan

Summarize evidence categories and recurring claim–evidence gaps. If counts are used, report both document-level and claim-level denominators; multiple pairs in one document are not independent studies.

Do not rank organizations or infer that a poorly documented control is ineffective. Do not infer that a proof of a model establishes correctness of an implementation outside that model.

## Planned outputs and boundaries

Potential outputs: a source register, a claim–evidence table with permitted excerpts or paraphrases, and a narrative synthesis.

No sources have been screened, no counts computed, and no findings established. The protocol itself contains no empirical result. Record amendments and dates before presenting any completed analysis.

