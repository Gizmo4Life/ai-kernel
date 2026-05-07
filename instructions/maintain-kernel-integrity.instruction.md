---
id: maintain-kernel-integrity.instruction
title: Maintain Kernel Integrity
type: instruction
tags: [workflow, audit, self-healing, maintenance, process, orchestration]
summary: A self-healing loop that audits the repository for architectural decay and addresses violations iteratively until compliance is achieved.
parent_standard: instruction-file.standard
skills: [global-healing-wave.skill, trace-impact-chain.skill, track-enforcement-posture.skill, detect-circular-delegation.skill, evaluate-against-standard.skill, check-id-uniqueness.skill, audit-repository-connectivity.skill, auto-link-glossary.skill, surgical-refactor.skill]
instructions: [refactor-to-kernel-standards.instruction, validate-kernel-integrity.instruction, codify-emerging-pattern.instruction]
standards: [kernel.standard, quality-gate.standard, versioning.standard, promotion.standard]
preconditions:
  - Flynn's analytical cabinet is online.
glossary_refs: [agent.glossary, context.glossary, delegation.glossary, frontmatter.glossary, instruction.glossary, prompt.glossary, skill.glossary, standard.glossary]
---

# Maintain Kernel Integrity

## Context
The AI Kernel is a complex, evolving Knowledge Graph. Without automated maintenance, "Entropy" causes naming collisions, orphaned nodes, and semantic drift. This instruction establishes a **Deterministic Self-Healing Loop** that ensures the repository remains "Hardened" as it scales.

## Architecture

```mermaid
graph TD
    instruction-file.standard --> maintain-kernel-integrity.instruction
    maintain-kernel-integrity.instruction --> global-healing-wave[global-healing-wave.skill]
    maintain-kernel-integrity.instruction --> trace-impact-chain[trace-impact-chain.skill]
    maintain-kernel-integrity.instruction --> track-enforcement-posture[track-enforcement-posture.skill]
    maintain-kernel-integrity.instruction --> detect-circular-delegation[detect-circular-delegation.skill]
    maintain-kernel-integrity.instruction --> evaluate-against-standard[evaluate-against-standard.skill]
    maintain-kernel-integrity.instruction --> check-id-uniqueness[check-id-uniqueness.skill]
    maintain-kernel-integrity.instruction --> audit-repository-connectivity[audit-repository-connectivity.skill]
    maintain-kernel-integrity.instruction --> auto-link-glossary[auto-link-glossary.skill]
    maintain-kernel-integrity.instruction --> surgical-refactor[surgical-refactor.skill]
```

## Execution Steps

### 1. Audit Phase (Detection)
Invoke the **[Hardened Audit Suite]**:
- **Safety**: Run `detect-circular-delegation.skill` to ensure a DAG.
- **Structural**: Run `check-id-uniqueness.skill` and `audit-repository-connectivity.skill`.
- **Compliance**: Run `evaluate-against-standard.skill` on any modified files.

### 2. Triage Phase (Prioritization)
Use `trace-impact-chain.skill` to analyze the "Blast Radius" of identified violations. Rank issues by their systemic risk.

### 3. Healing Phase (Remediation)
Execute the **[Restoration Wave]**:
- **Mass Restoration**: Run `global-healing-wave.skill` to repair frontmatter, links, and diagrams.
- **Surgical Refactor**: Invoke `surgical-refactor.skill` for complex structural repairs.
- **Maturity Check**: Run `track-enforcement-posture.skill` to verify the new automation coverage.

### 4. Verification Pass (Validation)
Re-run the **Audit Phase**. Loop until the `global-gap-report.md` shows **Zero Fails**.

## Postconditions
1. The system state matches the goal defined in the frontmatter.
2. All related Knowledge Graph nodes are updated and linked.

## Quality Gate

Maintenance health is governed by the **[Kernel Standard](../standards/kernel.standard.md)**.
- **Verification**: Zero collisions, Zero orphans, and 100% Versioning compliance.
- **Enforcement**: Flynn will not approve any PR that has an ID collision or a disconnected node.
