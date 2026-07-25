import sys

with open('src/pages/Home.tsx', 'r') as f:
    content = f.read()

inactive_section = """            <div className="flex items-center justify-center h-full text-white/20 font-black text-4xl uppercase tracking-widest">
              AV LIVE CMS INACTIVE
            </div>"""

new_section = """            <div className="absolute inset-0 z-10 flex flex-col items-start justify-center text-left px-8 md:px-20 max-w-[1400px] mx-auto w-full">
              <div className="w-32 h-6 bg-white/10 rounded-md mb-6 animate-pulse"></div>
              <div className="w-3/4 max-w-2xl h-12 bg-white/10 rounded-md mb-4 animate-pulse"></div>
              <div className="w-1/2 max-w-lg h-12 bg-white/10 rounded-md mb-10 animate-pulse"></div>
              <div className="w-40 h-12 bg-[#00B4D8]/20 rounded-xl animate-pulse"></div>
            </div>"""

if inactive_section in content:
    content = content.replace(inactive_section, new_section)
    with open('src/pages/Home.tsx', 'w') as f:
        f.write(content)
    print("Replaced inactive section")
else:
    print("Inactive section not found")
