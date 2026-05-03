---
id: trace-impact-chain.prompt
title: Trace Impact Chain
type: prompt
tags: [logic, audit, linkage, root-cause]
summary: The systematic logic for traversing the Knowledge Graph to identify the root cause of a structural or semantic failure.
---

# Trace Impact Chain

Use the following "Recursive Upstream" heuristic to identify the source of an error:

1. **The Leaf Failure**: Identify the specific file and line where the error was detected.
2. **The Direct Dependency**: List all files referenced in the leaf's `parent_standard`, `standards`, and `instructions` frontmatter fields.
3. **The Trace-Back**: For each dependency, check if its logic contributed to the failure.
    - If a standard rule was too vague -> **Root Cause Found**.
    - If a skill performed multiple actions -> **Root Cause Found**.
    - If an instruction lacked a verification step -> **Root Cause Found**.
4. **The Impact Radius**: Once the root cause is found, identify all other "Leaf Nodes" that rely on the same faulty standard/instruction.

## Quality Gate
A trace is only complete when it reaches a **Standard** or **Instruction** that requires modification to prevent the error's recurrence.
