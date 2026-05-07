"""
---
id: git_diff_audit.driver
type: driver
tags: [kernel, automation, actuator]
parent_standard: driver-file.standard
summary: Atomic actuator for git diff audit.
---
"""

import subprocess
import json
import sys

def main(pr_branch, base_branch="main"):
    try:
        # Get the diff summary
        result = subprocess.run(["git", "diff", f"{base_branch}...{pr_branch}", "--name-status"], capture_output=True, text=True)
        
        if result.returncode == 0:
            files = [line.strip() for line in result.stdout.split('\n') if line.strip()]
            print(json.dumps({
                "status": "success",
                "base": base_branch,
                "head": pr_branch,
                "changed_files": files,
                "count": len(files)
            }, indent=2))
        else:
            print(json.dumps({
                "status": "fail",
                "message": result.stderr
            }, indent=2))
            
    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}, indent=2))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"status": "error", "message": "Missing PR branch name"}, indent=2))
    else:
        pr_branch = sys.argv[1]
        base = sys.argv[2] if len(sys.argv) > 2 else "main"
        main(pr_branch, base)
