import urllib.request
import json
import sys
import os

def mcp_execute(server_url, tool_name, arguments=None):
    # Standard MCP Tool Execution over HTTP (SSE/JSON-RPC)
    # Note: Real MCP often uses Stdio or SSE, we'll implement a clean HTTP-Post pattern for atomic drivers.
    url = f"{server_url}/tools/{tool_name}/execute"
    payload = {"arguments": arguments or {}}
    
    req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers={'Content-Type': 'application/json'})
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode())
            return {"status": "success", "data": result}
    except Exception as e:
        return {"status": "error", "message": str(e), "hint": "Ensure the MCP server is reachable at " + server_url}

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(json.dumps({"error": "Usage: python3 mcp_query.py server_url tool_name [arguments_json]"}, indent=2))
    else:
        url, tool = sys.argv[1:3]
        args = json.loads(sys.argv[3]) if len(sys.argv) > 3 else {}
        print(json.dumps(mcp_execute(url, tool, args), indent=2))
