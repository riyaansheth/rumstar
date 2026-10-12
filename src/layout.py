"""Shared page shell: head, header, footer and small helpers."""
from html import escape

SITE = "https://rumstar.eu"
STAR = '<path d="M16 1 C17.5 11 21 14.5 31 16 C21 17.5 17.5 21 16 31 C14.5 21 11 17.5 1 16 C11 14.5 14.5 11 16 1Z"/>'
ARROW = '<svg class="arw" viewBox="0 0 20 20" aria-hidden="true"><path d="M4 10h11M11 5l5 5-5 5"/></svg>'

NAV = [
    ("/", "Home"),
    ("/expertise/", "Expertise"),
    ("/industries/", "Industries"),
    ("/approach/", "Our Approach"),
    ("/insights/", "Insights"),
    ("/about/", "About"),
]


def ph(text):
    """Visible placeholder for anything Rumstar still has to confirm."""
    return f'<span class="ph" title="Placeholder: to be confirmed by Rumstar">[{text}]</span>'


def section_label(num, text):
    return f'<p class="label"><span>{num}</span>{text}</p>'


def _nav_item(href, label, path):
    current = path == href or (href != "/" and path.startswith(href))
    return f'<a href="{href}"{" aria-current=\"page\"" if current else ""}>{label}</a>'


def page(path, title, description, body, body_class="", noindex=False):
    nav = "\n        ".join(_nav_item(h, l, path) for h, l in NAV)
    canonical = SITE + path
    robots = '\n<meta name="robots" content="noindex">' if noindex else ""
    return f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(description)}">
<link rel="canonical" href="{canonical}">{robots}
<meta property="og:type" content="website">
<meta property="og:site_name" content="Rumstar">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(description)}">
<meta property="og:url" content="{canonical}">
<meta name="theme-color" content="#F5F3EE">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/assets/fonts/instrument-serif.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/dm-sans.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/style.css">
<script>document.documentElement.classList.add('js')</script>
</head>
<body class="{body_class}">
<a class="skip" href="#main">Skip to content</a>

<header class="hdr">
  <div class="hdr-in">
    <a href="/" class="wordmark" aria-label="Rumstar, home">
      <svg viewBox="0 0 32 32" aria-hidden="true">{STAR}</svg><span>Rumstar</span>
    </a>
    <nav class="nav" id="nav" aria-label="Main">
        {nav}
        <a href="/contact/" class="nav-contact">Let&rsquo;s talk</a>
    </nav>
    <a href="/contact/" class="btn btn-sm hdr-cta">Let&rsquo;s talk</a>
    <button type="button" class="menu" aria-controls="nav" aria-expanded="false">
      <span class="menu-lines" aria-hidden="true"><i></i><i></i></span><span class="menu-word">Menu</span>
    </button>
  </div>
</header>

<main id="main">
{body}
</main>

<footer class="ftr">
  <div class="wrap">
    <div class="ftr-top">
      <p class="ftr-statement">Independent advice on payment costs, providers and performance.</p>
    </div>
    <div class="ftr-grid">
      <div class="ftr-col">
        <h2 class="ftr-h">Explore</h2>
        <ul>
          <li><a href="/expertise/">Expertise</a></li>
          <li><a href="/industries/">Industries</a></li>
          <li><a href="/approach/">Our Approach</a></li>
          <li><a href="/insights/">Insights</a></li>
          <li><a href="/about/">About</a></li>
          <li><a href="/faq/">Questions</a></li>
        </ul>
      </div>
      <div class="ftr-col">
        <h2 class="ftr-h">Contact</h2>
        <ul>
          <li><span>New enquiries</span><a href="mailto:onboarding@rumstar.eu">onboarding@rumstar.eu</a></li>
          <li><span>Existing clients</span><a href="mailto:support@rumstar.eu">support@rumstar.eu</a></li>
          <li><span>Telephone</span><a href="tel:+35797692104">+357 97 692104</a></li>
        </ul>
      </div>
      <div class="ftr-col">
        <h2 class="ftr-h">Company</h2>
        <address>
          RUMSTAR LIMITED<br>
          84 Larnakos, Pallouriotissa<br>
          1046 Nicosia, Cyprus
        </address>
        <p>Company registration no. HE&nbsp;498715<br>Registered in the Republic of Cyprus</p>
      </div>
      <div class="ftr-col ftr-notice">
        <h2 class="ftr-h">Regulatory notice</h2>
        <p>Rumstar provides advisory services only. It is not a payment institution or e-money institution, does not process payments and does not hold client funds.</p>
      </div>
    </div>
    <div class="ftr-base">
      <span>&copy; 2026 RUMSTAR LIMITED. All rights reserved.</span>
      <nav aria-label="Legal">
        <a href="/privacy/">Privacy</a>
        <a href="/terms/">Terms</a>
        <a href="/cookies/">Cookies</a>
      </nav>
    </div>
  </div>
  <p class="ftr-mark" aria-hidden="true">Rumstar</p>
</footer>

<script src="/assets/site.js" defer></script>
</body>
</html>
'''


def page_head(kicker, title, lead, aside=""):
    """Editorial header used at the top of inner pages."""
    return f'''<section class="phead wrap">
  <p class="crumb">{kicker}</p>
  <h1 class="phead-title reveal">{title}</h1>
  <div class="phead-foot">
    <p class="lead reveal">{lead}</p>
    {aside}
  </div>
</section>'''


def closing(title="Find out what your payments are really costing you.",
            text="Send us a recent statement. We will tell you plainly whether there is anything worth changing."):
    return f'''<section class="closing">
  <div class="wrap closing-in">
    <h2 class="closing-title reveal">{title}</h2>
    <div class="closing-side">
      <p>{text}</p>
      <a href="/contact/" class="btn btn-paper">Start a conversation {ARROW}</a>
      <p class="closing-direct">Or write to <a href="mailto:onboarding@rumstar.eu">onboarding@rumstar.eu</a></p>
    </div>
  </div>
</section>'''


def redirect(target):
    return f'''<!doctype html>
<html lang="en-GB"><head><meta charset="utf-8">
<title>Moved</title>
<link rel="canonical" href="{SITE}{target}">
<meta name="robots" content="noindex">
<meta http-equiv="refresh" content="0; url={target}">
</head><body><p>This page has moved to <a href="{target}">{SITE}{target}</a>.</p></body></html>
'''
