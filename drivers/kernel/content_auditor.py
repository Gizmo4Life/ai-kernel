import os
import re
import json
import sys

def audit_content(repo_root):
    results = []
    placeholders = ['TODO', 'FIXME', 'TBD', 'PLACEHOLDER', 'ADD CONTENT']
    
    for root, _, files in os.walk(repo_root):
        for name in files:
            if name.endswith('.md') and name != 'README.md':
                fpath = os.path.join(root, name)
                with open(fpath, 'r') as f:
                    content = f.read()
                
                # Resilient FM/Body splitting
                if content.startswith('---'):
                    parts = content.split('---')
                    body = parts[2] if len(parts) > 2 else ""
                else:
                    body = content
                
                file_results = {
                    "file": os.path.relpath(fpath, repo_root),
                    "issues": []
                }
                
                # 1. Placeholder Check
                # Special check for the auditor skill itself to ignore the literal list of placeholders
                if "audit-content-quality.skill" not in name:
                    for p in placeholders:
                        if p in body.upper():
                            file_results["issues"].append(f"Contains placeholder: {p}")
                
                # 2. Density Check
                word_count = len(body.split())
                if word_count < 10 and "context/" not in fpath:
                    file_results["issues"].append(f"Low knowledge density: {word_count} words")
                
                # 3. Header Check
                if '## Context' not in body and '## Execution Steps' not in body:
                    if not any(x in fpath for x in ['glossary', 'context', 'registry', 'README.md', 'AGENTS.md']):
                        file_results["issues"].append("Missing required architectural headers (Context/Execution Steps)")
                
                if file_results["issues"]:
                    results.append(file_results)
                    
    return results

if __name__ == "__main__":
    root = os.getcwd()
    audit_results = audit_content(root)
    print(json.dumps({
        "status": "success",
        "violations": audit_results,
        "count": len(audit_results)
    }, indent=2))
