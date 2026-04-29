---
id: audit-redundant-content.skill
title: Audit Redundant Content
type: skill
version: 1
created: 2026-04-28
updated: 2026-04-28
tags: [audit, cleanup, single-source-of-truth]
summary: Identifies inline definitions that should be replaced with links to the glossary.
tool: grep
inputs: path: The directory or file to audit.
outputs: redundancies: A list of files containing definitions that exist in the glossary.
standards: [glossary-entry.standard]
glossary_refs: [glossary-entry.glossary]
---

# Audit Redundant Content

This skill helps maintain the "Single Source of Truth" principle by finding where concepts are being defined manually instead of referenced.

## Execution Steps

1. **Load All Glossary IDs**: Get a list of all IDs from `glossary/`.
2. **Scan Path**: For each ID, search the target `path` for occurrences of the term or its aliases.
3. **Identify Definitions**: Use heuristics (e.g., proximity to "is a", "defined as", or appearing in a list of terms) to distinguish between a reference and a definition.
4. **Propose Refactor**: Suggest replacing the inline definition with a link to the glossary entry.
