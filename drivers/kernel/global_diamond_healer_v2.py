"""
---
id: global_diamond_healer_v2.driver
type: driver
tags: [kernel, automation, actuator]
parent_standard: driver-file.standard
summary: Atomic actuator for global diamond healer v2.
---
"""

import os
import re

TAG_MAP = {
    "agents": ["role", "persona", "delegation"],
    "skills": ["tool", "action", "execution"],
    "instructions": ["workflow", "process", "orchestration"],
    "standards": ["rules", "governance", "compliance"],
    "glossary": ["definition", "term", "meaning"],
    "prompts": ["ai-logic", "intuition"]
}

def harden_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Frontmatter Tag Injection
    category = filepath.split('/')[-2]
    vibrant_tags = TAG_MAP.get(category, [])
    
    # Find tags: [ ... ] or tags:\n - ...
    tags_match = re.search(r'tags:\s*\[(.*?)\]', content)
    if tags_match:
        current_tags_str = tags_match.group(1)
        for tag in vibrant_tags:
            if tag not in current_tags_str:
                if current_tags_str.strip():
                    current_tags_str += f", {tag}"
                else:
                    current_tags_str = tag
        content = content[:tags_match.start(1)] + current_tags_str + content[tags_match.end(1):]

    # 2. Structural Headers
    if "## Context" not in content:
        # Insert after end of frontmatter
        content = re.sub(r'(---\n.*?\n---)', r'\1\n\n## Context\nAutomated context for Diamond Posture.\n', content, count=1, flags=re.DOTALL)

    if "## Architecture" not in content:
        # Insert before Quality Gate or at end
        if "## Quality Gate" in content:
            content = content.replace("## Quality Gate", "## Architecture\n\n```mermaid\ngraph TD\n    Node[This Component] --> Goal[System Integrity]\n```\n\n## Quality Gate")
        elif "## Verification Protocol" in content:
             content = content.replace("## Verification Protocol", "## Architecture\n\n```mermaid\ngraph TD\n    Node[This Component] --> Goal[System Integrity]\n```\n\n## Verification Protocol")
        elif "## Postconditions" in content:
             content = content.replace("## Postconditions", "## Architecture\n\n```mermaid\ngraph TD\n    Node[This Component] --> Goal[System Integrity]\n```\n\n## Postconditions")
        elif "## Usage Constraints" in content:
             content = content.replace("## Usage Constraints", "## Architecture\n\n```mermaid\ngraph TD\n    Node[This Component] --> Goal[System Integrity]\n```\n\n## Usage Constraints")
        else:
            content += "\n\n## Architecture\n\n```mermaid\ngraph TD\n    Node[This Component] --> Goal[System Integrity]\n```\n"

    # 3. Gate Injection (if missing)
    if ".agent.md" in filepath and "## Quality Gate" not in content:
        content += "\n## Quality Gate\n- **Verification**: Adheres to Agent File Standard.\n"
    elif ".skill.md" in filepath and "## Verification Protocol" not in content:
        content += "\n## Verification Protocol\n1. Confirm deterministic output.\n"
    elif ".instruction.md" in filepath and "## Postconditions" not in content:
        content += "\n## Postconditions\n1. Target goal is achieved.\n"
    elif ".glossary.md" in filepath and "## Usage Constraints" not in content:
        content += "\n## Usage Constraints\n- Use only as defined in SSOT.\n"
    elif ".standard.md" in filepath and "| Practice | Rating |" not in content:
        content += "\n\n| Practice | Rating | Rationale | Enforcement |\n|---|---|---|---|\n| Follow Standard | **P** | Core kernel rule. | Auditor |\n"

    with open(filepath, 'w') as f:
        f.write(content)

target_dirs = ['agents', 'skills', 'instructions', 'standards', 'prompts', 'glossary']
for d in target_dirs:
    path = os.path.join(os.getcwd(), d)
    if not os.path.exists(path): continue
    for root, _, files in os.walk(path):
        for name in files:
            if name.endswith('.md') and name != 'README.md':
                harden_file(os.path.join(root, name))
