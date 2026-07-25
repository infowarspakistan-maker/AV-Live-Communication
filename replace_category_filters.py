import sys

with open('src/pages/Category.tsx', 'r') as f:
    content = f.read()

old_filter_section = """             <div className="bg-white p-8 rounded-[2.5rem] border border-gray-100 shadow-sm">
               <h3 className="text-[10px] font-black text-gray-400 uppercase tracking-widest mb-8">Hardware Partners</h3>
               <div className="space-y-4">
                  {brandsIncategory.map(brand => (
                    <Link key={brand} to={`/shop?brand=${brand.toString().toLowerCase()}`} className="flex items-center justify-between group">
                       <span className="text-sm font-black uppercase tracking-widest text-[#1A2B4C] group-hover:text-[#00B4D8] transition-colors">{brand}</span>
                       <div className="w-1.5 h-1.5 bg-gray-100 rounded-full group-hover:bg-[#00B4D8] transition-colors"></div>
                    </Link>
                  ))}
                  {brandsIncategory.length === 0 && (
                    <p className="text-[10px] text-gray-300 font-bold uppercase tracking-widest">No Active Brands</p>
                  )}
               </div>
             </div>"""

new_filter_section = """             <div className="bg-white rounded-[1.5rem] border border-gray-100 shadow-sm overflow-hidden">
               <div className="p-5">
                 <h3 className="font-black uppercase tracking-[0.15em] text-[10px] text-gray-500 mb-4">Hardware Partners</h3>
                 <div className="space-y-1.5 max-h-[220px] overflow-y-auto custom-scrollbar pr-2">
                    {brandsIncategory.map(brand => (
                      <Link key={brand} to={`/shop?brand=${brand.toString().toLowerCase()}`} className="flex items-center justify-between group py-1">
                         <div className="flex items-center gap-2.5">
                           <span className="text-[11px] font-bold uppercase tracking-widest text-[#1A2B4C] group-hover:text-[#00B4D8] transition-colors">{brand}</span>
                         </div>
                         <div className="w-1.5 h-1.5 bg-gray-200 rounded-full group-hover:bg-[#00B4D8] transition-colors"></div>
                      </Link>
                    ))}
                    {brandsIncategory.length === 0 && (
                      <p className="text-[9px] text-gray-400 font-bold uppercase tracking-widest py-2">No active partners</p>
                    )}
                 </div>
               </div>
             </div>"""

if old_filter_section in content:
    content = content.replace(old_filter_section, new_filter_section)
    with open('src/pages/Category.tsx', 'w') as f:
        f.write(content)
    print("Replaced in Category.tsx")
else:
    print("Could not find the exact old_filter_section string in Category.tsx")
