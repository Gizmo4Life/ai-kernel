import os
import re

def repair_fm(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    parts = re.split(r'^---$', content, flags=re.MULTILINE)
    if len(parts) < 3: return
    
    fm = parts[1]
    body = parts[2]
    
    # 1. Fix the "concatenation" issue
    # Matches things like "standard.mdglossary_refs"
    fm = re.sub(r'(\.standard|\.md|\.instruction|\.skill|\.prompt)(glossary_refs|tags|summary|skills|parent_standard)', r'\1\n\2', fm)
    
    # 2. Ensure each core field is on a new line
    fields = ['id', 'title', 'type', 'tags', 'summary', 'parent_standard', 'glossary_refs', 'skills', 'instructions', 'prompts']
    for field in fields:
        fm = re.sub(rf'({field}:)', r'\n\1', fm)
    
    # Cleanup double newlines
    fm = re.sub(r'\n+', '\n', fm).strip()
    
    new_content = f"---\n{fm}\n---{body}"
    with open(filepath, 'w') as f:
        f.write(new_content)

if __name__ == "__main__":
    for root, _, files in os.walk(os.getcwd()):
        for name in files:
            if name.endswith('.md') and name != 'README.md' and (root.endswith(('skills', 'instructions', 'prompts', 'standards'))):
                repair_fm(os.path.join(root, name))
