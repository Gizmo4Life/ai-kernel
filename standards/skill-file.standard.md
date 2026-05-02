---
id: skill-file.standard
title: Skill File Standard
type: standard
version: 4
created: 2026-04-28
updated: 2026-05-02
tags: [automation, quality, atomicity]
summary: Standards for defining atomic skills, emphasizing atomicity and tool clarity.
scope: skills/
parent_standard: kernel.standard
glossary_refs: [skill.glossary, atomicity.glossary]
---

# Skill File Standard

## Abstract
This standard governs the creation of atomic skills. It enforces the "Single Tool, Single Action" principle to ensure that skills remain modular and predictable.

## PADU Table

| Practice | Rating | Rationale | Enforcement | Exception |
|---|---|---|---|---|
| Maintain [Atomicity](glossary/atomicity.glossary.md) | **P** | Ensures skills are reusable. | `audit-for-architectural-violations.skill` | None |
| Define `tool` in frontmatter | **P** | Agents must know the tool. | `audit-frontmatter-completeness.skill` | None |
| Use single tool per skill | **P** | Prevents side effects. | `audit-for-architectural-violations.skill` | None |
| Define `inputs` and `outputs` | **P** | Contract for orchestration. | `audit-frontmatter-completeness.skill` | None |
| Multi-tool logic in one skill | **U** | Violates atomicity. | `audit-for-architectural-violations.skill` | None |

## Rationale
By forcing skills to be atomic and linking them to specific architectural audit skills, we ensure that the building blocks of the kernel remain modular and easy to re-compose.
