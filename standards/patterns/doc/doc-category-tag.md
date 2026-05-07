---
id: doc-category-tag
type: pattern
pillar: developer
category: geometry
glossary_refs: [context.glossary, frontmatter.glossary]
---

[Home](/) > [Docs](/docs/readme.md) > [Developer](/docs/developer/readme.md) > [Pattern](readme.md) > Category Tag

# Pattern: Category Tag

## 1. Problem
In a flat pattern directory (142+ files), machine consumers and agents cannot determine a pattern's domain without parsing its title or content. Human readers scanning logs or search results lack immediate context for what category a pattern belongs to.

## 2. Solution
Every pattern file's YAML frontmatter includes a `category` field drawn from a fixed vocabulary. The canonical vocabulary is maintained in the Category Index at the bottom of [docs/developer/pattern/readme.md](readme.md).

### Frontmatter Example
```yaml

## Architecture

```mermaid
graph TD
```
