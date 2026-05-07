---
id: versioning.standard
title: Versioning Standard
type: standard
tags: [governance, maintenance, versioning, rules, compliance]
summary: Rules for internal versioning and change tracking of Knowledge Graph nodes.
requirements: [parent_standard, "## PADU Table", "## Enforcement", "## Context", "## Context
This standard defines how the AI Kernel tracks the evolution of its nodes. To reduce "Frontmatter Bloat," versioning is handled as an internal bookkeeping logic rather than a manual field in the file body.

## Internal Versioning Logic
The AI Kernel uses **Content Hashing** to track state. The **[Integrity Guardian](../agents/integrity-guardian.agent.md)** maintains an internal `manifest.json` (or similar context file) that maps file IDs to their current SHA-256 hash.

- **Change Detection**: If the current hash does not match the manifest, the node is considered "Updated."
- **Breaking Changes**: If the `id` of a file changes, it is considered a **Major Version** change (Breaking). All dependent instructions must be refactored.
- **Verification**: The **Linkage Specialist** ensures that cross-references remain valid regardless of content updates.

## PADU Table

| Practice | Rating | Rationale | Enforcement | Exception |
|---|---|---|---|---|
| Use Content Hashing | **P** | Provides an objective, automated check for changes. | `integrity-guardian.agent` | None |
| Keep Versioning in Frontmatter | **U** | Administrative bloat; reduces data footprint for discovery. | `check-id-uniqueness.skill` | None |
| Major version on ID change | **P** | Signals a breaking link in the graph. | `linkage-specialist.agent` | None |
| Rely on Git/Filesystem Timestamps | **P** | Uses existing system metadata instead of manual fields. | `operator.agent` | None |

"Hardness" comes from automation. Manual versioning is prone to drift and human error. By shifting to content hashes and system metadata, we ensure the kernel's state is always accurately reflected without manual overhead.

## Enforcement
The posture is **Automated**. The **Integrity Guardian** manages the hash-based manifest during the self-healing loop.

### Gaps
#### Hidden Breaking Changes
**Risk**: A functional change in a skill might not change its `id`, but could break an instruction.
**Be Wary Of**: Large content changes that preserve the ID but alter the execution semantic.
