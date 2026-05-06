import os
import subprocess
import json
import sys

def run_step(name, command):
    print(f"--- [STEP] {name} ---")
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        if result.returncode == 0:
            print(f"SUCCESS: {name}")
            return result.stdout
        else:
            print(f"FAILURE: {name}\nError: {result.stderr}")
            return None
    except Exception as e:
        print(f"EXCEPTION: {name}\nError: {str(e)}")
        return None

def main():
    print("=== INITIALIZING GLOBAL HEALING WAVE (v5.0.0) ===")
    
    # 1. Structural Repair
    run_step("Frontmatter Repair", "python3 drivers/fm_repair.py")
    
    # 2. Semantic Healing
    run_step("Auto-Link Glossary", "python3 drivers/auto_linker.py .")
    
    # 3. Visual Healing
    run_step("Mermaid Diagram Generation", "python3 drivers/mermaid_gen.py .")
    
    # 4. Integrity Audits
    ids = run_step("ID Collision Audit", "python3 drivers/id_auditor.py .")
    conn = run_step("Connectivity Audit", "python3 drivers/connectivity_auditor.py .")
    cycles = run_step("Agent Cycle Audit", "python3 drivers/cycle_detector.py")
    
    # 5. Final Compliance Certification
    run_step("Global Compliance Audit", "python3 drivers/global_compliance_auditor.py")
    
    print("\n=== HEALING WAVE COMPLETE ===")
    print("View the final status in context/global-gap-report.md")

if __name__ == "__main__":
    main()
