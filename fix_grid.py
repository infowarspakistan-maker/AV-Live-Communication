import sys

with open('src/pages/ProductDetails.tsx', 'r') as f:
    lines = f.readlines()

new_lines = []
for idx, line in enumerate(lines):
    # Remove the `</div>` just before `{/* Detailed Intelligence Tabs */}`
    if "{/* Detailed Intelligence Tabs */}" in line and "</div>" in lines[idx-1]:
        # remove the last item from new_lines
        if new_lines and "</div>" in new_lines[-1]:
            new_lines.pop()
    
    # Add `</div>` just before `{/* Right: Technical Specs ...`
    if "{/* Right: Technical Specs" in line:
        new_lines.append("          </div>\n")
        
    new_lines.append(line)

with open('src/pages/ProductDetails.tsx', 'w') as f:
    f.writelines(new_lines)
