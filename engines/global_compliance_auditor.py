import os
import re
import subprocess
import json

def get_fm_field(filepath, field):
    try:
        with open(filepath, 'r') as f:
            content = f.read()
    except: return None
    
    match = re.search(rf'^{field}:\s*(.*)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None

def main():
    gap_report = {
        "summary": {"total_files": 0, "compliant_files": 0, "failed_files": 0, "total_debt": 0, "error_files": 0},
        "details": [],
        "errors": []
    }
    
    domains = ['agents', 'skills', 'instructions', 'standards', 'prompts', 'glossary']
    
    for d in domains:
        path = os.path.join(os.getcwd(), d)
        if not os.path.exists(path): continue
        for root, _, files in os.walk(path):
            for name in files:
                if name.endswith('.md') and name != 'README.md':
                    fpath = os.path.join(root, name)
                    gap_report["summary"]["total_files"] += 1
                    
                    parent = get_fm_field(fpath, 'parent_standard')
                    if not parent:
                        if d == 'skills': parent = 'skill-file.standard'
                        elif d == 'instructions': parent = 'instruction-file.standard'
                        elif d == 'standards': parent = 'standard-file.standard'
                        elif d == 'prompts': parent = 'prompt-file.standard'
                        elif d == 'agents': parent = 'agent-file.standard'
                        elif d == 'glossary': parent = 'glossary-entry.standard'

                    cmd = ["python3", "engines/standard_auditor.py", parent, fpath]
                    result = subprocess.run(cmd, capture_output=True, text=True)
                    try:
                        audit_data = json.loads(result.stdout)
                        if "error" in audit_data and "kernel.standard" not in fpath:
                            gap_report["summary"]["error_files"] += 1
                            gap_report["errors"].append({"file": fpath, "error": audit_data["error"]})
                        else:
                            score = float(audit_data['score'].replace('%',''))
                            if score < 100:
                                gap_report["summary"]["failed_files"] += 1
                                gap_report["details"].append(audit_data)
                                for status in audit_data['details'].values():
                                    if status == "FAIL": gap_report["summary"]["total_debt"] += 1
                            else:
                                gap_report["summary"]["compliant_files"] += 1
                    except Exception as e:
                        gap_report["summary"]["error_files"] += 1
                        gap_report["errors"].append({"file": fpath, "error": str(e), "output": result.stdout})

    with open('context/global-gap-report.md', 'w') as f:
        f.write("# Global Compliance Gap Report (v4.6.0)\n\n")
        f.write(f"## Summary\n")
        f.write(f"- Total Files Audited: {gap_report['summary']['total_files']}\n")
        f.write(f"- Fully Compliant Files: {gap_report['summary']['compliant_files']}\n")
        f.write(f"- Non-Compliant Files: {gap_report['summary']['failed_files']}\n")
        f.write(f"- Errored Files: {gap_report['summary']['error_files']}\n")
        f.write(f"- Total Logic Debt (Fails): {gap_report['summary']['total_debt']}\n\n")
        f.write(f"## Error Details\n\n")
        for err in gap_report["errors"]:
            f.write(f"- **File**: {err['file']}\n")
            f.write(f"  - **Error**: {err['error']}\n")
        f.write(f"\n## Failure Details\n\n")
        for detail in gap_report["details"]:
            f.write(f"### {detail['target']}\n")
            f.write(f"- **Standard**: {detail['standard']}\n")
            f.write(f"- **Score**: {detail['score']}\n")
            f.write("- **Fails**:\n")
            for req, status in detail['details'].items():
                if status == "FAIL": f.write(f"  - {req}\n")
            f.write("\n")

if __name__ == "__main__":
    main()
