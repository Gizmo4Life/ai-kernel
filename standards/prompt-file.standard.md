---
id: prompt-file.standard
title: Prompt File Standard
type: standard
version: 3
created: 2026-05-02
updated: 2026-05-02
tags: [governance, prompt-engineering]
summary: Standards for defining reusable AI prompts in the `prompts/` directory.
scope: prompts/
parent_standard: kernel.standard
glossary_refs: [prompt.glossary, kernel.standard]
---

# Prompt File Standard

## Abstract
This standard governs the structure and quality of standalone prompts. It ensures that prompts are modular, versioned, and documented with their intended variables.

## PADU Table

| Practice | Rating | Rationale | Enforcement | Exception |
|---|---|---|---|---|
| Define `variables` | **P** | Lists expected inputs. | `audit-frontmatter-completeness.skill` | None |
| Include `model_recommendation` | **A** | Context for tuning. | Agent Audit (Auditor) | Model-agnostic |
| Use Clear Versioning | **P** | Tracks model evolution. | `audit-frontmatter-completeness.skill` | None |
| Hardcoding specific data | **U** | Prevents reusability. | Agent Audit (Auditor) | None |
| Vague instructions | **D** | Non-deterministic behavior. | Agent Audit (Auditor) | None |

## Rationale
Standardizing prompt formats allows for automated metadata auditing, ensuring that all prompts are properly versioned and variable-defined before use.

## Enforcement
The posture for prompts is **Agent-Audited**. Structural elements (variables, versioning) are caught by metadata audit, but the "quality" and "determinism" of the prompt logic require an audit by the **Standards Auditor**.

### Gaps
#### Prompt Injection / Security
**Risk**: Reusable prompts may be written in a way that is vulnerable to injection if the `variables` are not properly sanitized by the calling agent.
**Be Wary Of**: Prompts that ask the model to "ignore all previous instructions" or similar patterns.

#### Regression
**Risk**: A prompt version update may work better for one model but break behavior for another.
**Be Wary Of**: Changing core prompt logic without updating the `version` field.
