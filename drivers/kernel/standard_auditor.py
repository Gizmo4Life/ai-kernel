import os
import re
import sys
import json

def get_requirements(standard_path):
    with open(standard_path, 'r') as f:
        content = f.read()
    
    parts = re.split(r'^---$', content, flags=re.MULTILINE)
    if len(parts) < 3: return []
    
    fm_raw = parts[1]
    
    match = re.search(r'requirements:\s*\[(.*?)\]', fm_raw)
    if match:
        # Strip whitespace AND surrounding quotes
        return [r.strip().strip('"').strip("'") for r in match.group(1).split(',') if r.strip()]
    return []

def audit_compliance(target_path, requirements):
    with open(target_path, 'r') as f:
        content = f.read()
    
    results = {}
    passed = 0
    for req in requirements:
        if re.search(rf'{re.escape(req)}', content, re.IGNORECASE):
            results[req] = "PASS"
            passed += 1
        else:
            results[req] = "FAIL"
            
    score = (passed / len(requirements)) * 100 if requirements else 100
    return results, score

def main(standard_id, target_path):
    standard_file = None
    for root, _, files in os.walk('standards'):
        for name in files:
            if name.endswith('.md'):
                fpath = os.path.join(root, name)
                with open(fpath, 'r') as f:
                    if f'id: {standard_id}' in f.read():
                        standard_file = fpath
                        break
        if standard_file: break
        
    if not standard_file:
        print(json.dumps({"error": f"Standard {standard_id} not found"}, indent=2))
        return

    reqs = get_requirements(standard_file)
    if not reqs:
        print(json.dumps({"error": f"No requirements found in {standard_id}"}, indent=2))
        return

    report, score = audit_compliance(target_path, reqs)
    
    output = {
        "standard": standard_id,
        "target": target_path,
        "score": f"{score:.1f}%",
        "details": report
    }
    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 standard_auditor.py <standard_id> <target_file>")
    else:
        main(sys.argv[1], sys.argv[2])
