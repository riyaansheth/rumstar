"""Shared page shell for every page on rumstar.eu."""
import json
from html import escape

SITE = "https://rumstar.eu"
STAR = '<path d="M16 1 C17.5 11 21 14.5 31 16 C21 17.5 17.5 21 16 31 C14.5 21 11 17.5 1 16 C11 14.5 14.5 11 16 1Z"/>'

# Cloudflare Web Analytics site token (cookieless). Leave empty to load no analytics at all.
# Before setting it, update the Privacy and Cookie notices in pages_d.py: they currently state that no analytics runs.
ANALYTICS_TOKEN = ""

NAV = [
    ("/", "Home"),
    ("/services.html", "Expertise"),
    ("/industries.html", "Industries"),
    ("/how-we-work.html", "Our Approach"),
    ("/guide.html", "Insights"),
    ("/about.html", "About"),
]

ORG = {
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    "name": "Rumstar",
    "legalName": "RUMSTAR LIMITED",
    "url": SITE + "/",
    "logo": SITE + "/assets/icons/icon-512.png",
    "image": SITE + "/assets/og-image.png",
    "description": "Independent payment consultancy advising businesses on payment costs, providers, approval rates and compliance.",
    "email": "onboarding@rumstar.eu",
    "telephone": "+357 97 692104",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "84 Larnakos, Pallouriotissa",
        "addressLocality": "Nicosia",
        "postalCode": "1046",
        "addressCountry": "CY",
    },
}


def ph(text):
    """Visible placeholder for figures and facts Rumstar still has to supply."""
    return f'<span class="ph" title="Placeholder: to be confirmed by Rumstar">[{text}]</span>'


def page(file, title, description, body, body_class="", noindex=False, mobile_cta=True):
    nav = "\n".join(f'    <a href="{href}">{label}</a>' for href, label in NAV)
    explore = "\n".join(f'        <li><a href="{href}">{label}</a></li>' for href, label in NAV[1:])
    url = SITE + "/" + ("" if file == "index.html" else file)
    robots = '\n<meta name="robots" content="noindex, follow">' if noindex else ""
    schema = f'\n<script type="application/ld+json">{json.dumps(ORG)}</script>' if file == "index.html" else ""
    analytics = (f'\n<script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon=\'{{"token": "{ANALYTICS_TOKEN}"}}\'></script>'
                 if ANALYTICS_TOKEN else "")
    mcta = ('\n<a href="/contact.html" class="mcta">Book a free 15 minute call'
            '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M4 10h11M11 5l5 5-5 5"/></svg></a>') if mobile_cta else ""
    t, d = escape(title), escape(description)
    return f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{t}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{url}">{robots}
<meta property="og:type" content="website">
<meta property="og:site_name" content="Rumstar">
<meta property="og:locale" content="en_GB">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Rumstar, independent payment consultancy. Pay less. Get paid more.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{t}">
<meta name="twitter:description" content="{d}">
<meta name="twitter:image" content="{SITE}/assets/og-image.png">
<meta name="theme-color" content="#f3f4f7" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#070912" media="(prefers-color-scheme: dark)">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/assets/icons/icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/icons/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/assets/fonts/funnel-display.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/funnel-sans.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/style.css">
<script>try {{ if (localStorage.getItem('theme') === 'dark') document.documentElement.dataset.theme = 'dark'; }} catch (e) {{}}</script>{schema}
</head>
<body class="{body_class}">

<a class="skip" href="#main">Skip to content</a>
<header class="top wrap">
  <a href="/" class="brand" aria-label="Rumstar home">
    <svg class="brand-star" viewBox="0 0 32 32" aria-hidden="true">{STAR}</svg>
    Rumstar
  </a>
  <nav id="site-nav" aria-label="Main">
{nav}
    <a href="/contact.html" class="nav-cta">Let&rsquo;s talk</a>
  </nav>
  <div class="top-right">
    <button type="button" class="theme" aria-label="Switch to dark mode">
      <svg class="sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4.5"/><path d="M12 2v2.5M12 19.5V22M2 12h2.5M19.5 12H22M4.9 4.9l1.8 1.8M17.3 17.3l1.8 1.8M4.9 19.1l1.8-1.8M17.3 6.7l1.8-1.8"/></svg>
      <svg class="moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5Z"/></svg>
    </button>
    <a href="/contact.html" class="pill">Let&rsquo;s talk</a>
    <button type="button" class="menu-btn" aria-controls="site-nav" aria-expanded="false"><span></span><span></span><span class="sr">Menu</span></button>
  </div>
