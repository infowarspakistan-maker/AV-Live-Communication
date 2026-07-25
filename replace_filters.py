import sys

with open('src/pages/Shop.tsx', 'r') as f:
    content = f.read()

old_filter_section = """          <div className="w-full lg:w-72 shrink-0 space-y-6">
            
            {/* Inventory Classification Widget */}
            <div className="bg-white p-6 rounded-[2rem] border border-gray-100 shadow-sm">
              <h3 className="font-black mb-6 uppercase tracking-[0.2em] text-[10px] text-gray-400">Inventory Classification</h3>
              
              <div className="relative">
                <select 
                  value={selectedCategory || ''}
                  onChange={(e) => updateFilters({ category: e.target.value || null })}
                  className="w-full appearance-none bg-white border border-gray-200 pl-4 pr-10 py-3.5 rounded-xl shadow-sm focus:outline-none focus:ring-2 focus:ring-[#00B4D8] font-black text-[10px] uppercase tracking-widest cursor-pointer text-[#1A2B4C]"
                >
                  <option value="">All Hardware</option>
                  {parentCategories.map(parent => {
                    const subs = getSubcategories(parent.id!);
                    return (
                      <optgroup key={parent.id} label={parent.name}>
                        <option value={parent.id!}>{parent.name}</option>
                        {subs.map(sub => {
                          return (
                            <option key={sub.id} value={sub.id!}>
                              {sub.name}
                            </option>
                          );
                        })}
                      </optgroup>
                    );
                  })}
                </select>
                <ChevronDown className="absolute right-4 top-1/2 -translate-y-1/2 text-gray-400 pointer-events-none" size={16} />
              </div>
            </div>

            {/* Hardware Partners (Brand Checkboxes) Widget */}
            <div className="bg-white p-6 rounded-[2rem] border border-gray-100 shadow-sm">
              <h3 className="font-black mb-6 uppercase tracking-[0.2em] text-[10px] text-gray-400">Hardware Partners</h3>
              
              <div className="space-y-3">
                {availableBrands.map(brand => {
                  const isChecked = selectedBrands.includes(brand.normalized);
                  return (
                    <button 
                      key={brand.normalized}
                      onClick={() => handleBrandToggle(brand.name)}
                      className="w-full flex items-center justify-between group py-1"
                    >
                      <div className="flex items-center gap-3">
                        <div className={`w-4 h-4 rounded border transition-all flex items-center justify-center ${isChecked ? 'bg-[#00B4D8] border-[#00B4D8] text-white' : 'border-gray-300 bg-white group-hover:border-[#00B4D8]'}`}>
                          {isChecked && <Check size={10} strokeWidth={3} />}
                        </div>
                        <span className={`text-xs font-bold uppercase tracking-widest transition-colors ${isChecked ? 'text-[#00B4D8]' : 'text-gray-500 group-hover:text-[#1A2B4C]'}`}>
                          {brand.name}
                        </span>
                      </div>
                      <span className="text-[9px] font-black text-gray-400 bg-gray-50 px-2 py-0.5 rounded-full">
                        {brand.count}
                      </span>
                    </button>
                  );
                })}
                {availableBrands.length === 0 && (
                  <p className="text-[10px] text-gray-400 font-bold uppercase tracking-widest py-2">No active partners for selected criteria</p>
                )}
              </div>
            </div>

            {/* Price Limit Widget */}
            <div className="bg-white p-6 rounded-[2rem] border border-gray-100 shadow-sm">
              <h3 className="font-black mb-6 uppercase tracking-[0.2em] text-[10px] text-gray-400">Value Limits (Rs.)</h3>
              
              <form onSubmit={handlePriceFilterApply} className="space-y-4">
                <div className="grid grid-cols-2 gap-3">
                  <div>
                    <label className="text-[9px] font-black text-gray-400 uppercase tracking-widest block mb-1.5">Min Limit</label>
                    <input 
                      type="number" 
                      placeholder="0"
                      value={localMinPrice}
                      onChange={(e) => setLocalMinPrice(e.target.value)}
                      className="w-full bg-gray-50 border border-gray-200 focus:outline-none focus:ring-1 focus:ring-[#00B4D8] rounded-xl px-3 py-2 text-xs font-bold text-[#1A2B4C]"
                    />
                  </div>
                  <div>
                    <label className="text-[9px] font-black text-gray-400 uppercase tracking-widest block mb-1.5">Max Limit</label>
                    <input 
                      type="number" 
                      placeholder="Any"
                      value={localMaxPrice}
                      onChange={(e) => setLocalMaxPrice(e.target.value)}
                      className="w-full bg-gray-50 border border-gray-200 focus:outline-none focus:ring-1 focus:ring-[#00B4D8] rounded-xl px-3 py-2 text-xs font-bold text-[#1A2B4C]"
                    />
                  </div>
                </div>
                
                <button 
                  type="submit"
                  className="w-full bg-[#1A2B4C] hover:bg-[#00B4D8] text-white text-[10px] font-black uppercase tracking-widest py-3 rounded-xl transition-all shadow-sm active:scale-98"
                >
                  Apply Value Limits
                </button>
              </form>
            </div>"""

