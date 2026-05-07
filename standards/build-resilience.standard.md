---
parent_standard: kernel.standard
id: build-resilience.standard
title: Build Resilience Standard (CMake/CI)
type: standard
tags: [ops, build, cicd, resilience, cmake]
status: stable
version: 1.0.0
padu:
  P: "Explicit source registration (no globbing); hermetic, deterministic builds."
  A: "Deterministic builds but with version-locked remote dependencies."
  D: "Globbing (file discovery) or non-deterministic build order."
  U: "Build fails intermittently or requires manual network access."
glossary_refs: [standard.glossary]
---# Build Resilience Standard

## 1. CMake Registration
- **Mandatory**: Every source file MUST be registered explicitly in the build configuration (e.g., `CMakeLists.txt`).
- **Forbidden**: Globbing (`file(GLOB ...)`) is D-rated. It leads to non-deterministic builds and unintended inclusions.

## 2. Dependency Management
- **Hybrid Acquisition**: Use local dependencies when available; remote fallback MUST be version-locked and optional.
- **Object Sharing**: Share compiled objects between production and test targets to ensure parity and speed.

## 3. Quality Gate
- **Verification**: Run build from a clean state without network access.
- **Enforcement**: Any PR introducing globbing or unversioned remote fetches will be **Rejected**.

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
