---
id: global-healing-wave.skill
title: Global Healing Wave
type: skill
tags: [automation, quality, healing, self-healing, orchestration, tool, action, execution]
interface:
  input: {}
  output: { status: "complete", report_path: "context/global-gap-report.md" }
implementation:
  engine: "python3 engines/master_healer.py"
  command: "python3 engines/master_healer.py"
summary: Orchestrates all hardened tools to perform a repository-wide structural, visual, and semantic restoration.
parent_standard: skill-file.standard
glossary_refs: [context.glossary, skill.glossary, standard.glossary]
---

# Global Healing Wave

## Context
Individual audits and fixes are prone to "Logic Drift." This skill provides a single, atomic command to bring the entire AI Kernel into 100% compliance by coordinating our full suite of deterministic engines.

## Architecture

```mermaid
graph TD
    skill-file.standard --> global-healing-wave.skill
```

## Execution Steps
1. **Engine Invocation**: Run `master_healer.py`.
2. **Review**: Inspect the console output for success/failure of each step.
3. **Certification**: Verify the `context/global-gap-report.md` for final stability scores.

## Verification Protocol
1. Introduce a missing header in a skill.
2. Run `python3 engines/master_healer.py`.
3. Verify that the file is flagged in the final report.

## Quality Gate
- **Verification**: All steps must report `SUCCESS`.
- **Enforcement**: Mandatory step after any mass-refactor or before any major branch merge.
