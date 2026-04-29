---
id: resolve-naming-ambiguity.instruction
title: Resolve Naming Ambiguity
type: instruction
version: 1
created: 2026-04-28
updated: 2026-04-28
tags: [workflow, glossary, architect]
summary: Workflow for handling overlapping or confusingly named concepts in the glossary.
goal: A clear, distinct, and unambiguous glossary.
skills: [find-similar-terms.skill, provide-glossary-guidance.skill]
instructions: [resolve-glossary-conflict.instruction]
standards: [glossary-entry.standard, kernel.standard]
preconditions: - A potential naming conflict has been identified.
---

# Resolve Naming Ambiguity

This instruction provides the logic for maintaining conceptual clarity in the AI Kernel.

## Steps

1. **Detection**: Run `find-similar-terms.skill` for the target term.
2. **Analysis**: Invoke **Flynn** via `provide-glossary-guidance.skill`.
3. **Decision Tree**: - **Merge**: If terms are identical in intent, use [Resolve Glossary Conflict](resolve-glossary-conflict.instruction.md).
    - **Rename**: If one term is more specific, propose a renaming to include a namespace or qualifier (e.g., `Standard` -> `File Standard`).
    - **Disambiguate**: If terms must coexist, add a `## Disambiguation` section to both entries explicitly linking and contrasting them.
4. **[Quality Gate](glossary/quality-gate.glossary.md)**: - Verify that no two IDs in the repository are confusingly similar (e.g., `standard` vs `standards`).
5. **Update References**: If renaming occurred, run the `Refactor to Kernel Standards` instruction to fix links.
