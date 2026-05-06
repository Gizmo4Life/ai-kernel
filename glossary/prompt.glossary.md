---
id: prompt.glossary
title: Prompt
type: glossary
parent_standard: glossary-entry.standard
tags: [core, technical, communication, definition, term, meaning]
summary: A reusable, template-driven set of instructions for an AI model that exists independently of a specific skill or agent.
aliases: [ai-instruction, template-prompt]
related: [skill.glossary, agent.glossary]
---

## Context
Canonical definition of a core AI Kernel concept.


# Prompt

A **Prompt** in the AI Kernel is a standalone artifact designed to guide AI behavior for a specific, recurring task.


## Architecture

```mermaid
graph TD
    glossary-entry.standard --> prompt.glossary
```
## Utility
While **Skills** use tools and **Agents** have roles, **Prompts** provide the "personality" or "logic" for the LLM itself. They are extracted into the `prompts/` directory when they have utility across multiple skills or agents, preventing duplication of complex prompt engineering.

## Standards
Prompts are governed by the [Prompt File Standard](../standards/prompt-file.standard.md).

## Usage Constraints
- This term must only be used in its architectural context.
- Semantic drift from the canonical definition is Unacceptable (U).
