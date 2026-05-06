---
id: mon-alerting.standard
title: Monitoring & Alerting Standard
type: standard
tags: [operability, monitoring, alerting, quality, rules, governance, compliance]
summary: Standards for aggregate detection systems, prioritizing unhealthiness detection over diagnostic specificity.
requirements: [parent_standard, "## PADU Table", "## Enforcement", "## Context", "## Architecture"]
scope: "/**/*"
parent_standard: operability.standard
glossary_refs: [agent.glossary, context.glossary, progressive-disclosure.glossary, skill.glossary, standard.glossary, tel-naming.standard]
---

# Monitoring & Alerting Standard

## Context
Monitoring is the system's "Pain Receptor." Its goal is to detect that the system is no longer healthy, not to diagnose *why*. By prioritizing aggregation, we reduce alert fatigue and ensure that a single monitor can cover a wide range of failure modes.

## Architecture

```mermaid
graph TD
    operability.standard --> mon-alerting.standard
```

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
|---|---|---|---|---|
| One Monitor : Many Scenarios | **P** | Maximizes detection coverage with minimal alert noise. | Agent Audit | Trivial components |
| Alert links to Dashboard | **P** | Provides the first step for deterministic restoration. | `linkage-specialist.agent` | None |
| Diagnostic Alerts | **D** | Leads to "Alert Storms" where one root cause triggers 50 alerts. | Agent Audit | Critical safety loops |
| Informational Alerts | **U** | Causes "Alert Fatigue" and leads to ignored production issues. | `mon-audit.skill` | None |

## Rationale
In a high-fidelity telemetry environment, we don't need the monitor to tell us what is wrong. We only need it to tell us that *something* is wrong. We then use the **Diagnostic Dashboard** to perform the surgical diagnosis.

## Enforcement
The posture is **Automated**. The **Linkage Specialist** verifies that every defined Monitor has a corresponding `correlation_id` to its target Dashboard.
