---
id: save-conversation-context.skill
title: Save Conversation Context
type: skill
version: 1
created: 2026-04-28
updated: 2026-04-28
tags: [memory, context.glossary, documentation]
summary: Saves important information collected during a conversation into the /context/ directory.
tool: editor
inputs: filename: The name of the context file (e.g., 'project-x-architecture.md').
  content: The summarized information to save.
outputs: status: Confirmation of file creation in /context/.
standards: []
glossary_refs: []
---

# Save Conversation Context

This skill implements the **Context Management** requirement from `AGENTS.md`. It ensures that long-term memory of a project or conversation is persisted outside of the transient conversation log.

## Execution Steps

1. **Summarize**: Distill the conversation into key decisions, findings, or code snippets.
2. **Name**: Choose an appropriately named file based on the context (e.g., `user-preferences.md`, `feature-y-design.md`).
3. **Write**: Create or append to the file in the `/context/` directory.
4. **Link**: (Optional) Reference related glossary terms or standards in the context file.
