---
id: perform-meta-audit.instruction
title: Perform Meta-Audit
type: instruction
tags: [workflow, audit, quality, process, orchestration]
summary: The master workflow for coordinating all individual auditors and generating a synthesized system health report.
parent_standard: instruction-file.standard
skills: [auto-link-glossary.skill, surgical-refactor.skill, search-kernel.skill, doc-audit.skill, check-id-uniqueness.skill, audit-repository-connectivity.skill, doc-audit.skill, tel-audit.skill, triage-architectural-violations.skill]
standards: [kernel.standard, quality-gate.standard]
preconditions:
  - Repository is in a "Stable" state (all files saved).
glossary_refs: [context.glossary, frontmatter.glossary, skill.glossary]
---

# Perform Meta-Audit

## Context
The Meta-Audit is the "Supreme Court" of the AI Kernel. It runs every specialized auditor and uses the **Triage Skill** to produce a single, prioritized backlog of work.

## Architecture

```mermaid
graph TD
    instruction-file.standard
goal --> perform-meta-audit.instruction
    perform-meta-audit.instruction --> check-id-uniqueness[check-id-uniqueness.skill]
    perform-meta-audit.instruction --> audit-repository-connectivity[audit-repository-connectivity.skill]
    perform-meta-audit.instruction --> doc-audit[doc-audit.skill]
    perform-meta-audit.instruction --> tel-audit[tel-audit.skill]
    perform-meta-audit.instruction --> triage-architectural-violations[triage-architectural-violations.skill]
```

## Execution Steps
1. **Structural Pass**: Run `check-id-uniqueness.skill` and `audit-frontmatter-completeness.skill`.
2. **Connectivity Pass**: Run `audit-repository-connectivity.skill`.
3. **Semantic Pass**: Run `doc-audit.skill` and `tel-audit.skill`.
4. **Synthesis**: Pass all findings to `triage-architectural-violations.skill`.
5. **Reporting**: Create a new `context/supreme-audit-[version].md` report.

## Postconditions
1. A new, dated supreme audit report exists in `/context/`.
2. The report identifies 100% of P0-P3 violations currently present in the graph.

## Quality Gate
- **Verification**: The Meta-Audit must be reproducible.
- **Enforcement**: No "Push" to stable is allowed if the Meta-Audit report contains P0 or P1 violations.
