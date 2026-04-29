---
id: authority.glossary
title: Authority
type: glossary
version: 1
created: 2026-04-28
updated: 2026-04-28
tags: [core, autonomy, agent.glossary ]
summary: The level of permission granted to an agent to either propose changes for review or suggest actions without direct modification.
aliases: [permission-level, autonomy-rank]
related: [ agent.glossary, agent-file.standard ]
---

# Authority

**Authority** defines the boundaries of an agent's power within the repository.

## Levels

- **Propose**: The agent can generate code changes or new files and present them for user approval.
- **Suggest**: The agent can only provide textual recommendations or analysis without drafting specific file modifications.
- **Execute**: (Discouraged) The agent can commit changes directly. This level is reserved for high-confidence maintenance tasks.
