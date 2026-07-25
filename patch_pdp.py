import sys

with open('src/pages/ProductDetails.tsx', 'r') as f:
    content = f.read()

# 1. We need to extract the title block from the right column and insert it above the grid.
# The grid starts with: <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16">

old_grid_start = '<div className="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16">'

new_header = """
      <div 
        className="max-w-6xl mx-auto mb-8 border-b border-gray-100 pb-6"
        style={{ marginBottom: '8px', paddingBottom: '7px', paddingLeft: '-4px', paddingRight: '1px' }}
      >
        <div className="flex flex-wrap items-center gap-3 mb-2 text-xs font-black uppercase tracking-widest text-[#00B4D8]">
           <span>{product.brand}</span>
           <span className="w-1.5 h-1.5 bg-gray-300 rounded-full"></span>
           <span className="text-gray-400">SKU: {product.sku}</span>
        </div>
        
        <h1 
          className="text-3xl md:text-4xl lg:text-5xl font-black tracking-tight leading-tight text-[#1A2B4C] mb-4"
          style={{ fontSize: '24px' }}
        >
          {product.productName}
        </h1>
      </div>
"""

# Let's remove the title from the right column.
old_right_col_title = """                <div>
                  <div className="flex items-center gap-3 mb-4">
                     <span className="text-[#00B4D8] text-xs font-black uppercase tracking-[0.2em]">{product.brand}</span>
                     <span className="w-1 h-1 bg-gray-300 rounded-full"></span>
                     <span className="text-[10px] text-gray-400 font-black uppercase tracking-widest">SKU: {product.sku}</span>
                  </div>
                  
                  <h1 className="text-2xl lg:text-3xl font-black tracking-tight leading-[1.1] mb-6">{product.productName}</h1>
                  
                  <div className="text-gray-500 font-medium leading-relaxed text-lg prose prose-sm max-w-none break-words">
                    <ReactMarkdown rehypePlugins={[rehypeRaw]} remarkPlugins={[remarkGfm]}>
                      {product.shortDescription || product.description || ''}
                    </ReactMarkdown>
                  </div>
                </div>"""

new_right_col_title = """                <div 
                  className="bg-white p-6 md:p-8 rounded-[2rem] border border-gray-100 shadow-sm space-y-3 w-full h-auto overflow-hidden break-words"
                  style={{ height: '248.85000000000002px' }}
                >
                  <span className="block text-[10px] font-black uppercase tracking-widest text-[#00B4D8]">
                    Quick Overview
                  </span>
                  <div className="text-gray-500 font-medium leading-relaxed text-lg prose prose-sm max-w-none break-words">
                    <ReactMarkdown rehypePlugins={[rehypeRaw]} remarkPlugins={[remarkGfm]}>
                      {product.shortDescription || product.description || ''}
                    </ReactMarkdown>
                  </div>
                </div>"""


content = content.replace(old_grid_start, new_header + "\n      " + old_grid_start)
content = content.replace(old_right_col_title, new_right_col_title)

# Now, we need to move the Detailed Intelligence Tabs into the left column (lg:col-span-7)
# The left column currently ends with:
#              </div>
#           </div>
#           {/* Right: Technical Specs & Purchase Module (Span 5) */}

left_col_end = """             </div>
          </div>
          {/* Right: Technical Specs & Purchase Module (Span 5) */}"""

# We extract the Detailed Intelligence Tabs from the bottom.
# They are located after:
#           </div>
#         </div>
#         {/* Detailed Intelligence Tabs */}

old_tabs_section_start = """        </div>
        {/* Detailed Intelligence Tabs */}
        <div className="mt-32 max-w-5xl mx-auto">"""

# wait, the string extraction might be tricky. Let's do it using indices.
start_tabs = content.find('{/* Detailed Intelligence Tabs */}')
end_tabs = content.find('{/* Related Products */}')

if start_tabs != -1 and end_tabs != -1:
    tabs_content = content[start_tabs:end_tabs].strip()
    
    # We replace the top level div of tabs:
    # <div className="mt-32 max-w-5xl mx-auto"> with <div className="mt-12 w-full">
    tabs_content = tabs_content.replace('<div className="mt-32 max-w-5xl mx-auto">', '<div className="mt-12 w-full">')
    
    # Remove the tabs from original location
    # Remember it was preceded by `        </div>`
    # Let's just remove the block from start_tabs to end_tabs.
    content = content[:start_tabs] + content[end_tabs:]
    
    # Insert tabs_content at the end of the left column
    content = content.replace(left_col_end, "\n             {/* Detailed Intelligence Tabs */}\n             " + tabs_content + "\n          </div>\n          {/* Right: Technical Specs & Purchase Module (Span 5) */} ")

with open('src/pages/ProductDetails.tsx', 'w') as f:
    f.write(content)

print("PDP Layout patched")
