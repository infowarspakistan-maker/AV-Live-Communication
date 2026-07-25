import sys

with open('index.html', 'r') as f:
    content = f.read()

content = content.replace(
    '<title>AV Live Communications | Video Conference in Pakistan & Hybrid Events</title>',
    '<title>Video Conferencing & Event Management Pakistan | AV Live</title>'
)

content = content.replace(
    '<meta name="description" content="Pakistan\'s leading provider for Video Conference in Pakistan and Video conferencing in Pakistan. We are Hybrid Event management and Esports Event experts, also offering AI Development and IT equipment. Call us at 03214256263." />',
    '<meta name="description" content="Pakistan\'s leading video conferencing & event management company — corporate, hybrid, and esports events in Lahore, Karachi & Islamabad. Get a quote." />'
)

content = content.replace(
    '<meta property="og:title" content="AV Live Communications | Video Conference in Pakistan & Hybrid Events" />',
    '<meta property="og:title" content="Video Conferencing & Event Management Pakistan | AV Live" />'
)

content = content.replace(
    '<meta property="og:description" content="Pakistan\'s leading provider for Video Conference in Pakistan and Video conferencing in Pakistan. We are Hybrid Event management and Esports Event experts, also offering AI Development and IT equipment. Call us at 03214256263." />',
    '<meta property="og:description" content="Pakistan\'s leading video conferencing & event management company — corporate, hybrid, and esports events in Lahore, Karachi & Islamabad. Get a quote." />'
)

content = content.replace(
    '<meta name="keywords" content="Video conference in Pakistan, Video conferencing in Pakistan, Hybrid Event management, Esports Event expert, AI Development, IT equipment" />',
    '<meta name="keywords" content="Video conferencing solutions Pakistan, Corporate event management Lahore, Corporate event management Karachi, Corporate event management Islamabad, Hybrid event production Pakistan, Esports event management Pakistan" />'
)

with open('index.html', 'w') as f:
    f.write(content)

with open('src/components/SEO.tsx', 'r') as f:
    seo = f.read()

seo = seo.replace(
    "title = 'AV Live Communications | Video Conference in Pakistan & Hybrid Events'",
    "title = 'Video Conferencing & Event Management Pakistan | AV Live'"
)

seo = seo.replace(
    "description = 'AV Live Communications specializes in Video Conference in Pakistan, Video conferencing in Pakistan, Hybrid Event management, and Esports Event expertise. Also providing AI Development and IT equipment. Contact us at 03214256263.'",
    "description = 'Pakistan\\'s leading video conferencing & event management company — corporate, hybrid, and esports events in Lahore, Karachi & Islamabad. Get a quote.'"
)

seo = seo.replace(
    "keywords = 'Video conference in Pakistan, Video conferencing in Pakistan, Hybrid Event management, Esports Event expert, AI Development, IT equipment'",
    "keywords = 'Video conferencing solutions Pakistan, Corporate event management Lahore, Corporate event management Karachi, Corporate event management Islamabad, Hybrid event production Pakistan, Esports event management Pakistan'"
)

with open('src/components/SEO.tsx', 'w') as f:
    f.write(seo)

print("Meta patched")
