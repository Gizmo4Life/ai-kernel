# AI Kernel

A personal workflow framework for autonomous agents. This repository acts as a machine-readable engineering brain, codifying standards, skills, instructions, and agents to ensure high-integrity development across various AI-assisted environments.

## Directory Structure

- [agents/](agents/README.md): Definitions for autonomous actors and their authority levels.
- [context/](context/README.md): Persistent conversation and project state for long-term memory.
- [glossary/](glossary/README.md): Single source of truth for all concepts and technical terms.
- [instructions/](instructions/README.md): Orchestrated, multi-step workflows with mandatory quality gates.
- [prompts/](prompts/README.md): Reusable, template-driven AI instructions and logic.
- [skills/](skills/README.md): Atomic, tool-centric actions adhering to the single-responsibility principle.
- [standards/](standards/README.md): Hierarchical quality governance (PADU scale) for all repository components.

## Core Principles

- **Single Source of Truth**: All concepts must be defined in the [Glossary](glossary/README.md).
- **Atomicity**: Skills must perform a single action using a single tool.
- **Orchestration**: Complex tasks are handled by Instructions that coordinate atomic skills.
- **Hierarchical Governance**: Standards are tiered from global (Kernel Standard) to domain-specific implementations.

## For AI Agents

Agents should start with [AGENTS.md](AGENTS.md) for canonical instructions and framework usage.
