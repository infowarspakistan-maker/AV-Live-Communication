import sys

with open('src/pages/Category.tsx', 'r') as f:
    content = f.read()

import_structured_data = "import { StructuredData } from '../components/StructuredData';\n"
if "import { StructuredData }" not in content:
    content = content.replace("import { SEO } from '../components/SEO';", "import { SEO } from '../components/SEO';\n" + import_structured_data)

# Let's insert the StructuredData block inside the main return
seo_block = """      <SEO 
        title={`${currentCategory.name} | AV Live Pakistan`} 
        description={currentCategory.description || `Browse our selection of ${currentCategory.name}.`} 
      />"""

structured_data_block = """      <StructuredData 
        data={{
          "@context": "https://schema.org/",
          "@type": "CollectionPage",
          "name": currentCategory.name,
          "description": currentCategory.description,
          "url": `https://avlive.com.pk/category/${currentCategory.slug}`,
          "mainEntity": {
            "@type": "ItemList",
            "itemListElement": categoryProducts.map((p, idx) => ({
              "@type": "ListItem",
              "position": idx + 1,
              "url": `https://avlive.com.pk/product/${p.id}`
            }))
          }
        }}
      />"""

if "<StructuredData" not in content:
    content = content.replace(seo_block, seo_block + "\n" + structured_data_block)

with open('src/pages/Category.tsx', 'w') as f:
    f.write(content)
print("Category patched")
