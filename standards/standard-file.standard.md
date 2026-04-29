---
id: standard-file.standard
title: Standard File Standard
type: standard
version: 1
created: 2026-04-28
updated: 2026-04-28
tags: [governance, quality]
summary: Meta-standard for defining how standard files themselves must be structured.
scope: standards/
applies_to: [standard.glossary]
glossary_refs: [ standard.glossary, padu-scale.glossary ]
---

# Standard File Standard

This is a meta-standard that governs how all standard files in `standards/` are written.

## PADU Table

| Practice | Rating | Rationale | Exception |
|---|---|---|---|
| Include a PADU table | **P** | The primary mechanism for evaluating practices. | None |
| Define `scope` in frontmatter | **P** | Explicitly states where the standard applies. | None |
| List `glossary_refs` | **P** | Links standards back to the concepts they use. | None |
| Rating Legend inclusion | **A** | Helps human readers understand PADU. | Redundant if README/Glossary is clear. |
| Vague practice descriptions | **U** | Prevents objective evaluation. | None |

## Rationale

Standards must be machine-parsable and unambiguous so that skills like `evaluate-against-standard` can function reliably.
