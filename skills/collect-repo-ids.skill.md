---
id: collect-repo-ids.skill
title: Collect Repository IDs
type: skill
version: 1
created: 2026-04-28
updated: 2026-04-28
tags: [audit, technical]
summary: Extracts all unique 'id' fields from the repository's YAML frontmatter.
tool: grep
inputs: path: Directory to scan.
outputs: id_list: A list of all valid IDs in the kernel.
standards: []
glossary_refs: [frontmatter.glossary]
---

# Collect Repository IDs

Atomic skill for indexing the repository.

## Execution Steps

1. **Grep**: Search for `id:` at the start of frontmatter blocks.
2. **Normalize**: Strip whitespace and prefixes.
3. **Report**: provide the master list of discovered IDs.
