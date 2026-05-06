import urllib.request
import json
import sys
import os

def fetch_issue_data(owner, repo, issue_number, token):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"
    req = urllib.request.Request(url)
    req.add_header("Authorization", f"token {token}")
    req.add_header("Accept", "application/vnd.github.v3+json")
    
    try:
        with urllib.request.urlopen(req) as response:
            issue = json.loads(response.read().decode())
            return {
                "status": "success",
                "issue_number": issue_number,
                "title": issue['title'],
                "body": issue['body'],
                "labels": [l['name'] for l in issue['labels']],
                "state": issue['state']
            }
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(json.dumps({"status": "error", "message": "Usage: python3 github_issue_audit.py owner repo issue_number [token]"}, indent=2))
    else:
        owner, repo, issue_number = sys.argv[1:4]
        token = sys.argv[4] if len(sys.argv) > 4 else os.getenv("GITHUB_TOKEN")
        if not token:
            print(json.dumps({"status": "error", "message": "Missing GITHUB_TOKEN"}, indent=2))
        else:
            print(json.dumps(fetch_issue_data(owner, repo, issue_number, token), indent=2))
