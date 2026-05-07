"""
---
id: nit_pick_auditor.driver
type: driver
tags: [kernel, automation, actuator]
parent_standard: driver-file.standard
summary: Atomic actuator for nit pick auditor.
---
"""

import os
import re
import json
import sys

def audit_nit_picks(repo_root):
    results = []
    
    for root, _, files in os.walk(repo_root):
        for name in files:
            if name.endswith('.md') and name != 'README.md':
                fpath = os.path.join(root, name)
                with open(fpath, 'r') as f:
                    lines = f.readlines()
                    content = "".join(lines)
                
                file_results = {
                    "file": os.path.relpath(fpath, repo_root),
                    "issues": []
                }
                
                # 1. Trailing Whitespace
                for i, line in enumerate(lines):
                    if line.endswith(' \n') or line.endswith('\t\n'):
                        file_results["issues"].append(f"L{i+1}: Trailing whitespace")
                
                # 2. EOF Newline
                if lines and not lines[-1].endswith('\n'):
                    file_results["issues"].append("Missing newline at EOF")
                
                # 3. Tag Casing Drift
                tag_match = re.search(r'tags: \[(.*)\]', content)
                if tag_match:
                    tags = [t.strip() for t in tag_match.group(1).split(',')]
                    for t in tags:
                        if t != t.lower() and t not in ['AI', 'Kernel', 'DAG', 'OTel', 'MCP']:
                            file_results["issues"].append(f"Inconsistent tag casing: '{t}' (Expected lowercase or proper noun)")

                # 4. Relative Link Validation
                links = re.findall(r'\[.*?\]\((.*?\.md)\)', content)
                for link in links:
                    if link.startswith('http'): continue
                    # Resolve relative path
                    link_path = os.path.normpath(os.path.join(os.path.dirname(fpath), link))
                    if not os.path.exists(link_path):
                        file_results["issues"].append(f"Broken relative link: {link}")

                if file_results["issues"]:
                    results.append(file_results)
                    
    return results

if __name__ == "__main__":
    root = os.getcwd()
    picks = audit_nit_picks(root)
    print(json.dumps({
        "status": "success",
        "violations": picks,
        "count": len(picks)
    }, indent=2))
