---
id: identify-out-of-scope-content.skill
title: Identify Out-of-Scope Content
type: skill
tags: [logic, audit, semantics, tool, action, execution]
summary: Detect content within a file that violates the atomicity of its current domain or tier.
interface:n  input: { query: "string" }n  output: { results: [] }nimplementation:n  engine: "bash"n  command: "grep {{query}} ."parent_standard: skill-file.standard
glossary_refs: [context.glossary, instruction.glossary, orchestration.glossary, skill.glossary, standard.glossary]
---

# Identify Out-of-Scope Content

## Context
This skill provides the "Sensing" logic for the De-conflation engine. It compares a file's content against its `type` (Standard, Skill, etc.) and flags any blocks that belong in a different domain.

## Architecture

```mermaid
graph TD
    skill-file.standardtool --> identify-out-of-scope-content.skill
```

## Execution Steps
1. **Domain Alignment Check**: Scan for content patterns that belong in other tiers.
    - **Skill Files**: Flag any multi-step "Workflows" or "Concept Definitions."
    - **Instruction Files**: Flag any "Atomic Tool Usage" or "Static Rules."
    - **Standard Files**: Flag any "Surgical Commands" or "Step-by-step Logic."
2. **SSOT Gap Analysis**: Check if the flagged content already exists in the target domain.
3. **Candidate Selection**: List all content blocks that require extraction.

## Verification Protocol
1. Input a Skill file containing a 5-paragraph glossary definition.
2. Verify the output flags the definition as "Out of Scope" for the Skill domain.
3. Verify the output correctly suggests the `glossary/` folder as the target.

## Quality Gate
- **Verification**: Detection must be based on the **Atomic Extraction Standard**.
- **Enforcement**: False positives (flagging core logic as out-of-scope) must be <5%.
