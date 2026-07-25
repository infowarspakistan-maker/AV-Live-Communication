import sys

with open('src/pages/Home.tsx', 'r') as f:
    content = f.read()

start_tag = "{/* Video Conferencing Slider */}"
end_tag = "{/* Setup Wizard Banner */}"

if start_tag in content and end_tag in content:
    start_idx = content.find(start_tag)
    end_idx = content.find(end_tag)
    
    # Remove the Video Conferencing Slider section
    content = content[:start_idx] + content[end_idx:]
    
    with open('src/pages/Home.tsx', 'w') as f:
        f.write(content)
    print("Patched successfully")
else:
    print("Tags not found")
