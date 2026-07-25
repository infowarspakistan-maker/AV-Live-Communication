import re

with open('index.html', 'r') as f:
    content = f.read()

head_additions = """    <title>AV Live Communications | Video Conference & Event Management in Pakistan</title>
    <meta name="description" content="Premium video conference in Pakistan and expert event management in Pakistan. Available in Lahore, Karachi, Islamabad. Call us at 03214256263 for professional AV solutions, IP phones, and corporate setups." />
    <meta name="keywords" content="video conference in Pakistan, event management in Pakistan, Poly, Cisco, IP phones, Lahore, Karachi, Islamabad, AV solutions" />
    <meta property="og:title" content="AV Live Communications | Video Conference & Event Management in Pakistan" />
    <meta property="og:description" content="Premium video conference in Pakistan and expert event management in Pakistan. Available in Lahore, Karachi, Islamabad. Call 03214256263." />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="https://avlive.com.pk/" />
"""

body_additions = """
    <!-- SEO Content for Crawlers -->
    <noscript>
      <div style="padding: 20px; font-family: sans-serif;">
        <h1>AV Live Communications: Video Conference in Pakistan & Event Management in Pakistan</h1>
        <p>Welcome to AV Live Communications, your premier partner for professional <strong>video conference in Pakistan</strong> and expert <strong>event management in Pakistan</strong>. We serve major cities including Lahore, Karachi, and Islamabad.</p>
        <p>Contact us today at <strong>03214256263</strong>.</p>
        <h2>Our Services</h2>
        <ul>
          <li>High-quality Video Conferencing Solutions (Poly, Cisco, Grandstream)</li>
          <li>Comprehensive Event Management in Pakistan</li>
          <li>Professional Audio Visual (AV) Systems</li>
          <li>Enterprise IP Phones and PBX</li>
        </ul>
        <h2>Why Choose Us?</h2>
        <p>With years of experience, AV Live Communications is dedicated to providing state-of-the-art communication technologies. Whether you need to set up a boardroom for seamless remote collaboration or plan a large-scale corporate event, we have the expertise to deliver flawless execution.</p>
      </div>
    </noscript>
"""

content = re.sub(r'<title>.*?</title>\s*<meta name="description" content=".*?" />', head_additions, content, flags=re.DOTALL)
content = content.replace('<body>', '<body>' + body_additions)

with open('index.html', 'w') as f:
    f.write(content)
