import sys

with open('src/pages/ProductDetails.tsx', 'r') as f:
    content = f.read()

import_seo = "import { SEO } from '../components/SEO';"
new_import = "import { SEO } from '../components/SEO';\nimport { StructuredData } from '../components/StructuredData';"
if import_seo in content:
    content = content.replace(import_seo, new_import)

seo_block = """      <SEO 
        title={`${product.productName} | ${product.brand} | AV Live`}
        description={product.description?.replace(/<[^>]*>?/gm, '').substring(0, 160) || `Buy ${product.productName} by ${product.brand}. Expert AV hardware and collaboration tools.`}
        image={product.images?.[0]}
      />"""

structured_data = """      <SEO 
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
            "availability": product.stockQuantity && product.stockQuantity > 0 ? "https://schema.org/InStock" : "https://schema.org/OutOfStock"
          }
        }}
      />"""

if seo_block in content:
    content = content.replace(seo_block, structured_data)

with open('src/pages/ProductDetails.tsx', 'w') as f:
    f.write(content)
