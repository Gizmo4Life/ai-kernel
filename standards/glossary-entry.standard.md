---
id: glossary-entry.standard
title: Glossary Entry Standard
type: standard
version: 2
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
This standard defines the requirements for glossary entries. It ensures that every term in the repository has a single, unambiguous definition that is machine-discoverable through YAML frontmatter and human-readable through clear markdown. This is the cornerstone of the "Single Source of Truth" (SSoT) principle.

## Related Standards
- [Kernel Standard](kernel.standard.md): The architectural parent enforcing SSoT.

## PADU Table

| Practice | Rating | Rationale | Exception |
|---|---|---|---|
| Use `aliases` for synonyms | **P** | Improves searchability and discovery for agents. | None |
| Define `related` terms | **P** | Builds the semantic layer of the Knowledge Graph. | None |
| Single-sentence `summary` | **P** | Ideal for machine-based scanning and progressive disclosure. | None |
| Redefining existing terms | **U** | Creates confusion and violates SSoT. | None |
| Inline definitions elsewhere | **U** | Concepts must always link back to the glossary. | None |

## Rationale
The glossary is the "dictionary" of the AI Kernel. Standardizing its format ensures that agents can quickly resolve terminology conflicts and understand the relationships between complex technical concepts.
