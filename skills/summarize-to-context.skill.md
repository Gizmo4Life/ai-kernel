---
id: summarize-to-context.skill
title: Summarize to Context
type: skill
tags: [memory, context.glossary, summarization, tool, action, execution]
summary: Extracts decisions, rationales, and key technical findings from a conversation into a structured context file.
parent_standard: skill-file.standardtool: editor
inputs: conversation_log: The raw conversation transcript.
  target_file: The name of the file in /context/ to update or create.
outputs: context_entry: A structured summary of the conversation.
standards: []
glossary_refs: [context.glossary, heuristics.glossary, skill.glossary]
---

## Context
Extracts decisions, rationales, and key technical findings from a conversation into a structured context file.


# Summarize to Context

This skill implements the "Context Management" directive by distilling transient conversation history into persistent repository knowledge.


## Architecture

```mermaid
graph TD
    skill-file.standardtool --> summarize-to-context.skill
```
## Extraction [Heuristics](glossary/heuristics.glossary.md)

Focus on:
- **Decisions**: What was agreed upon? (e.g., "Move glossary to root").
- **Rationales**: Why was it decided? (e.g., "To increase visibility").
- **Technical Specs**: New IDs, schemas, or naming conventions established.
- **Open Questions**: Anything left unresolved for the next session.

## Format

```markdown
## [Date] — [Brief Topic]

- **Key Decision**: ...
- **Rationale**: ...
- **Impact**: ... (e.g., "Updated 5 files in /standards")
- **Open Questions**: ...
```

## Verification Protocol
1. Perform a manual dry-run of the execution steps.
2. Verify that the output matches the expected result defined in the Quality Gate.
