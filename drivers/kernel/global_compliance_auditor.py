"""
---
id: global_compliance_auditor.driver
type: driver
tags: [kernel, audit, compliance]
parent_standard: driver-file.standard
summary: Recursively audits the repository for frontmatter compliance across MD and PY files and updates the global gap report.
---
"""
import os
import json
import re

def extract_fm_field(content, field, is_py=False):
    if is_py:
        match = re.search(r'"""\s*---\s*(.*?)\s*---\s*"""', content, re.DOTALL)
        if not match:
            match = re.search(r"'''\s*---\s*(.*?)\s*---\s*'''", content, re.DOTALL)
    else:
        match = re.search(r'^---\s*(.*?)\s*---\s*', content, re.DOTALL)
    
    if match:
        fm_block = match.group(1)
        field_match = re.search(f'^{field}:\s*(.*)', fm_block, re.MULTILINE)
        if field_match:
            return field_match.group(1).strip().strip('"').strip("'")
    return None

def audit_repo(root_dir):
    results = {"total": 0, "compliant": 0, "fails": []}
    for root, _, files in os.walk(root_dir):
        if '.git' in root or '__pycache__' in root: continue
        for name in files:
            if name.endswith('.md') or (name.endswith('.py') and 'drivers/' in root):
                fpath = os.path.join(root, name)
                try:
                    with open(fpath, 'r', encoding='utf-8') as f:
                        content = f.read()
                except: continue
                results["total"] += 1
                if extract_fm_field(content, 'id', name.endswith('.py')):
                    results["compliant"] += 1
                else:
                    results["fails"].append(os.path.relpath(fpath, root_dir))
    return results

if __name__ == "__main__":
    root = os.getcwd()
    report = audit_repo(root)
    
    # Write to Global Gap Report
    with open('context/global-gap-report.md', 'w') as f:
        f.write("# Global Compliance Gap Report (v8.1.13)\n\n")
        f.write(f"- Total Files Audited: {report['total']}\n")
        f.write(f"- Fully Compliant Files: {report['compliant']}\n")
        f.write(f"- Non-Compliant Files: {len(report['fails'])}\n")
        f.write(f"- Logic Density: {(report['compliant']/report['total'])*100:.1f}%\n\n")
        f.write("## Failure Details\n")
        for fail in report["fails"]:
            f.write(f"- {fail}\n")
            
    print(json.dumps(report, indent=2))
