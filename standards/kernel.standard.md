---
id: kernel.standard
title: Kernel Standard
type: standard
version: 1
created: 2026-04-28
updated: 2026-04-28
tags: [core, architecture, quality]
summary: The master standard for the AI Kernel's architecture and organization.
scope: /
glossary_refs: [ atomicity.glossary, orchestration.glossary, quality-gate.glossary, bootstrap.glossary, knowledge-graph.glossary ]
---

# Kernel Standard

This is the supreme standard governing the entire AI Kernel repository.

## PADU Table

| Practice | Rating | Rationale | Exception |
|---|---|---|---|
| Use `.{filetype}.md` naming convention | **P** | Enables clear file-system discovery and type-based filtering. | README.md |
| Link to Glossary for every concept | **P** | Ensures Single Source of Truth. | Common English terms. |
| Use Atomic Skills and Orchestrated Instructions | **P** | Core architectural principle for scalability. | Trivial helpers. |
| Include Frontmatter on all content files | **P** | Essential for machine discovery and Knowledge Graph integrity. | README.md |
| Multi-tool Skills | **U** | Violates atomicity. | None |
| Instructions without Quality Gates | **U** | Risk of sub-standard commits. | None |

## Rationale

The AI Kernel is a machine-readable knowledge base. Strict adherence to naming, modularity, and linking is required for agents to navigate the system without hallucination or redundancy.
