# Spacegame Documentation Synthesis (v1.0.0)

This document categorizes the documentation patterns discovered in the Spacegame repository to establish the "Preferred Practice" for the AI Kernel.

## [Preferred] [P-Rated]
> [!TIP]
> These patterns represent high-integrity, machine-readable logic.

| Pattern | Rationale |
| :--- | :--- |
| **Tiered Logic (T2/T3)** | Separating functional domains (Capabilities) from components (Modules) prevents architectural sprawl. |
| **Pillar-Prefixed Naming** | Using `game-`, `engine-`, or `ops-` prefixes enables instant semantic categorization. |
| **Atomic Extraction** | Moving generic logic (patterns) out of project docs into a sidecar repository (AI Kernel). |
| **Determinism** | Using `.[type].md` suffixes for 0-token discovery (Standard, Skill, Instruction). |

## [Acceptable] [A-Rated]
> [!NOTE]
> These patterns are functional but require maintenance.

| Pattern | Rationale |
| :--- | :--- |
| **Doc-as-Code** | Maintaining documentation alongside source files is better than an external wiki. |
| **Mermaid Topology** | Visualizing system connections is useful in Capabilities/Modules (but discouraged in Standards). |
| **Pillar Indices** | Using `readme.md` files as maps for subdirectories. |

## [Discouraged] [D-Rated]
> [!WARNING]
> These patterns create structural debt and noise.

| Pattern | Rationale |
| :--- | :--- |
| **Un-suffixed Filenames** | `*.md` files are ambiguous; agents cannot distinguish between a Rule (Standard) and an Action (Skill) via `ls`. |
| **Global Context Bloat** | Repeating the entire system's background in every atomic file increases token waste. |
| **Deep Directory Nesting** | Nesting files 4+ layers deep (e.g., `docs/arch/mod/sub/`) hides the Knowledge Graph. |

## [Unacceptable] [U-Rated]
> [!CAUTION]
> These patterns must be purged immediately.

| Pattern | Rationale |
| :--- | :--- |
| **Broken Fences** | Malformed frontmatter that merges with the body. |
| **Literal Newlines** | Using `\n` in text instead of actual carriage returns. |
| **Duplicate IDs** | Re-using the same `id:` across multiple files. |
