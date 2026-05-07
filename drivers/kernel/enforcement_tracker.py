"""
---
id: enforcement_tracker.driver
type: driver
tags: [kernel, automation, actuator]
parent_standard: driver-file.standard
summary: Atomic actuator for enforcement tracker.
---
"""

import os
import re
import json
import sys

def get_maturity_score(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Extract PADU table
    # Matches everything between the table headers and the end of the table
    table_match = re.search(r'\| Practice \| Rating \|.*?\|.*?\|(.*?)\n\n', content, re.DOTALL)
    if not table_match: return None
    
    rows = table_match.group(1).strip().split('\n')
    total_rules = len(rows)
    automated_rules = 0
    
    for row in rows:
        cols = [c.strip() for c in row.split('|') if c.strip()]
        if len(cols) >= 4:
            enforcement = cols[3]
            # Rule is "Automated" if Enforcement points to a .skill or .py script
            if '.skill' in enforcement or '.py' in enforcement:
                automated_rules += 1
                
    return {
        "total": total_rules,
        "automated": automated_rules,
        "maturity": (automated_rules / total_rules) if total_rules > 0 else 0
    }

def main(standards_dir):
    report = {}
    for root, _, files in os.walk(standards_dir):
        for name in files:
            if name.endswith('.md') and name != 'README.md':
                fpath = os.path.join(root, name)
                score = get_maturity_score(fpath)
                if score:
                    report[os.path.basename(fpath)] = score
                    
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    standards_dir = os.path.join(os.getcwd(), 'standards')
    main(standards_dir)
