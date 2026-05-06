---
id: padu-scale.glossary
title: PADU Scale
type: glossary
tags: [core, quality, governance, definition, term, meaning]
summary: The four-tier rating system (Preferred, Acceptable, Discouraged, Unacceptable) used to evaluate technical practices and repository health.
aliases: [quality-scale, rating-system]
related: [standard.glossary, quality-gate.glossary]
---

## Context
Canonical definition of a core AI Kernel concept.


# PADU Scale

The **PADU Scale** is the kernel's mechanism for objective quality governance. Every [Standard](../standards/README.md) contains a PADU table that classifies practices into one of four categories.


## Architecture

```mermaid
graph TD
```
## The Ratings

| Rating | Name | Description |
|---|---|---|
| **P** | **Preferred** | The ideal way to perform a task. Should be the default choice. |
| **A** | **Acceptable** | A valid alternative when **P** is not feasible or optimal. |
| **D** | **Discouraged** | A pattern that works but has known flaws or technical debt. Requires justification. |
| **U** | **Unacceptable** | A pattern that is strictly forbidden. Must be refactored immediately. |

## Enforcement Column
Every PADU table now includes an **Enforcement** column. This column identifies the tool, skill, or manual process used to detect violations of the standard. 

- **Automated**: Linked to a specific [Skill](../skills/README.md) or regex.
- **Agent-Audited**: Relies on the **Standards Auditor** or **Flynn** to identify during a pass.
- **Manual**: Requires human verification during a quality gate.

## Usage Constraints
- This term must only be used in its architectural context.
- Semantic drift from the canonical definition is Unacceptable (U).
