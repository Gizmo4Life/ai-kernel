---
id: generate-padu-table.skill
title: Generate PADU Table
type: skill
version: 1
created: 2026-04-28
updated: 2026-04-28
tags: [generation, standard.glossary ]
summary: Synthesizes researched and scanned patterns into a formal PADU table.
tool: editor
inputs: researched_patterns: Output from research.
  codebase_patterns: Output from scan.
outputs: padu_table: A formatted markdown table.
standards: [standard-file.standard]
glossary_refs: [padu-scale.glossary]
---

# Generate PADU Table

This skill converts raw pattern data into the kernel's formal quality format.

## Execution Steps

1. **Synthesize**: Combine industry best practices with codebase realities.
2. **Rank**: Assign P, A, D, or U ratings based on project goals.
3. **Draft**: Create the markdown table with clear rationales and exceptions.
4. **Review**: Present for final orchestration review.
