---
id: resolve-glossary-conflict.instruction
title: Resolve Glossary Conflict
type: instruction
tags: [conflict-resolution, glossary, cleanup, workflow, process, orchestration]
summary: Workflow for merging similar glossary entries or clarifying ambiguous terms.
parent_standard: instruction-file.standard
skills: [auto-link-glossary.skill, surgical-refactor.skill, search-kernel.skill, doc-audit.skill,  find-glossary-terms.skill, provide-glossary-guidance.skill, evaluate-against-standard.skill ]
standards: [glossary-entry.standard]
preconditions: - Two or more glossary entries are identified as potentially redundant.
  - Or, a term has multiple conflicting definitions.
glossary_refs: [context.glossary, frontmatter.glossary, instruction.glossary, skill.glossary, standard.glossary]
---

## Context
Workflow for merging similar glossary entries or clarifying ambiguous terms.


# Resolve Glossary Conflict

Flynn's workflow for maintaining the "Single Source of Truth" in the glossary.


## Architecture

```mermaid
graph TD
    instruction-file.standard --> resolve-glossary-conflict.instruction
    resolve-glossary-conflict.instruction --> auto-link-glossary[auto-link-glossary.skill]
    resolve-glossary-conflict.instruction --> surgical-refactor[surgical-refactor.skill]
    resolve-glossary-conflict.instruction --> search-kernel[search-kernel.skill]
    resolve-glossary-conflict.instruction --> doc-audit[doc-audit.skill]
    resolve-glossary-conflict.instruction --> find-glossary-terms[find-glossary-terms.skill]
    resolve-glossary-conflict.instruction --> provide-glossary-guidance[provide-glossary-guidance.skill]
    resolve-glossary-conflict.instruction --> evaluate-against-standard[evaluate-against-standard.skill]
```
## Execution Steps

1. **Map the Conflict**: List the IDs and summaries of all conflicting entries.
2. **Evaluate Core Intent**: Determine the primary concept that encompasses all variants.
3. **Select Canonical Term**: Choose the most descriptive and standard term as the primary `id`.
4. **Merge Content**: Combine the best parts of all definitions into the canonical file.
5. **Update Aliases**: Add the decommissioned terms to the `aliases` field of the canonical entry.
6. **Redirect References**: (Optional but Recommended) Search for references to the old IDs and update them to point to the new canonical entry.
7. **Decommission**: Delete the redundant files.

## Postconditions
1. The system state matches the goal defined in the frontmatter.
2. All related Knowledge Graph nodes are updated and linked.
