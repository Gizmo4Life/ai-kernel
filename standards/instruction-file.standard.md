---
id: instruction-file.standard
title: Instruction File Standard
type: standard
version: 5
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

## Enforcement
The posture for instructions is **Automated**. We check for the presence of the `skills:` list in frontmatter and look for "Quality Gate" sections in the markdown body.

### Gaps
#### Gate Effectiveness
**Risk**: An instruction might have a section titled "Quality Gate", but the actual step might be trivial or non-binding (e.g., "Check if the file looks okay").
**Be Wary Of**: Quality gates that do not explicitly invoke the `evaluate-against-standard.skill` or another audit-level skill.

#### Dependency Staleness
**Risk**: Instructions may refer to skills that have been refactored or renamed, leading to runtime failures.
**Be Wary Of**: Broken links in the `skills:` list of the frontmatter. (Enforced by `verify-repository-integrity.instruction`).
