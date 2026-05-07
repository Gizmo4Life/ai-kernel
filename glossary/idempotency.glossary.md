---
id: idempotency.glossary
title: Idempotency
type: glossary
tags: [logic, engineering, reliability]
summary: The property of certain operations in mathematics and computer science whereby they can be applied multiple times without changing the result beyond the initial application.
---# Idempotency

## Definition
An idempotent operation is one that has no additional effect if it is called more than once with the same input parameters. In repository governance, this means a "Healing Wave" should be safe to run repeatedly without corrupting data.

## Implementation Standard
- **Logic**: All edit drivers (JSON/YAML/XML) must be idempotent.
- **Verification**: Running a skill twice must result in the same system state as running it once.

## Architecture

```mermaid
graph TD
```
