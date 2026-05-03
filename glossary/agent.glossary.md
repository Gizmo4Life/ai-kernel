---
id: agent.glossary
title: Agent
type: glossary
tags: [core, autonomy, actor]
summary: An autonomous actor defined by a specific role, a set of skills it can use, and the standards it must follow.
aliases: [persona, bot, actor]
related: [ skill.glossary, instruction.glossary, standard.glossary ]
---

## Context
Canonical definition of a core AI Kernel concept.


# Agent

An **Agent** is a specialized persona that operates within the kernel. It is defined not just by what it can do (skills) but by how it behaves (standards) and what it aims to achieve (role).


## Architecture

```mermaid
graph TD
    Term[Concept Term] --> Definition[Semantic Definition]
    Definition --> Constraints[Usage Constraints]
```
## Attributes

- **Role**: A concise description of the agent's purpose.
- **Skills**: The tools and atomic actions available to the agent.
- **Instructions**: The complex workflows the agent is capable of executing.
- **Autonomy**: Whether the agent can execute changes directly or must propose them for approval.
- **PADU Policy**: Specific constraints on how the agent interprets quality standards.

## Usage Constraints
- This term must only be used in its architectural context.
- Semantic drift from the canonical definition is Unacceptable (U).
