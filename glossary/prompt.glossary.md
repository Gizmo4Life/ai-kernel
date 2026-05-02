---
id: prompt.glossary
title: Prompt
type: glossary
version: 1
created: 2026-05-02
updated: 2026-05-02
tags: [core, technical, communication]
summary: A reusable, template-driven set of instructions for an AI model that exists independently of a specific skill or agent.
aliases: [ai-instruction, template-prompt]
related: [skill.glossary, agent.glossary]
---

# Prompt

A **Prompt** in the AI Kernel is a standalone artifact designed to guide AI behavior for a specific, recurring task.

## Utility
While **Skills** use tools and **Agents** have roles, **Prompts** provide the "personality" or "logic" for the LLM itself. They are extracted into the `prompts/` directory when they have utility across multiple skills or agents, preventing duplication of complex prompt engineering.

## Standards
Prompts are governed by the [Prompt File Standard](../standards/prompt-file.standard.md).
