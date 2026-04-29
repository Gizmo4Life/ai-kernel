---
id: scan-codebase-patterns.skill
title: Scan Codebase Patterns
type: skill
version: 1
created: 2026-04-28
updated: 2026-04-28
tags: [audit, search, patterns]
summary: Identifies existing code patterns (exemplary or problematic) within a local repository.
tool: grep
inputs: domain: The subject (e.g., 'Error Handling').
outputs: patterns: A list of code snippets and their location.
standards: []
glossary_refs: [antipattern.glossary]
---

# Scan Codebase Patterns

This skill scans the local repository for real-world usage of a specific `domain`.

## Execution Steps

1. **Grep**: Search for keywords related to the domain.
2. **Contextualize**: Identify recurring patterns in the search results.
3. **Classify**: - **Positive**: Widespread, clever, or effective patterns.
    - **Negative**: Fragile, complex, or legacy patterns.
4. **Report**: provide a list of existing practices for standard codification.
