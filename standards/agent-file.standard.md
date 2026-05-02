---
id: agent-file.standard
title: Agent File Standard
type: standard
version: 3
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
This standard defines the requirements for defining autonomous agents within the AI Kernel. It ensures that every agent has a clear objective, defined boundaries of authority, and a PADU-governed behavioral policy.

## PADU Table

| Practice | Rating | Rationale | Enforcement | Exception |
|---|---|---|---|---|
| Define `authority` level | **P** | Explicitly states agent power. | `audit-frontmatter-completeness.skill` | None |
| Include Agent PADU table | **P** | Defines behavioral constraints. | Agent Audit (Auditor) | None |
| List `delegates` | **P** | Establishes chain of command. | `verify-repository-integrity.instruction` | None |
| Define `context` requirements | **P** | States necessary knowledge. | `verify-repository-integrity.instruction` | None |
| Circular Delegation | **U** | Risk of infinite logic loops. | Agent Audit (Auditor) | None |

## Rationale
Standardizing agent definitions ensures that the human user can trust the boundaries of an agent's autonomy and understand how it interacts with other system components.
