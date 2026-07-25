import sys

with open('src/pages/ProductDetails.tsx', 'r') as f:
    content = f.read()

old_schema = """          "offers": {
            "@type": "Offer",
            "url": `https://avlive.com.pk/product/${product.id}`,
            "priceCurrency": "PKR",
            "price": product.salePrice || product.regularPrice,
            "availability": product.stockQuantity && product.stockQuantity > 0 ? "https://schema.org/InStock" : "https://schema.org/OutOfStock"
          }"""

new_schema = """          "offers": {
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
          }"""

content = content.replace(old_schema, new_schema)

with open('src/pages/ProductDetails.tsx', 'w') as f:
    f.write(content)
print("Schema patched")
