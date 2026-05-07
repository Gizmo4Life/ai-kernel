---
id: runbook.standard
title: Universal Runbook Standard
type: standard
tags: [ops, runbook, triage, on-call]
status: stable
version: 1.0.0
padu:
  P: "Runbook contains a severity matrix, impact scope, and clear escalation paths."
  A: "Runbook has triage steps but missing formal escalation or severity gates."
  D: "Runbook is missing diagnostic dashboard links or triage logic."
  U: "Runbook lacks any actionable restoration steps for on-call personnel."
glossary_refs: [instruction.glossary, standard.glossary]
---

# Universal Runbook Standard

## 1. Severity Matrix
| Severity | Threshold | Response Time |
| :--- | :--- | :--- |
| **SEV-1** | > 10% Error Rate or Total Outage | 15 Mins |
| **SEV-2** | > 1% Error Rate or 2x Latency | 30 Mins |
| **SEV-3** | Degraded Performance | 4 Hours |

## 2. Impact Scope
- **SEV-1**: Universal service failure; all users blocked.
- **SEV-2**: Significant degradation; subset of users or core features affected.

## 3. Triage Protocol
- **Strategy**: Adhere to the [Operational Triage Instruction](../instructions/operational-triage.instruction.md).
- **Action**: Identify the failing span from the SigNoz dashboard and proceed to the corresponding module runbook.

## 4. Escalation Path
- **Action**: If triage fails within the response time window:
  - **Level 1**: Primary On-Call Engineer.
  - **Level 2**: Engineering Leadership.

## 5. Architecture
```mermaid
graph TD
    Alert[Alert Trigger] --> Triage[Operational Triage]
    Triage --> Module[Module Runbook]
    Module --> Restore[Service Restored]
    Triage -- Fail --> Escalation[Global Escalation]
```

## Architecture

```mermaid
graph TD
```
