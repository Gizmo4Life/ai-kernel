---
id: instruction-file.standard
title: Instruction File Standard
type: standard
version: 3
created: 2026-04-28
updated: 2026-05-02
tags: [workflow, quality, orchestration]
summary: Standards for defining multi-step instructions, emphasizing orchestration and quality gates.
scope: instructions/
parent_standard: kernel.standard
glossary_refs: [instruction.glossary, orchestration.glossary, quality-gate.glossary]
---

# Instruction File Standard

## Abstract
This standard governs the creation of multi-step instructions. Unlike atomic skills, instructions are responsible for the [Orchestration](glossary/orchestration.glossary.md) of multiple components to achieve a high-level goal. It mandates the inclusion of quality gates to ensure that workflows maintain repository standards at every stage.

## Related Standards
- [Kernel Standard](kernel.standard.md): The architectural parent setting orchestration expectations.
- [Skill File](skill-file.standard.md): The standard for the atomic units being orchestrated.

## PADU Table

| Practice | Rating | Rationale | Exception |
|---|---|---|---|
| Coordinate via Orchestration | **P** | Instructions must link skills, not implement tools. | None |
| Include a [Quality Gate](glossary/quality-gate.glossary.md) | **P** | Ensures adherence to standards before completion. | Informational flows. |
| Define `preconditions` | **P** | Prevents execution in unstable or invalid environments. | None |
| Skipping quality gates | **U** | Risk of committing sub-standard or corrupt knowledge. | None |

## Rationale
Instructions provide the "safety layer" for the AI Kernel. They codify the human's preferred workflows and ensure that agents follow the same rigorous process every time they perform a complex task.
