---
id: context.glossary
title: Context
type: glossary
version: 1
created: 2026-04-28
updated: 2026-04-28
tags: [core, memory, documentation]
summary: Important information collected during a conversation or project, persisted for long-term memory.
aliases: [background, conversation-history, project-state]
related: [save-conversation-context.skill]
---

# Context

**Context** refers to the persistent state and knowledge gathered during interactions. In the AI Kernel, context is explicitly managed to overcome the limitations of transient conversation windows.

## Usage

- **Directory**: Stored in the `/context/` folder.
- **Persistence**: Unlike conversation logs, context files are curated and maintained as part of the repository.
- **Agent Awareness**: Agents use context files to understand project-specific nuances without needing to be re-taught in every session.
