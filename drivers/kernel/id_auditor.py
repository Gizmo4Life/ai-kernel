import os
import re
import json
import sys

def get_id(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    match = re.search(r'^id:\s*(.*)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None

def main(target_dir):
    id_map = {} # id -> list of file paths
    
    for root, _, files in os.walk(target_dir):
        for name in files:
            if name.endswith('.md') and name != 'README.md':
                fpath = os.path.join(root, name)
                file_id = get_id(fpath)
                if file_id:
                    if file_id not in id_map:
                        id_map[file_id] = []
                    id_map[file_id].append(os.path.relpath(fpath, target_dir))
    
    collisions = {k: v for k, v in id_map.items() if len(v) > 1}
    print(json.dumps(collisions, indent=2))

if __name__ == "__main__":
    dir_to_scan = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    main(dir_to_scan)
