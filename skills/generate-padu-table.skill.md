---
id: generate-padu-table.skill
title: Generate PADU Table
type: skill
tags: [generation, standard.glossary, tool, action, execution]
summary: Synthesizes patterns into a formal, atomic PADU table.
interface:n  input: { query: "string" }n  output: { results: [] }nimplementation:n  engine: "bash"n  command: "grep {{query}} ."
parent_standard: skill-file.standard
inputs:
  researched_patterns: Output from industry research.
  codebase_patterns: Output from local scan.
outputs:
  padu_table: A formatted markdown table.
standards: [standard-file.standard]
prompts: [ synthesize-padu-logic.prompt ]
glossary_refs: [context.glossary, padu-scale.glossary, prompt.glossary, skill.glossary, standard.glossary]
---

## Context
Synthesizes patterns into a formal, atomic PADU table.

# Generate PADU Table

This skill converts pattern data into the kernel's formal quality format.

## Architecture

```mermaid
graph TD
    skill-file.standard --> generate-padu-table.skill
```
## Execution Steps

1. **Synthesize**: Combine industry best practices with codebase realities.
2. **Rank**: Use the **[Synthesize PADU Logic](../prompts/synthesize-padu-logic.prompt.md)** prompt to assign P, A, D, or U ratings.
3. **Draft**: Create the markdown table. **Every practice must fit in a single row.**
4. **Rationalize**: provide a clear reason for the rating and an **Enforcement** method.

## Verification Protocol
1. Perform a manual dry-run of the execution steps.
2. Verify that the output matches the expected result defined in the Quality Gate.

## Quality Gate

Standard creation is governed by the **[Standard File Standard](../standards/standard-file.standard.md)**.
- **Verification**: The table must be **Atomic**. If more than 8 practices are identified, the table must be split into hierarchical children.
- **Enforcement**: Tables missing the **Enforcement** column are **Unacceptable (U)** and cannot be promoted to a standard.
