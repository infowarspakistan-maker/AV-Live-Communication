import sys

with open('src/pages/Solutions.tsx', 'r') as f:
    content = f.read()

content = content.replace("import { Link } from 'react-router-dom';\nimport { SEO } from '../components/SEO';\n from 'react-router-dom';", "import { Link } from 'react-router-dom';\nimport { SEO } from '../components/SEO';")

with open('src/pages/Solutions.tsx', 'w') as f:
    f.write(content)
