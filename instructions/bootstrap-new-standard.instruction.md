---
id: bootstrap-new-standard.instruction
title: Bootstrap New Standard
type: instruction
tags: [workflow, quality, onboarding, process, orchestration]
summary: Orchestrates the full process of researching, drafting, auditing, and committing a new technical standard.
parent_standard: instruction-file.standard
skills: [auto-link-glossary.skill, surgical-refactor.skill, search-kernel.skill, doc-audit.skill, evaluate-against-standard.skill]
instructions: [ populate-standard.instruction, create-glossary-entry.instruction ]
standards: [ standard-file.standard, glossary-entry.standard, instruction-file.standard ]
preconditions:
  - A technical domain for the standard has been identified.
  - Flynn and the Standards Auditor agents are available.
glossary_refs: [agent.glossary, bootstrap.glossary, context.glossary, frontmatter.glossary, glossary-entry.glossary, instruction.glossary, orchestration.glossary, quality-gate.glossary, skill.glossary, standard.glossary]
---

## Context
Orchestrates the full process of researching, drafting, auditing, and committing a new technical standard.


# Bootstrap New Standard

This is the primary workflow for expanding the AI Kernel's reach into new domains.


## Architecture

```mermaid
graph TD
    instruction-file.standard --> bootstrap-new-standard.instruction
    bootstrap-new-standard.instruction --> auto-link-glossary[auto-link-glossary.skill]
    bootstrap-new-standard.instruction --> surgical-refactor[surgical-refactor.skill]
    bootstrap-new-standard.instruction --> search-kernel[search-kernel.skill]
    bootstrap-new-standard.instruction --> doc-audit[doc-audit.skill]
    bootstrap-new-standard.instruction --> evaluate-against-standard[evaluate-against-standard.skill]
```
## Execution Steps

1. **Research & Draft**: Execute the [populate-standard.instruction](populate-standard.instruction.md) instruction.
2. **Glossary Alignment**: For any new terms identified in Step 1, create new glossary entries using the [create-glossary-entry.instruction](create-glossary-entry.instruction.md) instruction.
3. **Refine**: Address any meta-standard violations identified during the draft.
4. **Final Audit**: Task the **[Standards Auditor](../agents/standards-auditor.agent.md)** to perform a final compliance pass.
5. **Commit**: Save the new standard and all supporting glossary entries.


## Postconditions
1. The system state matches the goal defined in the frontmatter.
2. All related Knowledge Graph nodes are updated and linked.

## Quality Gate

Expansion integrity is governed by the **[Standard File Standard](../standards/standard-file.standard.md)**.
- **Verification**: Run `evaluate-against-standard.skill` on the final draft. Ensure a 100% pass rate against the meta-standard.
- **Enforcement**: If any **Unacceptable (U)** violations remain, the standard must not be committed to the `standards/` directory.
