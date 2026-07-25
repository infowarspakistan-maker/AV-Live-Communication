import re

with open('src/pages/ProductDetails.tsx', 'r') as f:
    lines = f.readlines()

depth = 0
for idx, line in enumerate(lines):
    if "return (" in line:
        print(f"Line {idx+1}: return (")
        depth = 1
        continue
    if depth > 0:
        opened = len(re.findall(r'<[a-zA-Z]+[^>]*[^/]>', line))
        closed = len(re.findall(r'</[a-zA-Z]+>', line))
        self_closing = len(re.findall(r'<[a-zA-Z]+[^>]*/>', line))
        
        # This regex is too simple for full JSX, but let's just count <div and </div
        opened = line.count("<div")
        closed = line.count("</div")
        
        depth += (opened - closed)
        if depth <= 0:
            print(f"Line {idx+1}: depth is {depth}. Line content: {line.strip()}")
            break
