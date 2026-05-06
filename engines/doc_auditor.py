import os
import re
import json
import sys

def audit_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    violations = []
    
    # Check for mandatory headers
    if "## Context" not in content: violations.append("missing_context")
    if "## Architecture" not in content: violations.append("missing_architecture")
    
    # Tier-specific checks
    if ".agent.md" in filepath and "## Quality Gate" not in content:
        violations.append("missing_quality_gate")
    elif ".skill.md" in filepath and "## Verification Protocol" not in content:
        violations.append("missing_verification_protocol")
    elif ".instruction.md" in filepath and "## Postconditions" not in content:
        violations.append("missing_postconditions")
    elif ".glossary.md" in filepath and "## Usage Constraints" not in content:
        violations.append("missing_usage_constraints")
    
    return violations

def main(target_dir):
    results = {}
    for root, dirs, files in os.walk(target_dir):
        # SKIP context and .github
        if 'context' in dirs:
            dirs.remove('context')
        if '.github' in dirs:
            dirs.remove('.github')
            
        for name in files:
            if name.endswith('.md') and name != 'README.md':
                fpath = os.path.join(root, name)
                v = audit_file(fpath)
                if v:
                    results[os.path.relpath(fpath, target_dir)] = v
    
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    dir_to_audit = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    main(dir_to_audit)
