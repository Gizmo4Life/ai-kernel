---
id: driver.glossary
title: Driver
type: glossary
tags: [execution, logic, atomic, connectivity, mechanism, definition, term, meaning]
summary: A directly executable logic file (Python, Bash, etc.) that performs the atomic work of a skill, such as calling an API or parsing data.
parent_standard: glossary-entry.standard
---

# Driver

## Context
In the AI Kernel hierarchy, the **Driver** is the "Bottom Layer" of execution. It is the bridge between the agent's intent (Skill) and the physical action (Execution). 

## Usage Constraints
- **Atomicity**: A driver must never attempt to perform multi-step orchestration. Orchestration belongs in **Instructions** or **Agents**.
- **Determinism**: Given the same inputs, a driver must produce the same machine-readable output.
- **Portability**: Drivers should be self-contained and easily executable from any shell.

## Architecture

```mermaid
graph TD
    glossary-entry.standard --> driver.glossary
```
