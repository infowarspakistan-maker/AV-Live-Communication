import sys

with open('src/pages/Esports.tsx', 'r') as f:
    content = f.read()

import_seo = "import { SEO } from '../components/SEO';\n"
if "import { SEO }" not in content:
    content = content.replace("import { useState }", "import { useState } from 'react';\n" + import_seo)
else:
    import_seo = ""

seo_tag = """
      <SEO 
        title="Esports Event Management Pakistan | AV Live" 
        description="Expert esports event management and production in Pakistan. We provide 144Hz+ displays, zero-latency networks, and broadcast AV for tournaments in Lahore, Karachi, and Islamabad." 
        keywords="Esports event management Pakistan, gaming tournament AV setup, LAN party infrastructure, esports production Lahore, gaming event Karachi"
      />
"""

if "<SEO" not in content:
    content = content.replace('<div className="bg-[#1A2B4C] min-h-screen text-white">', '<div className="bg-[#1A2B4C] min-h-screen text-white">' + seo_tag)

with open('src/pages/Esports.tsx', 'w') as f:
    f.write(content)
print("Esports patched")
