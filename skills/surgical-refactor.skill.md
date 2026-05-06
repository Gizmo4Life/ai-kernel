---
id: surgical-refactor.skill
title: Surgical Refactor
type: skill
tags: [automation, refactor, sed, rapid-update, tool, action, execution]
interface:
  input: 
    target_pattern: "regex_pattern"
    replacement: "replacement_string"
    file_glob: "path/to/files/*.md"
  output:
    modified_files: ["file1.md", "file2.md"]
implementation:
  engine: "sed"
  command: "sed -i '' 's/{{target_pattern}}/{{replacement}}/g' {{file_glob}}"
summary: Performs high-speed, bulk regex refactoring across multiple files (The Agentic Vim).
---

# Surgical Refactor

## Context
Mass-updating IDs, tags, or headers across 100+ files is slow and token-expensive if done manually. This skill uses `sed` to perform surgical, bulk updates in milliseconds.

## Architecture

```mermaid
graph TD
    Agent[Agent] --> Pattern[Define: Regex Pattern]
    Pattern --> Glob[Define: File Glob]
    Glob --> Sed[Engine: sed -i]
    Sed --> Update[Update: Bulk Files]
```

## Execution Steps
1. **Define Pattern**: Identify the specific string or regex to be replaced.
2. **Define Scope**: Specify the file glob (e.g., `glossary/*.md`).
3. **Execute**: Run the `sed` command.
4. **Verify**: Use `grep` to confirm the replacement.

## Verification Protocol
1. Create a test file with `test_string`.
2. Run `sed -i '' 's/test_string/hardened_string/g' test_file.md`.
3. Verify the file contains `hardened_string` using `cat`.

## Quality Gate
- **Verification**: Must be run with specific globs to avoid accidental global corruption.
- **Enforcement**: Large-scale refactors (>10 files) must use this skill instead of manual editing.
