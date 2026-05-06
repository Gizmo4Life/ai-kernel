---
id: perform-atomic-extraction.instruction
title: Perform Atomic Extraction
type: instruction
tags: [workflow, de-conflation, refactor, process, orchestration]
summary: The master workflow for moving out-of-scope content to its correct SSOT domain and restoring reachability.
parent_standard: instruction-file.standard
skills: [auto-link-glossary.skill, surgical-refactor.skill, search-kernel.skill, doc-audit.skill, identify-out-of-scope-content.skill, linkage-specialist.agent]
standards: [atomic-extraction.standard, kernel.standard]
preconditions:
  - An out-of-scope content block has been identified.
glossary_refs: [agent.glossary, context.glossary, instruction.glossary, reachability.glossary, skill.glossary, standard.glossary]
---

# Perform Atomic Extraction

## Context
This instruction is the "Scalpel" of the AI Kernel. It orchestrates the removal of foreign logic and the insertion of SSOT links, ensuring that the system remains atomic as it evolves.

## Architecture

```mermaid
graph TD
    instruction-file.standard --> perform-atomic-extraction.instruction
    perform-atomic-extraction.instruction --> auto-link-glossary[auto-link-glossary.skill]
    perform-atomic-extraction.instruction --> surgical-refactor[surgical-refactor.skill]
    perform-atomic-extraction.instruction --> search-kernel[search-kernel.skill]
    perform-atomic-extraction.instruction --> doc-audit[doc-audit.skill]
    perform-atomic-extraction.instruction --> identify-out-of-scope-content[identify-out-of-scope-content.skill]
    perform-atomic-extraction.instruction --> linkage-specialist.agent[linkage-specialist.agent]
```

## Execution Steps
1. **Isolation**: Capture the exact character-range of the out-of-scope content.
2. **Transfer**: Create a new file in the appropriate domain (e.g., `glossary/*.md`) with the extracted content.
3. **Formalization**: Apply the mandatory headers (Context, Architecture, Gate) to the new file.
4. **Linkage**: Replace the original content block in the source file with a markdown link to the new node.
5. **Validation**: Run the **Connectivity Audit** to ensure the new node is reachable.

## Postconditions
1. The source file no longer contains the out-of-scope logic.
2. A new, fully compliant SSOT node exists in the correct domain.
3. A reachable link exists from the source to the target.

## Quality Gate
- **Verification**: The extraction must not result in "Dead Nodes" (orphans).
- **Enforcement**: Any extraction that removes logic without providing a functional replacement link is **Unacceptable (U)**.
