---
id: naming.standard
title: Naming Standard
type: standard
tags: [governance, organization, naming, rules, compliance]
summary: Rules for unambiguous file naming and ID assignment in the AI Kernel.
requirements: [parent_standard, "## PADU Table", "## Enforcement", "## Context", "## Context
This standard defines the "Unambiguous Naming" policy for the AI Kernel. It ensures that in a flat filesystem, files remain distinct and their purpose is immediately obvious through their filename. It prevents the "canonical term pollution" where a specific concept usurps a general term.

## The Specificity Hierarchy
- **Level 1 (Root)**: Abstract, kernel-level concepts. Use simple, canonical terms (e.g., `test.md`, `standard.md`).
- **Level 2 (Domain)**: Concepts specific to a technical domain or folder. MUST use a domain prefix (e.g., `js-test.md`, `agent-standard.md`).
- **Level 3 (Implementation)**: Highly specific instances. Use multiple qualifiers (e.g., `react-component-unit-test.md`).

## PADU Table

| Practice | Rating | Rationale | Enforcement | Exception |
|---|---|---|---|---|
| Domain-Prefixed naming | **P** | Prevents conflation in a flat filesystem. | `find-similar-terms.skill` | Root concepts |
| Namespace Qualification | **P** | `[domain]-[concept]` is the ideal format. | `audit-frontmatter-completeness.skill` | None |
| Using synonyms for clarity | **A** | Helps distinguish between similar actions. | evaluate-against-standard.skill (Flynn) | None |
| Canonical term usurping | **U** | Using a broad term for a narrow concept. | `find-similar-terms.skill` | None |
| ID vs Alias collision | **U** | Using an ID that exists elsewhere as an alias. | `find-similar-terms.skill` | None |

In a decentralized Knowledge Graph, naming collisions are the primary source of logic drift. By enforcing a domain-prefixed naming scheme, we ensure that an agent can safely add `python-test` without worrying about overwriting or conflating it with `kernel-test`.

## Enforcement
The posture is **Hybrid-Automated**. `find-similar-terms.skill` now checks for lexical overlap and prefixing. Flynn performs the final semantic check on whether a term is "General" or "Specific".

### Gaps
#### Prefix Inconsistency
**Risk**: One agent might use `js-` and another `javascript-`, creating fragmented domains.
**Be Wary Of**: Using varied synonyms for the same domain prefix.
