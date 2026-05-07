---
parent_standard: kernel.standard
id: skill-file.standard
title: Skill File Standard
type: standard
tags: [governance, standard, skill, interface, transactional]
status: stable
version: 1.1.0
padu:
  P: "Skill defines a formal interface, verification command, and a deterministic reversion path."
  A: "Skill has an interface and verification but missing a formal undo path."
  D: "Skill is non-deterministic or missing verification protocols."
  U: "Skill has side-effects with no way to verify or revert."
glossary_refs: [agent.glossary, standard.glossary, context.glossary, skill.glossary]
---# Skill File Standard

## Context
Skills are the "Atomic Acts" of the AI Kernel. To ensure system stability, every skill must be **Transactional**. This means an agent can provably verify the outcome and safely "Undo" the action if the verification fails.

## Structural Requirements
1. **Interface**: Explicit `input` and `output` JSON schemas.
2. **Verification**: A deterministic command or logic block to verify the success of the act.
3. **Reversion**: A deterministic command or logic block to restore the system state upon failure.

## Transactional Protocol
Agents MUST follow the **Verify-or-Revert** cycle:
- **Execute**: Run the `implementation` command.
- **Verify**: Run the `verification` command.
- **Rollback**: If `verification` fails, run `reversion` immediately.

## Quality Gate
- **Verification**: Every skill must be rated P on the PADU scale.
- **Enforcement**: Flynn will reject any skill that performs destructive edits without a formal `reversion` path.

## PADU Table

[Auto-Generated Placeholder for Compliance]

## Enforcement

[Auto-Generated Placeholder for Compliance]
