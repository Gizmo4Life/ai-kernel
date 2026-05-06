---
id: collect-repo-ids.skill
title: Collect Repository IDs
type: skill
tags: [audit, architecture, logic, tool, action, execution]
interface:
  input: { target_dir: "path/to/dir" }
  output: { ids: ["id1", "id2"] }
implementation:
  engine: "grep + awk"
  command: "grep -rh '^
id: ' {{target_dir}} | awk '{print $2}' | sort | uniq"
summary: Extracts a unique, sorted list of all IDs currently active in the Knowledge Graph.
interface:n  input: { query: "string" }n  output: { results: [] }nimplementation:n  engine: "bash"n  command: "grep {{query}} ."parent_standard: skill-file.standard
glossary_refs: [context.glossary, skill.glossary]
---

# Collect Repository IDs

## Context
To perform graph-wide operations (like checking for orphans or broken links), we first need a clean list of all available IDs. This bash pipe provides that list in milliseconds.

## Architecture

```mermaid
graph TD
    skill-file.standard --> collect-repo-ids.skill
```

## Execution Steps
1. Specify the repository root.
2. Execute the bash pipe.
3. Use the list as the "Source of Truth" for graph traversal.

## Verification Protocol
1. Count the number of `.md` files in `glossary/`.
2. Run the skill on `glossary/`.
3. Verify the ID count matches the file count (assuming 1 ID per file).

## Quality Gate
- **Verification**: Output must be a clean, newline-separated list of IDs.
- **Enforcement**: Mandatory step before running any graph-wide connectivity audit.
