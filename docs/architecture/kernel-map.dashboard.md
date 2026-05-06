---
id: kernel-map.dashboard
title: AI Kernel Master Map
type: dashboard
tags: [architecture, orientation, map]
summary: The supreme visual orientation layer for the AI Kernel, linking global governance to local component implementation.
glossary_refs: [agent.glossary, context.glossary, instruction.glossary, orchestration.glossary, skill.glossary, standard.glossary]
---

# AI Kernel Master Map

## Context
This dashboard serves as the **Entry Point** for the AI Kernel. It visualizes the relationships between the root standards and the atomic folders where the logic resides.

## Architecture

```mermaid
graph TD
```

## Navigation Layer

| Domain | Description | Technical README |
|---|---|---|
| **Standards** | Global rules and quality bars. | [standards/README.md](../standards/README.md) (ID: standards-manifest.md) |
| **Skills** | Atomic logic and tool usage. | [skills/README.md](../skills/README.md) (ID: skills-manifest.md) |
| **Instructions** | Workflows and orchestration. | [instructions/README.md](../instructions/README.md) (ID: instructions-manifest.md) |
| **Agents** | Autonomous roles and Tiers. | [agents/README.md](../agents/README.md) (ID: agents-manifest.md) |
| **Glossary** | Single source of truth for terms. | [glossary/README.md](../glossary/README.md) (ID: glossary-manifest.md) |
| **Prompts** | Reusable AI instructions. | [prompts/README.md](../prompts/README.md) (ID: prompts-manifest.md) |

## Persona Orientation

### For Consumers (Agent Integrators)
- Start with the **[Kernel Standard](../standards/kernel.standard.md)** to understand the interface rules.
- Review the **[Skill Registry](../skills/README.md)** for available atomic actions.

### For Maintainers (Kernel Developers)
- Review the **[Self-Healing Loop](../instructions/maintain-kernel-integrity.instruction.md)**.
- Refer to the **[Operability Standard](../standards/operability.standard.md)** for restoration kits.
