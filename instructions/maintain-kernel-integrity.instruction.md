---
id: maintain-kernel-integrity.instruction
title: Maintain Kernel Integrity
type: instruction
tags: [workflow, audit, self-healing, maintenance, process, orchestration]
summary: A self-healing loop that audits the repository for architectural decay and addresses violations iteratively until compliance is achieved.
parent_standard: instruction-file.standardgoal: A 100% compliant repository with zero Unacceptable (U) or Discouraged (D) violations.
skills: [evaluate-against-standard.skill, check-id-uniqueness.skill, audit-repository-connectivity.skill, extract-prompt.skill]
instructions: [refactor-to-kernel-standards.instruction, validate-kernel-integrity.instruction, codify-emerging-pattern.instruction]
standards: [kernel.standard, quality-gate.standard, versioning.standard, promotion.standard]
preconditions:
  - Flynn's analytical cabinet is online.
glossary_refs: [agent.glossary, context.glossary, frontmatter.glossary, instruction.glossary, skill.glossary, standard.glossary]
---

# Maintain Kernel Integrity

## Context
The AI Kernel is a complex, evolving Knowledge Graph. Without automated maintenance, "Entropy" causes naming collisions, orphaned nodes, and semantic drift. This instruction establishes a **Deterministic Self-Healing Loop** that ensures the repository remains "Hardened" as it scales.

## Architecture

```mermaid
graph TD
    instruction-file.standardgoal --> maintain-kernel-integrity.instruction
    maintain-kernel-integrity.instruction --> evaluate-against-standard[evaluate-against-standard.skill]
    maintain-kernel-integrity.instruction --> check-id-uniqueness[check-id-uniqueness.skill]
    maintain-kernel-integrity.instruction --> audit-repository-connectivity[audit-repository-connectivity.skill]
    maintain-kernel-integrity.instruction --> extract-prompt[extract-prompt.skill]
```

## Steps

### 1. Audit Phase (Detection)
Flynn invokes the **[Cabinet Audit Workflow](flynn.agent.md#interaction-pattern)**:
- **Integrity Guardian**: Structural check + **[Check ID Uniqueness](../skills/check-id-uniqueness.skill.md)**.
- **Linkage Specialist**: Connectivity check + **[Audit Repository Connectivity](../skills/audit-repository-connectivity.skill.md)**.
- **Semantic Auditor**: Logic check.
- **Standards Auditor**: Compliance check.
- **Librarian**: **Manifest Check** (Ensure READMEs are up-to-date).
- **Standards Scout**: **[Promotion Analysis](../standards/promotion.standard.md)**.

### 2. Triage Phase (Prioritization)
Flynn ranks the identified violations:
1. **Critical (U)**: **ID Collisions**, Circularity, missing frontmatter.
2. **Structural (U)**: **Orphaned nodes**, non-atomic skills.
3. **Evolutionary (U/D)**: Patterns requiring **Promotion**, Versioning drift.

### 3. Healing Phase (Remediation)
Flynn iterates through the prioritized list:
- **Refactor**: Invoke **[Refactor to Kernel Standards](refactor-to-kernel-standards.instruction.md)**.
- **Codification**: If the **Standards Auditor** flags an "Enforcement Gap" or an un-codified pattern, invoke the **Standards Scout** via **[Codify Emerging Pattern](codify-emerging-pattern.instruction.md)**.
- **Manifests**: Task the **Librarian** to regenerate or update `README.md` files to reflect new core files.
- **Linkage**: For every orphaned node, task the **Linkage Specialist** to find a parent standard or related term.
- **Versioning**: Update `version` and `updated` fields according to the **[Versioning Standard](../standards/versioning.standard.md)**.

### 4. Verification Pass (Validation)
Re-run the **Audit Phase** on the modified files. Loop until zero **Unacceptable (U)** violations remain.


## Postconditions
1. The system state matches the goal defined in the frontmatter.
2. All related Knowledge Graph nodes are updated and linked.

## Quality Gate

Maintenance health is governed by the **[Kernel Standard](../standards/kernel.standard.md)**.
- **Verification**: Zero collisions, Zero orphans, and 100% Versioning compliance.
- **Enforcement**: Flynn will not approve any PR that has an ID collision or a disconnected node.
