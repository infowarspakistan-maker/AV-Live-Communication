import sys

with open('server.ts', 'r') as f:
    content = f.read()

sitemap_route = """
  // Sitemap generation endpoint
  app.get('/sitemap.xml', async (req, res) => {
    try {
      const baseUrl = 'https://avlive.com.pk';
      
      const staticRoutes = [
        '/',
        '/shop',
        '/services',
        '/contact',
        '/about',
        '/setup-wizard'
      ];

      // Fetch products
      const productsSnap = await db.collection('products').where('status', '==', 'active').get();
      const products = productsSnap.docs.map(doc => doc.id);

      // Fetch categories
      const categoriesSnap = await db.collection('categories').get();
      const categories = categoriesSnap.docs.map(doc => doc.id);

      let xml = `<?xml version="1.0" encoding="UTF-8"?>\\n`;
      xml += `<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\\n`;

      // Add static routes
      for (const route of staticRoutes) {
        xml += `  <url>\\n`;
        xml += `    <loc>${baseUrl}${route}</loc>\\n`;
        xml += `    <changefreq>weekly</changefreq>\\n`;
        xml += `    <priority>${route === '/' ? '1.0' : '0.8'}</priority>\\n`;
        xml += `  </url>\\n`;
      }

      // Add category routes
      for (const catId of categories) {
        xml += `  <url>\\n`;
        xml += `    <loc>${baseUrl}/category/${catId}</loc>\\n`;
        xml += `    <changefreq>weekly</changefreq>\\n`;
        xml += `    <priority>0.7</priority>\\n`;
        xml += `  </url>\\n`;
      }

      // Add product routes
      for (const productId of products) {
        xml += `  <url>\\n`;
        xml += `    <loc>${baseUrl}/product/${productId}</loc>\\n`;
        xml += `    <changefreq>daily</changefreq>\\n`;
        xml += `    <priority>0.9</priority>\\n`;
        xml += `  </url>\\n`;
      }

      xml += `</urlset>`;

      res.header('Content-Type', 'application/xml');
      res.send(xml);
    } catch (error) {
      console.error('Error generating sitemap:', error);
      res.status(500).end();
    }
  });

"""

content = content.replace(sitemap_route, "")

with open('server.ts', 'w') as f:
    f.write(content)
