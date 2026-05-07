"""
---
id: fm_updater.driver
type: driver
tags: [kernel, editor, frontmatter, automation]
parent_standard: driver-file.standard
summary: Deterministically updates a specific YAML frontmatter field in a node.
---
"""
import os
import re
import sys
import json

def update_fm(target_path, field, value):
    try:
        with open(target_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Determine if it's a python driver or markdown
        is_py = target_path.endswith('.py')
        
        if is_py:
            pattern = r'("""\s*---\s*)(.*?)(\s*---\s*""")'
            match = re.search(pattern, content, re.DOTALL)
        else:
            pattern = r'(^---\s*)(.*?)(\s*---\s*)'
            match = re.search(pattern, content, re.DOTALL)
            
        if not match:
            return {"status": "error", "message": "No frontmatter found"}
            
        header, fm_block, footer = match.groups()
        
        # Update or add field
        field_pattern = f'^{field}:\\s*(.*)'
        if re.search(field_pattern, fm_block, re.MULTILINE):
            new_fm = re.sub(field_pattern, f'{field}: {value}', fm_block, flags=re.MULTILINE)
        else:
            new_fm = fm_block.strip() + f'\n{field}: {value}'
            
        new_content = content.replace(fm_block, new_fm)
        
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        return {"status": "success", "file": target_path, "field": field, "value": value}
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(json.dumps({"status": "error", "message": "Usage: fm_updater.py <path> <field> <value>"}))
        sys.exit(1)
        
    res = update_fm(sys.argv[1], sys.argv[2], sys.argv[3])
    print(json.dumps(res))
