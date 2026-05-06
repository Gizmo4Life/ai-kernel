---
id: find-glossary-terms.skill
title: Find Glossary Terms
type: skill
tags: [discovery, search, glossary, tool, action, execution]
summary: Searches the glossary for terms or aliases matching a query.
parent_standard: skill-file.standardtool: grep
inputs: query: The term or concept to search for.
outputs: matches: A list of matching glossary file paths and their IDs.
standards: [glossary-entry.standard]
glossary_refs: [context.glossary, frontmatter.glossary, glossary-entry.glossary, skill.glossary]
---

## Context
Searches the glossary for terms or aliases matching a query.


# Find Glossary Terms

This skill uses `grep` to quickly find if a concept is already defined in the glossary, preventing duplication.


## Architecture

```mermaid
graph TD
    skill-file.standardtool --> find-glossary-terms.skill
```
## Execution Steps

1. **Search Aliases**: Run `grep -ri` on the `glossary/` folder looking for the query in the `aliases` frontmatter field.
2. **Search Titles**: Search for the query in the `title` frontmatter field.
3. **Filter Results**: Return the unique list of matching files.
4. **Link Suggestion**: If a match is found, provide the link format `[Title](file:///path/to/file)`.

## Verification Protocol
1. Perform a manual dry-run of the execution steps.
2. Verify that the output matches the expected result defined in the Quality Gate.
