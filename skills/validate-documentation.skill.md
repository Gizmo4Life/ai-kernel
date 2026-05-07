---
id: validate-documentation.skill
title: Documentation Validation Audit
type: skill
tags: [audit, documentation, verification, transactional]
interface:
  input: { target_path: "string" }
  output: { status: "success" }
summary: An atomic check to verify that documentation nodes are present and compliant.
---# Documentation Validation

## Execution
- **Command**: `python3 drivers/kernel/global_compliance_auditor.py <target_path>`

## Verification
- **Check**: Verify the audit output contains zero "D" or "U" rated findings for the target.

## Reversion
- **Undo**: Not applicable for read-only audits. For repair waves, use `git checkout`.

## Architecture

```mermaid
graph TD
```
