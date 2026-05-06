import os
import re

def harden_standard(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Only harden if requirements field is missing
    if "requirements:" in content: return

    # Inject requirements after summary
    # requirements: [parent_standard, "## PADU Table", "## Enforcement", "## Context"]
    content = re.sub(r'(summary:.*?\n)', r'\1requirements: [parent_standard, "## PADU Table", "## Enforcement", "## Context", "## Architecture"]\n', content)

    with open(filepath, 'w') as f:
        f.write(content)

if __name__ == "__main__":
    standards_dir = os.path.join(os.getcwd(), 'standards')
    for root, _, files in os.walk(standards_dir):
        for name in files:
            if name.endswith('.md') and name != 'README.md':
                harden_standard(os.path.join(root, name))
