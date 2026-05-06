import urllib.request
import json
import sys
import os

def fetch_pr_data(owner, repo, pr_number, token):
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/comments"
    req = urllib.request.Request(url)
    req.add_header("Authorization", f"token {token}")
    req.add_header("Accept", "application/vnd.github.v3+json")
    
    try:
        with urllib.request.urlopen(req) as response:
            comments = json.loads(response.read().decode())
            return {
                "status": "success",
                "pr_number": pr_number,
                "comments": [{"user": c['user']['login'], "body": c['body'], "path": c['path']} for c in comments],
                "count": len(comments)
            }
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(json.dumps({"status": "error", "message": "Usage: python3 github_pr_audit.py owner repo pr_number [token]"}, indent=2))
    else:
        owner, repo, pr_number = sys.argv[1:4]
        token = sys.argv[4] if len(sys.argv) > 4 else os.getenv("GITHUB_TOKEN")
        if not token:
            print(json.dumps({"status": "error", "message": "Missing GITHUB_TOKEN"}, indent=2))
        else:
            print(json.dumps(fetch_pr_data(owner, repo, pr_number, token), indent=2))
