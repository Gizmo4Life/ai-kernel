---
id: populate-standard.instruction
title: Populate Standard
type: instruction
tags: [workflow, technical, research, process, orchestration]
summary: Orchestrates the research and synthesis phase of standard creation.
parent_standard: instruction-file.standard
skills: [auto-link-glossary.skill, surgical-refactor.skill, search-kernel.skill, doc-audit.skill, research-domain-patterns.skill, scan-codebase-patterns.skill, generate-padu-table.skill]
standards: [instruction-file.standard, standard-file.standard]
preconditions:
  - The Standards Scout agent is available.
glossary_refs: [agent.glossary, context.glossary, frontmatter.glossary, instruction.glossary, orchestration.glossary, padu-scale.glossary, skill.glossary, standard.glossary]
---

## Context
Orchestrates the research and synthesis phase of standard creation.


# Populate Standard

This instruction guides the **[Standards Scout](../agents/standards-scout.agent.md)** through the data-gathering phase of codification.


## Architecture

```mermaid
graph TD
    instruction-file.standard --> populate-standard.instruction
    populate-standard.instruction --> auto-link-glossary[auto-link-glossary.skill]
    populate-standard.instruction --> surgical-refactor[surgical-refactor.skill]
    populate-standard.instruction --> search-kernel[search-kernel.skill]
    populate-standard.instruction --> doc-audit[doc-audit.skill]
    populate-standard.instruction --> research-domain-patterns[research-domain-patterns.skill]
    populate-standard.instruction --> scan-codebase-patterns[scan-codebase-patterns.skill]
    populate-standard.instruction --> generate-padu-table[generate-padu-table.skill]
```
## Execution Steps

1. **Industry Research**: Run `research-domain-patterns.skill` to identify global best practices for the target domain.
2. **Codebase Scan**: Run `scan-codebase-patterns.skill` to identify how the domain is currently handled in the repository.
3. **Synthesis**: Run `generate-padu-table.skill` to combine research and reality into a draft PADU table.


## Postconditions
1. The system state matches the goal defined in the frontmatter.
2. All related Knowledge Graph nodes are updated and linked.

## Quality Gate

Standard accuracy is governed by the **[Standard File Standard](../standards/standard-file.standard.md)**.
- **Verification**: Ensure the generated PADU table includes at least one **Unacceptable (U)** practice to provide clear boundaries.
- **Enforcement**: If the table contains only **Preferred (P)** practices, it is considered "soft" and must be re-evaluated for more rigorous enforcement.
