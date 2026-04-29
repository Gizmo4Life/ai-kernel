---
id: skill.glossary
title: Skill
type: glossary
version: 1
created: 2026-04-28
updated: 2026-04-28
tags: [core, automation, tool-use]
summary: An atomic, tool-centric action that an AI agent can perform to achieve a specific outcome.
aliases: [action, tool-command, capability]
related: [ instruction.glossary, agent.glossary ]
---

# Skill

A **Skill** is a discrete capability that leverages specific tools (e.g., git, grep, editor) to perform a task. Skills are the building blocks of automated workflows.

## Design Principles

- **Atomicity**: A skill should do one thing well.
- **Tool-Centricity**: Explicitly defines which tools are required.
- **Input/Output Contract**: Clearly specifies what it needs and what it produces.

## Usage

Skills are referenced in **Instructions** (multi-step sequences) and assigned to **Agents** (autonomous actors).
