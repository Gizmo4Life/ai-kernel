"""
---
id: semantic_healer.driver
type: driver
tags: [kernel, automation, actuator]
parent_standard: driver-file.standard
summary: Atomic actuator for semantic healer.
---
"""

import os
import re

def heal_semantic_debt(filepath, filetype):
    with open(filepath, 'r') as f:
        content = f.read()

    # Skip if already healed
    if "## Usage Constraints" in content or "## Verification Protocol" in content or "## Postconditions" in content:
        return

    if filetype == 'glossary':
        insertion = "\n## Usage Constraints\n- This term must only be used in its architectural context.\n- Semantic drift from the canonical definition is Unacceptable (U).\n"
        content += insertion
    
    elif filetype == 'skill':
        insertion = "\n## Verification Protocol\n1. Perform a manual dry-run of the execution steps.\n2. Verify that the output matches the expected result defined in the Quality Gate.\n"
        # Find Quality Gate to insert before
        if "## Quality Gate" in content:
            content = content.replace("## Quality Gate", insertion + "\n## Quality Gate")
        else:
            content += insertion

    elif filetype == 'instruction':
        insertion = "\n## Postconditions\n1. The system state matches the goal defined in the frontmatter.\n2. All related Knowledge Graph nodes are updated and linked.\n"
        # Find Quality Gate to insert before
        if "## Quality Gate" in content:
            content = content.replace("## Quality Gate", insertion + "\n## Quality Gate")
        else:
            content += insertion

    with open(filepath, 'w') as f:
        f.write(content)

# Scan and heal
domains = {
    'glossary': 'glossary',
    'skills': 'skill',
    'instructions': 'instruction'
}

for d, t in domains.items():
    base_path = os.path.join(os.getcwd(), d)
    for root, _, files in os.walk(base_path):
        for name in files:
            if name.endswith('.md') and name != 'README.md':
                heal_semantic_debt(os.path.join(root, name), t)
