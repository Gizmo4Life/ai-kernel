---
id: agent-file.standard
title: Agent File Standard
type: standard
version: 2
created: 2026-04-28
updated: 2026-05-02
tags: [governance, agent]
summary: Standards for defining autonomous agents, their roles, and authority.
scope: agents/
parent_standard: kernel.standard
glossary_refs: [ agent.glossary, authority.glossary, delegation.glossary ]
---

# Agent File Standard

## Abstract
This standard defines the requirements for defining autonomous agents within the AI Kernel. It ensures that every agent has a clear objective, defined boundaries of authority, and a PADU-governed behavioral policy. This consistency allows agents to reliably delegate tasks to one another without violating repository safety or quality rules.

## Related Standards
- [Kernel Standard](kernel.standard.md): The root standard governing all kernel components.
- [Skill File](skill-file.standard.md): Governs the atomic actions agents use.
- [Instruction File](instruction-file.standard.md): Governs the complex workflows agents execute.

## PADU Table

| Practice | Rating | Rationale | Exception |
|---|---|---|---|
| Define `authority` level | **P** | Explicitly states if an agent can propose or just suggest. | None |
| Include an Agent PADU table | **P** | Defines the behavioral constraints and preferences. | None |
| List `delegates` | **P** | Establishes the agent's "chain of command" or peer network. | None |
| Define `context` requirements | **P** | States which standards/skills the agent must load to function. | None |
| Circular Delegation | **U** | Risk of infinite logic loops between agents. | None |

## Rationale
Agents are the "active" nodes of the kernel. Standardizing their definition ensures that the human user can trust the boundaries of an agent's autonomy and understand how it interacts with other system components.
