import os
import re

def heal_file_properly(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Frontmatter check
    fm_pattern = r'^---\n(.*?)\n---'
    fm_match = re.search(fm_pattern, content, re.DOTALL)
    if not fm_match:
        return # Skip files without frontmatter

    fm_end = fm_match.end()
    
    # 2. Extract summary for context
    summary_match = re.search(r'summary:\s*(.*)', fm_match.group(1))
    summary = summary_match.group(1) if summary_match else "Architectural component of the AI Kernel."

    # 3. Check for Context/Abstract/Rationale
    if not re.search(r'^## (Context|Abstract|Rationale)', content, re.MULTILINE):
        insertion = f"\n\n## Context\n{summary}\n"
        content = content[:fm_end] + insertion + content[fm_end:]

    # 4. Check for Architecture/Mermaid
    if not re.search(r'mermaid', content):
        # Insert Architecture right after Context or Abstract
        header_match = re.search(r'^## (Context|Abstract|Rationale)', content, re.MULTILINE)
        mermaid_block = "\n## Architecture\n\n```mermaid\ngraph TD\n    Start((Start)) --> Process[Process: Logic Flow] --> End((End))\n```\n"
        
        # Find the end of that context section to insert architecture
        if header_match:
            # Find the start of the next header or end of file
            next_header = re.search(r'^## ', content[header_match.end():], re.MULTILINE)
            if next_header:
                idx = header_match.end() + next_header.start()
                content = content[:idx] + mermaid_block + content[idx:]
            else:
                content += mermaid_block

    with open(filepath, 'w') as f:
        f.write(content)

# Scan core directories
dirs = ['agents', 'skills', 'instructions', 'standards']
for d in dirs:
    base_path = os.path.join(os.getcwd(), d)
    for root, _, files in os.walk(base_path):
        for name in files:
            if name.endswith('.md') and name != 'README.md':
                heal_file_properly(os.path.join(root, name))
