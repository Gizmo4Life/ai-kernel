import subprocess
import json
import sys

def main():
    try:
        result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        changes = [line.strip() for line in result.stdout.split('\n') if line.strip()]
        print(json.dumps({
            "status": "success",
            "modified_files": changes,
            "count": len(changes)
        }, indent=2))
    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}, indent=2))

if __name__ == "__main__":
    main()
