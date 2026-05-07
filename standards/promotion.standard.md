---
id: promotion.standard
title: Promotion Standard
type: standard
tags: [governance, evolution, patterns, rules, compliance]
summary: Rules for promoting knowledge from raw context to formal core files.
requirements: [parent_standard, "## PADU Table", "## Enforcement", "## Context", "## Context
This standard defines the "Path to Core" for all new knowledge. it prevents the `context/` directory from becoming a dumping ground by mandating that emerging patterns be codified once they reach a specific "Density" threshold.

## Promotion Thresholds
- **Tier 2 (SME) Draft**: 1-2 occurrences of a pattern in `context/`. No formal standard required yet.
- **Discouraged (D)**: 3 occurrences without a standard. Flagged by the **Standards Scout**.
- **Mandatory Promotion**: 5+ occurrences or use in a critical `instruction`. MUST be codified into a **Standard** or **Glossary Entry**.

## PADU Table

| Practice | Rating | Rationale | Enforcement | Exception |
|---|---|---|---|---|
| 3-Strike Codification | **P** | Codify once a pattern appears 3 times. | `standards-scout.agent` | Experimental code |
| Promote to Atomic Child | **P** | Keep standards small and linked. | `generate-padu-table.skill` | None |
| Link context to Standard | **P** | Shows the "Origin Story" of the rule. | `linkage-specialist.agent` | None |
| Ghost Standards | **U** | Operating by rules not in the `standards/` folder. | `semantic-auditor.agent` | None |
| Context Stagnation | **U** | Leaving 5+ patterns un-codified in `context/`. | `standards-scout.agent` | None |

"Hardness" comes from the transition of soft context into hard standards. By mandating promotion, we ensure that the kernel's "Experience" is constantly being refined into enforceable rules.

## Enforcement
The posture is **Agent-Audited**. The **Standards Scout** is tasked with "Searching for Density" and proposing promotions via the `codify-emerging-pattern.instruction`.

### Gaps
#### Pattern Fragmentation
**Risk**: A pattern might exist 10 times but using slightly different terms, hiding its density from the Scout.
**Be Wary Of**: Similar logic across different `context/` files that should be unified.
