import os
import re

def heal_visual_glossary(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Ensure Context exists
    if "## Context" not in content:
        # Insert after frontmatter
        fm_match = re.search(r'^---\n.*?\n---', content, re.DOTALL)
        if fm_match:
            idx = fm_match.end()
            content = content[:idx] + "\n\n## Context\nCanonical definition of a core AI Kernel concept.\n" + content[idx:]

    # 2. Ensure Architecture exists
    if "## Architecture" not in content:
        mermaid = "\n## Architecture\n\n```mermaid\ngraph TD\n    Term[Concept Term] --> Definition[Semantic Definition]\n    Definition --> Constraints[Usage Constraints]\n```\n"
        # Insert after Context
        context_match = re.search(r'## Context', content)
        if context_match:
            # Find next header or end
            next_h = re.search(r'^## ', content[context_match.end():], re.MULTILINE)
            if next_h:
                idx = context_match.end() + next_h.start()
                content = content[:idx] + mermaid + content[idx:]
            else:
                content += mermaid

    # 3. Fix Usage Constraints (move to a ## header if they are just text)
    if "## Usage Constraints" not in content and "Usage Constraints" in content:
        content = content.replace("Usage Constraints", "## Usage Constraints")

    with open(filepath, 'w') as f:
        f.write(content)

# Scan glossary
base_path = os.path.join(os.getcwd(), 'glossary')
for root, _, files in os.walk(base_path):
    for name in files:
        if name.endswith('.md') and name != 'README.md':
            heal_visual_glossary(os.path.join(root, name))
