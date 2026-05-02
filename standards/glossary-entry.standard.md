---
id: glossary-entry.standard
title: Glossary Entry Standard
type: standard
version: 3
created: 2026-04-28
updated: 2026-05-02
tags: [governance, glossary]
summary: Standards for defining new terms and concepts in the glossary.
scope: glossary/
parent_standard: kernel.standard
glossary_refs: [ glossary-entry.glossary, standard.glossary, heuristics.glossary ]
---

# Glossary Entry Standard

## Abstract
This standard defines the requirements for glossary entries. It ensures that every term has a single, unambiguous definition that is machine-discoverable.

## PADU Table

| Practice | Rating | Rationale | Enforcement | Exception |
|---|---|---|---|---|
| Use `aliases` for synonyms | **P** | Improves discovery. | Agent Audit (Librarian) | None |
| Define `related` terms | **P** | Builds Knowledge Graph. | `verify-repository-integrity.instruction` | None |
| Single-sentence `summary` | **P** | Ideal for machine scanning. | `audit-frontmatter-completeness.skill` | None |
| Redefining existing terms | **U** | Violates SSoT. | `find-similar-terms.skill` | None |
| Inline definitions elsewhere | **U** | Violates SSoT. | `audit-redundant-content.skill` | None |

## Rationale
The glossary's integrity is protected by a suite of skills that search for conceptual overlap and redundant definitions across the repository.
