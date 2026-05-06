---
id: audit-repository-connectivity.skill
title: Connectivity Auditor
type: skill
tags: [quality, architecture, graph, audit, tool, action, execution]
interface:
  input: { target_dir: "path/to/directory" }
  output: { orphans: ["orphan_id_1", "orphan_id_2"] }
implementation:
  engine: "python3 scratch/connectivity_auditor.py"
  command: "python3 scratch/connectivity_auditor.py {{target_dir}}"
summary: Verifies Knowledge Graph reachability by identifying orphans and broken references.
---

# Connectivity Auditor

## Context
A disconnected node is "Dark Knowledge." This skill uses graph-traversal logic to ensure every node in the AI Kernel is reachable from the root standards.

## Architecture

```mermaid
graph TD
    Input[Target Directory] --> Engine[connectivity_auditor.py]
    Engine --> Map[Map: Frontmatter Refs]
    Map --> Trace[Trace: Incoming References]
    Trace --> Orphan[Detect: Nodes with 0 In-Refs]
    Orphan --> Result[JSON Orphan Report]
```

## Execution Steps
1. **Target Identification**: Specify the repository root.
2. **Engine Invocation**: Run `connectivity_auditor.py`.
3. **Healing**: Link any identified orphans to their appropriate parent standard or manifest.

## Verification Protocol
1. Create a "Floating Node" with no `parent_standard` and no references in other files.
2. Run `python3 scratch/connectivity_auditor.py .`.
3. Verify that the floating node's ID appears in the `orphans` list.

## Quality Gate
- **Verification**: Zero orphans allowed (excluding `kernel.standard`).
- **Enforcement**: Any unreachable node is **Unacceptable (U)**.
