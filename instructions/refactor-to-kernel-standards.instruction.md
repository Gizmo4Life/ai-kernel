---
id: refactor-to-kernel-standards.instruction
title: Refactor to Kernel Standards
type: instruction
tags: [workflow, architecture, refactor, process, orchestration]
summary: A maximalist workflow for aligning repository content with the core architectural principles of the AI Kernel.
parent_standard: instruction-file.standard
skills: [auto-link-glossary.skill, surgical-refactor.skill, search-kernel.skill, doc-audit.skill, audit-for-architectural-violations.skill, provide-glossary-guidance.skill, evaluate-against-standard.skill]
instructions: [create-glossary-entry.instruction, populate-standard.instruction]
standards: [skill-file.standard, instruction-file.standard, glossary-entry.standard, kernel.standard]
preconditions:
  - Repository content exists that needs alignment.
  - Flynn and the Librarian agents are available.
glossary_refs: [bootstrap.glossary, context.glossary, frontmatter.glossary, glossary-entry.glossary, instruction.glossary, orchestration.glossary, quality-gate.glossary, skill.glossary, standard.glossary]
---

## Context
A maximalist workflow for aligning repository content with the core architectural principles of the AI Kernel.

# Refactor to Kernel Standards

This instruction codifies the "maximalist extraction" process used to maintain the framework's integrity.

## Architecture

```mermaid
graph TD
    instruction-file.standard --> refactor-to-kernel-standards.instruction
    refactor-to-kernel-standards.instruction --> auto-link-glossary[auto-link-glossary.skill]
    refactor-to-kernel-standards.instruction --> surgical-refactor[surgical-refactor.skill]
    refactor-to-kernel-standards.instruction --> search-kernel[search-kernel.skill]
    refactor-to-kernel-standards.instruction --> doc-audit[doc-audit.skill]
    refactor-to-kernel-standards.instruction --> audit-for-architectural-violations[audit-for-architectural-violations.skill]
    refactor-to-kernel-standards.instruction --> provide-glossary-guidance[provide-glossary-guidance.skill]
    refactor-to-kernel-standards.instruction --> evaluate-against-standard[evaluate-against-standard.skill]
```
## Execution Steps

1. **Audit**: Run [audit-for-architectural-violations.skill](../skills/audit-for-architectural-violations.skill.md) across the target directory or file.
2. **Glossary Extraction**:
    - For every inline concept found, use [provide-glossary-guidance.skill](../skills/provide-glossary-guidance.skill.md).
    - If `NEW_ENTRY` is recommended, execute [create-glossary-entry.instruction](create-glossary-entry.instruction.md).
    - Replace the inline definition with a link to the new glossary file.
3. **Modularization**:
    - If a **Skill** is found to be non-atomic, decompose it into new atomic skills.
    - Create a new **Instruction** to orchestrate the new skills.
4. **Standard Extraction**:
    - If a skill or instruction contains "hardcoded" quality rules, move them to a relevant **Standard** (PADU table).
5. **Commit**: Save and propose changes.

## Postconditions
1. The system state matches the goal defined in the frontmatter.
2. All related Knowledge Graph nodes are updated and linked.

## Quality Gate

Architectural integrity is governed by the **[Kernel Standard](../standards/kernel.standard.md)**.
- **Verification**: Run `evaluate-against-standard.skill` on the new/refactored files using the relevant file-type standards.
- **Enforcement**: If any refactored file receives a **Unacceptable (U)** rating, the refactor is considered incomplete and must be re-processed.
