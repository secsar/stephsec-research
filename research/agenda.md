# Research agenda

**Status:** public agenda and proposed directions; no findings reported.

The questions below are starting points within Stéphane Ikoué's evolving research interests. They are not an exhaustive inventory or a fixed set of tracks. One investigation may lead to another, and multiple areas may converge around a shared problem.

The established interests and proposed adjacent explorations are distinguished below. Neither an agenda entry nor a proposed extension is a claim of a funded project, institutional affiliation, completed qualification, or research finding. The [connected research map](map.md) shows how questions can branch and feed back into one another.

## Cybersecurity assurance

**Question:** How do public technical studies connect a security claim to evidence, assumptions, and limitations?

Proposed approach: structured document review using the [assurance evidence protocol](../protocols/assurance-evidence-review.md). Distinguish tests, formal reasoning, implementation evidence, and operational observations.

Potential output: an evidence classification and a traceable synthesis.

Main limitation: reporting quality is not the same as actual security effectiveness. An absent description cannot establish an absent practice.

## Cyberwarfare

**Question:** How do public accounts distinguish observed technical effects, strategic interpretation, and attribution judgments?

Proposed approach: compare a clearly bounded set of public case accounts; code who makes each claim, the cited evidence, alternatives considered, and the uncertainty expressed.

Potential output: a comparative analytical note separating technical observations from strategic conclusions.

Main limitation: public records are incomplete and sources can repeat the same underlying claim. Publication location or repeated reporting does not establish attribution.

## Cyber military selective service

**Question:** What governance and readiness tradeoffs arise across voluntary cyber reserves, specialist recruitment, and compulsory mobilization proposals?

Proposed approach: select jurisdictions and a time window before reviewing primary policy documents. Separate enacted arrangements, proposals, and commentary. Compare eligibility, skills assessment, activation, oversight, individual protections, and evaluation measures.

Potential output: a comparative research framework, followed by a sourced analysis if the study proceeds.

Main limitation: policy language does not establish implementation or effectiveness. This agenda does not describe current legal obligations or advocate compulsory service.

## Cybercrime and international cooperation

**Question:** Which coordination and evidence-handling barriers are documented in public cross-border cybercrime cases?

Proposed approach: bounded case comparison using official reports and public records. Record jurisdiction, institution, case stage, claimed barrier, proposed response, and supporting evidence.

Potential output: a thematic synthesis of documented coordination problems.

Main limitation: public cases are selected and may overrepresent successful investigations. Do not infer the prevalence of barriers from a small case collection.

## Botnets in African contexts

**Question:** How do measurement coverage, geolocation assumptions, and reporting practices shape conclusions about botnet activity in selected African countries?

Proposed approach: review public measurement studies and their collection methods. Specify countries, periods, network populations, and denominators. Keep device location, infrastructure location, victim location, and operator attribution separate.

Potential output: a measurement-quality review and a guide to interpreting regional observations.

Main limitation: Africa is not a single network environment. Sensor coverage, address allocation, hosting, and compromised-device observations cannot alone establish operator nationality or population-wide prevalence.

No live-device probing, malware deployment, or access to compromised systems is part of this proposed document review.

## Intelligence and national security

**Question:** How can analytical notes make evidence provenance, alternative explanations, and confidence judgments more explicit?

Proposed approach: apply a transparent coding framework to a bounded set of public analytical products. Distinguish source reliability, claim credibility, corroboration, and dependence between sources.

Potential output: a source-evaluation template and a comparative research note.

Main limitation: an explicit method does not eliminate judgment or compensate for missing evidence. No access to classified sources is claimed.

## Proposed adjacent explorations

These directions extend the established agenda where they support a clear research question. They are proposals for inquiry, not a claim that each is already a completed specialization.

### AI and agent security

**Question:** How should delegated authority, tool access, memory, and evidence use be constrained when an agent performs security-related work?

Potential study: compare explicit policy enforcement, approval mechanisms, and provenance checks in isolated tasks while measuring legitimate completion and false denials. The [agent-assisted evidence protocol](../protocols/agent-assurance-evaluation.md) is one initial design.

Connections: assurance, identity, privacy, intelligence, human-agent interaction, and organizational governance. Evidence about one model, task, or tool interface must not be generalized to all agents.

### Security modeling and threat modeling

