---
id: find-frontmatter-refs.skill
title: Find Frontmatter References
type: skill
tags: [audit, technical, tool, action, execution]
summary: Scans the repository for fields that reference other IDs (e.g., glossary_refs, standards).
interface:n  input: { query: "string" }n  output: { results: [] }nimplementation:n  engine: "bash"n  command: "grep {{query}} ."parent_standard: skill-file.standard
inputs: path: Directory to scan.
outputs: ref_map: A mapping of files to the IDs they reference.
standards: []
glossary_refs: [context.glossary, frontmatter.glossary, skill.glossary]
---

## Context
Scans the repository for fields that reference other IDs (e.g., glossary_refs, standards).


# Find Frontmatter References

Atomic skill for identifying dependencies.


## Architecture

```mermaid
graph TD
    skill-file.standardtool --> find-frontmatter-refs.skill
```
## Execution Steps

1. **Grep**: Search for `glossary_refs`, `standards`, `delegates`, and `context` fields.
2. **Parse**: Extract the list of IDs from these fields.
3. **Report**: provide a map of which files depend on which IDs.

## Verification Protocol
1. Perform a manual dry-run of the execution steps.
2. Verify that the output matches the expected result defined in the Quality Gate.
