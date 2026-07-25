import sys

with open('src/pages/ProductDetails.tsx', 'r') as f:
    content = f.read()

tabs_content = """             {/* Detailed Intelligence Tabs */}
             <div className="mt-12 w-full">
               <div className="flex gap-8 mb-12 overflow-x-auto border-b border-gray-200 text-[21px] pl-5">
                  {[
                    { id: 'overview', label: 'Product Overview' },
                    { id: 'specs', label: 'Technical Specs' },
                    { id: 'in-the-box', label: "What's in the Box" },
                    { id: 'support', label: 'Support & Warranty' }
                  ].map(tab => (
                    <button
                       key={tab.id}
                      onClick={() => setActiveTab(tab.id as any)}
                      style={{ fontSize: tab.id === 'overview' ? '14px' : tab.id === 'in-the-box' ? '12px' : undefined }}
                      className={`text-xs font-black uppercase tracking-[0.2em] pb-6 border-b-4 transition-all whitespace-nowrap ${activeTab === tab.id ? 'border-[#00B4D8] text-[#1A2B4C]' : 'border-transparent text-gray-400 hover:text-[#1A2B4C]'}`}
                    >
                      {tab.label}
                    </button>
                  ))}
               </div>
               
               <div className="min-h-[400px] pl-14 -mb-1 -mr-1">
                 <AnimatePresence mode="wait">
                   {activeTab === 'overview' && (
                     <motion.div
                        key="overview"
                       initial={{ opacity: 0, y: 10 }}
                       animate={{ opacity: 1, y: 0 }}
                       exit={{ opacity: 0, y: -10 }}
                     >
                       <div className="prose prose-lg max-w-none text-gray-500 font-medium leading-relaxed" dangerouslySetInnerHTML={{ __html: product.description || '' }} />
                       
                       <div className="mt-16 grid grid-cols-1 md:grid-cols-3 gap-8">
                          <div className="bg-white p-8 rounded-3xl shadow-sm border border-gray-100 text-center">
                             <PlayCircle className="w-12 h-12 text-[#00B4D8] mx-auto mb-4" />
                             <h4 className="font-black text-[#1A2B4C] mb-2">Plug and Play</h4>
                             <p className="text-sm text-gray-500 font-medium">Deploy in minutes with minimal configuration required.</p>
                          </div>
                          <div className="bg-white p-8 rounded-3xl shadow-sm border border-gray-100 text-center">
                             <Headset className="w-12 h-12 text-[#00B4D8] mx-auto mb-4" />
                             <h4 className="font-black text-[#1A2B4C] mb-2">Enterprise Audio</h4>
                             <p className="text-sm text-gray-500 font-medium">Crystal clear communication with advanced noise blocking.</p>
                          </div>
                          <div className="bg-white p-8 rounded-3xl shadow-sm border border-gray-100 text-center">
                             <ShieldCheck className="w-12 h-12 text-[#00B4D8] mx-auto mb-4" />
                             <h4 className="font-black text-[#1A2B4C] mb-2">Secure Architecture</h4>
                             <p className="text-sm text-gray-500 font-medium">Built with enterprise-grade security protocols standard.</p>
                          </div>
                       </div>
                     </motion.div>
                   )}
                   {activeTab === 'specs' && (
                     <motion.div
                        key="specs"
                       initial={{ opacity: 0, y: 10 }}
                       animate={{ opacity: 1, y: 0 }}
                       exit={{ opacity: 0, y: -10 }}
                     >
                       <div className="bg-white rounded-[2rem] border border-gray-100 shadow-sm overflow-hidden">
                         {specificationsList.length > 0 ? (
                           <div className="divide-y divide-gray-50">
                             {specificationsList.map((spec, idx) => {
                               const parts = spec.split(':');
                               if (parts.length < 2) return null;
                               const label = parts[0];
                               const val = parts.slice(1).join(':');
                               return (
                                 <div key={idx} className="flex flex-col md:flex-row md:items-center p-6 hover:bg-gray-50 transition-colors">
                                   <span className="w-1/3 text-xs font-black uppercase tracking-widest text-gray-400 mb-2 md:mb-0">{label.trim()}</span>
                                   <span className="w-2/3 text-sm font-bold text-[#1A2B4C]">{val.trim()}</span>
                                 </div>
                               );
                             })}
                           </div>
                         ) : (
                           <div className="p-12 text-center text-gray-500 font-medium">
                             No detailed specifications available for this product.
                           </div>
                         )}
                       </div>
                     </motion.div>
                   )}
                   {activeTab === 'in-the-box' && (
                     <motion.div
                        key="in-the-box"
                       initial={{ opacity: 0, y: 10 }}
                       animate={{ opacity: 1, y: 0 }}
                       exit={{ opacity: 0, y: -10 }}
                     >
                       <div className="bg-white rounded-[2rem] border border-gray-100 shadow-sm p-12 text-center">
                          <Box className="w-16 h-16 text-gray-300 mx-auto mb-6" />
                          <h3 className="text-2xl font-black text-[#1A2B4C] mb-8">Standard Package Contents</h3>
                          <ul className="max-w-md mx-auto text-left space-y-4">
                            <li className="flex items-center gap-4 text-gray-600 font-medium"><CheckCircle className="text-emerald-500" size={20} /> Main Hardware Unit</li>
                            <li className="flex items-center gap-4 text-gray-600 font-medium"><CheckCircle className="text-emerald-500" size={20} /> Power Supply & Cable</li>
                            <li className="flex items-center gap-4 text-gray-600 font-medium"><CheckCircle className="text-emerald-500" size={20} /> Network Cable (Cat5e/Cat6)</li>
                            <li className="flex items-center gap-4 text-gray-600 font-medium"><CheckCircle className="text-emerald-500" size={20} /> Mounting Hardware (if applicable)</li>
                            <li className="flex items-center gap-4 text-gray-600 font-medium"><CheckCircle className="text-emerald-500" size={20} /> Setup Guide & Documentation</li>
                          </ul>
                       </div>
                     </motion.div>
                   )}
                   {activeTab === 'support' && (
                     <motion.div
                        key="support"
                       initial={{ opacity: 0, y: 10 }}
                       animate={{ opacity: 1, y: 0 }}
                       exit={{ opacity: 0, y: -10 }}
                     >
                       <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                         <div className="bg-white rounded-[2rem] border border-gray-100 shadow-sm p-10">
                            <ShieldCheck className="w-12 h-12 text-[#00B4D8] mb-6" />
                            <h3 className="text-xl font-black text-[#1A2B4C] mb-4">Standard Warranty</h3>
                            <p className="text-gray-500 font-medium leading-relaxed mb-6">
                              This product includes a standard 1-year manufacturer warranty covering defects in materials and workmanship.
                            </p>
                            <button className="text-xs font-black text-[#00B4D8] uppercase tracking-widest hover:underline">
                              View Warranty Details
                            </button>
                         </div>
                         <div className="bg-white rounded-[2rem] border border-gray-100 shadow-sm p-10">
                            <CreditCard className="w-12 h-12 text-[#00B4D8] mb-6" />
                            <h3 className="text-xl font-black text-[#1A2B4C] mb-4">Extended Protection</h3>
                            <p className="text-gray-500 font-medium leading-relaxed mb-6">
                              Add AV Live Premier Support for advanced hardware replacement, 24/7 technical assistance, and priority RMA handling.
                            </p>
                            <button className="text-xs font-black text-[#00B4D8] uppercase tracking-widest hover:underline">
                              Contact Sales for Quote
                            </button>
                         </div>
                       </div>
                     </motion.div>
                   )}
                 </AnimatePresence>
               </div>
             </div>"""

target = "          {/* Right: Technical Specs & Purchase Module (Span 5) */}"
if target in content:
    content = content.replace(target, tabs_content + "\n" + target)
    print("Tabs inserted!")
else:
    print("Target string not found!")

with open('src/pages/ProductDetails.tsx', 'w') as f:
    f.write(content)
