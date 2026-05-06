---
id: review-pull-request.instruction
title: Review Pull Request
type: instruction
tags: [workflow, git, github, review, audit, process, orchestration]
summary: A workflow for synchronizing local state with a Pull Request and auditing the changes against repository standards and human reviewer feedback.
parent_standard: instruction-file.standard
skills: [git-fetch.skill, git-diff-audit.skill, github-pr-audit.skill, evaluate-against-standard.skill, trace-impact-chain.skill]
instructions: [maintain-kernel-integrity.instruction]
standards: [kernel.standard, quality-gate.standard, versioning.standard]
preconditions:
  - A Pull Request is open on the remote origin.
  - The agent has a valid GITHUB_TOKEN if comments are required.
glossary_refs: [agent.glossary, context.glossary, frontmatter.glossary, instruction.glossary, skill.glossary, standard.glossary]
---

# Review Pull Request

## Context
High-integrity development requires a bridge between "Automated Audits" and "Human Intent." This instruction codifies the process of ingesting PR metadata (diffs, comments) to ensure that the final merge preserves the Diamond Logic of the AI Kernel.

## Architecture

```mermaid
graph TD
    instruction-file.standard --> review-pull-request.instruction
    review-pull-request.instruction --> git-fetch[git-fetch.skill]
    review-pull-request.instruction --> git-diff-audit[git-diff-audit.skill]
    review-pull-request.instruction --> github-pr-audit[github-pr-audit.skill]
    review-pull-request.instruction --> evaluate-against-standard[evaluate-against-standard.skill]
    review-pull-request.instruction --> trace-impact-chain[trace-impact-chain.skill]
```

## Execution Steps

### 1. Synchronization Phase
1. **Fetch**: Invoke `git-fetch.skill` to synchronize remote branch metadata.
2. **Checkout**: Switch the local workspace to the PR's source branch.

### 2. Data Ingestion Phase
1. **Audit Diffs**: Run `git-diff-audit.skill` to identify the files modified in the PR.
2. **Audit Comments**: Invoke `github-pr-audit.skill` to ingest human reviewer feedback and change requests.

### 3. Impact Analysis Phase
1. **Blast Radius**: For every modified core node (Glossary, Standard), run `trace-impact-chain.skill` to identify secondary breakage.
2. **Compliance**: Run `evaluate-against-standard.skill` on all modified files to ensure zero logic debt.

### 4. Triage & Synthesis
1. **Comparison**: Analyze the solution against the reviewer comments.
2. **Remediation**: If conflicts exist, invoke `maintain-kernel-integrity.instruction` to heal the drift.

## Postconditions
1. All reviewer comments have been addressed or triaged.
2. The PR branch is in 100% compliance with repository standards.

## Quality Gate
Review integrity is governed by the **[Kernel Standard](../standards/kernel.standard.md)**.
- **Verification**: Zero standard violations on the PR branch.
- **Enforcement**: Flynn will not approve a PR until all `github-pr-audit` comments are addressed.
