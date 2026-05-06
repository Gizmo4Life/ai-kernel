---
id: synonym.standard
title: Synonym Standard
type: standard
tags: [governance, discovery, semantics]
summary: Standards for defining and managing synonyms in the AI Kernel to prevent logic duplication.
scope: "/**/*"
parent_standard: kernel.standard
glossary_refs: [knowledge-graph.glossary, reachability.glossary]
---

# Synonym Standard

## Context
Synonyms are the "Discovery Anchors" of the AI Kernel. Because agents search via keywords and semantic similarity, a lack of synonyms leads to "Ghost Logic" (recreating existing functionality under a different name). This standard mandates the inclusion of alternative terms for every core concept.

## Architecture

```mermaid
graph TD
    Search[Search: "Feedback"] --> Match[Match: Synonym "Codify Feedback"]
    Match --> Node[Node: System-First Remediation]
    Node --> Execution[Execution: No Duplication]
```

## Mandatory Requirements
1. **Frontmatter**: Every Glossary and Instruction file must include a `synonyms: []` list.
2. **Body**: Every Glossary entry must include a `## Synonyms` section for human/agent cross-reference.

## PADU Table

| Practice | Rating | Rationale | Enforcement | Exception |
|---|---|---|---|---|
| Define 3+ Synonyms | **P** | Increases the "Semantic Surface Area" for discovery. | `librarian.agent` | Very unique terms |
| Use "Vibrant" Keywords | **P** | Use terms the user is likely to say (e.g., "Fix", "Wrong"). | `standards-auditor.agent` | None |
| Naming Divergence | **U** | Creating a file with a name that is a synonym of another file. | `find-similar-terms.skill` | None |
| Narrative Overlap | **D** | Describing synonyms in the summary instead of the field. | `doc-audit.skill` | None |

## Rationale
By formalizing synonyms, we make the Knowledge Graph "Stickier." It ensures that regardless of the prompt's phrasing, the agent is routed to the single source of truth.

## Enforcement
The posture is **Automated**. The `find-similar-terms.skill` must be run during the creation of any new node to check for synonym collisions.
