---
id: resolve-glossary-conflict.instruction
title: Resolve Glossary Conflict
type: instruction
version: 1
created: 2026-04-28
updated: 2026-04-28
tags: [conflict-resolution, glossary, cleanup]
summary: Workflow for merging similar glossary entries or clarifying ambiguous terms.
goal: A clean glossary with non-overlapping entries and comprehensive aliases.
skills: [ find-glossary-terms.skill, provide-glossary-guidance.skill, evaluate-against-standard.skill ]
standards: [glossary-entry.standard]
preconditions: - Two or more glossary entries are identified as potentially redundant.
  - Or, a term has multiple conflicting definitions.
---

# Resolve Glossary Conflict

Flynn's workflow for maintaining the "Single Source of Truth" in the glossary.

## Steps

1. **Map the Conflict**: List the IDs and summaries of all conflicting entries.
2. **Evaluate Core Intent**: Determine the primary concept that encompasses all variants.
3. **Select Canonical Term**: Choose the most descriptive and standard term as the primary `id`.
4. **Merge Content**: Combine the best parts of all definitions into the canonical file.
5. **Update Aliases**: Add the decommissioned terms to the `aliases` field of the canonical entry.
6. **Redirect References**: (Optional but Recommended) Search for references to the old IDs and update them to point to the new canonical entry.
7. **Decommission**: Delete the redundant files.
