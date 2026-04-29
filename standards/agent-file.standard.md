---
id: agent-file.standard
title: Agent File Standard
type: standard
version: 2
created: 2026-04-28
updated: 2026-04-28
tags: [autonomy, persona, quality]
summary: Standards for defining autonomous agents in the `agents/` directory, including authority and delegation.
scope: agents/
applies_to: [agent.glossary]
glossary_refs: [ agent.glossary, padu-scale.glossary ]
---

# Agent File Standard

Governs the structure of all files in the `agents/` directory.

## PADU Table

| Practice | Rating | Rationale | Exception |
|---|---|---|---|
| Define `authority` in frontmatter | **P** | Explicitly states if the agent can `propose` or `suggest`. | None |
| Include a PADU table in the body | **P** | Constrains the agent's approach to problem solving. | None |
| Define `delegates` in frontmatter | **P** | Defines which other agents this agent can task. | None |
| Define `context` in frontmatter | **P** | Lists glossary, standards, and instructions relevant to the agent. | None |
| Define `role` in frontmatter | **A** | Broad purpose of the agent. | None |
| Granting 'execute' authority | **D** | High risk; prefer 'propose' for most agents. | Low-risk audit agents. |

## Rationale

Agents must have well-defined boundaries and toolkits. The inclusion of an internal PADU table ensures the agent evaluates its own proposed solutions against project-specific values before presenting them.
