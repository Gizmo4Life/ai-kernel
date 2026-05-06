---
id: agent-file.standard
title: Agent File Standard
type: standard
requirements: [authority, scope, capabilities, "## Quality Gate"], tags: [governance, agent, rules, compliance]
summary: Standards for defining autonomous agents, emphasizing the 2-tier delegation model.
scope: "/agents/**/*.agent.md"
parent_standards: [ kernel.standard, standard-file.standard ]
prompts: [ id_list ]
glossary_refs: [agent.glossary, authority.glossary, context.glossary, delegation.glossary, domain-owner.glossary, instruction.glossary, orchestration.glossary, skill.glossary, standard.glossary, subject-matter-expert.glossary]
---

# Agent File Standard

## Context
This standard defines the requirements for autonomous agents within the AI Kernel. It enforces a **2-Tier Delegation Model** to ensure clear ownership and prevent conceptual drift between domain management and subject-matter expertise.


## Architecture

```mermaid
graph TD
```
## The Delegation Tiers
- **Tier 1: [Domain Owner](../glossary/domain-owner.glossary.md)**: Custodians of a specific filesystem scope. They orchestrate and maintain their domain.
- **Tier 2: [Subject Matter Expert](../glossary/subject-matter-expert.glossary.md)**: Specialized agents contracted by Tier 1 for analysis or specific modifications.

## PADU Table

| Practice | Rating | Rationale | Enforcement | Exception |
|---|---|---|---|---|
| Mandate 3-Point Profile | **P** | Tokenizes Authority, Scope, and Capabilities. | `doc-audit.skill` | None |
| Define Agent Tier (1 or 2) | **P** | Clarifies the agent's role in the hierarchy. | doc-audit.skill | None |
| Scope-Restricted Authority | **P** | Ensures agents cannot modify files outside their token. | `verify-repository-integrity.instruction` | None |
| Tier 1 Orchestration | **P** | Owners should drive the workflow, not just skills. | `audit-for-architectural-violations.skill` | None |
| Tier 2 owning a domain | **U** | Conflicts with the custodial model. | doc-audit.skill | None |
| Circular Delegation | **U** | Risk of infinite logic loops. | `detect-circular-delegation.skill` | None |

By separating "Ownership" from "Expertise", we allow the AI Kernel to scale. New domains can be added with their own Tier 1 owners, all sharing the same pool of Tier 2 experts.

## Enforcement
The posture for agents is **Hybrid-Automated**. Structural elements and circularity are enforced via `verify-repository-integrity.instruction`. Tier classification and role-to-authority consistency still require semantic audit by the **evaluate-against-standard.skill**.

### Gaps
#### Behavioral Consistency
**Risk**: An agent's PADU table might contradict its Tier classification (e.g., an SME claiming domain ownership).
**Be Wary Of**: SMEs with broad "Preferred" practices that involve repository-wide reorganization.
