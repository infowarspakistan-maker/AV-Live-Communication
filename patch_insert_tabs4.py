import sys

with open('src/pages/ProductDetails.tsx', 'r') as f:
    content = f.read()

# We need to find:
#              </div>
#           </div>
#              {/* Detailed Intelligence Tabs */}
# and change it to:
#              </div>
#              {/* Detailed Intelligence Tabs */}

old_str = """             </div>
          </div>
             {/* Detailed Intelligence Tabs */}"""

new_str = """             </div>
             {/* Detailed Intelligence Tabs */}"""

if old_str in content:
    content = content.replace(old_str, new_str)
    
# And we need to add `          </div>` before `{/* Right: Technical Specs & Purchase Module (Span 5) */}`
old_str2 = """             </div>
          {/* Right: Technical Specs & Purchase Module (Span 5) */}"""

new_str2 = """             </div>
          </div>
          {/* Right: Technical Specs & Purchase Module (Span 5) */}"""

if old_str2 in content:
    content = content.replace(old_str2, new_str2)

with open('src/pages/ProductDetails.tsx', 'w') as f:
    f.write(content)
print("Grid fixed")
