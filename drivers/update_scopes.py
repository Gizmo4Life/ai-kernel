import os
import re

# Mapping of file id to new glob scope
scope_map = {
    'kernel.standard': '/**/*',
    'standard-file.standard': '/standards/**/*.standard.md',
    'agent-file.standard': '/agents/**/*.agent.md',
    'skill-file.standard': '/skills/**/*.skill.md',
    'instruction-file.standard': '/instructions/**/*.instruction.md',
    'glossary-entry.standard': '/glossary/**/*.glossary.md',
    'prompt-file.standard': '/prompts/**/*.prompt.md',
    'doc-local.standard': '/**/README.md',
    'doc-architecture.standard': '/docs/architecture/**/*.md',
    'doc-developer.standard': '/**/* [tag:developer]',
    'doc-external.standard': '/**/* [tag:external]',
    'tel-naming.standard': '/**/*',
    'mon-alerting.standard': '/**/*',
    'operability.standard': '/**/*',
    'inc-response.standard': '/**/*'
}

def update_scope(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Extract ID from frontmatter
    id_match = re.search(r'id:\s*(.*)', content)
    if not id_match:
        return

    standard_id = id_match.group(1).strip()
    if standard_id in scope_map:
        new_scope = scope_map[standard_id]
        # Replace scope: line
        content = re.sub(r'scope:\s*.*', f'scope: "{new_scope}"', content)
        
        with open(filepath, 'w') as f:
            f.write(content)

# Scan standards directory
base_path = os.path.join(os.getcwd(), 'standards')
for root, _, files in os.walk(base_path):
    for name in files:
        if name.endswith('.standard.md'):
            update_scope(os.path.join(root, name))
