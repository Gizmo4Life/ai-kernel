import subprocess
import json
import sys

def main(message):
    try:
        # Stage all changes
        subprocess.run(["git", "add", "."], capture_output=True)
        
        # Commit
        result = subprocess.run(["git", "commit", "-m", message], capture_output=True, text=True)
        
        if result.returncode == 0:
            print(json.dumps({
                "status": "success",
                "message": message,
                "output": result.stdout.split('\n')[0]
            }, indent=2))
        else:
            print(json.dumps({
                "status": "fail",
                "output": result.stderr
            }, indent=2))
            
    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}, indent=2))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"status": "error", "message": "Missing commit message"}, indent=2))
    else:
        main(sys.argv[1])
