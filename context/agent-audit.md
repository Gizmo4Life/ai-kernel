# Agent Capability Manifest (v2.4.0)
## Agent: flynn.agent.md
- Interaction Pattern:        1
- Quality Gate:        1
- Skills: 
- Instructions: 
- Glossary Refs: [ domain-owner.glossary, knowledge-graph.glossary ]

## Agent: integrity-guardian.agent.md
- Interaction Pattern:        0
- Quality Gate:        1
- Skills: [ find-similar-terms.skill, detect-circular-delegation.skill, audit-frontmatter-completeness.skill ]
- Instructions: [ verify-repository-integrity.instruction ]
- Glossary Refs: [ domain-owner.glossary, knowledge-graph.glossary ]

## Agent: librarian.agent.md
- Interaction Pattern:        1
- Quality Gate:        0
- Skills: [ find-similar-terms.skill, audit-redundant-content.skill, provide-glossary-guidance.skill ]
- Instructions: 
- Glossary Refs: [ standard.glossary, padu-scale.glossary ]

## Agent: linkage-specialist.agent.md
- Interaction Pattern:        1
- Quality Gate:        0
- Skills: [ audit-repository-connectivity.skill, find-frontmatter-refs.skill, find-glossary-terms.skill ]
- Instructions: 
- Glossary Refs: 

## Agent: operator.agent.md
- Interaction Pattern:        1
- Quality Gate:        0
- Skills: 
- Instructions: [ kernel-first-remediation.instruction ]
- Glossary Refs: 

## Agent: semantic-auditor.agent.md
- Interaction Pattern:        1
- Quality Gate:        0
- Skills: [ audit-for-architectural-violations.skill, evaluate-against-standard.skill ]
- Instructions: 
- Glossary Refs: 

## Agent: standards-auditor.agent.md
- Interaction Pattern:        1
- Quality Gate:        0
- Skills: [ evaluate-against-standard.skill, audit-for-architectural-violations.skill, audit-frontmatter-completeness.skill ]
- Instructions: 
- Glossary Refs: 

## Agent: standards-scout.agent.md
- Interaction Pattern:        1
- Quality Gate:        0
- Skills: [ scan-codebase-patterns.skill, generate-padu-table.skill ]
- Instructions: [ codify-emerging-pattern.instruction ]
- Glossary Refs: [ standard.glossary, padu-scale.glossary ]

