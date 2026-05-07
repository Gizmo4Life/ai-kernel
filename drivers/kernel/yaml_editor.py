"""
---
id: yaml_editor.driver
type: driver
tags: [kernel, editor, yaml, automation]
parent_standard: driver-file.standard
summary: Deterministically updates a key in a YAML block using regex.
---
"""
import os
import re
import json
import sys

def update_yaml(fpath, key, value):
    try:
        if not os.path.exists(fpath):
            return {"status": "error", "message": f"File not found: {fpath}"}
            
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Determine if it's a python driver or markdown
        is_py = fpath.endswith('.py')
        
        if is_py:
            pattern = r'("""\s*---\s*)(.*?)(\s*---\s*""")'
            match = re.search(pattern, content, re.DOTALL)
        else:
            pattern = r'(^---\s*)(.*?)(\s*---\s*)'
            match = re.search(pattern, content, re.DOTALL)
            
        if not match:
            # If no frontmatter, try to find the key in the whole file (for plain YAML files)
            fm_block = content
        else:
            header, fm_block, footer = match.groups()
        
        # Update or add field
        # This handles simple key: value pairs
        field_pattern = f'^{key}:\\s*(.*)'
        if re.search(field_pattern, fm_block, re.MULTILINE):
            new_fm = re.sub(field_pattern, f'{key}: {value}', fm_block, flags=re.MULTILINE)
        else:
            new_fm = fm_block.strip() + f'\n{key}: {value}'
            
        if match:
            new_content = content.replace(fm_block, new_fm)
        else:
            new_content = new_fm
        
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        return {"status": "success", "file": fpath, "key": key, "value": value}
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(json.dumps({"status": "error", "message": "Usage: yaml_editor.py <path> <key> <value>"}))
        sys.exit(1)
        
    res = update_yaml(sys.argv[1], sys.argv[2], sys.argv[3])
    print(json.dumps(res, indent=2))
