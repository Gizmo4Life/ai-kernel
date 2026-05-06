---
id: orchestration.glossary
title: Orchestration
type: glossary
tags: [core, workflow, instruction.glossary, definition, term, meaning]
summary: The coordination of multiple atomic skills to achieve a high-level goal or instruction.
aliases: [sequencing, workflow-management]
related: [ instruction.glossary, skill.glossary, atomicity.glossary ]
---

## Context
Canonical definition of a core AI Kernel concept.


# Orchestration

**Orchestration** is the process of sequencing **Skills** and **Quality Gates** to fulfill an **Instruction**.


## Architecture

```mermaid
graph TD
```
## Characteristics

- **Multi-Skill**: Instructions use orchestration to link search, analysis, and modification skills.
- **Goal-Oriented**: Focuses on the final outcome rather than individual tool invocations.
- **Conditional**: Orchestration often includes branching logic (e.g., "If audit fails, go back to Step 2").

## Usage Constraints
- This term must only be used in its architectural context.
- Semantic drift from the canonical definition is Unacceptable (U).
