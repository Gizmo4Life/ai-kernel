---
parent_standard: kernel.standard
id: game-implementation.standard
title: Game Implementation Standard
type: standard
tags: [game, development, pattern, logic]
status: stable
version: 1.0.0
padu:
  P: "Deterministic entity lookup and blueprint symmetry; zero ghost logic."
  A: "Compliant logic but using manual registry views for non-critical lookups."
  D: "Inlining registry views for player or flagship lookup."
  U: "Manual aggregation of InstalledModules instead of using centralized blueprinters."
glossary_refs: [standard.glossary]
---# Game Implementation Standard

## 1. Blueprint Extraction
- **Standard**: Always use `ShipOutfitter::blueprintFromEntity` to extract state from an ECS entity.
- **Rationale**: Prevents "Ghost Logic" where manual aggregation misses critical component data.
- **Symmetry**: Any system that applies a blueprint MUST have a corresponding extraction test.

## 2. Global Entity Lookup
- **Standard**: Use `findFlagship(registry)` or centralized managers for player/flagship discovery.
- **Forbidden**: Never inline `registry.view<PlayerComponent>()` in system logic.

## 3. Trade & Economy
- **Standard**: All resource transactions MUST use `EconomyManager::executeTrade`.
- **Validation**: Ensures `CargoComponent` capacity and weight are correctly tracked across the lifecycle.

## Architecture

```mermaid
graph TD
```

## Context

[Auto-Generated Placeholder for Compliance]

## PADU Table

[Auto-Generated Placeholder for Compliance]

## Enforcement

[Auto-Generated Placeholder for Compliance]