new_filter_section = """          <div className="w-full lg:w-72 shrink-0 space-y-4">
            <div className="bg-white rounded-[1.5rem] border border-gray-100 shadow-sm overflow-hidden flex flex-col">
              
              <div className="p-5 border-b border-gray-50">
                <h3 className="font-black uppercase tracking-[0.15em] text-[10px] text-gray-500 mb-4">Inventory Classification</h3>
                <div className="relative">
                  <select 
                    value={selectedCategory || ''}
                    onChange={(e) => updateFilters({ category: e.target.value || null })}
                    className="w-full appearance-none bg-gray-50 border border-gray-100 pl-3 pr-8 py-2.5 rounded-lg focus:outline-none focus:ring-1 focus:ring-[#00B4D8] font-bold text-[11px] uppercase tracking-wider cursor-pointer text-[#1A2B4C] transition-all"
                  >
                    <option value="">All Hardware</option>
                    {parentCategories.map(parent => {
                      const subs = getSubcategories(parent.id!);
                      return (
                        <optgroup key={parent.id} label={parent.name}>
                          <option value={parent.id!}>{parent.name}</option>
                          {subs.map(sub => {
                            return (
                              <option key={sub.id} value={sub.id!}>
                                {sub.name}
                              </option>
                            );
                          })}
                        </optgroup>
                      );
                    })}
                  </select>
                  <ChevronDown className="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 pointer-events-none" size={14} />
                </div>
              </div>
              
              <div className="p-5 border-b border-gray-50">
                <h3 className="font-black uppercase tracking-[0.15em] text-[10px] text-gray-500 mb-4">Hardware Partners</h3>
                <div className="space-y-1 max-h-[220px] overflow-y-auto custom-scrollbar pr-2">
                  {availableBrands.map(brand => {
                    const isChecked = selectedBrands.includes(brand.normalized);
                    return (
                      <button 
                        key={brand.normalized}
                        onClick={() => handleBrandToggle(brand.name)}
                        className="w-full flex items-center justify-between group py-1.5"
                      >
                        <div className="flex items-center gap-2.5">
                          <div className={`w-3.5 h-3.5 rounded border transition-all flex items-center justify-center ${isChecked ? 'bg-[#00B4D8] border-[#00B4D8] text-white' : 'border-gray-300 bg-white group-hover:border-[#00B4D8]'}`}>
                            {isChecked && <Check size={10} strokeWidth={3} />}
                          </div>
                          <span className={`text-[10px] font-bold uppercase tracking-widest transition-colors ${isChecked ? 'text-[#00B4D8]' : 'text-gray-500 group-hover:text-[#1A2B4C]'}`}>
                            {brand.name}
                          </span>
                        </div>
                        <span className="text-[9px] font-black text-gray-400 bg-gray-50 px-1.5 py-0.5 rounded-md border border-gray-100">
                          {brand.count}
                        </span>
                      </button>
                    );
                  })}
                  {availableBrands.length === 0 && (
                    <p className="text-[9px] text-gray-400 font-bold uppercase tracking-widest py-2">No active partners</p>
                  )}
                </div>
              </div>

              <div className="p-5">
                <h3 className="font-black uppercase tracking-[0.15em] text-[10px] text-gray-500 mb-4">Value Limits (Rs.)</h3>
                <form onSubmit={handlePriceFilterApply} className="space-y-3">
                  <div className="grid grid-cols-2 gap-2">
                    <div>
                      <input 
                        type="number" 
                        placeholder="Min"
                        value={localMinPrice}
                        onChange={(e) => setLocalMinPrice(e.target.value)}
                        className="w-full bg-gray-50 border border-gray-100 focus:outline-none focus:ring-1 focus:ring-[#00B4D8] rounded-lg px-2.5 py-2 text-[11px] font-bold text-[#1A2B4C]"
                      />
                    </div>
                    <div>
                      <input 
                        type="number" 
                        placeholder="Max"
                        value={localMaxPrice}
                        onChange={(e) => setLocalMaxPrice(e.target.value)}
                        className="w-full bg-gray-50 border border-gray-100 focus:outline-none focus:ring-1 focus:ring-[#00B4D8] rounded-lg px-2.5 py-2 text-[11px] font-bold text-[#1A2B4C]"
                      />
                    </div>
                  </div>
                  <button 
                    type="submit"
                    className="w-full bg-[#1A2B4C] hover:bg-[#00B4D8] text-white text-[10px] font-black uppercase tracking-[0.15em] py-2.5 rounded-lg transition-colors"
                  >
                    Apply Limits
                  </button>
                </form>
              </div>

            </div>"""

if old_filter_section in content:
    content = content.replace(old_filter_section, new_filter_section)
    with open('src/pages/Shop.tsx', 'w') as f:
        f.write(content)
    print("Replaced in Shop.tsx")
else:
    print("Could not find the exact old_filter_section string in Shop.tsx")
