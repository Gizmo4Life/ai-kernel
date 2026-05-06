---
id: capability.glossary
title: Capability
type: glossary
tags: [governance, authority, token, definition, term, meaning]
summary: A specific "License to Act" granted to an agent, represented by an authorized Skill or Instruction ID.
---

# Capability

## Context
Capabilities are the "Tokens" of the agent governance model. They define what an agent is *capable* of doing, whereas **Authority** defines what they are *permitted* to propose.

## Architecture

```mermaid
graph TD
    Agent[Agent Role] --> License[Capability Token]
    License --> Skill[Authorized Skill]
    Skill --> Action[Deed: Verified Action]
```

## Usage Constraints
- A Capability must be explicitly listed in the `capabilities` field of the agent frontmatter.
- An agent must not invoke a Skill for which it does not possess the corresponding Capability token.
- Capability grants are governed by the **Capability Standard**.
