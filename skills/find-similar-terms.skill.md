---
id: find-similar-terms.skill
title: Find Similar Terms
type: skill
version: 1
created: 2026-04-28
updated: 2026-04-28
tags: [discovery, glossary, ambiguity]
summary: Searches the glossary for terms with similar names or overlapping summaries to identify potential ambiguity.
tool: grep
inputs: term: The new or existing term to check.
outputs: similar_terms: A list of terms that might be confused with the input.
standards: [glossary-entry.standard]
glossary_refs: [heuristics.glossary]
---

# Find Similar Terms

This skill identifies potential naming collisions and conceptual overlaps in the glossary.

## Execution Steps

1. **Lexical Search**: Grep the glossary for partial matches of the `term` and its aliases.
2. **Semantic Check**: (LLM-assisted) Compare the summary and body of the target term with existing entries.
3. **Cluster**: Identify "clusters" of terms that describe similar technical spaces (e.g., 'Audit', 'Review', 'Verify').
4. **Report**: provide a list of candidates for disambiguation.
