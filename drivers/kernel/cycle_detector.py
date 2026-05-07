"""
---
id: cycle_detector.driver
type: driver
tags: [kernel, automation, actuator]
parent_standard: driver-file.standard
summary: Atomic actuator for cycle detector.
---
"""

import os
import re
import json
import sys

def get_delegations(agent_dir):
    graph = {} # agent_id -> list of delegate_ids
    
    for root, _, files in os.walk(agent_dir):
        for name in files:
            if name.endswith('.md') and name != 'README.md':
                fpath = os.path.join(root, name)
                with open(fpath, 'r') as f:
                    content = f.read()
                
                # Extract ID
                id_match = re.search(r'^id:\s*(.*)$', content, re.MULTILINE)
                if not id_match: continue
                agent_id = id_match.group(1).strip()
                
                # Extract Delegates: [a, b, c]
                del_match = re.search(r'delegates:\s*\[(.*?)\]', content)
                delegates = [d.strip() for d in del_match.group(1).split(',') if d.strip()] if del_match else []
                
                graph[agent_id] = delegates
    return graph

def find_cycles(graph):
    cycles = []
    visited = set()
    path = []

    def visit(node):
        if node in path:
            # Found a cycle!
            cycle_start = path.index(node)
            cycles.append(path[cycle_start:] + [node])
            return
        
        if node in visited: return
        
        visited.add(node)
        path.append(node)
        
        for neighbor in graph.get(node, []):
            # Strip .agent suffix for matching
            base_neighbor = neighbor.replace('.agent', '')
            visit(base_neighbor)
            
        path.pop()

    for node in graph:
        visit(node)
    return cycles

if __name__ == "__main__":
    agent_dir = os.path.join(os.getcwd(), 'agents')
    graph = get_delegations(agent_dir)
    cycles = find_cycles(graph)
    print(json.dumps({"cycles": cycles}, indent=2))
