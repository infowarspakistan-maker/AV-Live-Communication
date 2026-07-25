import sys

with open('vite.config.ts', 'r') as f:
    content = f.read()

chunks_old = "manualChunks: undefined,"
chunks_new = """manualChunks(id) {
            if (id.includes('node_modules')) {
              if (id.includes('react') || id.includes('react-dom') || id.includes('react-router-dom')) {
                return 'vendor-react';
              }
              if (id.includes('firebase')) {
                return 'vendor-firebase';
              }
              if (id.includes('lucide-react')) {
                return 'vendor-icons';
              }
              if (id.includes('motion')) {
                return 'vendor-motion';
              }
              return 'vendor';
            }
          },"""
content = content.replace(chunks_old, chunks_new)

with open('vite.config.ts', 'w') as f:
    f.write(content)
