---
id: audit-frontmatter-completeness.skill
title: Audit Frontmatter Completeness
type: skill
version: 1
created: 2026-04-28
updated: 2026-04-28
tags: [audit, technical, frontmatter.glossary ]
summary: Verifies that every file in the repository contains the mandatory YAML frontmatter fields required by its type.
tool: editor
inputs: file_path: The file to audit.
outputs: missing_fields: A list of mandatory fields that are missing or empty.
standards: [standard-file.standard]
glossary_refs: [frontmatter.glossary]
---

# Audit Frontmatter Completeness

This skill ensures that every node in the Knowledge Graph is fully indexed.

## Execution Steps

1. **Detect Type**: Read the `type:` field in the frontmatter.
2. **Verify Mandatory Fields**: - **Global**: `id`, `title`, `type`, `version`, `created`, `updated`, `summary`.
    - **Standard**: `scope`, `glossary_refs`.
    - **Skill**: `tool`, `inputs`, `outputs`.
    - **Instruction**: `goal`, `skills`.
    - **Agent**: `role`, `authority`, `delegates`.
3. **Report**: provide a list of missing or malformed fields.
