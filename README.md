---
id: kernel-root-manifest
title: AI Kernel Root
type: manifest
summary: The central entry point and organizational overview of the AI Kernel framework.
---

# AI Kernel

The **AI Kernel** is a personal development sidecar and workflow framework. It codifies glossary definitions, coding standards, skills, instructions, prompts, and agent definitions into a machine-traversable Knowledge Graph.

## Repository Structure

The kernel is organized into 7 core functional domains:

1. **[Agents](agents/README.md)**: Autonomous actors and Tier 2 SMEs (Flynn, Librarian, etc.).
2. **[Standards](standards/README.md)**: PADU-rated quality bars and architectural rules.
3. **[Skills](skills/README.md)**: Atomic, tool-using logic nodes.
4. **[Instructions](instructions/README.md)**: Multi-step orchestrated workflows.
5. **[Glossary](glossary/README.md)**: Canonical definitions and the Specificity Hierarchy.
6. **[Prompts](prompts/README.md)**: Reusable AI system instructions and templates.
7. **[Context](context/README.md)**: Conversation logs, decisions, and learning data.

## Core Principles
- **Atomicity**: Every skill performs exactly one technical action.
- **Orchestration**: Instructions coordinate skills; they do not perform raw tool actions.
- **Single Source of Truth**: All definitions reside in the Glossary.
- **Self-Healing**: The kernel maintains its own integrity via the **[Maintain Kernel Integrity](instructions/maintain-kernel-integrity.instruction.md)** workflow.

## Usage
To use this framework, load the **[Kernel Standard](standards/kernel.standard.md)** and delegate tasks to **[Flynn](agents/flynn.agent.md)** or the **[Operator](agents/operator.agent.md)**.
