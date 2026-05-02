---
id: prompt-file.standard
title: Prompt File Standard
type: standard
version: 1
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
This standard governs the structure and quality of standalone prompts. It ensures that prompts are modular, versioned, and documented with their intended model performance and variables. By separating prompt logic from implementation code (skills), we enable easier testing and refinement of prompt engineering.

## PADU Table

| Practice | Rating | Rationale | Exception |
|---|---|---|---|
| Define `variables` in frontmatter | **P** | Explicitly lists the inputs the prompt expects (e.g., `{{code}}`). | Simple static prompts. |
| Include `model_recommendation` | **A** | Notes which model (e.g., Claude 3.5 Sonnet) the prompt was tuned for. | Model-agnostic prompts. |
| Use Clear Versioning | **P** | Critical for tracking performance shifts as models evolve. | None |
| Hardcoding specific data | **U** | Prevents the prompt from being reusable. | None |
| Vague instructions | **D** | Leads to non-deterministic agent behavior. | None |

## Rationale
Prompts are a core asset of the AI Kernel. Standardizing their format allows agents to dynamically load and inject them into their workflows without needing to "know" the prompt's content beforehand.
