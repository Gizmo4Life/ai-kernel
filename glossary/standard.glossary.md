---
id: standard.glossary
title: Standard
type: glossary
parent_standard: glossary-entry.standard
tags: [core, governance, quality, definition, term, meaning]
summary: A set of rules or guidelines governing the creation and maintenance of content, evaluated using the PADU scale.
aliases: [guideline, rule, requirement]
related: [ padu-scale.glossary, glossary-entry.glossary ]
---

## Context
Canonical definition of a core AI Kernel concept.


# Standard

A **Standard** is a formal document that defines the quality bars and constraints for a specific domain (e.g., C++ coding, documentation structure, API design).


## Architecture

```mermaid
graph TD
    glossary-entry.standard --> standard.glossary
```
## Key Characteristics

- **PADU Scale**: Uses Preferred, Acceptable, Discouraged, and Unacceptable ratings to categorize practices.
- **Enforcement**: Standards are used by skills and agents to validate work products.
- **Scope**: Clearly defines which files or actions the standard applies to.

## Components

1. **Frontmatter**: Defines the `scope` and `applies_to` fields.
2. **PADU Table**: The core logic of the standard, mapping practices to ratings.
3. **Rationale**: Explanations for why certain practices are rated the way they are.

## Usage Constraints
- This term must only be used in its architectural context.
- Semantic drift from the canonical definition is Unacceptable (U).
