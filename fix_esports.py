import sys

with open('src/pages/Esports.tsx', 'r') as f:
    content = f.read()

content = content.replace("import { useState } from 'react';\nimport { SEO } from '../components/SEO';\n from 'react';", "import { useState } from 'react';\nimport { SEO } from '../components/SEO';")

with open('src/pages/Esports.tsx', 'w') as f:
    f.write(content)