</header>

<main id="main">
{body}
</main>

<footer class="foot">
 <div class="wrap">
  <div class="foot-grid">
    <div>
      <a href="/" class="brand" aria-label="Rumstar home">
        <svg class="brand-star" viewBox="0 0 32 32" aria-hidden="true">{STAR}</svg>
        Rumstar
      </a>
      <p class="foot-line">Independent payment consultancy.</p>
      <p class="foot-legal">Rumstar provides advisory services only. It is not a payment institution or e-money institution, does not process payments and does not hold client funds.</p>
    </div>
    <nav class="foot-explore" aria-label="Site">
      <ul>
{explore}
        <li><a href="/faq.html">FAQ</a></li>
        <li><a href="/contact.html">Contact</a></li>
      </ul>
    </nav>
    <address>
      <b>RUMSTAR LIMITED</b>
      84 Larnakos, Pallouriotissa<br>
      1046 Nicosia, Cyprus
    </address>
    <dl>
      <div><dt>Company Registration No.</dt><dd>HE 498715</dd></div>
      <div><dt>Registered in</dt><dd>Republic of Cyprus</dd></div>
      <div><dt>Tel</dt><dd><a href="tel:+35797692104">+357 97 692104</a></dd></div>
      <div><dt>Email</dt><dd><a href="mailto:support@rumstar.eu">support@rumstar.eu</a></dd></div>
    </dl>
  </div>
  <div class="foot-bottom">
    <span>&copy; 2026 RUMSTAR LIMITED. All rights reserved.</span>
    <nav aria-label="Legal">
      <a href="/privacy.html">Privacy Notice</a>
      <a href="/terms.html">Terms &amp; Conditions</a>
      <a href="/cookies.html">Cookies &amp; Storage</a>
      <a href="/complaints.html">Complaints</a>
      <button type="button" class="cookie-reopen">Cookie notice</button>
    </nav>
  </div>
 </div>
 <div class="foot-mark" aria-hidden="true">Rumstar</div>
</footer>
{mcta}
<div class="cookie-note" role="region" aria-label="Cookie notice" hidden>
  <p><b>No cookies, no tracking.</b> We only remember your light or dark mode choice, and that you have seen this notice, in your own browser. <a href="/cookies.html">Cookies &amp; storage</a></p>
  <button type="button" class="cookie-ok">OK</button>
</div>

<script src="/script.js"></script>{analytics}
</body>
</html>
'''


def hero(kicker, title, lede, extra="", show_cta=True):
    actions = '''    <div class="actions hero-actions">
      <a href="/contact.html" class="btn">Book a free 15 minute call</a>
      <a href="tel:+35797692104" class="link">Or call +357 97 692104</a>
    </div>
''' if show_cta else ""
    return f'''  <section class="page-hero wrap">
    <svg class="page-star" viewBox="0 0 32 32" aria-hidden="true">{STAR}</svg>
    <p class="kicker">{kicker}</p>
    <h1 class="page-title">{title}</h1>
    <p class="lede">{lede}</p>
{actions}{extra}  </section>
'''


def cta(title="Send us a statement. We will tell you what we see.", text="A free 15 minute call is usually enough to know whether it is worth going further."):
    return f'''  <section class="cta-wrap wrap">
    <div class="cta">
      <svg class="cta-star" viewBox="0 0 32 32" aria-hidden="true">{STAR}</svg>
      <h2>{title}</h2>
      <p>{text}</p>
      <div class="actions">
        <a href="/contact.html" class="btn">Book a free 15 minute call</a>
        <a href="mailto:onboarding@rumstar.eu" class="link">onboarding@rumstar.eu</a>
      </div>
    </div>
  </section>
'''
