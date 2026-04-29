---
id: instruction-file.standard
title: Instruction File Standard
type: standard
version: 2
created: 2026-04-28
updated: 2026-04-28
tags: [workflow, quality]
summary: Standards for defining multi-step instructions, emphasizing orchestration and quality gates.
scope: instructions/
applies_to: [instruction.glossary]
glossary_refs: [ instruction.glossary, orchestration.glossary, quality-gate.glossary ]
---

# Instruction File Standard

Governs the structure of all files in the `instructions/` directory.

## PADU Table

| Practice | Rating | Rationale | Exception |
|---|---|---|---|
| Use [Orchestration](glossary/orchestration.glossary.md) | **P** | Instructions should coordinate skills, not implement tools. | None |
| Include a [Quality Gate](glossary/quality-gate.glossary.md) | **P** | Ensures work meets standard before proceeding or finishing. | Simple informational flows. |
| Define `preconditions` | **P** | Prevents execution in an unstable or invalid state. | None |
| List all `skills` required | **P** | Provides a clear manifest for the agent's toolbox. | None |
| Hardcoding specific paths | **D** | Reduces reusability across projects. | Root repo maintenance. |
| Manual validation steps | **A** | Necessary when automated audit is impossible. | None |
| Skipping quality gates | **U** | Allows sub-standard content to be committed. | None |

## Rationale

Instructions are the "programs" of the AI Kernel. They provide the safety and consistency needed for complex multi-agent workflows.
