"""
---
id: json_editor.driver
type: driver
tags: [kernel, editor, json, automation]
parent_standard: driver-file.standard
summary: Deterministically reads or updates a key in a JSON file.
---
"""
import os
import json
import sys

def process_json(fpath, key=None, value=None, action="read"):
    try:
        if not os.path.exists(fpath):
            return {"status": "error", "message": f"File not found: {fpath}"}
            
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        if action == "read":
            if key:
                # Support nested keys via dot notation: "metadata.id"
                keys = key.split('.')
                val = data
                for k in keys:
                    val = val.get(k)
                    if val is None: break
                return {"status": "success", "data": val}
            return {"status": "success", "data": data}
            
        elif action == "update":
            if not key:
                return {"status": "error", "message": "Key required for update action"}
            
            # Support nested updates
            keys = key.split('.')
            target = data
            for k in keys[:-1]:
                if k not in target: target[k] = {}
                target = target[k]
            
            # Parse value as JSON if it looks like it (list/dict)
            try:
                if value.startswith('{') or value.startswith('['):
                    value = json.loads(value)
            except: pass
            
            target[keys[-1]] = value
            
            with open(fpath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
                
            return {"status": "success", "file": fpath, "key": key, "value": value}
            
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"status": "error", "message": "Usage: json_editor.py <path> [key] [value] [action]"}))
        sys.exit(1)
        
    path = sys.argv[1]
    key = sys.argv[2] if len(sys.argv) > 2 else None
    val = sys.argv[3] if len(sys.argv) > 3 else None
    act = sys.argv[4] if len(sys.argv) > 4 else ("update" if val else "read")
    
    res = process_json(path, key, val, act)
    print(json.dumps(res, indent=2))
