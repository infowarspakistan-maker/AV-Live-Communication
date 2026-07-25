import sys

with open('src/components/SEO.tsx', 'r') as f:
    content = f.read()

content = content.replace(
    "title = 'AV Live Communications | Video Conference & Event Management in Pakistan'",
    "title = 'AV Live Communications | Video Conference in Pakistan & Hybrid Events'"
)

content = content.replace(
    "description = 'AV Live Communications is Pakistan\\'s leading provider of professional video conference in Pakistan and expert event management in Pakistan. We serve Lahore, Karachi, and Islamabad. Contact us at 03214256263.'",
    "description = 'AV Live Communications specializes in Video Conference in Pakistan, Video conferencing in Pakistan, Hybrid Event management, and Esports Event expertise. Also providing AI Development and IT equipment. Contact us at 03214256263.'"
)

content = content.replace(
    "keywords = 'video conference in Pakistan, event management in Pakistan, AV solutions, IP phones, video conferencing, Pakistan AV, Lahore, Karachi, Islamabad, Polycom Pakistan, Cisco IP phones, Grandstream Pakistan'",
    "keywords = 'Video conference in Pakistan, Video conferencing in Pakistan, Hybrid Event management, Esports Event expert, AI Development, IT equipment'"
)

with open('src/components/SEO.tsx', 'w') as f:
    f.write(content)
