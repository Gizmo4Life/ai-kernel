---
id: bootstrap-new-standard.instruction
title: Bootstrap New Standard
type: instruction
version: 2
created: 2026-04-28
updated: 2026-04-28
tags: [workflow, quality, onboarding]
summary: Orchestrates the full process of researching, drafting, auditing, and committing a new technical standard.
goal: A high-quality, codebase-aware standard committed to the repository.
skills: [evaluate-against-standard.skill]
instructions: [ populate-standard.instruction, create-glossary-entry.instruction ]
standards: [ standard-file.standard, glossary-entry.standard, instruction-file.standard ]
preconditions: - A technical domain for the standard has been identified.
  - Flynn and the Standards Auditor agents are available.
glossary_refs: [ bootstrap.glossary, orchestration.glossary, quality-gate.glossary ]
---

# Bootstrap New Standard

This is the primary workflow for expanding the AI Kernel's reach into new domains.

## Steps

1. **Research & Draft**: Execute the [populate-standard.instruction](instructions/populate-standard.instruction.md) instruction.
2. **Glossary Alignment**: For any new terms identified in Step 1, create new glossary entries using the [create-glossary-entry.instruction](instructions/create-glossary-entry.instruction.md) instruction.
3. **[Quality Gate](glossary/quality-gate.glossary.md)**: Run `evaluate-against-standard` on the draft using `standard-file-standard`.
4. **Refine**: Address any meta-standard violations.
5. **Final Audit**: Task the **Standards Auditor** to do a final pass.
6. **Commit**: Save the new standard and all supporting glossary entries.
