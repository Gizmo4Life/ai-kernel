# AI Kernel

## Context
This file serves as the master entry point for understanding the agentic hierarchy of the AI Kernel. It defines how Tier 0, Tier 1, and Tier 2 agents collaborate to maintain the system.

## Architecture

```mermaid
graph TD
    User((User)) --> Operator[Operator: Tier 0]
    Operator --> Flynn[Flynn: Tier 1 Owner]
    Flynn --> SMEs[SMEs: Tier 2 Cabinet]
```

## How to Use This Framework

You are operating with the ai-kernel personal workflow framework.
This repository is a companion workspace — it provides reusable
glossary definitions, coding standards, skills, instructions,
prompts, and agent definitions.

## How to Use This Framework

### Agent Brain ###

1. [Glossary](glossary/glossary-entry.glossary.md): Before defining a concept inline, check `glossary/`.
   If a definition exists, link to it. If not, ask [flynn](agents/flynn.agent.md) for guidance on whether to create a new definition or inline it.
2. [Standards](glossary/standard.glossary.md): When working in a scoped context (e.g. C++ code),
   load the relevant standard from `standards/` and validate
   output against its [PADU table](glossary/padu-scale.glossary.md). Standards follow a hierarchical model; ensure you load the relevant parent standard (e.g. [Kernel Standard](standards/kernel.standard.md)) for global rules.
3. [Skills](glossary/skill.glossary.md): Atomic actions are defined in `skills/`. Read the
   [frontmatter](glossary/frontmatter.glossary.md) to find relevant skills, then load the body when needed, the body defines how to effectively utilize a tool or apply a skill.
4. [Instructions](glossary/instruction.glossary.md): Multi-step workflows are in `instructions/`, these should define how to coordinate skills in order to solve a problem to a high standard of quality. These files leverage standards as quality gates, and will apply them as appropriate throughout the workflow. Rather than standards defining whether or not D solutions are ever allowed, it should be context dependent, and instructions should define this in their quality gates.
5. [Prompts](glossary/prompt.glossary.md): Standalone AI instructions are in `prompts/`. Use these for reusable LLM logic and template-driven communication that exists outside of a specific skill or agent definition.
6. [Agents](glossary/agent.glossary.md): Autonomous agent definitions are in `agents/`. Each agent has an overall objective or purpose, and in its definition should be a [PADU table](glossary/padu-scale.glossary.md) that guides and constrains the agent's approach to problem solving. The frontmatter for the agent should define the tools it can use, where it has authority to propose changes vs. only suggest, and what agents it can [delegate](glossary/delegation.glossary.md) to. The frontmatter should also define any [context](glossary/context.glossary.md) (i.e. glossary, standards, instructions) that the agent should be aware of in order to solve problems effectively.

### Context Management ###
Save important information collected during a conversation in [/context/](context/) in appropriately named files for the context of the information. This is useful for organizing long term memory of a conversation or project.

## File Discovery

All content files use YAML [frontmatter](glossary/frontmatter.glossary.md). To find relevant files:
- Scan frontmatter `tags` and `scope` fields
- Use `glossary_refs` and `standards` fields to resolve dependencies
- Load file bodies only when the frontmatter indicates relevance ([Progressive Disclosure](glossary/progressive-disclosure.glossary.md))

## Constraints

- Never redefine a concept that exists in the glossary. Link to it.
- Validate output against applicable standards before presenting.
- Prefer solutions rated P or A on the [PADU scale](glossary/padu-scale.glossary.md).
- D-rated solutions require explicit justification.
- U-rated solutions must never be proposed.
