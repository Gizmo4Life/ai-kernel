---
id: audit-for-architectural-violations.skill
title: Audit for Architectural Violations
type: skill
version: 1
created: 2026-04-28
updated: 2026-04-28
tags: [audit, architecture, quality]
summary: Analyzes kernel files for violations of the core architectural principles (Atomicity, Orchestration, Single Source of Truth).
tool: editor
inputs: file_path: The file to audit.
outputs: violations: A list of architectural issues found.
standards: [ skill-file.standard, instruction-file.standard ]
glossary_refs: [ atomicity.glossary, orchestration.glossary, quality-gate.glossary ]
---

# Audit for Architectural Violations

This skill performs a "maximalist" check for architectural integrity.

## Execution Steps

1. **Check for [Atomicity](glossary/atomicity.glossary.md)**: (For Skills) Does the file use more than one tool or perform more than one logical action?
2. **Check for [Orchestration](glossary/orchestration.glossary.md)**: (For Instructions) Does the file perform tool actions directly instead of coordinating skills?
3. **Check for [Quality Gates](glossary/quality-gate.glossary.md)**: (For Instructions) Is there a mandatory validation step using `evaluate-against-standard`?
4. **Check for Inline Definitions**: (Global) Are there concepts defined in the body that should be moved to the glossary?
5. **Check for Cross-Linking**: Are key terms linked to the glossary?
6. **Report**: provide a detailed list of violations for the refactor loop.
