"""
---
id: xml_editor.driver
type: driver
tags: [kernel, editor, xml, automation]
parent_standard: driver-file.standard
summary: Deterministically reads or updates an element in an XML file.
---
"""
import os
import xml.etree.ElementTree as ET
import json
import sys

def process_xml(fpath, xpath=None, new_text=None, action="read"):
    try:
        if not os.path.exists(fpath):
            return {"status": "error", "message": f"File not found: {fpath}"}
            
        tree = ET.parse(fpath)
        root = tree.getroot()
        
        if action == "read":
            if xpath:
                elements = root.findall(xpath)
                results = [el.text for el in elements]
                return {"status": "success", "data": results}
            return {"status": "success", "data": ET.tostring(root, encoding='unicode')}
            
        elif action == "update":
            if not xpath or new_text is None:
                return {"status": "error", "message": "XPath and new_text required for update"}
            
            elements = root.findall(xpath)
            for el in elements:
                el.text = new_text
            
            tree.write(fpath, encoding='utf-8', xml_declaration=True)
            return {"status": "success", "file": fpath, "xpath": xpath, "count": len(elements)}
            
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"status": "error", "message": "Usage: xml_editor.py <path> [xpath] [new_text] [action]"}))
        sys.exit(1)
        
    path = sys.argv[1]
    xp = sys.argv[2] if len(sys.argv) > 2 else None
    txt = sys.argv[3] if len(sys.argv) > 3 else None
    act = sys.argv[4] if len(sys.argv) > 4 else ("update" if txt else "read")
    
    res = process_xml(path, xp, txt, act)
    print(json.dumps(res, indent=2))
