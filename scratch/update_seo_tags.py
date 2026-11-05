with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace favicon tag
old_fav = '<link rel="icon" type="image/webp" href="profile.webp">'
new_fav = '''    <!-- Favicon & Touch Icons for Google Search & Browsers -->
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png">
    <link rel="icon" type="image/png" sizes="96x96" href="/favicon-96x96.png">
    <link rel="icon" type="image/png" sizes="192x192" href="/favicon-192x192.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">'''

if old_fav in content:
    content = content.replace(old_fav, new_fav)
    print("Replaced favicon tag")
else:
    print("Favicon tag not found!")

# 2. Add og:site_name
old_og = '<meta property="og:image" content="https://tarun-mankar.web.app/profile.webp">'
new_og = '''<meta property="og:image" content="https://tarun-mankar.web.app/profile.webp">
    <meta property="og:site_name" content="Tarun Mankar">'''

if old_og in content:
    content = content.replace(old_og, new_og)
    print("Added og:site_name")
else:
    print("og:image tag not found!")

# 3. Update WebSite schema
old_schema = '''    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "WebSite",
      "name": "Tarun Mankar — Freelancer | Web & Mobile App Developer | AI Content Creator",
      "url": "https://tarun-mankar.web.app/"
    }
    </script>'''

new_schema = '''    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "WebSite",
      "name": "Tarun Mankar",
      "alternateName": ["Tarun Mankar Portfolio", "tarunmankar", "Tarun Mankar Web"],
      "url": "https://tarun-mankar.web.app/"
    }
    </script>'''

if old_schema in content:
    content = content.replace(old_schema, new_schema)
    print("Updated WebSite schema")
else:
    print("WebSite schema not found directly, checking variations...")
    import re
    pattern = r'<script type="application/ld\+json">\s*\{\s*"@context":\s*"https://schema\.org",\s*"@type":\s*"WebSite"[\s\S]*?</script>'
    content = re.sub(pattern, new_schema.strip(), content)
    print("Replaced with regex")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done updating index.html")

