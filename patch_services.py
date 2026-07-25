import sys

with open('src/pages/Services.tsx', 'r') as f:
    content = f.read()

content = content.replace(
    'title="Event Management & AV Rental Services | AV Live Pakistan"',
    'title="Hybrid Event Production & Management Pakistan | AV Live"'
)

content = content.replace(
    'description="Book professional AV teams for corporate summits, hybrid events, or e-Sports tournaments. SMD screens, PA systems, and multi-camera live streaming."',
    'description="Comprehensive corporate and hybrid event management in Pakistan. We connect live audiences with virtual attendees across Lahore, Karachi, and Islamabad."'
)

with open('src/pages/Services.tsx', 'w') as f:
    f.write(content)
print("Services patched")
