import os
import re

"""
Standard Compliance Healer (v1.1.0) - THE PURGE
---
Purpose: Surgically REMOVES Architecture sections from all standards.
Actions: Architectural Purge, PADU Matrix Expansion, Enforcement Injection.
"""

def purge_architecture(content):
    # Regex to find ## Architecture section and everything until the next ## header or end of file
    pattern = r'## Architecture.*?(?=##|$)'
    new_content = re.sub(pattern, '', content, flags=re.DOTALL)
    return new_content

def heal_standard(fpath):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. THE PURGE: Remove Architecture
    content = purge_architecture(content)

    # 2. Ensure remaining mandatory sections
    sections = ['## Context', '## PADU Table', '## Enforcement']
    for section in sections:
        if section not in content:
            content += f"\n{section}\n\n[Auto-Generated Placeholder for Compliance]\n"

    # 3. Cleanup double newlines from the purge
    content = re.sub(r'\n{3,}', '\n\n', content)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[PURGE] Architecture Removed: {os.path.basename(fpath)}")

def run_purge_wave():
    std_dir = '/Users/Dan/repos/ai-kernel/standards'
    for root, dirs, files in os.walk(std_dir):
        for file in files:
            if file.endswith('.standard.md') and file != 'standard-file.standard.md':
                heal_standard(os.path.join(root, file))

if __name__ == "__main__":
    run_purge_wave()
