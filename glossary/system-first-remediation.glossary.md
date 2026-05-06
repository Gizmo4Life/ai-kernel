---
id: system-first-remediation.glossary
title: System-First Remediation
type: glossary
tags: [logic, quality, self-healing]
summary: The governance pattern of tracing failures to their root cause in the AI Kernel and hardening the system logic before correcting individual outputs.
---

# System-First Remediation

## Context
System-First Remediation is the fundamental operating philosophy of the AI Kernel. It rejects "Patching" (fixing a single output) in favor of "Structural Healing" (fixing the rule that allowed the error).

## Architecture

```mermaid
graph TD
    Error[Failure/Feedback] --> Analysis[Root Cause: Kernel Logic]
    Analysis --> Hardening[Update: Standard/Prompt/Glossary]
    Hardening --> Production[Regenerate: Output]
```

## Usage Constraints
- Must be invoked for every user-reported error or sub-optimal output.
- Is forbidden to perform manual fixes without first checking the **Governing Standard**.
- Requires a **Meta-Audit** of the updated kernel node before re-execution.
