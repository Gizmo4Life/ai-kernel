import os
import re

"""
Diamond Pattern Hardener (v1.0.0)
---
Purpose: Mass-injects Diamond Frontmatter into migrated pattern files.
Scope: standards/patterns/**/*.md
"""

def harden_pattern(fpath):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already has ID
    if 'id:' in content[:100]:
        return

    rel_path = os.path.relpath(fpath, '/Users/Dan/repos/ai-kernel')
    node_id = os.path.basename(fpath).replace('.md', '.pattern')
    title = os.path.basename(fpath).replace('.md', '').replace('-', ' ').title()
    
    # Extract existing frontmatter if present
    match = re.search(r'^---\s*(.*?)\s*---\s*', content, re.DOTALL)
    existing_fm = match.group(1) if match else ""
    
    header = f"""---
id: {node_id}
title: {title}
type: pattern
tags: [engineering, pattern, global]
summary: Universal engineering pattern extracted from legacy project logic.
---

"""
    if match:
        new_content = header + content[match.end():]
    else:
        new_content = header + content

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"[HARDEN] Pattern Secured: {node_id}")

def run_hardening_wave():
    pattern_dir = '/Users/Dan/repos/ai-kernel/standards/patterns'
    for root, dirs, files in os.walk(pattern_dir):
        for file in files:
            if file.endswith('.md'):
                harden_pattern(os.path.join(root, file))

if __name__ == "__main__":
    run_hardening_wave()
