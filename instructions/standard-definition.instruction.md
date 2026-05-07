---
id: standard-definition
type: protocol
pillar: governance
glossary_refs: [context.glossary, standard.glossary]
---

[Home](/) > [Docs](/docs/readme.md) > [Governance](/docs/governance/readme.md) > [Protocol](readme.md) > Standard Definition

## 1. Objective
Assign a [Pattern] to a [Standard] and define its contextual fitness using the PADU matrix.

## 2. Contextual Selection
- **Action:** Identify the specific [Standard] (/docs/governance/standard/readme.md) that governs the pattern's domain (e.g., `document-organization.md`).
- **Verify:** The pattern is functionally relevant to the target standard.

## 3. PADU Assignment
- **Action:** Insert the pattern into the Standard's Markdown table.
- **Action:** Assign a rating:
  - **Preferred (P):** The strategic, primary target shape.
  - **Acceptable (A):** Permitted but not strategic; requires justification.
  - **Discouraged (D):** Allowed only for legacy or migration; requires a tech-debt tag.
  - **Unacceptable (U):** Forbidden; triggers a build/audit failure.
- **Action:** Write the specific **Nuance** justifying the rating for that context.

## 4. Verification
- **Verify:** The pattern link is valid and points to `docs/developer/pattern/`.
- **Verify:** The standard reflects the latest architectural decisions.

## Architecture

```mermaid
graph TD
```
