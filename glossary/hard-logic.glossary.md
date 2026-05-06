---
id: hard-logic.glossary
title: Hard Logic
type: glossary
tags: [architecture, logic, stability, definition, term, meaning]
summary: Structural or machine-enforceable rules that define the constraints of the system (Standards, Skills, Globs).
---

# Hard Logic

## Context
"Hard Logic" is the skeleton of the AI Kernel. It stands in contrast to "Soft Logic" (Descriptions, Summaries, Narrative). The Hard Logic must be stable and deterministic to ensure the system remains predictable as it scales.

## Architecture

```mermaid
graph TD
    Hard[Hard Logic: Constraints] --> Enforce[Enforcement: Automated]
    Soft[Soft Logic: Narrative] --> Guide[Guidance: Agentic]
    Enforce --> Stability[Stability: High]
```

## Usage Constraints
- Hard Logic must be defined in a **Standard** or **Skill**.
- Soft Logic must never supersede Hard Logic in a **Quality Gate**.
- Changes to Hard Logic require **Tier 1 (Domain Owner)** approval.
