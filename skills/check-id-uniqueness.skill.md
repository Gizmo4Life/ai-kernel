---
id: check-id-uniqueness.skill
title: Check ID Uniqueness
type: skill
tags: [audit, technical, integrity, tool, action, execution]
summary: Scans the entire repository to ensure that every `id` in frontmatter is globally unique.
tool: grep
inputs:
  scope: The directory to scan (defaults to `/`).
outputs:
  collisions: A list of duplicate IDs and their file paths.
standards: [kernel.standard]
glossary_refs: [frontmatter.glossary, knowledge-graph.glossary]
---

# Check ID Uniqueness

## Context
In a decentralized Knowledge Graph, ID collisions are a fatal error. If two files share an ID, cross-references become ambiguous and the graph's integrity is compromised. This skill serves as the **Global Safety Gate**, ensuring that every identifier in the repository is a unique, deterministic pointer.

## Architecture

```mermaid
graph TD
    Start((Trigger Audit)) --> Extract[Extract: grep id: pattern]
    Extract --> Normalize[Normalize: Strip whitespace/values]
    Normalize --> Count{Count Occurrences}
    Count -->|Count > 1| Collision[Flag: ID Collision Found]
    Count -->|Count = 1| Success[Pass: ID Unique]
    Collision --> Report[Output: Error List]
    Success --> Report
    Report --> End((Audit Complete))
```

## Execution Steps

1. **Extract IDs**: Run `grep -r "id:" .` across the repository.
2. **Normalize**: Strip whitespace and extract the ID values.
3. **Count Occurrences**: Identify any ID that appears more than once.
4. **Report Collisions**:
    - List the duplicated ID.
    - provide the absolute paths of all files claiming that ID.


## Verification Protocol
1. Perform a manual dry-run of the execution steps.
2. Verify that the output matches the expected result defined in the Quality Gate.

## Quality Gate

ID integrity is governed by the **[Kernel Standard](../standards/kernel.standard.md)**.
- **Verification**: The check must be case-sensitive and scan all file types except `README.md`.
- **Enforcement**: Any ID collision is an **Unacceptable (U)** violation. The repository is considered "Broken" until the collision is resolved via renaming.
