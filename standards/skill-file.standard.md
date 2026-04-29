---
id: skill-file.standard
title: Skill File Standard
type: standard
version: 2
created: 2026-04-28
updated: 2026-04-28
tags: [automation, quality]
summary: Standards for defining atomic skills in the `skills/` directory, emphasizing atomicity and tool clarity.
scope: skills/
applies_to: [skill.glossary]
glossary_refs: [ skill.glossary, atomicity.glossary ]
---

# Skill File Standard

Governs the structure of all files in the `skills/` directory.

## PADU Table

| Practice | Rating | Rationale | Exception |
|---|---|---|---|
| Maintain [Atomicity](glossary/atomicity.glossary.md) | **P** | Ensures skills are reusable and predictable. | None |
| Define `tool` in frontmatter | **P** | Agents need to know which internal tool to invoke. | None |
| Use a single tool per skill | **P** | Prevents complex side effects and makes testing easier. | None |
| Define `inputs` and `outputs` | **P** | Establishes a clear machine-readable contract. | None |
| Link to `standards` | **P** | Ensures the skill's output meets repo quality bars. | Informational skills. |
| Combining multiple tool actions | **U** | Violates atomicity; should be an instruction. | None |
| Multi-step logic (>3 steps) | **D** | Indicators of an instruction disguised as a skill. | Trivial sub-steps. |

## Rationale

Skills are the "atomic functions" of the AI Kernel. They must be modular, stateless, and focused on a single outcome to be effectively orchestrated.
