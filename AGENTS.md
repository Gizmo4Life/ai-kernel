---
id: agents-master
title: AI Kernel Agentic Hierarchy
type: documentation
tags: [architecture, agents, hierarchy]
glossary_refs: [agent.glossary, context.glossary, driver.glossary, frontmatter.glossary, glossary-entry.glossary, instruction.glossary, padu-scale.glossary, progressive-disclosure.glossary, prompt.glossary, sidecar.glossary, skill.glossary, standard.glossary]
---

# AI Kernel

## Context
This file serves as the master entry point for understanding the agentic hierarchy of the AI Kernel and its role as a Universal Sidecar. It defines how Tier 0, Tier 1, and Tier 2 agents collaborate to maintain the system.

## Architecture

```mermaid
graph TD
```

## How to Use This Framework

You are operating with the ai-kernel personal workflow framework.
This repository is a companion workspace — it provides reusable
glossary definitions, coding standards, skills, instructions,
prompts, and agent definitions.

## How to Use This Framework

### Agent Brain ###

1. [Glossary](glossary/glossary-entry.glossary.md): Before defining a concept inline, check `glossary/`.
   If a definition exists, link to it. If not, ask [flynn](agents/flynn.agent.md) for guidance on whether to create a new definition or inline it.
2. [Standards](glossary/standard.glossary.md): When working in a scoped context (e.g. C++ code),
   load the relevant standard from `standards/` and validate
   output against its [PADU table](glossary/padu-scale.glossary.md). Standards follow a hierarchical model; ensure you load the relevant parent standard (e.g. [Kernel Standard](standards/kernel.standard.md)) for global rules.
3. [Skills](glossary/skill.glossary.md): Atomic actions are defined in `skills/`. Read the
   [frontmatter](glossary/frontmatter.glossary.md) to find relevant skills, then load the body when needed, the body defines how to effectively utilize a tool or apply a skill.
4. [Drivers](glossary/driver.glossary.md): Directly executable logic (Python/Bash) that implements a Skill's mechanics.
5. [Instructions](glossary/instruction.glossary.md): Multi-step workflows in `instructions/`.
6. [Prompts](glossary/prompt.glossary.md): Standalone AI instructions in `prompts/`.
7. [Agents](glossary/agent.glossary.md): Autonomous agent definitions in `agents/`.

### Context Management ###
Save important information collected during a conversation in [/context/](context/) in appropriately named files for the context of the information. This is useful for organizing long term memory of a conversation or project.

## File Discovery

All content files use YAML [frontmatter](glossary/frontmatter.glossary.md). To find relevant files:
- Scan frontmatter `tags` and `scope` fields
- Use `glossary_refs` and `standards` fields to resolve dependencies
- Load file bodies only when the frontmatter indicates relevance ([Progressive Disclosure](glossary/progressive-disclosure.glossary.md))

## Constraints

- Never redefine a concept that exists in the glossary. Link to it.
- Validate output against applicable standards before presenting.
- Prefer solutions rated P or A on the [PADU scale](glossary/padu-scale.glossary.md).
- D-rated solutions require explicit justification.
- U-rated solutions must never be proposed.
