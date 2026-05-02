---
id: kernel.standard
title: Kernel Standard
type: standard
version: 3
created: 2026-04-28
updated: 2026-05-02
tags: [core, architecture, quality, root]
summary: The supreme architectural standard for the AI Kernel repository.
scope: /
glossary_refs: [atomicity.glossary, orchestration.glossary, quality-gate.glossary, bootstrap.glossary, knowledge-graph.glossary]
---

# Kernel Standard

## Abstract
The **Kernel Standard** is the foundational governance document for the AI Kernel. It establishes the core architectural principles—Atomicity, Orchestration, and Single Source of Truth—that all other standards, skills, and instructions must inherit.

## PADU Table

| Practice | Rating | Rationale | Enforcement | Exception |
|---|---|---|---|---|
| Use `.{filetype}.md` naming | **P** | Enables deterministic discovery. | `ls` / Agent Audit | README.md |
| Hierarchical Standards | **P** | Organizes rules logically. | `verify-repository-integrity.instruction` | None |
| Link to Glossary for all terms | **P** | Eliminates definition drift. | `audit-redundant-content.skill` | Common language |
| Atomic Skills / Orchestration | **P** | Core architectural principle. | `audit-for-architectural-violations.skill` | Trivial helpers |
| Missing Frontmatter | **U** | Breaks the Knowledge Graph. | `audit-frontmatter-completeness.skill` | None |
| Inline Definitions | **U** | Violates Single Source of Truth. | `audit-redundant-content.skill` | None |

## Rationale
The Kernel Standard acts as the "Constitution" of the repository. By linking every rule to a specific enforcement skill or audit process, we ensure that architectural integrity is a measurable metric, not just a guideline.
