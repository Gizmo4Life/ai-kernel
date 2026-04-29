---
id: refactor-to-kernel-standards.instruction
title: Refactor to Kernel Standards
type: instruction
version: 2
created: 2026-04-28
updated: 2026-04-28
tags: [workflow, architecture, refactor]
summary: A maximalist workflow for aligning repository content with the core architectural principles of the AI Kernel.
goal: A fully modular, linked, and standards-compliant repository.
skills: [audit-for-architectural-violations.skill, provide-glossary-guidance.skill, evaluate-against-standard.skill]
instructions: [create-glossary-entry.instruction, populate-standard.instruction]
standards: [skill-file.standard, instruction-file.standard, glossary-entry.standard, kernel.standard]
preconditions: - Repository content exists that needs alignment.
  - Flynn and the Librarian agents are available.
glossary_refs: [bootstrap.glossary, orchestration.glossary, quality-gate.glossary]
---

# Refactor to Kernel Standards

This instruction codifies the "maximalist extraction" process used to maintain the framework's integrity.

## Steps

1. **Audit**: Run [audit-for-architectural-violations.skill](skills/audit-for-architectural-violations.skill.md) across the target directory or file.
2. **Glossary Extraction**: - For every inline concept found, use [provide-glossary-guidance.skill](skills/provide-glossary-guidance.skill.md).
    - If `NEW_ENTRY` is recommended, execute [create-glossary-entry.instruction](instructions/create-glossary-entry.instruction.md).
    - Replace the inline definition with a link to the new glossary file.
3. **Modularization**: - If a **Skill** is found to be non-atomic, decompose it into new atomic skills.
    - Create a new **Instruction** to orchestrate the new skills.
4. **Standard Extraction**: - If a skill or instruction contains "hardcoded" quality rules, move them to a relevant **Standard** (PADU table).
5. **[Quality Gate](glossary/quality-gate.glossary.md)**: - Run `evaluate-against-standard` on the new/refactored files using the relevant file-type standards and the [Kernel Standard](standards/kernel.standard.md).
6. **Integrity Check**: - (Optional) Run the [verify-repository-integrity.instruction](instructions/verify-repository-integrity.instruction.md) instruction.
7. **Commit**: Save and propose changes.
