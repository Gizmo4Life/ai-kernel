---
id: skill-file.standard
title: Skill File Standard
type: standard
version: 3
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
This standard governs the creation of atomic skills. It enforces the "Single Tool, Single Action" principle to ensure that skills remain modular and predictable. Atomic skills are the building blocks of the AI Kernel, designed to be easily orchestrated into complex instructions or used directly by agents.

## Related Standards
- [Kernel Standard](kernel.standard.md): The architectural parent setting atomicity expectations.
- [Instruction File](instruction-file.standard.md): The standard for coordinating these skills.

## PADU Table

| Practice | Rating | Rationale | Exception |
|---|---|---|---|
| Maintain [Atomicity](glossary/atomicity.glossary.md) | **P** | Ensures skills are reusable across different workflows. | None |
| Define `tool` in frontmatter | **P** | Agents must know which internal tool to invoke. | None |
| Use a single tool per skill | **P** | Prevents complex side effects and hidden dependencies. | None |
| Define `inputs` and `outputs` | **P** | Establishes a machine-readable contract for orchestration. | None |
| Multi-tool logic in one skill | **U** | Violates atomicity; must be an instruction. | None |

## Rationale
Modularity is the key to the AI Kernel's scalability. By forcing skills to be atomic, we ensure that as the repository grows, we can recompose existing functions into new instructions without needing to rewrite core logic.
