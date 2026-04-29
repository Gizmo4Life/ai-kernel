---
id: find-frontmatter-refs.skill
title: Find Frontmatter References
type: skill
version: 1
created: 2026-04-28
updated: 2026-04-28
tags: [audit, technical]
summary: Scans the repository for fields that reference other IDs (e.g., glossary_refs, standards).
tool: grep
inputs: path: Directory to scan.
outputs: ref_map: A mapping of files to the IDs they reference.
standards: []
glossary_refs: [frontmatter.glossary]
---

# Find Frontmatter References

Atomic skill for identifying dependencies.

## Execution Steps

1. **Grep**: Search for `glossary_refs`, `standards`, `delegates`, and `context` fields.
2. **Parse**: Extract the list of IDs from these fields.
3. **Report**: provide a map of which files depend on which IDs.
