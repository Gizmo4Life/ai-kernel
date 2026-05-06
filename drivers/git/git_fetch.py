import subprocess
import json
import sys

def main():
    try:
        # Fetch all remotes
        result = subprocess.run(["git", "fetch", "--all"], capture_output=True, text=True)
        
        if result.returncode == 0:
            print(json.dumps({
                "status": "success",
                "output": result.stderr # Fetch output is often in stderr
            }, indent=2))
        else:
            print(json.dumps({
                "status": "fail",
                "message": result.stderr
            }, indent=2))
            
    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}, indent=2))

if __name__ == "__main__":
    main()
