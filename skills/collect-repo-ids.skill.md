---
id: collect-repo-ids.skill
title: Collect Repository IDs
type: skill
tags: [audit, technical]
summary: Extracts all unique 'id' fields from the repository's YAML frontmatter.
tool: grep
inputs: path: Directory to scan.
outputs: id_list: A list of all valid IDs in the kernel.
standards: []
glossary_refs: [frontmatter.glossary]
---

## Context
Extracts all unique 'id' fields from the repository's YAML frontmatter.


# Collect Repository IDs

Atomic skill for indexing the repository.


## Architecture

```mermaid
graph TD
    Start((Start)) --> Process[Process: Logic Flow] --> End((End))
```
## Execution Steps

1. **Grep**: Search for `id:` at the start of frontmatter blocks.
2. **Normalize**: Strip whitespace and prefixes.
3. **Report**: provide the master list of discovered IDs.

## Verification Protocol
1. Perform a manual dry-run of the execution steps.
2. Verify that the output matches the expected result defined in the Quality Gate.
