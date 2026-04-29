---
id: progressive-disclosure.glossary
title: Progressive Disclosure
type: glossary
version: 1
created: 2026-04-28
updated: 2026-04-28
tags: [core, optimization, scanning]
summary: A design pattern where information is revealed in stages (frontmatter first, body later) to minimize token consumption and context window pressure.
aliases: [staged-loading, lazy-loading]
related: [frontmatter.glossary]
---

# Progressive Disclosure

**Progressive Disclosure** is an optimization strategy for AI agents. It involves providing just enough information for the agent to decide if a file is relevant before loading the entire content.

## Implementation

In the AI Kernel, this is achieved by:
1. **Scanning**: Agents first read only the YAML frontmatter of potential files.
2. **Decision**: Based on the `summary`, `tags`, and `id`, the agent decides if the file is needed.
3. **Fetching**: The agent then loads the full body of only the relevant files.

This significantly reduces token costs and keeps the agent's context focused on the task at hand.
