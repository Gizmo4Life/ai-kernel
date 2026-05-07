---
id: agent-file.standard
title: Agent File Standard
type: standard
tags: [governance, agent, rules, compliance]
summary: Standards for defining autonomous agents, emphasizing the 2-tier delegation model and protocol-delegation.
glossary_refs: [delegation.glossary, agent.glossary, standard.glossary, context.glossary, instruction.glossary, skill.glossary]
---# Agent File Standard

## Context
This standard defines the requirements for autonomous agents within the AI Kernel. It enforces a **2-Tier Delegation Model** and a **Protocol-Delegation** pattern to ensure clear ownership and prevent procedural drift.

## PADU Table

| Practice | Rating | Rationale | Enforcement |
|---|---|---|---|
| [Protocol Delegation] | **P** | Workflows are thin stubs that delegate to canonical instructions. | Manual Audit |
| [Finite Compliance] | **P** | Execution is bounded by a checklist with build-test validation gates. | Manual Audit |
| [Logic Density Limit] | **P** | Workflows MUST contain < 5 lines of procedural logic. | Manual Audit |
| Define Agent Tier (1 or 2) | **P** | Clarifies the agent's role in the hierarchy. | doc-audit.skill |
| Inline Workflow Logic | **D** | Embedding protocol steps directly in agent files instead of delegating. | Standard Review |
| Unbounded Execution | **U** | Agent execution without a finite checklist or definition of done. | Blocked Merge |

## Enforcement
The posture for agents is **Hybrid-Automated**. Structural elements are enforced via `verify-repository-integrity.instruction`. Protocol delegation and logic density still require semantic audit by the **evaluate-against-standard.skill**.

## Architecture

```mermaid
graph TD
```
