---
id: verify-repository-integrity.instruction
title: Verify Repository Integrity
type: instruction
tags: [workflow, audit, maintenance, process, orchestration]
summary: Orchestrates the indexing and reference discovery skills to ensure knowledge graph integrity and delegation safety.
parent_standard: instruction-file.standard
skills: [auto-link-glossary.skill, surgical-refactor.skill, search-kernel.skill, doc-audit.skill,  collect-repo-ids.skill, doc-audit.skill, detect-circular-delegation.skill ]
standards: [instruction-file.standard]
preconditions:
  - Access to the repository root.
glossary_refs: [context.glossary, delegation.glossary, frontmatter.glossary, instruction.glossary, knowledge-graph.glossary, quality-gate.glossary, skill.glossary, standard.glossary]
---

## Context
Orchestrates the indexing and reference discovery skills to ensure knowledge graph integrity and delegation safety.


# Verify Repository Integrity

This instruction ensures the repository's [Knowledge Graph](glossary/knowledge-graph.glossary.md) is unbroken and safe.


## Architecture

```mermaid
graph TD
    instruction-file.standard
goal --> verify-repository-integrity.instruction
    verify-repository-integrity.instruction --> collect-repo-ids[collect-repo-ids.skill]
    verify-repository-integrity.instruction --> find-frontmatter-refs[doc-audit.skill]
    verify-repository-integrity.instruction --> detect-circular-delegation[detect-circular-delegation.skill]
```
## Execution Steps

1. **Index**: Run `collect-repo-ids.skill` to run audit-repository-connectivity.skill of valid IDs.
2. **Discovery**: Run `doc-audit.skill` to map all dependencies.
3. **Cross-Check**: Verify every reference against the master ID list.
4. **Delegation Audit**: Run `detect-circular-delegation.skill` on the `agents/` directory.
5. **[Quality Gate](glossary/quality-gate.glossary.md)**:
    - If any ID is missing, flag as a critical standard violation.
    - If circular delegations are found, flag as a critical structural failure.
    - Report all broken nodes or loops to the user for remediation.

## Postconditions
1. The system state matches the goal defined in the frontmatter.
2. All related Knowledge Graph nodes are updated and linked.
