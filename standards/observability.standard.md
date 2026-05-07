---
parent_standard: kernel.standard
id: observability.standard
title: Observability & Telemetry Standard
type: standard
tags: [ops, telemetry, observability, tracing, otel]
status: stable
version: 1.0.0
padu:
  P: "100% trace coverage for all business logic; <pillar>.<module>.<action> dot-notation."
  A: "Basic tracing present but missing granular attributes or dashboard panels."
  D: "Logging-only or non-standard naming conventions."
  U: "Zero observability; 'Black Box' execution."
glossary_refs: [standard.glossary]
---# Observability & Telemetry Standard

## 1. Nomenclature & Naming
- **Standard**: All spans MUST follow the hierarchical dot-notation: `<pillar>.<module>.<action>`.
- **Rationale**: Ensures global searchability and consistent dashboarding in SigNoz/Grafana.

## 2. Dashboard Requirements (SigNoz)
- **Mandatory Panels**:
  - Latency (P99) by span action.
  - Error Rate by module.
  - Throughput (Ops/sec) for critical loops.
- **Enforcement**: New features impacting P-rated capabilities MUST update the corresponding Diagnostic Dashboard.

## 3. Span Runbooks
- **Requirement**: Every critical system span MUST have a corresponding Span Runbook.
- **Content**: Must include Diagnostic Mapping (Metrics -> Logic) and Mitigation steps.

## 4. PADU Table
| Practice | Rating | Rationale |
| :--- | :--- | :--- |
| **Dot-Notation Spans** | **P** | Enables hierarchical aggregation. |
| **Critical Failure Metrics** | **P** | Defines the "Red Line" for T2 Capabilities. |
| **Manual Span Mapping** | **A** | Traceable but higher maintenance than auto-instrumentation. |
| **Black Box Logic** | **U** | Logic with zero telemetry visibility. |

## Architecture

```mermaid
graph TD
```

## Context

[Auto-Generated Placeholder for Compliance]

## PADU Table

[Auto-Generated Placeholder for Compliance]

## Enforcement

[Auto-Generated Placeholder for Compliance]
