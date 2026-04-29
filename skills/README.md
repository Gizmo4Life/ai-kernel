---
id: skills-manifest
title: Skills Manifest
type: manifest
version: 1
created: 2026-04-28
updated: 2026-04-28
summary: Human-navigable map and organizational overview of the skills directory.
---

# Skills

Atomic, tool-centric actions that agents can perform. All skills must adhere to the [Atomicity](../glossary/atomicity.glossary.md) principle.

## Foundational Skills

- [Evaluate Against Standard](evaluate-against-standard.skill.md): Audit content for PADU compliance.
- [Find Glossary Terms](find-glossary-terms.skill.md): Search the glossary for existing definitions.
- [Audit Redundant Content](audit-redundant-content.skill.md): Identify inline definitions that should be linked.
- [Audit for Architectural Violations](audit-for-architectural-violations.skill.md): Check for non-atomic or un-orchestrated content.
- [Audit Frontmatter Completeness](audit-frontmatter-completeness.skill.md): Verify mandatory YAML fields.
- [Find Similar Terms](find-similar-terms.skill.md): Identify potential naming ambiguity.

## Technical Maintenance

- [Collect Repository IDs](collect-repo-ids.skill.md): Index the knowledge graph.
- [Find Frontmatter References](find-frontmatter-refs.skill.md): Map dependency links.

## Domain Standards

- [Research Domain Patterns](research-domain-patterns.skill.md): Extract industry best practices.
- [Scan Codebase Patterns](scan-codebase-patterns.skill.md): Identify local patterns.
- [Generate PADU Table](generate-padu-table.skill.md): Synthesize patterns into a draft table.

## Utility Skills

- [Provide Glossary Guidance](provide-glossary-guidance.skill.md): Flynn's logic for glossary management.
- [Save Conversation Context](save-conversation-context.skill.md): Persist state to the context folder.
- [Summarize to Context](summarize-to-context.skill.md): Extract decisions from logs.
