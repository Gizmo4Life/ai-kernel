import os
import re

def fix_hierarchy(filepath, category):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Map category to direct parent
    parent_map = {
        "agents": "agent-file.standard",
        "skills": "skill-file.standard",
        "instructions": "instruction-file.standard",
        "prompts": "prompt-file.standard",
        "glossary": "glossary-entry.standard"
    }
    
    new_parent = parent_map.get(category)
    if not new_parent: return

    # Update parent_standard
    content = re.sub(r'parent_standard:\s*[\w\-\.]+', f'parent_standard: {new_parent}', content)
    
    # If missing, inject after type
    if "parent_standard:" not in content:
        content = re.sub(r'(type:.*?\n)', r'\1parent_standard: ' + new_parent + '\n', content)

    with open(filepath, 'w') as f:
        f.write(content)

def harden_tier_standards():
    # Agent Standard
    with open('standards/agent-file.standard.md', 'r') as f:
        content = f.read()
    content = re.sub(r'requirements: \[.*?\]', 'requirements: [authority, scope, capabilities, "## Quality Gate"]', content)
    with open('standards/agent-file.standard.md', 'w') as f: f.write(content)

    # Prompt Standard
    with open('standards/prompt-file.standard.md', 'r') as f:
        content = f.read()
    content = re.sub(r'requirements: \[.*?\]', 'requirements: ["## Context", "## Architecture"]', content)
    with open('standards/prompt-file.standard.md', 'w') as f: f.write(content)

if __name__ == "__main__":
    harden_tier_standards()
    for d in ['agents', 'skills', 'instructions', 'prompts', 'glossary']:
        path = os.path.join(os.getcwd(), d)
        if not os.path.exists(path): continue
        for root, _, files in os.walk(path):
            for name in files:
                if name.endswith('.md') and name != 'README.md':
                    fix_hierarchy(os.path.join(root, name), d)
