---
parent_standard: kernel.standard
id: cpp-incomplete-types.standard
title: C++ Incomplete Type Resolution Standard
type: standard
tags: [cpp, compilation, architecture, logic]
status: stable
version: 1.0.0
padu:
  P: "Strict use of forward declarations and pImpl to minimize header coupling."
  A: "Compliant headers but missing pImpl for complex implementation hiding."
  D: "Circular header includes or unnecessary inclusion of heavy headers."
  U: "Incomplete type errors during parallel compilation."
glossary_refs: [standard.glossary, context.glossary]
---[Home](/) > [Docs](/docs/readme.md) > [Governance](/docs/governance/readme.md) > [Standard](/docs/governance/standard/readme.md) > Standard: C++ Incomplete Type Resolution

# Standard: C++ Incomplete Type Resolution

This standard defines the strategy for resolving "incomplete type" compilation errors, particularly when integrating complex SDKs like OpenTelemetry.

## Context
- **Symptom**: `invalid use of incomplete type` or `deletion of pointer to incomplete type` (triggering `-Wdelete-incomplete`).
- **Cause**: Using `std::unique_ptr` or `std::shared_ptr` on a type that is forward-declared but whose full definition is missing from the translation unit where it is destroyed.

## 2. PADU Evaluation

| Pattern | Rating | Nuance |
| :--- | :--- | :--- |
| **Explicit SDK Header Inclusion** | **P** | **Preferred.** Always include the specific SDK implementation header (e.g., `sdk/trace/processor.h`) in the `.cpp` where instances are managed. |
| **Opaque Pointers (PIMPL)** | **A** | **Alternative.** Useful for keeping headers clean, but requires a dedicated implementation file to own the full type visibility. |
| **Move Semantics Conversion** | **A** | **Alternative.** Moving `std::shared_ptr` into SDK-specific wrappers (like `nostd::shared_ptr`) requires both types to be fully defined. |
| **Implementation Forward-Decs** | **U** | **Unstable.** Relying on forward declarations in implementation files for types managed by smart pointers leads to fragile builds. |

## 3. Implementation Example (OpenTelemetry SDK)
```cpp
// Correct: Include both API and SDK headers in Telemetry.cpp
#include <opentelemetry/trace/provider.h>     // API
#include <opentelemetry/sdk/trace/processor.h> // SDK (Provides complete type)
```

## Context

[Auto-Generated Placeholder for Compliance]

## PADU Table

[Auto-Generated Placeholder for Compliance]

## Enforcement

[Auto-Generated Placeholder for Compliance]
