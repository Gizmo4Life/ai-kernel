---
id: cross-repo-governance.standard
title: Cross-Repository Governance Standard
type: standard
tags: [governance, multi-repo, sidecar, orchestration, architecture]
status: stable
version: 1.0.0
padu:
  P: "Sidecar Kernel is the unique source of truth for all standards; target repos link to it."
  A: "Standards are duplicated but kept in sync via automated healing waves."
  D: "Target repos have local standards that override the Sidecar without justification."
  U: "No linkage between target repo and Sidecar governance."
glossary_refs: [context.glossary, orchestration.glossary, sidecar.glossary, skill.glossary, standard.glossary]
---# Cross-Repository Governance Standard

## Context
High-scale development requires consistent standards across multiple repositories. The "Sidecar Pattern" ensures that every project in a workspace benefits from the same hardened logic, while preventing "Standard Fragmentation."

## Structural Requirements
1. **SSoT (Single Source of Truth)**: The AI Kernel Sidecar is the definitive source for all `standards/` and `glossary/` definitions.
2. **Path Awareness**: Drivers and Skills must support a `target_root` argument to operate on external repositories.
3. **Registry Transparency**: The Sidecar's `registry/service-map.md` should include all repositories currently under its governance.
4. **Context Isolation**: Each project should maintain its own `context/` folder, but summary reports should be aggregated into the Sidecar.

## Multi-Model Orchestration
1. **Tiered Access**: High-level orchestration (Flynn) should happen in the Sidecar using premium models.
2. **Domain Scoping**: Target repo agents should be scoped to their local source code but inherit "Skill Invocations" from the Sidecar.

## Quality Gate
- **Verification**: Run `python3 drivers/kernel/connectivity_auditor.py` across the multi-root workspace.
- **Enforcement**: All target repos MUST pass a Sidecar-driven `compliance_audit` before merging into `main`.

## Architecture

```mermaid
graph TD
```
