---
id: search-kernel.skill
title: Kernel Semantic Search
type: skill
tags: [audit, search, grep, discovery, tool, action, execution]
interface:
  input: { query: "search_term", domain: "path/to/dir" }
  output: { results: ["file_path:line_number:content"] }
implementation:
  engine: "grep"
  command: "grep -rnE '{{query}}' {{domain}} --include='*.md'"
summary: Performs high-speed, line-numbered search across the Knowledge Graph.
---

# Kernel Semantic Search

## Context
Finding specific patterns, headers, or references across 100+ files requires a high-speed search engine. This skill uses `grep` to provide instant, line-numbered results for any semantic query.

## Architecture

```mermaid
graph TD
    Query[Query: Header/Pattern] --> Grep[Engine: grep -rnE]
    Grep --> Filter[Filter: *.md]
    Filter --> Result[List: Path:Line:Content]
```

## Execution Steps
1. Define the query pattern (e.g., `## Quality Gate`).
2. Specify the domain (e.g., `agents/`).
3. Execute and process the line-numbered results.

## Verification Protocol
1. Search for a known string (e.g., `id: operator.agent`).
2. Verify that `agents/operator.agent.md` is returned with the correct line number.

## Quality Gate
- **Verification**: Output must include line numbers for rapid navigation.
- **Enforcement**: Must be used for all "Where is X defined?" queries to save tokens.
