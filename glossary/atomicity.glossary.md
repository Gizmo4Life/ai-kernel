---
id: atomicity.glossary
title: Atomicity
type: glossary
version: 1
created: 2026-04-28
updated: 2026-04-28
tags: [core, technical, skill.glossary ]
summary: The principle that a skill should perform a single, indivisible action using a single tool.
aliases: [single-responsibility]
related: [ skill.glossary, orchestration.glossary ]
---

# Atomicity

**Atomicity** is the core design principle for **Skills** in the AI Kernel.

## Principles

- **Single Action**: A skill should do one thing (e.g., "Search", "Update File").
- **Single Tool**: A skill should rely on one primary tool (e.g., `grep`, `editor`).
- **Statelessness**: A skill should not rely on the side effects of other skills beyond its explicit inputs.

Atomic skills are easier to test, reuse, and sequence into complex **Instructions**.
