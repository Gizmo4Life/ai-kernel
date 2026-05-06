---
id: save-conversation-context.skill
title: Save Conversation Context
type: skill
tags: [maintenance, context, tool, action, execution]
summary: Saves curated information from the current conversation to the `context/` folder.
tool: editor
inputs:
  filename: The name of the context file.
  content: The curated information to save.
outputs:
  status: Confirmation of the save action.
standards: [kernel.standard]
glossary_refs: [context.glossary]
---

## Context
Saves curated information from the current conversation to the `context/` folder.


# Save Conversation Context

This skill ensures that important decisions and data survive across AI sessions.


## Architecture

```mermaid
graph TD
    Start((Start)) --> Process[Process: Logic Flow] --> End((End))
```
## Execution Steps

1. **Format Content**: Ensure the `content` includes frontmatter with `type: context`.
2. **Path Selection**: Use the `context/` directory.
3. **Write**: Save the file using the `.context.md` extension.
4. **Link**: provide a link to the new context file.


## Verification Protocol
1. Perform a manual dry-run of the execution steps.
2. Verify that the output matches the expected result defined in the Quality Gate.

## Quality Gate

Context management is governed by the **[Kernel Standard](../standards/kernel.standard.md)**.
- **Verification**: Ensure the filename is descriptive and follows the `[topic].context.md` pattern.
- **Enforcement**: Context files must not contain redundant data already in the glossary; they should link to the glossary instead.
