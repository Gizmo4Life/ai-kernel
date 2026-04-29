---
id: evaluate-against-standard.skill
title: Evaluate Against Standard
type: skill
version: 1
created: 2026-04-28
updated: 2026-04-28
tags: [audit, quality, padu]
summary: Evaluates a piece of content against a standard's PADU table and reports compliance.
tool: editor
inputs: content: The text or file to be evaluated.
  standard_id: The ID of the standard file to use (e.g., glossary-entry-standard).
outputs: report: A list of practices found, their PADU ratings, and any required justifications.
standards: [standard-file.standard]
glossary_refs: [ standard.glossary, padu-scale.glossary ]
---

# Evaluate Against Standard

This skill allows an agent to perform a quality audit on any content by mapping its characteristics to the rows of a [PADU table](glossary/padu-scale.glossary.md).

## Execution Steps

1. **Load Standard**: Read the file body of the specified `standard_id`.
2. **Extract Table**: Parse the PADU table from the standard.
3. **Analyze Content**: For each row in the table, check if the content follows the practice.
4. **Assign Ratings**: - If a practice is followed and rated **P** or **A**, mark as compliant.
    - If a practice is followed and rated **D**, flag for justification.
    - If a practice is violated and rated **U**, mark as a failure.
5. **Generate Report**: Present a summary table of the evaluation.
