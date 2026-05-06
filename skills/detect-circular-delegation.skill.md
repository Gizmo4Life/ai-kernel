---
id: detect-circular-delegation.skill
title: Agent Cycle Detector
type: skill
tags: [safety, orchestration, agents, graph, tool, action, execution]
interface:
  input: { agent_dir: "path/to/agents" }
  output: { cycles: [["agentA", "agentB", "agentA"]] }
implementation:
  engine: "python3 drivers/kernel/cycle_detector.py"
  command: "python3 drivers/kernel/cycle_detector.py"
summary: Prevents infinite delegation loops by identifying cycles in the multi-agent hierarchy.
parent_standard: skill-file.standard
glossary_refs: [agent.glossary, context.glossary, delegation.glossary, orchestration.glossary, skill.glossary, standard.glossary]
---

# Agent Cycle Detector

## Context
Multi-agent orchestration is vulnerable to infinite loops if delegation is not a Directed Acyclic Graph (DAG). This skill uses graph-traversal logic to ensure that "Agentic Loops" are identified and broken.

## Architecture

```mermaid
graph TD
    skill-file.standard --> detect-circular-delegation.skill
```

## Execution Steps
1. **Engine Invocation**: Run `cycle_detector.py` against the `agents/` directory.
2. **Analysis**: Inspect the `cycles` list in the JSON output.
3. **Healing**: Break any identified loops by refining the `delegates: []` metadata.

## Verification Protocol
1. Create `agentA` delegating to `agentB`.
2. Create `agentB` delegating back to `agentA`.
3. Run `python3 drivers/kernel/cycle_detector.py`.
4. Verify that the cycle `[agentA, agentB, agentA]` is reported.

## Quality Gate
- **Verification**: Output must be `{"cycles": []}` in a healthy kernel.
- **Enforcement**: Any circular delegation is a **Critical Failure (U)** and must be resolved before deployment.
