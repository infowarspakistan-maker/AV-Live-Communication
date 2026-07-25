import sys

with open('src/pages/Home.tsx', 'r') as f:
    content = f.read()

old_schema = """      <StructuredData 
        data={{
          "@context": "https://schema.org",
          "@type": "Organization",
          "name": "AV Live Communications",
          "url": "https://avlive.com.pk",
          "logo": "https://avlive.com.pk/logo.png",
          "description": "Pakistan's leading provider of professional AV solutions, IP phones, and video conferencing.",
          "address": {
            "@type": "PostalAddress",
            "addressLocality": "Lahore",
            "addressCountry": "PK"
          }
        }}
      />"""

new_schema = """      <StructuredData 
        data={[
          {
            "@context": "https://schema.org",
            "@type": "LocalBusiness",
            "name": "AV Live Communications",
            "image": "https://avlive.com.pk/og-image.jpg",
            "@id": "https://avlive.com.pk",
            "url": "https://avlive.com.pk",
            "telephone": "+923214256263",
            "address": {
              "@type": "PostalAddress",
              "addressLocality": "Lahore",
              "addressCountry": "PK"
            },
            "areaServed": [
              {
                "@type": "City",
                "name": "Lahore"
              },
              {
                "@type": "City",
                "name": "Karachi"
              },
              {
                "@type": "City",
                "name": "Islamabad"
              }
            ],
            "description": "Pakistan's leading video conferencing & event management company — corporate, hybrid, and esports events in Lahore, Karachi & Islamabad.",
            "openingHoursSpecification": {
              "@type": "OpeningHoursSpecification",
              "dayOfWeek": [
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday"
              ],
              "opens": "09:00",
              "closes": "18:00"
            }
          },
          {
            "@context": "https://schema.org",
            "@type": "Service",
            "serviceType": "Video Conferencing Solutions Pakistan",
            "provider": {
              "@type": "LocalBusiness",
              "name": "AV Live Communications"
            },
            "areaServed": ["Lahore", "Karachi", "Islamabad"],
            "description": "Professional video conferencing hardware and setup for boardrooms and remote teams."
          },
          {
            "@context": "https://schema.org",
            "@type": "Service",
            "serviceType": "Hybrid Event Production Pakistan",
            "provider": {
              "@type": "LocalBusiness",
              "name": "AV Live Communications"
            },
            "areaServed": ["Lahore", "Karachi", "Islamabad"],
            "description": "Comprehensive corporate and hybrid event management, connecting live audiences with virtual attendees."
          },
          {
            "@context": "https://schema.org",
            "@type": "Service",
            "serviceType": "Esports Event Management Pakistan",
            "provider": {
              "@type": "LocalBusiness",
              "name": "AV Live Communications"
            },
            "areaServed": ["Lahore", "Karachi", "Islamabad"],
            "description": "Expert production, live streaming, and AV setup for large-scale competitive gaming and esports tournaments."
          }
        ]}
      />"""

content = content.replace(old_schema, new_schema)

with open('src/pages/Home.tsx', 'w') as f:
    f.write(content)
print("StructuredData patched")
