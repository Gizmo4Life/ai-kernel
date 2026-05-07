"""
---
id: connectivity_auditor.driver
type: driver
tags: [kernel, automation, actuator]
parent_standard: driver-file.standard
summary: Atomic actuator for connectivity auditor.
---
"""

import os
import re
import json
import sys

def get_frontmatter_refs(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Extract ID
    id_match = re.search(r'^id:\s*(.*)$', content, re.MULTILINE)
    file_id = id_match.group(1).strip() if id_match else None
    
    # Extract Parent and Refs
    refs = []
    
    # Matches patterns like parent_standard: id OR glossary_refs: [id1, id2]
    patterns = [
        r'parent_standard:\s*([\w\-\.]+)',
        r'parent_standards:\s*\[(.*?)\]',
        r'glossary_refs:\s*\[(.*?)\]',
        r'instructions:\s*\[(.*?)\]',
        r'skills:\s*\[(.*?)\]'
    ]
    
    for p in patterns:
        matches = re.finditer(p, content, re.MULTILINE)
        for m in matches:
            val = m.group(1)
            if '[' in p: # Handle lists
                items = [i.strip() for i in val.split(',') if i.strip()]
                refs.extend(items)
            else:
                refs.append(val.strip())
                
    return file_id, refs

def main(target_dir):
    graph = {} # id -> list of out-refs
    
    for root, _, files in os.walk(target_dir):
        for name in files:
            if name.endswith('.md') and name != 'README.md':
                fpath = os.path.join(root, name)
                file_id, refs = get_frontmatter_refs(fpath)
                if file_id:
                    graph[file_id] = refs
    
    # Identify Orphans (Nodes with no incoming references)
    # Note: This is a simplified reachability check
    all_referenced = set()
    for refs in graph.values():
        all_referenced.update(refs)
        
    orphans = [node for node in graph.keys() if node not in all_referenced and node != "kernel.standard"]
    
    print(json.dumps({"orphans": orphans}, indent=2))

if __name__ == "__main__":
    dir_to_scan = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    main(dir_to_scan)
