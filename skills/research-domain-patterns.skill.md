---
id: research-domain-patterns.skill
title: Research Domain Patterns
type: skill
tags: [research, standards, tool, action, execution]
summary: Analyzes industry best practices for a specific technical domain.
interface:n  input: { query: "string" }n  output: { results: [] }nimplementation:n  engine: "bash"n  command: "grep {{query}} ."
parent_standard: skill-file.standard
inputs: domain: The subject (e.g., 'React Testing').
outputs: practices: A list of recommended patterns and anti-patterns.
standards: []
glossary_refs: [antipattern.glossary, authority.glossary, context.glossary, skill.glossary, standard.glossary]
---

## Context
Analyzes industry best practices for a specific technical domain.


# Research Domain Patterns

This skill researches industry standards for a specified `domain`.


## Architecture

```mermaid
graph TD
    skill-file.standard --> research-domain-patterns.skill
```
## Execution Steps

1. **Search**: Find high-authority sources for the domain.
2. **Extract**: Identify widely adopted "Preferred" practices.
3. **Identify Antipatterns**: Note common pitfalls and discourages practices.
4. **Report**: Summarize findings for the next step in the standard creation loop.

## Verification Protocol
1. Perform a manual dry-run of the execution steps.
2. Verify that the output matches the expected result defined in the Quality Gate.
