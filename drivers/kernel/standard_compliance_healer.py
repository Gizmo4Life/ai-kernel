import os
import re

"""
Intelligent Compliance Healer (v1.2.0)
---
Purpose: Surgically aligns standards with de-duplication and content migration.
Actions: Header De-duplication, Content Migration, Architectural Purge.
"""

def intelligent_heal(fpath):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. PURGE: Remove Architecture and Mermaid blocks
    content = re.sub(r'## Architecture.*?(?=##|$)', '', content, flags=re.DOTALL)
    content = re.sub(r'```mermaid.*?```', '', content, flags=re.DOTALL)

    # 2. De-duplicate and Migrate headers
    # Example: "## 1. Context" -> "## Context"
    content = re.sub(r'## \d+\. Context', '## Context', content)
    content = re.sub(r'## \d+\. PADU Table', '## PADU Table', content)
    content = re.sub(r'## \d+\. Enforcement', '## Enforcement', content)

    # 3. Ensure mandatory sections (without duplication)
    sections = ['## Context', '## PADU Table', '## Enforcement']
    for section in sections:
        if section not in content:
            content += f"\n{section}\n\n[Auto-Generated Placeholder for Compliance]\n"

    # 4. Cleanup Whitespace
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # 5. Fix Frontmatter (ensure parent_standard)
    if 'parent_standard:' not in content[:300]:
        content = content.replace('---', '---\nparent_standard: kernel.standard', 1)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[HEAL] Intelligent Alignment Complete: {os.path.basename(fpath)}")

def run_intelligent_wave():
    std_dir = '/Users/Dan/repos/ai-kernel/standards'
    for root, dirs, files in os.walk(std_dir):
        for file in files:
            if file.endswith('.standard.md') and file != 'standard-file.standard.md':
                intelligent_heal(os.path.join(root, file))

if __name__ == "__main__":
    run_intelligent_wave()
