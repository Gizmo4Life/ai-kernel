---
id: skill-file.standard
title: Skill File Standard
type: standard
version: 5
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
Modularity is the key to the AI Kernel's scalability. By forcing skills to be atomic and linking them to specific architectural audit skills, we ensure that the building blocks of the kernel remain modular.

## Enforcement
The posture for skills is **Automated**. We use the `audit-for-architectural-violations.skill` to check for multiple tool mentions and ensure the "Execution Steps" are sufficiently simple.

### Gaps
#### Hidden Tool Dependencies
**Risk**: A skill might claim to use `grep` but actually rely on a secondary tool (like `awk` or `sed`) inside its command string that isn't declared in frontmatter.
**Be Wary Of**: Complex one-liners in "Execution Steps" that chain multiple CLI utilities.

#### Action Over-reach
**Risk**: A skill might use a single tool (`editor`) but perform multiple logical actions (e.g., "Find and Replace" AND "Formatting").
**Be Wary Of**: Skill descriptions that use the word "and" to describe their primary objective.
