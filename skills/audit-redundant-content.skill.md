---
id: audit-redundant-content.skill
title: Redundant Content Auditor
type: skill
tags: [quality, deduplication, optimization, tool, action, execution]
interface:
  input: { target_dir: "path/to/dir" }
  output: { duplicates: ["path1", "path2"] }
implementation:
  engine: "find + md5 + awk"
  command: "find {{target_dir}} -name '*.md' -exec md5 {} + | sort | awk 'BEGIN{last=\"\"} {if($1==last) print $2; last=$1}'"
summary: Identifies byte-identical duplicate files to prevent Knowledge Graph redundancy.
---

# Redundant Content Auditor

## Context
Redundancy is the enemy of SSOT (Single Source of Truth). This skill identifies files that have different names but identical content, allowing for surgical deduplication.

## Architecture

```mermaid
graph TD
    Input[Target Directory] --> Find[Find: .md files]
    Find --> Hash[MD5: Generate Fingerprints]
    Hash --> Sort[Sort: Group Identical Hashes]
    Sort --> Awk[Detect: Duplicate Hashes]
    Awk --> Result[List: Duplicate File Paths]
```

## Execution Steps
1. Specify the directory to audit.
2. Execute the hash-and-compare pipe.
3. Review the duplicate list and perform atomic deletion or linking.

## Verification Protocol
1. Create a copy of an existing file: `cp target.md target_copy.md`.
2. Run the skill on the directory.
3. Verify that `target_copy.md` is listed as a duplicate.

## Quality Gate
- **Verification**: Only byte-identical files are flagged.
- **Enforcement**: Zero byte-identical duplicates permitted in the logic domains.
