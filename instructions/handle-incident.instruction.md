---
id: handle-incident.instruction
title: Handle Incident
type: instruction
tags: [workflow, operability, incident-response, restoration]
summary: The master orchestration workflow for resolving production alerts through deterministic restoration.
goal: Rapid restoration of system health with minimal manual diagnosis.
skills: [evaluate-against-standard.skill]
standards: [inc-response.standard, operability.standard]
preconditions:
  - An aggregate alert has been triggered by a Monitor.
  - A 3-piece Restoration Kit (Dashboard, Runbook, Actions) is available for the target component.
---

# Handle Incident

## Context
This instruction defines the bridge between **Detection** and **Restoration**. It ensures that when an alert fires, the responder follows a deterministic path that eliminates "Creative Troubleshooting" in favor of "Systemic Healing."

## Architecture

```mermaid
graph TD
    Alert((Aggregate Alert)) --> Dashboard[1. Check Status: Dashboard]
    Dashboard --> Identify[2. Identify: Unhealthy Spans]
    Identify --> Prioritize[3. Prioritize: Critical Path first]
    Prioritize --> Runbook[4. Diagnose: Refer to Runbook]
    Runbook --> Action[5. Restore: Execute Restoration Action]
    Action --> Verify[6. Verify: Re-check Dashboard]
    Verify -->|Unhealthy| Runbook
    Verify -->|Healthy| Success((Incident Resolved))
```

## Steps

1. **Intake**: Accept the aggregate alert signal.
2. **Dashboard Review**: Open the **[Span Diagnostic Dashboard](../standards/inc-response.standard.md)** linked in the alert.
3. **Identification**: Identify which specific spans are reporting unhealthiness.
4. **Prioritization**: If multiple spans are failing, prioritize the "Critical Path" (e.g., Auth over Logging).
5. **Diagnostic Runbook**: Open the **[Span Diagnostic Runbook](../standards/inc-response.standard.md)** for the highest-priority failing span.
6. **Execution**:
    - **Verify**: Run the verification step defined in the runbook.
    - **Apply**: Execute the **Restoration Action** (Skill/Instruction).
    - **Re-verify**: Re-run the verification to confirm the fix.
7. **Reporting**: Update the incident status and close the alert.


## Postconditions
1. The system state matches the goal defined in the frontmatter.
2. All related Knowledge Graph nodes are updated and linked.

## Quality Gate

Restoration integrity is governed by the **[Incident Response Standard](../standards/inc-response.standard.md)**.
- **Verification**: The incident is only considered "Resolved" when the Dashboard reports **Green** for all affected spans.
- **Enforcement**: Bypassing the Runbook for a manual fix is **Discouraged (D)** as it prevents the system from learning the remediation pattern.
