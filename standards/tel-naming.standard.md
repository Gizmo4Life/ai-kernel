---
parent_standard: kernel.standard
id: tel-naming.standard
title: Telemetry Naming Standard
type: standard
tags: [telemetry, observability, naming, rules, governance, compliance]
summary: Standards for naming spans, metrics, and logs to ensure cross-domain observability.
requirements: [parent_standard, "## PADU Table", "## Enforcement", "## Context", "## Context
This standard defines a deterministic hierarchy for all telemetry signals. It ensures that observability data from different services (e.g., a C++ backend and a React frontend) can be correlated seamlessly in a single dashboard.

## The Tri-Part Pattern
All telemetry keys (Spans, Metrics, Log Attributes) must follow the **`<pillar>.<module>.<action>`** pattern:

- **Pillar**: The high-level functional domain (e.g., `auth`, `storage`, `ui`, `kernel`).
- **Module**: The specific component or service (e.g., `session`, `cache`, `router`, `integrity`).
- **Action**: The technical operation being performed (e.g., `validate`, `fetch`, `render`, `audit`).

## PADU Table

| Practice | Rating | Rationale | Enforcement | Exception |
|---|---|---|---|---|
| Use Tri-Part Naming | **P** | Enables deterministic filtering and grouping. | `tel-audit.skill` | None |
| Lowercase Dot Notation | **P** | Standardizes across different telemetry providers. | `tel-audit.skill` | None |
| Include `correlation_id` | **P** | Critical for tracing requests across boundaries. | evaluate-against-standard.skill | None |
| Use CamelCase or SnakeCase | **U** | Inconsistent with the global dot-notation standard. | `tel-audit.skill` | None |
| Vague actions (e.g., `.process`) | **D** | Provides zero diagnostic value. | evaluate-against-standard.skill | None |

"Hard" observability requires a shared vocabulary. By forcing a pillar-based hierarchy, we prevent "Key Pollution" where different developers use different names for the same logical event.

## Enforcement
The posture is **Hybrid-Automated**. We will implement a `tel-audit.skill` to regex-check keys in codebase strings.
