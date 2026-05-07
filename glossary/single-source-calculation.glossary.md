---
id: single-source-calculation.glossary
title: Single Source of Calculation (SSC)
type: glossary
tags: [architecture, logic, reliability]
summary: A design pattern where a specific calculation or logic gate is centralized in exactly one module to prevent "Ghost Logic" or desynchronization.
---

# Single Source of Calculation (SSC)

## Definition
SSC ensures that complex derivations (e.g., ship mass, trade prices, or compliance scores) are performed by a single authority. All other modules must request the result from this authority rather than re-implementing the logic.

## Implementation Standard
- **Authority**: Identify the T3 module that owns the calculation.
- **Consumption**: All other modules must use the authority's API.

## Architecture

```mermaid
graph TD
```
