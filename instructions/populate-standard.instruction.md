---
id: populate-standard.instruction
title: Populate Standard
type: instruction
version: 1
created: 2026-04-28
updated: 2026-04-28
tags: [workflow, orchestration.glossary ]
summary: Orchestrates the research and scanning skills to generate a draft PADU table.
goal: A draft PADU table grounded in both industry standards and codebase reality.
skills: [ research-domain-patterns.skill, scan-codebase-patterns.skill, generate-padu-table.skill, provide-glossary-guidance.skill ]
standards: [ instruction-file.standard, skill-file.standard ]
preconditions: - A technical domain has been specified.
---

# Populate Standard

This instruction coordinates the discovery and synthesis of technical patterns.

## Steps

1. **Discovery**: - Run `research-domain-patterns` to find industry best practices.
    - Run `scan-codebase-patterns` to find local exemplary and problematic patterns.
2. **Analysis**: - Synthesize the findings. If new terms are found, use `provide-glossary-guidance` to update the glossary.
3. **Generation**: - Run `generate-padu-table` with the synthesized data.
4. **[Quality Gate](glossary/quality-gate.glossary.md)**: - Review the table against the `standard-file-standard`.
5. **Final Output**: provide the draft table for incorporation into the new standard file.
