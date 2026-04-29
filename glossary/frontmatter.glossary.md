---
id: frontmatter.glossary
title: Frontmatter
type: glossary
version: 1
created: 2026-04-28
updated: 2026-04-28
tags: [core, metadata, technical]
summary: YAML metadata at the top of markdown files used for machine-readable indexing and progressive disclosure.
aliases: [metadata, header, yaml-block]
related: [progressive-disclosure.glossary]
---

# Frontmatter

**Frontmatter** is a block of YAML-formatted data located at the very beginning of a file, delimited by triple dashes (`---`).

## Role in the Kernel

- **Discovery**: Agents scan frontmatter to find files by tag, type, or ID without reading the full body.
- **Linking**: Provides machine-readable references (`glossary_refs`, `standards`) that tools can use to build a knowledge graph.
- **Scanning Efficiency**: Supports **Progressive Disclosure** by providing a `summary` field.
