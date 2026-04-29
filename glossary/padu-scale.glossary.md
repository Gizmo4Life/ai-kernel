---
id: padu-scale.glossary
title: PADU Scale
type: glossary
version: 1
created: 2026-04-28
updated: 2026-04-28
tags: [core, governance, quality]
summary: A four-tier rating system (Preferred, Acceptable, Discouraged, Unacceptable) for evaluating project practices.
aliases: [rating-system, compliance-scale]
related: [standard.glossary]
---

# PADU Scale

The **PADU Scale** is the kernel's mechanism for categorizing and enforcing technical decisions. It allows for nuance between "always do this" and "never do this."

## Ratings

| Rating | Code | Description |
|---|---|---|
| **Preferred** | **P** | The default choice. Use this unless there is a specific, documented reason not to. |
| **Acceptable** | **A** | A valid alternative that requires no special justification but is not the primary recommendation. |
| **Discouraged** | **D** | Avoid this if possible. If used, the rationale must be documented and approved. |
| **Unacceptable** | **U** | Never use. Agents are forbidden from proposing or implementing these practices. |
