---
id: verify-repository-integrity.instruction
title: Verify Repository Integrity
type: instruction
version: 1
created: 2026-04-28
updated: 2026-04-28
tags: [workflow, audit, maintenance]
summary: Orchestrates the indexing and reference discovery skills to ensure knowledge graph integrity.
goal: A healthy repository with zero broken frontmatter references.
skills: [ collect-repo-ids.skill, find-frontmatter-refs.skill ]
standards: [instruction-file.standard]
preconditions: - Access to the repository root.
---

# Verify Repository Integrity

This instruction ensures the repository's [Knowledge Graph](glossary/knowledge-graph.glossary.md) is unbroken.

## Steps

1. **Index**: Run `collect-repo-ids` to build the master list of valid IDs.
2. **Discovery**: Run `find-frontmatter-refs` to map all dependencies.
3. **Cross-Check**: Verify every reference against the master ID list.
4. **[Quality Gate](glossary/quality-gate.glossary.md)**: - If any ID is missing, flag as a critical standard violation.
    - Report all broken nodes to the user for remediation.
