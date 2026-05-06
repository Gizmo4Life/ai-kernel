---
id: check-id-uniqueness.skill
title: ID Uniqueness Auditor
type: skill
tags: [quality, architecture, audit, tool, action, execution]
interface:
  input: { target_dir: "path/to/directory" }
  output: { collisions: { "colliding_id": ["file_path_1", "file_path_2"] } }
implementation:
  engine: "python3 scratch/id_auditor.py"
  command: "python3 scratch/id_auditor.py {{target_dir}}"
summary: Verifies that every node in the AI Kernel Knowledge Graph possesses a globally unique ID.
parent_standard: skill-file.standard
glossary_refs: [context.glossary, frontmatter.glossary, skill.glossary]
---

# ID Uniqueness Auditor

## Context
Global uniqueness is the primary constraint for the AI Kernel Knowledge Graph. This skill identifies ID collisions across all domains to prevent cross-linking errors and semantic confusion.

## Architecture

```mermaid
graph TD
    skill-file.standard --> check-id-uniqueness.skill
```

## Execution Steps
1. **Target Identification**: Specify the repository root or a sub-folder.
2. **Engine Invocation**: Run `id_auditor.py`.
3. **Surgical Triage**: Address any collisions identified in the JSON output.

## Verification Protocol
1. Create two files with the same `id: duplicate.test`.
2. Run `python3 scratch/id_auditor.py .`.
3. Verify that `duplicate.test` appears in the JSON output with both file paths.

## Quality Gate
- **Verification**: Output must be an empty JSON object `{}` in a healthy repo.
- **Enforcement**: Zero collisions are permitted in the stable branch.
