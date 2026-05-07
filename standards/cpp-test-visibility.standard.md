---
id: cpp-test-visibility.standard
title: C++ Test Visibility Standard
type: standard
tags: [cpp, testing, visibility, architecture]
status: stable
version: 1.0.0
padu:
  P: "Private members made visible to tests via 'friend' classes or accessor patterns."
  A: "Tests focus only on public interface but logic is complex."
  D: "Exposing private data as public just for testing."
  U: "Critical logic is untestable due to encapsulation constraints."
glossary_refs: [context.glossary, standard.glossary]
---[Home](/) > [Docs](/docs/readme.md) > [Governance](/docs/governance/readme.md) > [Standard](/docs/governance/standard/readme.md) > Standard: C++ Test Visibility

# Standard: C++ Test Visibility

This standard defines the rules for exposing class internals to unit tests to ensure high testability without compromising encapsulation for production logic.

## 1. Context
- **Symptom**: Compilation errors in test suites attempting to access `private` or `protected` members required for state verification.
- **Goal**: Enable direct verification of critical internal logic (e.g., `refreshStats`).

## 2. PADU Evaluation

| Pattern | Rating | Nuance |
| :--- | :--- | :--- |
| [cpp-visibility-promotion](/docs/developer/pattern/cpp-visibility-promotion.md) | **P** | **Preferred.** Explicitly moving members to `public` provides the cleanest interface for Catch2 and keeps the implementation standard-compliant. |
| **Friend Class Testing** | **A** | **Alternative.** Useful if the logic is sensitive and cannot be exposed, but creates high coupling with specific test files. |
| **Logic Duplication** | **U** | **Unstable.** Copying logic into tests for verification leads to maintenance drift and hidden bugs. |

## 3. Best Practice
Only promote members that are critical to the "Success Criteria" defined in the feature's elicitation documentation.

## Architecture

```mermaid
graph TD
```
