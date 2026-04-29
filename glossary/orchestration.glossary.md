---
id: orchestration.glossary
title: Orchestration
type: glossary
version: 1
created: 2026-04-28
updated: 2026-04-28
tags: [core, workflow, instruction.glossary ]
summary: The coordination of multiple atomic skills to achieve a high-level goal or instruction.
aliases: [sequencing, workflow-management]
related: [ instruction.glossary, skill.glossary, atomicity.glossary ]
---

# Orchestration

**Orchestration** is the process of sequencing **Skills** and **Quality Gates** to fulfill an **Instruction**.

## Characteristics

- **Multi-Skill**: Instructions use orchestration to link search, analysis, and modification skills.
- **Goal-Oriented**: Focuses on the final outcome rather than individual tool invocations.
- **Conditional**: Orchestration often includes branching logic (e.g., "If audit fails, go back to Step 2").
