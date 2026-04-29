---
id: find-glossary-terms.skill
title: Find Glossary Terms
type: skill
version: 1
created: 2026-04-28
updated: 2026-04-28
tags: [discovery, search, glossary]
summary: Searches the glossary for terms or aliases matching a query.
tool: grep
inputs: query: The term or concept to search for.
outputs: matches: A list of matching glossary file paths and their IDs.
standards: [glossary-entry.standard]
glossary_refs: [glossary-entry.glossary]
---

# Find Glossary Terms

This skill uses `grep` to quickly find if a concept is already defined in the glossary, preventing duplication.

## Execution Steps

1. **Search Aliases**: Run `grep -ri` on the `glossary/` folder looking for the query in the `aliases` frontmatter field.
2. **Search Titles**: Search for the query in the `title` frontmatter field.
3. **Filter Results**: Return the unique list of matching files.
4. **Link Suggestion**: If a match is found, provide the link format `[Title](file:///path/to/file)`.
