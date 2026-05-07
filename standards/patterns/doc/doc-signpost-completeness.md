---
id: doc-signpost-completeness
type: pattern
pillar: developer
category: geometry
glossary_refs: [agent.glossary]
---[Home](/) > [Docs](/docs/readme.md) > [Developer](/docs/developer/readme.md) > [Pattern](readme.md) > Signpost Completeness

# Pattern: Signpost Completeness

## 1. Problem
A documentation subdirectory without a `readme.md` signpost is invisible to navigational tooling and agent discovery. Parent readmes that omit subdirectories from their listing create orphaned branches in the Knowledge Graph.

## 2. Solution
Every subdirectory under `docs/` that contains markdown files **must** have a `readme.md` signpost. Every parent directory's readme **must** list all child subdirectories in both its human-readable **Sub-directories** section and its **Machine Navigation Metadata** YAML block.

### Signpost Readme Template
```markdown

## Architecture

```mermaid
graph TD
```
