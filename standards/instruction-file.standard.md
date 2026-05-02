---
id: instruction-file.standard
title: Instruction File Standard
type: standard
version: 4
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
This standard governs the creation of multi-step instructions. It mandates the inclusion of quality gates and the use of orchestration over tool implementation.

## PADU Table

| Practice | Rating | Rationale | Enforcement | Exception |
|---|---|---|---|---|
| Coordinate via Orchestration | **P** | Links skills, not tools. | `audit-for-architectural-violations.skill` | None |
| Include a [Quality Gate](glossary/quality-gate.glossary.md) | **P** | Adheres to standards. | `audit-for-architectural-violations.skill` | Simple flows |
| Define `preconditions` | **P** | Prevents invalid states. | `audit-frontmatter-completeness.skill` | None |
| Skipping quality gates | **U** | Risk of sub-standard work. | `audit-for-architectural-violations.skill` | None |

## Rationale
Instructions are the orchestrated "programs" of the kernel. Their integrity is enforced by architectural audit skills that verify the presence of quality gates and proper skill sequencing.
