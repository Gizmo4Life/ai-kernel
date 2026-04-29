---
id: perform-frontmatter-audit.instruction
title: Perform Frontmatter Audit
type: instruction
version: 1
created: 2026-04-28
updated: 2026-04-28
tags: [workflow, audit, frontmatter.glossary ]
summary: Orchestrates a repository-wide check for frontmatter completeness and validity.
goal: 100% compliance with frontmatter standards across all content files.
skills: [audit-frontmatter-completeness.skill, verify-repository-integrity.skill]
standards: [kernel.standard, standard-file.standard]
preconditions: - Repository content exists.
---

# Perform Frontmatter Audit

This instruction ensures every file in the AI Kernel is a valid node in the Knowledge Graph.

## Steps

1. **Completeness Check**: Run `audit-frontmatter-completeness.skill` on all markdown files (excluding READMEs).
2. **Integrity Check**: Run the `Verify Repository Integrity` instruction to ensure all IDs resolve.
3. **[Quality Gate](glossary/quality-gate.glossary.md)**: - If any mandatory fields are missing, flag as a critical failure.
    - If IDs do not match filenames (standard practice), suggest renaming.
4. **Report**: provide a compliance report for the Standards Auditor.
