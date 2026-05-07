"""
---
id: repo_aggregator.driver
type: driver
tags: [kernel, audit, aggregation, manifest]
parent_standard: driver-file.standard
summary: Recursively aggregates node metadata (id, title, summary) into a machine-readable manifest.
---
"""
import os
import re
import json
import sys

def extract_field(content, field, is_py=False):
    if is_py:
        match = re.search(r'"""\s*---\s*(.*?)\s*---\s*"""', content, re.DOTALL)
    else:
        match = re.search(r'^---\s*(.*?)\s*---\s*', content, re.DOTALL)
    
    if match:
        fm_block = match.group(1)
        field_match = re.search(f'^{field}:\\s*(.*)', fm_block, re.MULTILINE)
        if field_match:
            return field_match.group(1).strip().strip('"').strip("'")
    return None

def aggregate_repo(root_dir):
    nodes = []
    for root, _, files in os.walk(root_dir):
        if '.git' in root or '__pycache__' in root: continue
        for name in files:
            if name.endswith('.md') or (name.endswith('.py') and 'drivers/' in root):
                fpath = os.path.join(root, name)
                try:
                    with open(fpath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    node_id = extract_field(content, 'id', name.endswith('.py'))
                    if node_id:
                        nodes.append({
                            "id": node_id,
                            "path": os.path.relpath(fpath, root_dir),
                            "title": extract_field(content, 'title', name.endswith('.py')) or name,
                            "summary": extract_field(content, 'summary', name.endswith('.py')) or "No summary."
                        })
                except: continue
    return nodes

if __name__ == "__main__":
    root = os.getcwd()
    manifest = aggregate_repo(root)
    print(json.dumps(manifest, indent=2))
