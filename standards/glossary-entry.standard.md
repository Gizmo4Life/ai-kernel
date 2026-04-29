---
id: glossary-entry.standard
title: Glossary Entry Standard
type: standard
version: 1
created: 2026-04-28
updated: 2026-04-28
tags: [governance, documentation]
summary: Standards for creating and maintaining glossary entries within the AI Kernel.
scope: glossary/
applies_to: [glossary]
glossary_refs: [ glossary-entry.glossary, padu-scale.glossary, frontmatter.glossary ]
---

# Glossary Entry Standard

This standard governs the structure and content of all files in `glossary/`.

## PADU Table

| Practice | Rating | Rationale | Exception |
|---|---|---|---|
| Use YAML frontmatter | **P** | Required for machine discovery and progressive disclosure. | None |
| Include `aliases` field | **P** | Improves searchability and link resolution. | Terms with no synonyms. |
| Include `summary` field | **P** | Critical for progressive disclosure. | None |
| Link to related terms | **A** | Helps build the knowledge graph. | Isolated concepts. |
| Inline concept definitions | **U** | Violates single-source-of-truth. | None |
| Using H1 for title | **P** | Standard markdown structure. | None |

## Rationale

The glossary is the backbone of the kernel's knowledge. Strict adherence to frontmatter standards ensures that agents can navigate the repository efficiently without exceeding context limits.
