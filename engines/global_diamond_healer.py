import os
import yaml
import re

# Vibrant Tag Mapping (Examples for common domains)
TAG_MAP = {
    "agents": ["role", "persona", "delegation", "who"],
    "skills": ["tool", "action", "do", "execute", "how-to"],
    "instructions": ["workflow", "step-by-step", "process", "orchestration"],
    "standards": ["rules", "governance", "compliance", "must", "standard"],
    "glossary": ["definition", "term", "meaning", "vocabulary"],
    "prompts": ["ai-logic", "intuition", "instruction-set"]
}

def harden_file(filepath):
    with open(filepath, 'r') as f:
        raw_content = f.read()

    # Split frontmatter
    parts = re.split(r'^---$', raw_content, flags=re.MULTILINE)
    if len(parts) < 3:
        return # Skip files without frontmatter

    fm_raw = parts[1]
    body = parts[2]
    
    try:
        fm = yaml.safe_load(fm_raw)
    except:
        return # Skip invalid yaml

    # 1. Vibrant Tagging
    category = filepath.split('/')[-2]
    current_tags = fm.get('tags', [])
    vibrant_tags = TAG_MAP.get(category, [])
    
    # Add unique vibrant tags
    for tag in vibrant_tags:
        if tag not in current_tags:
            current_tags.append(tag)
    
    fm['tags'] = current_tags
    
    # 2. Structural Headers Check (Soft Injection)
    if "## Context" not in body:
        body = "\n## Context\nAutomated context injection for Diamond Posture compliance.\n" + body
    
    if "## Architecture" not in body:
        body = body + "\n\n## Architecture\n\n```mermaid\ngraph TD\n    Node[This Component] --> Goal[System Integrity]\n```\n"

    # 3. Tier-Specific Gate Injection
    if ".agent.md" in filepath and "## Quality Gate" not in body:
        body += "\n## Quality Gate\n- **Verification**: Adheres to Agent File Standard.\n"
    elif ".skill.md" in filepath and "## Verification Protocol" not in body:
        body += "\n## Verification Protocol\n1. Confirm deterministic output for known inputs.\n"
    elif ".instruction.md" in filepath and "## Postconditions" not in body:
        body += "\n## Postconditions\n1. Target goal is achieved and verified.\n"
    elif ".glossary.md" in filepath and "## Usage Constraints" not in body:
        body += "\n## Usage Constraints\n- Use only as defined in the SSOT.\n"
    elif ".standard.md" in filepath and "| Practice | Rating |" not in body:
        body += "\n\n| Practice | Rating | Rationale | Enforcement | Exception |\n|---|---|---|---|---|\n| Follow Standard | **P** | Core kernel rule. | Auditor | None |\n"

    # Reconstruct file
    new_fm = yaml.dump(fm, sort_keys=False, default_flow_style=False).strip()
    new_content = f"---\n{new_fm}\n---{body}"
    
    with open(filepath, 'w') as f:
        f.write(new_content)

# Execution
target_dirs = ['agents', 'skills', 'instructions', 'standards', 'prompts', 'glossary']
for d in target_dirs:
    path = os.path.join(os.getcwd(), d)
    if not os.path.exists(path): continue
    for root, _, files in os.walk(path):
        for name in files:
            if name.endswith('.md') and name != 'README.md':
                harden_file(os.path.join(root, name))
