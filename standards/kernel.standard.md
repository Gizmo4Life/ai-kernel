---
id: kernel.standard
title: Kernel Standard
type: standard
version: 2
created: 2026-04-28
updated: 2026-05-02
tags: [core, architecture, quality, root]
summary: The supreme architectural standard for the AI Kernel repository.
scope: /
glossary_refs: [atomicity.glossary, orchestration.glossary, quality-gate.glossary, bootstrap.glossary, knowledge-graph.glossary]
---

# Kernel Standard

## Abstract
The **Kernel Standard** is the foundational governance document for the AI Kernel. It establishes the core architectural principles—Atomicity, Orchestration, and Single Source of Truth—that all other standards, skills, and instructions must inherit. As the root of the standard hierarchy, it defines the global expectations for repo organization and machine-readability.

## Related Standards
- [Standard File](standard-file.standard.md): Governs the meta-structure of this and all other standards.
- [Glossary Entry](glossary-entry.standard.md): Governs the atomic units of knowledge.
- [Skill File](skill-file.standard.md): Governs atomic actions.

## PADU Table

| Practice | Rating | Rationale | Exception |
|---|---|---|---|
| Use `.{filetype}.md` naming | **P** | Enables deterministic file-system discovery. | README.md |
| Hierarchical Standards | **P** | Organizes rules from broad to specific. | None |
| Link to Glossary for all terms | **P** | Eliminates definition drift and redundancy. | Common language. |
| Atomic Skills / Orchestrated Instructions | **P** | Ensures modularity and reusability. | Trivial helpers. |
| Missing Frontmatter | **U** | Breaks the machine-readable Knowledge Graph. | None |
| Inline Definitions | **U** | Violates Single Source of Truth (SSoT). | None |

## Rationale
The Kernel Standard acts as the "Constitution" of the repository. By enforcing strict modularity and naming conventions at the root, we ensure that as the kernel grows, it remains navigable by autonomous agents without constant human intervention.
