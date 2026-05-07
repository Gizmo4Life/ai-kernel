---
parent_standard: kernel.standard
id: mon-alerting.standard
title: Monitoring & Alerting Standard
type: standard
tags: [operability, monitoring, alerting, quality, rules, governance, compliance]
summary: Standards for aggregate detection systems, prioritizing unhealthiness detection over diagnostic specificity.
requirements: [parent_standard, "## PADU Table", "## Enforcement", "## Context", "## Context
Monitoring is the system's "Pain Receptor." Its goal is to detect that the system is no longer healthy, not to diagnose *why*. By prioritizing aggregation, we reduce alert fatigue and ensure that a single monitor can cover a wide range of failure modes.
## Monitoring Principles
### 1. Aggregation over Diagnosis
- **Rule**: Create one monitor for many scenarios.
- **Example**: A single monitor for "API Latency > 500ms" covers database slowness, network congestion, and code inefficiencies simultaneously.
### 2. Detection over Feedback
- **Rule**: Monitors should only trigger when a specific **SLO (Service Level Objective)** is violated.
- **Exclusion**: Do not alert on "Warning" states that do not impact user success.
### 3. Clear Escalation
- **Rule**: Every alert must point directly to a **Span Diagnostic Dashboard** (`*.dashboard.md`).
## PADU Table
| Practice | Rating | Rationale | Enforcement | Exception |
|
glossary_refs: [agent.glossary, skill.glossary, standard.glossary]
---

|---|---|---|---|
| One Monitor : Many Scenarios | **P** | Maximizes detection coverage with minimal alert noise. | evaluate-against-standard.skill | Trivial components |
| Alert links to Dashboard | **P** | Provides the first step for deterministic restoration. | `linkage-specialist.agent` | None |
| Diagnostic Alerts | **D** | Leads to "Alert Storms" where one root cause triggers 50 alerts. | evaluate-against-standard.skill | Critical safety loops |
| Informational Alerts | **U** | Causes "Alert Fatigue" and leads to ignored production issues. | `mon-audit.skill` | None |

## Rationale
In a high-fidelity telemetry environment, we don't need the monitor to tell us what is wrong. We only need it to tell us that *something* is wrong. We then use the **Diagnostic Dashboard** to perform the surgical diagnosis.

## Enforcement
The posture is **Automated**. The **Linkage Specialist** verifies that every defined Monitor has a corresponding `correlation_id` to its target Dashboard.

