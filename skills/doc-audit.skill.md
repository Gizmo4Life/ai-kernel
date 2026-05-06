---
id: doc-audit.skill
title: Document Auditor
type: skill
tags: [quality, documentation, audit, tool, action, how-to]
interface:
  input: { target_dir: "path/to/directory" }
  output: { violations: { "file_path": ["violation_type"] } }
implementation:
  engine: "python3 drivers/doc_auditor.py"
  command: "python3 drivers/doc_auditor.py {{target_dir}}"
summary: High-performance structural auditor that enforces mandatory headers across the AI Kernel.
interface:n  input: { query: "string" }n  output: { results: [] }nimplementation:n  engine: "bash"n  command: "grep {{query}} ."
parent_standard: skill-file.standard
glossary_refs: [context.glossary, skill.glossary, standard.glossary]
---

# Document Auditor

## Context
Structural integrity is the foundation of the AI Kernel's machine-readability. This skill replaces manual "reading" with deterministic regex-based parsing to ensure every node possesses its mandatory headers (Context, Architecture, Quality Gate).

## Architecture

```mermaid
graph TD
    skill-file.standard --> doc-audit.skill
```

## Execution Steps
1. **Target Identification**: Specify the folder to be audited.
2. **Engine Invocation**: Run the `doc_auditor.py` script against the target.
3. **Synthesis**: Process the JSON output to identify high-priority debt.

## Verification Protocol
1. Create a "Bad File" missing a `## Context` header.
2. Run `python3 drivers/doc_auditor.py .`
3. Verify that the "Bad File" is correctly flagged in the JSON output.

## Quality Gate
- **Verification**: Output must be a valid JSON object.
- **Enforcement**: 100% accuracy in detecting missing mandatory headers.
