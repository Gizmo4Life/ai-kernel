"""
---
id: impact_analyzer.driver
type: driver
tags: [kernel, automation, actuator]
parent_standard: driver-file.standard
summary: Atomic actuator for impact analyzer.
---
"""

import os
import re
import json
import sys

def find_dependents(target_id, repo_root):
    dependents = []
    
    # We look for the ID in various fields: glossary_refs, standards, parent_standard, etc.
    # And also in the body text if it's a glossary term.
    
    for root, _, files in os.walk(repo_root):
        for name in files:
            if name.endswith('.md') and name != 'README.md':
                fpath = os.path.join(root, name)
                with open(fpath, 'r') as f:
                    content = f.read()
                
                # Check frontmatter and body
                if target_id in content:
                    # Extract this file's ID
                    id_match = re.search(r'^id:\s*(.*)$', content, re.MULTILINE)
                    file_id = id_match.group(1).strip() if id_match else os.path.basename(fpath)
                    
                    if file_id != target_id:
                        dependents.append({
                            "id": file_id,
                            "path": os.path.relpath(fpath, repo_root),
                            "context": "Reference found"
                        })
    return dependents

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Missing target ID"}, indent=2))
    else:
        target = sys.argv[1]
        root = os.getcwd()
        deps = find_dependents(target, root)
        print(json.dumps({
            "target": target,
            "dependents": deps,
            "count": len(deps)
        }, indent=2))
