---
id: fm-updater.skill
title: Frontmatter Updater Skill
type: skill
tags: [editor, frontmatter, metadata, transactional]
interface:
  input: { fpath: "string", key: "string", value: "string" }
  output: { status: "success" }
summary: Deterministically updates a single frontmatter field in a file.
glossary_refs: [frontmatter.glossary]
---# Frontmatter Updater

## Execution
- **Command**: `python3 drivers/kernel/fm_updater.py <fpath> <key> <value>`

## Verification
- **Check**: `python3 drivers/kernel/global_compliance_auditor.py <fpath>`
- **Goal**: Confirm the file is compliant and the field matches the expected value.

## Reversion
- **Undo**: `git checkout -- <fpath>`
- **Note**: This restores the file to its last committed state.

## Architecture

```mermaid
graph TD
```
