import sys
import re

with open('src/pages/ProductDetails.tsx', 'r') as f:
    lines = f.readlines()

# Find the start of the main return block
start_idx = 0
for idx, line in enumerate(lines):
    if "const specificationsList =" in line:
        # we know it's 3 lines
        start_idx = idx + 3
        break

top_part = "".join(lines[:start_idx])

# Now the new return block
new_return = """  return (
    <div className="bg-[#F8F9FA] min-h-screen text-[#1A2B4C]">
      <SEO 
        title={`${product.productName} | ${product.brand} | AV Live`}
        description={product.description?.replace(/<[^>]*>?/gm, '').substring(0, 160) || `Buy ${product.productName} by ${product.brand}. Expert AV hardware and collaboration tools.`}
        image={product.images?.[0]}
      />
      <StructuredData 
        data={{
          "@context": "https://schema.org/",
          "@type": "Product",
          "name": product.productName,
          "image": product.images || [],
          "description": product.description?.replace(/<[^>]*>?/gm, '') || product.shortDescription,
          "sku": product.sku,
          "brand": {
            "@type": "Brand",
            "name": product.brand
          },
          "offers": {
            "@type": "Offer",
            "url": `https://avlive.com.pk/product/${product.id}`,
            "priceCurrency": "PKR",
            "price": product.salePrice || product.regularPrice,
            "priceValidUntil": "2027-12-31",
            "itemCondition": "https://schema.org/NewCondition",
            "availability": product.stockQuantity && product.stockQuantity > 0 ? "https://schema.org/InStock" : "https://schema.org/OutOfStock",
            "seller": {
              "@type": "Organization",
              "name": "AV Live"
            }
          }
        }}
      />
      
      {/* Breadcrumbs */}
      <div className="bg-white border-b border-gray-100 py-2 sticky top-[72px] md:top-[88px] z-30">
        <div className="max-w-screen-2xl mx-auto px-4 sm:px-6 lg:px-8 flex justify-between items-center">
           <Breadcrumbs items={[
             { label: 'Hardware Catalog', path: '/shop' },
             ...(product.categorySlugs && product.categorySlugs.length > 0 ? [{ 
               label: product.categorySlugs[0].replace(/-/g, ' '), 
               path: `/category/${product.categorySlugs[0]}` 
             }] : []),
             { label: product.productName, path: `/product/${product.id}` }
           ]} />
        </div>
      </div>

      <div className="max-w-screen-2xl mx-auto px-4 sm:px-6 lg:px-8 mt-8 pb-16">
        
        {/* Unified Title Header */}
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

        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16">
          
          {/* Left: Image Gallery & Detailed Tabs (Span 7) */}
          <div className="lg:col-span-7 flex flex-col gap-4 md:gap-6 -mr-2 -mt-2">
             {/* Main Image */}
             <motion.div 
               initial={{ opacity: 0, scale: 0.95 }}
               animate={{ opacity: 1, scale: 1 }}
               className="bg-white rounded-[2rem] border border-gray-100 shadow-xl overflow-hidden relative w-full aspect-square md:w-[700px] md:h-[500px] mx-auto cursor-crosshair group flex items-center justify-center p-12 shrink-0"
               onMouseEnter={() => setIsZooming(true)}
               onMouseLeave={() => setIsZooming(false)}
               onMouseMove={handleMouseMove}
             >
               <div className="absolute top-6 left-6 flex flex-col gap-2 z-10">
                 {product.salePrice < product.regularPrice && (
                   <div className="bg-[#00B4D8] text-white text-[10px] font-black uppercase tracking-widest px-4 py-2 rounded-full shadow-lg">
                     Save Rs. {((product.regularPrice || 0) - (product.salePrice || 0)).toLocaleString()}
                   </div>
                 )}
                 {product.stockQuantity < 5 && product.stockQuantity > 0 && (
                   <div className="bg-amber-500 text-white text-[10px] font-black uppercase tracking-widest px-4 py-2 rounded-full shadow-lg">
                     Only {product.stockQuantity} Left
                   </div>
                 )}
               </div>
               
               <div className="absolute top-6 right-6 flex gap-2 z-10 opacity-0 group-hover:opacity-100 transition-opacity">
                  <button className="w-10 h-10 bg-white/80 backdrop-blur rounded-full flex items-center justify-center text-[#1A2B4C] hover:bg-[#00B4D8] hover:text-white transition-all shadow-md">
                     <Share2 size={16} />
                  </button>
                  <button className="w-10 h-10 bg-white/80 backdrop-blur rounded-full flex items-center justify-center text-[#1A2B4C] hover:bg-rose-500 hover:text-white transition-all shadow-md">
                     <Heart size={16} />
                  </button>
               </div>

               <AnimatePresence mode="wait">
                 <motion.img 
                   key={activeImage}
                   initial={{ opacity: 0 }}
                   animate={{ opacity: 1 }}
                   exit={{ opacity: 0 }}
                   transition={{ duration: 0.2 }}
                   loading="lazy" 
                   src={product.images?.[activeImage] || 'https://placehold.co/800x800?text=No+Image'} 
                   alt={product.productName} 
                   className={`w-full h-full object-contain transition-transform duration-200 ${isZooming ? 'scale-[2]' : 'scale-100'}`}
                   style={isZooming ? {
                     transformOrigin: `${mousePos.x}% ${mousePos.y}%`
                   } : undefined}
                 />
               </AnimatePresence>
             </motion.div>

             {/* Thumbnail Strip */}
             <div className="flex gap-4 overflow-x-auto w-full shrink-0 no-scrollbar py-2">
               {product.images?.map((img, idx) => (
                 <button 
                   key={idx}
                   onClick={() => setActiveImage(idx)}
                   className={`w-20 h-20 md:w-24 md:h-24 rounded-2xl overflow-hidden border-2 transition-all shrink-0 bg-white ${activeImage === idx ? 'border-[#00B4D8] shadow-md scale-95' : 'border-transparent hover:border-gray-200 opacity-60 hover:opacity-100'}`}
                 >
                   <img loading="lazy" src={img} alt="Thumbnail" className="w-full h-full object-contain p-2" />
                 </button>
               ))}
             </div>

             {/* Detailed Intelligence Tabs */}
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
                       <div className="prose prose-sm md:prose-lg max-w-none text-gray-500 font-medium leading-relaxed" dangerouslySetInnerHTML={{ __html: product.description || '' }} />
                       
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
             </div>

          </div>

          {/* Right: Technical Specs & Purchase Module (Span 5) */}
          <div className="lg:col-span-5 flex flex-col relative">
            <div className="sticky top-[120px] lg:top-[160px]">
              <motion.div 
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className="space-y-8"
              >
                <div 
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
                </div>

                <div className="bg-white p-8 rounded-[2rem] border border-gray-100 shadow-sm space-y-6 md:w-[600px] md:h-[400px]">
                  <div className="flex items-end justify-between border-b border-gray-100 pb-6 ml-0 pl-[9px] pt-[7px]">
                    <div className="flex flex-col">
                      <span className="text-[30px] font-black text-[#1A2B4C] tracking-tight">Rs. {(product.salePrice ?? 0).toLocaleString()}</span>
                      {product.salePrice < product.regularPrice && (
                        <div className="flex items-center gap-2 mt-2">
                          <span className="text-sm text-gray-400 line-through font-bold">Rs. {(product.regularPrice ?? 0).toLocaleString()}</span>
                          <span className="text-[10px] font-black uppercase tracking-widest text-emerald-500 bg-emerald-50 px-2 py-1 rounded">
                            {Math.round(((product.regularPrice - product.salePrice) / product.regularPrice) * 100)}% OFF
                          </span>
                        </div>
                      )}
                    </div>
                  </div>

                  <div className="flex flex-col gap-3">
                     <div className="flex items-center gap-2 text-sm font-bold text-[#1A2B4C]">
                        {product.stockQuantity > 0 ? (
                           <>
                             <CheckCircle size={16} className="text-emerald-500" /> 
                             <span className="text-emerald-600">In Stock & Ready to Ship</span>
                           </>
                        ) : (
                           <>
                             <Info size={16} className="text-rose-500" /> 
                             <span className="text-rose-600">Currently Out of Stock</span>
                           </>
                        )}
                     </div>
                     <div className="text-[10px] text-gray-400 font-black uppercase tracking-widest pl-6">
                       Free Shipping on orders over Rs. 100,000
                     </div>
                  </div>

                  {/* Purchase Controls */}
                  <div className="flex flex-col gap-4 mt-1 pt-0.5 w-full sm:w-[400px] h-[140px]">
                    <div className="flex items-center gap-4">
                       <div className="flex items-center bg-gray-50 border border-gray-100 rounded-2xl p-2 w-32">
                         <button 
                           onClick={() => setQuantity(Math.max(1, quantity - 1))}
                           className="w-10 h-10 flex items-center justify-center text-gray-400 hover:text-[#1A2B4C] transition-colors bg-white rounded-xl shadow-sm"
                         >
                           <Minus size={16} />
                         </button>
                         <span className="flex-1 text-center font-black text-lg">{quantity}</span>
                         <button 
                           onClick={() => setQuantity(quantity + 1)}
                           className="w-10 h-10 flex items-center justify-center text-gray-400 hover:text-[#1A2B4C] transition-colors bg-white rounded-xl shadow-sm"
                         >
                           <Plus size={16} />
                         </button>
                       </div>
                       
                       <button 
                         onClick={handleAddToCart}
                         disabled={product.stockQuantity <= 0}
                         className="flex-1 bg-[#1A2B4C] text-white h-[60px] rounded-2xl font-black text-xs uppercase tracking-widest hover:bg-[#00B4D8] transition-all shadow-xl shadow-[#1A2B4C]/20 flex items-center justify-center gap-3 active:scale-95 disabled:opacity-50 disabled:cursor-not-allowed"
                       >
                         <ShoppingCart size={18} /> Add to Cart
                       </button>
                    </div>
                    
                    <button className="w-full bg-[#00B4D8] text-white h-[60px] rounded-2xl font-black text-xs uppercase tracking-widest hover:bg-[#0096B4] transition-all shadow-xl shadow-[#00B4D8]/20 flex items-center justify-center gap-3 active:scale-95 mt-2">
                       <Zap size={18} /> Buy Now with 1-Click
                    </button>
                  </div>
                </div>

                {/* Assurance Badges */}
                <div className="grid grid-cols-2 gap-4">
                   {[
                     { label: 'Authorized Dealer', desc: '100% Genuine', icon: Award },
                     { label: 'Secure Logistics', desc: 'Fully Insured', icon: Truck },
                     { label: 'Enterprise Support', desc: '24/7 Access', icon: ShieldCheck },
                     { label: 'RMA Management', desc: 'Hassle-Free', icon: RefreshCw }
                   ].map((item, idx) => (
                     <div key={idx} className="flex items-center gap-3 p-4 bg-white rounded-2xl border border-gray-100 shadow-sm hover:shadow-md transition-shadow">
                        <div className="w-10 h-10 rounded-xl bg-gray-50 flex items-center justify-center shrink-0 text-[#1A2B4C]">
                           <item.icon size={18} />
                        </div>
                        <div className="flex flex-col">
                           <span className="text-xs font-black text-[#1A2B4C]">{item.label}</span>
                           <span className="text-[9px] font-bold uppercase tracking-widest text-gray-400">{item.desc}</span>
                        </div>
                     </div>
                   ))}
                </div>
              </motion.div>
            </div>
          </div>
        </div>

        {/* Related Products */}
        {relatedProducts.length > 0 && (
          <div className="mt-16 pt-16 border-t border-gray-100">
            <h2 className="text-3xl font-black text-[#1A2B4C] mb-8 tracking-tight">Relevant Products</h2>
            <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
              {relatedProducts.map(rp => (
                <Link key={rp.id} to={`/product/${rp.id}`} className="group bg-white rounded-3xl p-6 border border-gray-100 shadow-sm hover:shadow-xl hover:border-[#00B4D8]/30 transition-all">
                  <div className="aspect-square bg-gray-50 rounded-2xl overflow-hidden mb-6 relative">
                    <img loading="lazy" src={rp.images?.[0] || 'https://placehold.co/600x600?text=No+Image'} alt={rp.productName} className="w-full h-full object-contain p-4 group-hover:scale-110 transition-transform duration-500" />
                  </div>
                  <h3 className="font-black text-lg text-[#1A2B4C] group-hover:text-[#00B4D8] transition-colors mb-2 line-clamp-2 leading-tight">{rp.productName}</h3>
                  <div className="flex items-center justify-between mt-4">
                    <span className="font-black text-lg">Rs. {(rp.salePrice ?? 0).toLocaleString()}</span>
                  </div>
                </Link>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
"""

with open('src/pages/ProductDetails.tsx', 'w') as f:
    f.write(top_part)
    f.write(new_return)
