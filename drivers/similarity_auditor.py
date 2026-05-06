import os
import re
import json
import sys

def get_glossary_data(glossary_dir):
    data = {} # id -> summary
    for root, _, files in os.walk(glossary_dir):
        for name in files:
            if name.endswith('.md') and name != 'README.md':
                fpath = os.path.join(root, name)
                with open(fpath, 'r') as f:
                    content = f.read()
                
                id_match = re.search(r'^id:\s*(.*)$', content, re.MULTILINE)
                sum_match = re.search(r'^summary:\s*(.*)$', content, re.MULTILINE)
                
                if id_match and sum_match:
                    data[id_match.group(1).strip()] = sum_match.group(1).strip()
    return data

def calculate_similarity(s1, s2):
    # Simple word-overlap similarity
    words1 = set(re.findall(r'\w+', s1.lower()))
    words2 = set(re.findall(r'\w+', s2.lower()))
    
    intersection = words1.intersection(words2)
    union = words1.union(words2)
    
    return len(intersection) / len(union) if union else 0

def find_collisions(data, threshold=0.4):
    collisions = []
    keys = list(data.keys())
    
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            sim = calculate_similarity(data[keys[i]], data[keys[j]])
            if sim >= threshold:
                collisions.append({
                    "term1": keys[i],
                    "term2": keys[j],
                    "similarity": f"{sim:.2f}"
                })
    return collisions

if __name__ == "__main__":
    glossary_dir = os.path.join(os.getcwd(), 'glossary')
    data = get_glossary_data(glossary_dir)
    collisions = find_collisions(data)
    print(json.dumps({"collisions": collisions}, indent=2))
