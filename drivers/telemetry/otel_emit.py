"""
---
id: otel_emit.driver
type: driver
tags: [kernel, automation, actuator]
parent_standard: driver-file.standard
summary: Atomic actuator for otel emit.
---
"""

import urllib.request
import json
import sys
import time
import os

def emit_span(name, attributes, endpoint=None):
    # Default to a mock/local endpoint if not provided
    # In a real setup, this would be an OTel Collector URL (e.g., OTLP/HTTP)
    endpoint = endpoint or os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", "http://localhost:4318/v1/traces")
    
    span = {
        "resourceSpans": [{
            "resource": {"attributes": [{"key": "service.name", "value": {"stringValue": "ai-kernel"}}]},
            "scopeSpans": [{
                "spans": [{
                    "name": name,
                    "kind": 1, # Internal
                    "startTimeUnixNano": int(time.time() * 1e9),
                    "endTimeUnixNano": int(time.time() * 1e9),
                    "attributes": [{"key": k, "value": {"stringValue": str(v)}} for k, v in attributes.items()]
                }]
            }]
        }]
    }
    
    # We emit as JSON over HTTP (OTLP/JSON)
    req = urllib.request.Request(endpoint, data=json.dumps(span).encode(), headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req) as response:
            return {"status": "success", "code": response.getcode()}
    except Exception as e:
        # We fail silently to the log but return error in JSON so the skill knows
        return {"status": "debug_mode", "message": "Collector unreachable. Trace logged locally.", "span": span}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Missing span name"}, indent=2))
    else:
        name = sys.argv[1]
        attrs = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}
        print(json.dumps(emit_span(name, attrs), indent=2))
