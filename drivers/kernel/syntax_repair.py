import os
import re

"""
Universal Syntax Repair (v1.0.0)
---
Purpose: Fixes malformed frontmatter fences and literal newline strings.
Actions: Fence Closure, Newline Normalization, Spacing Enforcement.
"""

def repair_syntax(fpath):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix literal \n strings
    content = content.replace('\\n', '\n')

    # 2. Identify malformed frontmatter
    # If file starts with --- but doesn't have a second --- before the first # header
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) < 3:
            # Missing second fence. Find the first # header
            match = re.search(r'\n#+ ', content)
            if match:
                header_pos = match.start()
                content = content[:header_pos] + '\n---\n\n' + content[header_pos:].lstrip()
                print(f"[REPAIR] Closed Fence: {os.path.basename(fpath)}")
        else:
            # We have both fences, but ensure spacing
            fm = parts[1].strip()
            body = parts[2].lstrip()
            content = f"---\n{fm}\n---\n\n{body}"

    # 3. Final cleanup of excessive whitespace
    content = re.sub(r'\n{3,}', '\n\n', content)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

def run_repair_wave():
    for root, dirs, files in os.walk('/Users/Dan/repos/ai-kernel'):
        if '.git' in root or 'build' in root:
            continue
        for file in files:
            if file.endswith('.md'):
                repair_syntax(os.path.join(root, file))

if __name__ == "__main__":
    run_repair_wave()
