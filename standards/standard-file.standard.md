---
id: standard-file.standard
title: Standard File Standard
type: standard
version: 2
created: 2026-04-28
updated: 2026-05-02
tags: [governance, quality, hierarchy]
summary: Meta-standard for defining the structure and hierarchy of technical standards in the AI Kernel.
scope: standards/
applies_to: [standard.glossary]
glossary_refs: [ standard.glossary, padu-scale.glossary, heuristics.glossary ]
---

# Standard File Standard

## Abstract
This meta-standard defines the structural and hierarchical requirements for all files in the `standards/` directory. It ensures that standards are not isolated documents but are part of a tiered governance system that can be traversed by agents to understand the full scope of quality expectations from broad categories down to language-specific implementation details.

## Hierarchy & Linking
Standards must explicitly state their relationship to other standards.
- **Parent Standards**: Broad categories (e.g., `testing.standard.md`) that set high-level coverage goals and architectural expectations.
- **Child Standards**: Specific implementations (e.g., `unit-testing.standard.md`) or language-specific overrides (e.g., `cpp-unit-testing.standard.md`) that inherit parent goals and provide granular rules.

## PADU Table

| Practice | Rating | Rationale | Exception |
|---|---|---|---|
| Include a concise **Abstract** | **P** | Provides immediate context for both agents and humans. | None |
| Define `parent_standard` | **P** | Establishes the hierarchy and inheritance chain. | Root-level standards. |
| Link related standards inline | **P** | Enables discovery of the full "Standard Map" for a topic. | None |
| Include a PADU table | **P** | The primary mechanism for objective evaluation. | None |
| Define `scope` in frontmatter | **P** | Explicitly states the file path or directory gravity. | None |
| Deep nesting (>3 levels) | **D** | Can make standards difficult to track and resolve. | Extremely complex domains. |
| Vague practice descriptions | **U** | Prevents automated agents from auditing effectively. | None |

## Rationale
By enforcing a hierarchical structure with mandatory abstracts and cross-linking, the AI Kernel transforms from a flat list of rules into a navigable governance graph. This allows an agent working on a React component to automatically discover that it must follow the `javascript.standard.md`, `testing.standard.md`, and `react-component.standard.md` simultaneously.
