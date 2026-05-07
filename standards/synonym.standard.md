---
parent_standard: kernel.standard
id: synonym.standard
title: Discovery Tag Standard
type: standard
tags: [governance, discovery, semantics, tagging, rules, compliance]
summary: Standards for using vibrant tags to ensure Knowledge Graph discoverability and prevent logic duplication.
requirements: [parent_standard, "## PADU Table", "## Enforcement", "## Context", "## Context
Tags are the primary "Discovery Anchors" for the AI Kernel. Because agents and search engines rely on the `
tags: []` field for semantic indexing, we must use this field to include all synonyms and alternative terms. This ensures that a search for "Feedback" correctly surfaces "System-First Remediation."
## Mandatory Requirements
1. **Frontmatter**: Every file must include a `
tags: []` list.
2. **Vibrant Tagging**: The tags list must include at least 3 alternative terms or common user keywords related to the node's function.
3. **Mnemonic Tags**: Include memorable phrases (e.g., "fix-the-factory") to aid human and agentic recall.
## PADU Table
| Practice | Rating | Rationale | Enforcement | Exception |
|
glossary_refs: [agent.glossary, skill.glossary]
---

|---|---|---|---|
| Use Common Keywords | **P** | Includes terms like "fix", "wrong", "change" to match user intent. | `librarian.agent` | None |
| Include Legacy Terms | **P** | Keeps old names (e.g., "kernel-first") as tags for backward compatibility. | `standards-auditor.agent` | None |
| Tag Overloading | **D** | Adding >10 unrelated tags just to "game" the search. | Flynn Review | None |
| Missing Logic Tags | **U** | Failing to tag a core workflow with its primary action words. | `doc-audit.skill` | None |

## Enforcement
The posture is **Automated**. The `librarian.agent` will periodically audit tags for semantic coverage and suggest "Vibrant" additions based on recent conversation history.