**Question:** How can a precise statement of authorized behavior and a realistic account of possible failure improve each other without becoming interchangeable?

Potential study: trace a policy property through a threat scenario, an enforcement decision, and a reproducible evaluation. Detailed specifications and scenario registers remain in their dedicated repositories; this research program studies their relationship and evidentiary value.

Connections: assurance, secure architecture, software design, agent security, and resilience. An internally consistent model can still omit a material requirement.

### Adversarial machine learning

**Question:** How do manipulated inputs, retrieval content, training data, or model components affect a defined security property and the legitimate task?

Potential study: isolate one manipulation surface and compare controls against both adversarial and benign cases. Record model and data versions, test conditions, and the distinction between a changed prediction and a security consequence.

Connections: threat modeling, AI security, measurement, and assurance. A narrow test suite cannot establish general robustness.

### Digital forensics and evidence provenance

**Question:** Which provenance records allow another reviewer to reconstruct how an observation became a claim?

Potential study: compare synthetic evidence packets with missing, transformed, or contradictory records. Evaluate reproducibility, continuity of references, and visibility of uncertainty.

Connections: cybercrime, intelligence, botnet measurement, and privacy. Integrity checks alone do not establish authenticity, truth, or legal admissibility.

### Critical infrastructure and cyber resilience

**Question:** How do defensive decisions, dependency failures, and recovery actions affect the continuity of an essential service?

Potential study: use a synthetic dependency model and tabletop exercise to examine recovery assumptions, priorities, and authorized action boundaries.

Connections: cyberwarfare, assurance, operational decision-making, governance, and workforce readiness. Simulated outcomes are not measured performance of actual infrastructure.

### Governance, law, and diplomacy

**Question:** How do institutional responsibilities, jurisdiction, oversight, and trust shape what a technical security workflow may do?

Potential study: compare a bounded set of public policy instruments or cooperation arrangements, distinguishing proposed rules, enacted provisions, and observed implementation. Verify the applicable version and jurisdiction for each study.

Connections: international cybercrime cooperation, cyber military selective service, intelligence, privacy, and infrastructure protection. This research direction does not supply current legal advice or imply professional licensure.

### Human factors, education, and workforce readiness

**Question:** Which interfaces, training practices, and team structures help people recognize uncertainty, supervise automation, and make defensible decisions?

Potential study: begin with task analysis and a proposed competency rubric; introduce participant studies only under an appropriate research protocol. Separate individual knowledge, demonstrated task performance, team coordination, and institutional readiness.

Connections: cyber military selective service, assurance, human-agent interaction, and intelligence analysis. A demonstration or exercise score must not be used as an unvalidated selection instrument.

### Privacy and responsible information sharing

**Question:** How can an investigation or defensive workflow retain useful evidence while minimizing unnecessary disclosure?

Potential study: define permitted recipients, purpose, data classes, transformations, and retention rules in a synthetic evidence-handoff scenario. Measure what information remains useful and which proposed protections create gaps or excessive denial.

Connections: forensics, cross-border cooperation, AI security, access control, and governance. Technical minimization must be evaluated alongside the actual purpose and institutional context.

## Cross-cutting research paths

| Originating area | A question it can open | Related branch |
| --- | --- | --- |
| Botnet observations | Does collection coverage justify the conclusion? | Measurement, forensics, intelligence |
| An evidence handoff | Who may receive which information, and why? | Privacy, law, diplomacy, security modeling |
| Agent authorization | Does a control preserve useful work under changing context? | AI security, assurance, human factors |
| Defensive continuity | Which capability or coordination gap affects recovery? | Resilience, workforce readiness, governance |
| An analytical judgment | Which observation would change the assessment? | Intelligence, provenance, study design |

The relationships are bidirectional: a finding in an adjacent branch may change the assumptions of the originating study.

## Platforms and other outputs

[Mission Assurance Workbench](../platform/README.md) is one concrete implementation direction. It supports research on authorized action, evidence, and review; it does not define the full agenda. Other questions may be better served by a comparative paper, a measurement protocol, an executable model, a teaching lab, or a separate platform.

## Progression

For each study: define scope, publish a protocol, collect permitted sources, record decisions, analyze, state limitations, and publish a versioned note. A change to the question or method should be documented rather than hidden.

