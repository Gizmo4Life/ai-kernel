import os
import re

def inject_fm(fpath):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has FM
    if '---' in content[:200]:
        return False
        
    fname = os.path.basename(fpath)
    driver_id = fname.replace('.py', '.driver')
    
    # Template for Driver Frontmatter
    fm_template = f'''"""
---
id: {driver_id}
type: driver
tags: [kernel, automation, actuator]
parent_standard: driver-file.standard
summary: Atomic actuator for {fname.replace('_', ' ').replace('.py', '')}.
---
"""
'''
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(fm_template + "\n" + content)
    return True

def process_drivers(drivers_root):
    count = 0
    for root, _, files in os.walk(drivers_root):
        for name in files:
            if name.endswith('.py'):
                fpath = os.path.join(root, name)
                if inject_fm(fpath):
                    count += 1
    return count

if __name__ == "__main__":
    drivers_dir = os.path.join(os.getcwd(), 'drivers')
    injected_count = process_drivers(drivers_dir)
    print(f"Injected frontmatter into {injected_count} drivers.")
