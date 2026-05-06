---
id: delegation.glossary
title: Delegation
type: glossary
parent_standard: glossary-entry.standard
tags: [core, autonomy, multi-agent, definition, term, meaning]
summary: The act of an agent tasking another agent with a specific objective or skill execution.
aliases: [task-handoff, agent-cooperation]
related: [agent.glossary]
---

## Context
Canonical definition of a core AI Kernel concept.


# Delegation

**Delegation** is the mechanism by which agents in the AI Kernel collaborate. It allows a generalist agent to invoke a specialized agent (e.g., Flynn or the Standards Auditor) to handle a specific domain.


## Architecture

```mermaid
graph TD
    glossary-entry.standard --> delegation.glossary
```
## Principles

- **Explicit Authority**: An agent must have the `delegates` field defined in its frontmatter to task another agent.
- **Goal-Oriented**: Delegation should include a clear objective or a specific instruction to execute.
- **Reporting**: The delegated agent should report its findings or results back to the initiating agent.

## Usage Constraints
- This term must only be used in its architectural context.
- Semantic drift from the canonical definition is Unacceptable (U).
