"""Builds every page of rumstar.eu into the repo root. Run: python3 src/build.py"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shell import SITE
from pages_a import home, services
from pages_b import how, industries, guide
from pages_c import about, faq, contact
from pages_d import privacy, terms, cookies, thank_you, not_found

OUT = os.environ.get('OUT', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..') + '/')
LASTMOD = "2026-10-12"

# (file, html, in sitemap, priority)
pages = [
    ('index.html', home(), True, '1.0'),
    ('services.html', services(), True, '0.9'),
    ('industries.html', industries(), True, '0.8'),
    ('how-we-work.html', how(), True, '0.8'),
    ('guide.html', guide(), True, '0.8'),
    ('about.html', about(), True, '0.7'),
    ('faq.html', faq(), True, '0.6'),
    ('contact.html', contact(), True, '0.8'),
    ('privacy.html', privacy(), True, '0.3'),
    ('terms.html', terms(), True, '0.3'),
    ('cookies.html', cookies(), True, '0.3'),
    ('thank-you.html', thank_you(), False, None),
    ('404.html', not_found(), False, None),
]

BANNED = r'—|\bseamless|\belevate|\bunlock|\bempower|\bleverag|cutting edge|next generation|holistic|synergy|\bsolutions?\b|\btransform|\bjourney|\becosystem|\brobust|\binnovative'
titles = {}
for name, html, _, _ in pages:
    hits = re.findall(BANNED, re.sub(r'<[^>]+>', ' ', html), re.I)
    if hits:
        print(f'{name}: banned words {set(hits)}')
    title = re.search(r'<title>(.*?)</title>', html).group(1)
    if title in titles:
        print(f'{name}: duplicate title with {titles[title]}')
    titles[title] = name
    with open(OUT + name, 'w') as f:
        f.write(html)
    print(f'wrote {name} ({len(html)} bytes, {html.count("class=\"ph\"")} placeholders)')

urls = "\n".join(
    f'  <url><loc>{SITE}/{"" if n == "index.html" else n}</loc><lastmod>{LASTMOD}</lastmod><priority>{p}</priority></url>'
    for n, _, inc, p in pages if inc)
with open(OUT + 'sitemap.xml', 'w') as f:
    f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')
with open(OUT + 'robots.txt', 'w') as f:
    f.write(f'User-agent: *\nAllow: /\nDisallow: /src/\n\nSitemap: {SITE}/sitemap.xml\n')
with open(OUT + 'site.webmanifest', 'w') as f:
    json.dump({
        "name": "Rumstar", "short_name": "Rumstar",
        "description": "Independent payment consultancy, Nicosia.",
        "start_url": "/", "display": "browser",
        "background_color": "#f3f4f7", "theme_color": "#070912",
        "icons": [
            {"src": "/assets/icons/icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "/assets/icons/icon-512.png", "sizes": "512x512", "type": "image/png"},
            {"src": "/assets/icons/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
        ],
    }, f, indent=2)
print('wrote sitemap.xml, robots.txt, site.webmanifest')
