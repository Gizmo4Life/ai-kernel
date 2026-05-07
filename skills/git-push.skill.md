---
id: git-push.skill
title: Git Remote Synchronizer
type: skill
tags: [git, version-control, connectivity, tool, action, execution]
interface:
  input: {}
  output: { status: "success", output: "..." }
implementation:
  engine: "python3 drivers/git/git_push.py"
  command: "python3 drivers/git/git_push.py"
summary: Synchronizes the local repository state with the remote origin/main branch.
parent_standard: skill-file.standard
glossary_refs: [authority.glossary, context.glossary, skill.glossary, standard.glossary]
---

# Git Remote Synchronizer

## Context
The final step of any hardening wave. This skill ensures that the local "Diamond State" is persisted to the remote authority.

## Execution Steps
1. **Engine Invocation**: Run `git_push.py`.
2. **Analysis**: Inspect the output for connectivity issues or merge conflicts.

## Quality Gate
- **Verification**: Output must confirm successful push to `origin/main`.
- **Enforcement**: Persistent push failures must be escalated to the **Operator**.

## Architecture

```mermaid
graph TD
    skill-file.standard --> git-push.skill
```

## Verification Protocol
1. Run {
  "status": "fail",
  "message": "fatal: unable to access 'https://github.com/Gizmo4Life/ai-kernel.git/': Could not resolve host: github.com
"
}.
2. Verify remote reflects local changes.

## Verification Protocol
1. Run `python3 drivers/git/git_push.py`.
2. Verify remote reflects local changes.
