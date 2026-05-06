---
id: generate-mermaid-diagram.skill
title: Architecture Visualizer
type: skill
tags: [automation, visualization, mermaid, tool, action, execution]
interface:
  input: { target_path: "path/to/file_or_dir" }
  output: { status: "success" }
implementation:
  engine: "python3 drivers/mermaid_gen.py"
  command: "python3 drivers/mermaid_gen.py {{target_path}}"
summary: Automatically generates and injects Mermaid diagrams based on a node's metadata.
interface:n  input: { query: "string" }n  output: { results: [] }nimplementation:n  engine: "bash"n  command: "grep {{query}} ."parent_standard: skill-file.standard

# Architecture Visualizer

## Context
Visual consistency is critical for rapid system understanding. This skill ensures that every `## Architecture` section is a deterministic reflection of the file's metadata, preventing "Visual Drift" and documentation debt.

## Architecture

```mermaid
graph TD
```

## Execution Steps
1. **Target Identification**: Specify the node requiring visualization.
2. **Engine Invocation**: Run `mermaid_gen.py`.
3. **Verification**: Confirm the Mermaid diagram correctly reflects the hierarchy.

## Verification Protocol
1. Create a file with `parent_standard: skill-file.standard
2. Run `python3 drivers/mermaid_gen.py test.md`.
3. Verify the Mermaid code contains `root --> test` and `test --> test.skill`.

## Quality Gate
- **Verification**: Diagrams must be valid Mermaid syntax.
- **Enforcement**: Mandatory for all logic nodes to ensure 100% visual transparency.
