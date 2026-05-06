import os
import re
import sys

def get_frontmatter(filepath):
    try:
        with open(filepath, 'r') as f:
            content = f.read()
    except: return None, None, None
    
    parts = re.split(r'^---$', content, flags=re.MULTILINE)
    if len(parts) < 3: return None, None, None
    
    fm_raw = parts[1]
    body = parts[2]
    
    data = {}
    id_match = re.search(r'^id:\s*(.*)$', fm_raw, re.MULTILINE)
    if not id_match: return None, None, None
    
    data['id'] = id_match.group(1).strip()
    
    parent_match = re.search(r'parent_standard:\s*([\w\-\.]+)', fm_raw)
    data['parent'] = parent_match.group(1).strip() if parent_match else None
    
    skills_match = re.search(r'skills:\s*\[(.*?)\]', fm_raw)
    data['skills'] = [s.strip() for s in skills_match.group(1).split(',') if s.strip()] if skills_match else []
    
    return data, body, fm_raw

def generate_mermaid(data):
    node_id = data['id']
    parent = data['parent']
    skills = data['skills']
    
    mermaid = "## Architecture\n\n```mermaid\ngraph TD\n"
    if parent:
        mermaid += f"    {parent} --> {node_id}\n"
    
    for s in skills:
        s_label = s.replace('.skill', '')
        mermaid += f"    {node_id} --> {s_label}[{s}]\n"
        
    mermaid += "```\n"
    return mermaid

def update_file(filepath):
    data, body, fm_raw = get_frontmatter(filepath)
    if not data: return
    
    new_mermaid = generate_mermaid(data)
    
    if "## Architecture" in body:
        new_body = re.sub(r'## Architecture\n\n```mermaid.*?```', new_mermaid.strip(), body, flags=re.DOTALL)
    else:
        new_body = body.strip() + "\n\n" + new_mermaid
        
    new_content = f"---\n{fm_raw.strip()}\n---{new_body}"
    
    with open(filepath, 'w') as f:
        f.write(new_content)

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    if os.path.isfile(target):
        update_file(target)
    else:
        for root, _, files in os.walk(target):
            for name in files:
                if name.endswith('.md') and name != 'README.md':
                    update_file(os.path.join(root, name))
