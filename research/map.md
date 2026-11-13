# Connected research map

**Status:** evolving map of research interests and connected questions. It is not an exhaustive inventory or a list of completed studies.

Research questions can branch, converge, or change as evidence develops. The purpose of this map is to show how a question becomes another useful question while preserving a clear scope for each study.

## Relationships between research areas

| Starting question | Connected area | What the connection adds | Potential feedback |
| --- | --- | --- | --- |
| What evidence justifies a security claim? | Cybersecurity assurance ↔ security modeling | Precise properties and evidence obligations | Failed evidence can reveal an incomplete model |
| How can intended behavior fail? | Threat modeling ↔ adversarial machine learning | Testable scenarios for manipulated inputs, models, and agent context | Experiments refine threat assumptions and defensive requirements |
| Can an agent act usefully within its authority? | AI and agent security ↔ identity, privacy, and human factors | Delegation, approval, revocation, information release, and usable oversight | Overblocking or unclear approvals can expose a faulty policy |
| What do observed network signals actually establish? | African botnet research ↔ measurement and digital forensics | Sensor coverage, artifact integrity, uncertainty, and repeatable interpretation | Forensic limits can change collection and measurement methods |
| Can evidence move across organizational boundaries responsibly? | Cybercrime cooperation ↔ law, diplomacy, and privacy | Authority, minimization, trust, governance, and institutional context | Procedural constraints can reshape technical protocols |
| What should a decision-maker believe from incomplete sources? | Intelligence ↔ evidence provenance and analytical methods | Source dependence, competing explanations, and calibrated judgments | New evidence can revise both judgments and collection priorities |
| How do defensive decisions affect essential services? | Cyberwarfare ↔ critical infrastructure and resilience | Civilian consequences, dependencies, continuity, and recovery | Recovery exercises can expose modeling and governance gaps |
| Which capabilities are needed for responsible cyber defense? | Cyber military selective service ↔ workforce and education | Demonstrated skills, supervision, readiness, governance, and safeguards | Exercise findings can challenge training or mobilization assumptions |

The map connects the research agenda with the technical work already represented in the security-modeling and threat-modeling repositories. AI security, forensics, resilience, privacy, human factors, and other branches can develop wherever the questions and evidence lead. Each study states its own method, progress, and evidentiary limits; inclusion in this map does not stand in for research results.

## Branching paths

### From infrastructure observations to responsible cooperation

An uncertain botnet observation raises a measurement question. Assessing that uncertainty raises a forensic provenance question. Sharing the resulting evidence raises a privacy and cross-border governance question. Automating part of the analysis then creates an AI-assurance question.

Each step can become an independent study. A single address or hosting location does not resolve the identity or nationality of an operator, and a technically consistent evidence package does not resolve every legal or institutional question.

### From a policy rule to an effective defense

A security model specifies a permission boundary. Threat modeling identifies a plausible violation. An experiment checks the enforcement mechanism. A human-factors study asks whether the required approval is understandable and usable. An assurance argument combines those findings and states what remains uncertain.

The feedback matters: an apparently secure control that prevents legitimate work may require a design change, not a declaration of success.

### From cyber readiness to governance

A defensive exercise reveals a competency gap. That gap can motivate research into instruction, assessment, human-agent supervision, and team coordination. The results may inform a separate comparison of recruitment, reserves, or mobilization proposals. They do not by themselves establish whether a policy is appropriate or whether an individual should be selected.

## Turning a connection into a study

Before opening a new branch, record the originating observation or question, the proposed contribution, the unit of analysis, the source or data needed, and the limits on possible conclusions. Give the branch its own protocol when its method or population differs.

| Research output | Suitable when | Example |
| --- | --- | --- |
| Literature or policy synthesis | The question concerns concepts, evidence, or institutional approaches | Comparing how public reports express attribution uncertainty |
| Formal or executable model | The question concerns permitted behavior or invariants | Modeling delegated authority and revocation |
| Measurement study | The question concerns an observable phenomenon | Assessing how sensor coverage changes botnet-related conclusions |
| Controlled experiment | The question concerns the effect of a defined intervention | Comparing evidence handoffs with different approval policies |
| Human-subject study | The question concerns judgment, learning, or behavior | Evaluating whether reviewers recognize unsupported conclusions |
| Research platform | Several studies need the same reproducible infrastructure | Mission Assurance Workbench |

These are possible outputs, not completed projects. A platform should serve a research question; the research program need not be confined to what the current platform can implement.

## Growth and revision

Add connections when they improve a question, reveal a missing assumption, or support a distinct contribution. Merge overlapping lines of inquiry when they share the same question and evidence. Retire or revise a branch when its premise is unsupported. Preserve earlier versions so changes in direction remain understandable.

See the [agenda](agenda.md) for current questions, the [method](../docs/research-method.md) for research practice, and the [platform concept](../platform/README.md) for one implementation direction.
