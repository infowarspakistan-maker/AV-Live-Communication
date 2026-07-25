import sys

with open('src/pages/Solutions.tsx', 'r') as f:
    content = f.read()

import_seo = "import { SEO } from '../components/SEO';\n"
if "import { SEO }" not in content:
    content = content.replace("import { Link }", "import { Link } from 'react-router-dom';\n" + import_seo)
else:
    import_seo = ""

seo_tag = """
      <SEO 
        title="Video Conferencing Solutions Pakistan | AV Live" 
        description="Professional video conferencing solutions in Pakistan. We equip boardrooms with Poly, Cisco, and HP hardware for seamless remote collaboration across Lahore, Karachi, and Islamabad." 
        keywords="Video conferencing solutions Pakistan, Polycom Studio Pakistan, Cisco Webex Pakistan, Boardroom AV setup, Video conference equipment Lahore"
      />
"""

if "<SEO" not in content:
    content = content.replace('<div className="py-16 bg-[#F8F9FA] min-h-screen text-[#1A2B4C]">', '<div className="py-16 bg-[#F8F9FA] min-h-screen text-[#1A2B4C]">' + seo_tag)

with open('src/pages/Solutions.tsx', 'w') as f:
    f.write(content)
print("Solutions patched")
