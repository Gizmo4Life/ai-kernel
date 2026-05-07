"""
---
id: kernel_server.driver
type: driver
tags: [kernel, automation, actuator]
parent_standard: driver-file.standard
summary: Atomic actuator for kernel server.
---
"""

import http.server
import json
import subprocess
import os

PORT = 8080

class KernelMCPServer(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/tools/execute":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            request = json.loads(post_data)
            
            tool_name = request.get("tool")
            arguments = request.get("arguments", {})
            
            response = self.execute_tool(tool_name, arguments)
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def execute_tool(self, tool, args):
        # Mapping Tool Names to Internal Drivers
        tool_map = {
            "global_heal": "python3 drivers/kernel/master_healer.py",
            "impact_audit": "python3 drivers/kernel/impact_analyzer.py",
            "compliance_audit": "python3 drivers/kernel/global_compliance_auditor.py",
            "content_audit": "python3 drivers/kernel/content_auditor.py"
        }
        
        if tool in tool_map:
            cmd = tool_map[tool]
            # Add arguments if provided
            if tool == "impact_audit" and "target_id" in args:
                cmd += f" {args['target_id']}"
                
            try:
                result = subprocess.check_output(cmd, shell=True).decode()
                return {"status": "success", "output": json.loads(result)}
            except Exception as e:
                return {"status": "error", "message": str(e)}
        return {"status": "error", "message": f"Tool '{tool}' not found in Kernel Registry"}

def run_server():
    server_address = ('', PORT)
    httpd = http.server.HTTPServer(server_address, KernelMCPServer)
    print(f"AI Kernel MCP Server running on port {PORT}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
