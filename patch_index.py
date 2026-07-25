import sys

with open('index.html', 'r') as f:
    content = f.read()

content = content.replace(
    '<title>AV Live Communications | Video Conference & Event Management in Pakistan</title>',
    '<title>AV Live Communications | Video Conference in Pakistan & Hybrid Events</title>'
)

content = content.replace(
    '<meta name="description" content="Premium video conference in Pakistan and expert event management in Pakistan. Available in Lahore, Karachi, Islamabad. Call us at 03214256263 for professional AV solutions, IP phones, and corporate setups." />',
    '<meta name="description" content="Pakistan\'s leading provider for Video Conference in Pakistan and Video conferencing in Pakistan. We are Hybrid Event management and Esports Event experts, also offering AI Development and IT equipment. Call us at 03214256263." />'
)

content = content.replace(
    '<meta name="keywords" content="video conference in Pakistan, event management in Pakistan, Poly, Cisco, IP phones, Lahore, Karachi, Islamabad, AV solutions" />',
    '<meta name="keywords" content="Video conference in Pakistan, Video conferencing in Pakistan, Hybrid Event management, Esports Event expert, AI Development, IT equipment" />'
)

content = content.replace(
    '<meta property="og:title" content="AV Live Communications | Video Conference & Event Management in Pakistan" />',
    '<meta property="og:title" content="AV Live Communications | Video Conference in Pakistan & Hybrid Events" />'
)

content = content.replace(
    '<meta property="og:description" content="Premium video conference in Pakistan and expert event management in Pakistan. Available in Lahore, Karachi, Islamabad. Call 03214256263." />',
    '<meta property="og:description" content="Pakistan\'s leading provider for Video Conference in Pakistan and Video conferencing in Pakistan. We are Hybrid Event management and Esports Event experts, also offering AI Development and IT equipment. Call us at 03214256263." />'
)

content = content.replace(
    '<h1>AV Live Communications: Video Conference in Pakistan & Event Management in Pakistan</h1>',
    '<h1>AV Live Communications: Video Conference in Pakistan & Hybrid Event Management</h1>'
)

content = content.replace(
    '<p>Welcome to AV Live Communications, your premier partner for professional <strong>video conference in Pakistan</strong> and expert <strong>event management in Pakistan</strong>. We serve major cities including Lahore, Karachi, and Islamabad.</p>',
    '<p>Welcome to AV Live Communications, your premier partner for professional <strong>video conferencing in Pakistan</strong>, <strong>Hybrid Event management</strong>, and <strong>Esports Event</strong> expertise. We serve major cities including Lahore, Karachi, and Islamabad.</p>'
)

content = content.replace(
    '<li>Comprehensive Event Management in Pakistan</li>\n          <li>Professional Audio Visual (AV) Systems</li>\n          <li>Enterprise IP Phones and PBX</li>',
    '<li>Hybrid Event Management & Esports Event Experts</li>\n          <li>AI Development Solutions</li>\n          <li>IT Equipment (Projectors, Screens, Computing)</li>'
)

with open('index.html', 'w') as f:
    f.write(content)
