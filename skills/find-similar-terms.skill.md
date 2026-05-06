---
id: find-similar-terms.skill
title: Glossary Similarity Auditor
type: skill
tags: [quality, glossary, search, tool, action, execution]
interface:
  input: { threshold: "float (0.0 to 1.0)" }
  output: { collisions: [{"term1": "id1", "term2": "id2", "similarity": "0.8"}] }
implementation:
  engine: "python3 drivers/similarity_auditor.py"
  command: "python3 drivers/similarity_auditor.py {{threshold}}"
summary: Identifies conceptually overlapping or duplicate terms in the glossary to prevent semantic sprawl.
parent_standard: skill-file.standard
glossary_refs: [context.glossary, instruction.glossary, skill.glossary, standard.glossary]
---

# Glossary Similarity Auditor

## Context
Semantic ambiguity is a form of architectural debt. If two terms describe the same concept (e.g., "Skill" vs. "Function"), they should be consolidated. This skill uses word-overlap analysis to identify potential collisions.

## Architecture

```mermaid
graph TD
    skill-file.standard --> find-similar-terms.skill
```

## Execution Steps
1. **Engine Invocation**: Run `similarity_auditor.py`.
2. **Analysis**: Review the JSON list for any similarity scores above 0.5.
3. **Consolidation**: Use the `resolve-naming-ambiguity.instruction` to merge overlapping terms.

## Verification Protocol
1. Create two glossary entries with identical summaries.
2. Run `python3 drivers/similarity_auditor.py`.
3. Verify that the two terms are flagged with a similarity score of `1.00`.

## Quality Gate
- **Verification**: Output must be a valid JSON collision report.
- **Enforcement**: Mandatory step during "Naming and Purity" audits.
