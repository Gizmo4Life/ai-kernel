---
id: antipattern.glossary
title: Antipattern
type: glossary
version: 1
created: 2026-04-28
updated: 2026-04-28
tags: [core, quality, software-engineering]
summary: A common response to a recurring problem that is usually ineffective and risks being highly counterproductive.
aliases: [bad-practice, dark-pattern]
related: [ padu-scale.glossary, standard.glossary ]
---

# Antipattern

An **Antipattern** is a pattern that may appear to be a beneficial solution to a problem but actually results in negative consequences.

## Role in the Kernel

In the AI Kernel, antipatterns are codified within **Standards** and assigned **U** (Unacceptable) or **D** (Discouraged) ratings on the **PADU Scale**.

## Identification

Antipatterns are often identified during codebase scans. When a pattern is found to be:
- Widely used but causing frequent bugs.
- Difficult to maintain or test.
- Obscuring the "pit of success".

It should be documented in the relevant standard to steer agents toward **P** (Preferred) alternatives.
