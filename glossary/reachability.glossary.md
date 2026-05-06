---
id: reachability.glossary
title: Reachability
type: glossary
tags: [connectivity, linkage, discovery, graph, definition, term, meaning]
summary: The property of a node in the Knowledge Graph being discoverable through a continuous chain of references starting from the Kernel Root.
---

# Reachability

## Context
Reachability ensures that the AI Kernel is a single, connected Knowledge Graph rather than a collection of isolated silos. It is the prerequisite for automated auditing and knowledge discovery.

## Architecture

```mermaid
graph TD
```

## Usage Constraints
- A node is "Unreachable" if it has no incoming references from a parent standard or master map.
- Reachability must be verified via the `audit-repository-connectivity.skill`.
