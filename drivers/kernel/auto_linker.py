import os
import re
import sys

def get_glossary_ids(glossary_dir):
    ids = []
    for root, _, files in os.walk(glossary_dir):
        for name in files:
            if name.endswith('.md') and name != 'README.md':
                # Extract ID from filename (assuming id matches filename)
                term_id = name.replace('.glossary.md', '.glossary')
                ids.append(term_id)
    return ids

def auto_link_file(filepath, glossary_ids):
    with open(filepath, 'r') as f:
        content = f.read()

    # Split frontmatter
    parts = re.split(r'^---$', content, flags=re.MULTILINE)
    if len(parts) < 3: return
    
    fm = parts[1]
    body = parts[2]
    
    # Find mentions of glossary terms in the body (whole words only)
    found_refs = []
    for term_id in glossary_ids:
        # Strip the .glossary suffix for searching in text
        base_term = term_id.replace('.glossary', '')
        if re.search(rf'\b{re.escape(base_term)}\b', body, re.IGNORECASE):
            found_refs.append(term_id)
            
    if not found_refs: return

    # Update glossary_refs in frontmatter
    refs_match = re.search(r'glossary_refs:\s*\[(.*?)\]', fm)
    if refs_match:
        current_refs = [r.strip() for r in refs_match.group(1).split(',') if r.strip()]
        for ref in found_refs:
            if ref not in current_refs:
                current_refs.append(ref)
        
        new_refs_str = f"glossary_refs: [{', '.join(sorted(current_refs))}]"
        new_fm = fm[:refs_match.start(0)] + new_refs_str + fm[refs_match.end(0):]
    else:
        # Add glossary_refs field if missing
        new_fm = fm.strip() + f"\nglossary_refs: [{', '.join(sorted(found_refs))}]\n"

    new_content = f"---\n{new_fm.strip()}\n---{body}"
    
    with open(filepath, 'w') as f:
        f.write(new_content)

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    glossary_path = os.path.join(os.getcwd(), 'glossary')
    g_ids = get_glossary_ids(glossary_path)
    
    if os.path.isfile(target):
        auto_link_file(target, g_ids)
    else:
        for root, _, files in os.walk(target):
            for name in files:
                if name.endswith('.md') and name != 'README.md' and 'glossary' not in root:
                    auto_link_file(os.path.join(root, name), g_ids)
