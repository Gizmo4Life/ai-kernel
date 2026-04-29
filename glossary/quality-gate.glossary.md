---
id: quality-gate.glossary
title: Quality Gate
type: glossary
version: 1
created: 2026-04-28
updated: 2026-04-28
tags: [core, quality, workflow]
summary: A checkpoint in an instruction or workflow where a standard is applied to validate the current state of work.
aliases: [checkpoint, validation-step]
related: [ standard.glossary, instruction.glossary ]
---

# Quality Gate

A **Quality Gate** is a mandatory validation step within an **Instruction**. It ensures that no work proceeds to the next stage unless it meets the criteria defined in a specific **Standard**.

## Implementation

In the AI Kernel, quality gates are implemented by invoking the `evaluate-against-standard` skill. If the output contains **U** (Unacceptable) ratings, the gate remains closed until corrections are made.
