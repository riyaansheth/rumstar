"""Legal pages, thank-you page and 404."""
from shell import page, hero, ph

UPDATED = "12 October 2026"


def legal(file, kicker, title, lede, sections, description):
    toc = "\n".join(f'        <li><a href="#{i}">{h}</a></li>' for i, h, _ in sections)
    body_secs = "\n".join(f'''      <section class="g-sec" id="{i}">
        <h2>{h}</h2>
{c}
      </section>''' for i, h, c in sections)
    body = hero(kicker, title, lede, show_cta=False) + f'''
  <section class="doc wrap">
    <aside class="toc" aria-label="Contents">
      <p>Contents</p>
      <ol>
{toc}
      </ol>
    </aside>
    <div class="doc-body prose legal-body">
      <p class="legal-meta">Last updated {UPDATED}. {ph("Draft: to be reviewed by Rumstar's legal adviser before it is relied on")}</p>
{body_secs}
    </div>
  </section>'''
    return page(file, {"Privacy Policy": "Privacy Policy | Rumstar Limited", "Terms of Use": "Website Terms of Use | Rumstar Limited", "Cookie Policy": "Cookie Policy | Rumstar Limited"}[kicker], description, body, "legal-page")


CONTROLLER = '''<p>RUMSTAR LIMITED, a company registered in the Republic of Cyprus under registration number HE 498715, with its registered office at 84 Larnakos, Pallouriotissa, 1046 Nicosia, Cyprus.</p>
        <p>Email: <a href="mailto:support@rumstar.eu">support@rumstar.eu</a>. Telephone: <a href="tel:+35797692104">+357 97 692104</a>.</p>'''


def privacy():
    secs = [
        ("who", "Who we are", f'''        <p>This policy explains how Rumstar collects and uses personal data when you visit rumstar.eu or contact us. Rumstar is the controller of that data.</p>
        {CONTROLLER}'''),
        ("collect", "What we collect", '''        <p><b>When you contact us.</b> If you email us, call us or use the enquiry form, we receive the details you choose to give: typically your name, work email, company, phone number, website and information about how your business takes payments. The enquiry form does not send anything to our servers. It opens your own email application with your answers filled in, and nothing is sent until you press send.</p>
        <p><b>When you become a client.</b> To do our work we may receive processing statements, contracts and related business documents. These are covered by our engagement terms and used only for that engagement.</p>
        <p><b>When you visit the website.</b> Like any website, the server that delivers our pages receives technical information such as your IP address and browser type in order to send the page to you. We also use privacy-friendly analytics that count visits without cookies and without identifying you. See the analytics section below.</p>'''),
        ("use", "How and why we use it", '''        <ul class="dashes">
          <li>To reply to your enquiry and arrange a conversation. Legal basis: our legitimate interest in responding to people who contact us, or steps you ask us to take before entering into a contract.</li>
          <li>To provide our services to clients. Legal basis: performance of a contract.</li>
          <li>To understand, in aggregate, how the website is used so we can improve it. Legal basis: our legitimate interest in running a useful website.</li>
          <li>To meet legal, tax and accounting obligations. Legal basis: legal obligation.</li>
        </ul>
        <p>We do not sell personal data, use it for advertising or make automated decisions about you.</p>'''),
        ("analytics", "Analytics", '''        <p>We use Cloudflare Web Analytics to see which pages are visited and how often. It does not use cookies, does not store anything on your device and does not build a profile of you. It is provided by Cloudflare, Inc.</p>'''),
        ("share", "Who we share it with", '''        <p>We use a small number of service providers who process data on our behalf:</p>
        <ul class="dashes">
          <li>Google, for business email (Google Workspace).</li>
          <li>Our website hosting providers, to deliver the website.</li>
          <li>Cloudflare, for domain name services and website analytics.</li>
        </ul>
        <p>We share client information with payment providers only when you ask us to, for example during a tender or negotiation on your behalf. We may also disclose data where the law requires it.</p>'''),
        ("transfers", "International transfers", '''        <p>Some of our providers may process data outside the European Economic Area. Where that happens, we rely on appropriate safeguards such as the European Commission's standard contractual clauses or an adequacy decision.</p>'''),
        ("retention", "How long we keep it", f'''        <p>We keep enquiry correspondence for {ph("retention period")} and client records for as long as required by Cypriot tax and company law. We then delete or anonymise them.</p>'''),
        ("rights", "Your rights", '''        <p>Under the General Data Protection Regulation you have the right to access your personal data, to have it corrected or erased, to restrict or object to its processing, and to data portability. Where we rely on consent, you can withdraw it at any time.</p>
        <p>To exercise any of these rights, email <a href="mailto:support@rumstar.eu">support@rumstar.eu</a>. You also have the right to complain to the Office of the Commissioner for Personal Data Protection in Cyprus.</p>'''),
        ("cookies", "Cookies", '''        <p>We do not use tracking or advertising cookies. See our <a href="cookies.html">Cookie Policy</a> for the small amount of information the site stores on your device.</p>'''),
        ("changes", "Changes to this policy", '''        <p>We may update this policy from time to time. The date at the top shows when it last changed.</p>'''),
    ]
    return legal("privacy.html", "Privacy Policy", "How we handle your personal data.",
                 "What we collect when you visit rumstar.eu or contact us, why, and the rights you have over it.", secs,
                 "How Rumstar Limited collects, uses and protects personal data, and your rights under the GDPR.")


def terms():
    secs = [
        ("about", "About these terms", f'''        <p>These terms govern your use of rumstar.eu. By using the website you accept them. They do not govern our advisory services, which are provided under separate written engagement terms.</p>
        {CONTROLLER}'''),
        ("information", "Information, not advice", '''        <p>The content of this website, including our payments guide, is general information about payments in the European Union. It is not legal, financial or regulatory advice and it is not tailored to your circumstances. Rules change, and how they apply depends on your business. Do not rely on the website as a substitute for advice on your own situation.</p>'''),
        ("status", "Our regulatory status", '''        <p>Rumstar provides advisory services only. It is not a payment institution or e-money institution, does not process payments and does not hold client funds. Payment services are provided by licensed providers under their own contracts with you.</p>'''),
        ("examples", "Examples and illustrations", '''        <p>Some pages contain illustrations, such as example payment flows or fee breakdowns. They are for explanation only, are not quotes or offers and do not represent the results of any particular client.</p>'''),
        ("ip", "Intellectual property", '''        <p>The text, design and graphics on this website belong to Rumstar or its licensors. You may view and print pages for your own reference. You may not copy, republish or use them commercially without our written permission.</p>'''),
        ("links", "Links to other websites", '''        <p>We may link to websites we do not control, such as regulators' registers. We are not responsible for their content or availability.</p>'''),
        ("liability", "Liability", '''        <p>We take care to keep the website accurate and available, but we do not guarantee that it is complete, current or free of errors. To the extent permitted by law, we are not liable for any loss arising from use of, or reliance on, the website. Nothing in these terms limits liability that cannot be limited by law.</p>'''),
        ("law", "Governing law", f'''        <p>These terms are governed by the laws of {ph("governing law, for example the Republic of Cyprus")}, and the courts of {ph("jurisdiction")} have jurisdiction over any dispute.</p>'''),
        ("contact", "Contact", '''        <p>Questions about these terms can be sent to <a href="mailto:support@rumstar.eu">support@rumstar.eu</a>.</p>'''),
    ]
    return legal("terms.html", "Terms of Use", "The terms for using this website.",
                 "The rules for using rumstar.eu. Our advisory work is covered separately by written engagement terms.", secs,
                 "Terms of use for the rumstar.eu website, operated by Rumstar Limited, Nicosia, Cyprus.")


def cookies():
    secs = [
        ("summary", "In short", '''        <p>rumstar.eu does not use tracking cookies, advertising cookies or third party cookies. It stores two small preferences on your device, and counts visits with analytics that do not use cookies.</p>'''),
        ("stored", "What we store on your device", '''        <div class="tbl"><table>
          <thead><tr><th>Name</th><th>Type</th><th>Purpose</th><th>Kept until</th></tr></thead>
          <tbody>
            <tr><td>theme</td><td>Local storage</td><td>Remembers whether you chose light or dark mode.</td><td>You clear your browser data</td></tr>
            <tr><td>cookie-notice</td><td>Local storage</td><td>Remembers that you have seen the cookie notice, so it is not shown again.</td><td>You clear your browser data</td></tr>
          </tbody>
        </table></div>
        <p>Both are set only by your own actions, are never sent to us and are used only to make the site work the way you asked.</p>'''),
        ("analytics", "Analytics without cookies", '''        <p>We use Cloudflare Web Analytics to count page views. It does not set cookies, does not use local storage and does not track you across websites.</p>'''),
        ("fonts", "Fonts and third parties", '''        <p>Our fonts are served from our own server, so loading a page does not send your details to a font provider.</p>'''),
        ("control", "Your choices", '''        <p>You can clear stored preferences at any time through your browser settings. The site works fully without them. You can see the cookie notice again with the link in the footer.</p>'''),
        ("contact", "Questions", '''        <p>Email <a href="mailto:support@rumstar.eu">support@rumstar.eu</a>. For how we handle personal data generally, see our <a href="privacy.html">Privacy Policy</a>.</p>'''),
    ]
    return legal("cookies.html", "Cookie Policy", "No tracking cookies. Here is what we do store.",
                 "A short, complete list of what this website stores on your device and why.", secs,
                 "Rumstar's cookie policy: no tracking cookies, two local preferences and cookieless analytics.")


def thank_you():
    body = hero("Thank you", "Your enquiry is ready to send.",
                "Your email application should have opened with your answers filled in, addressed to onboarding@rumstar.eu. Press send and it is on its way.",
                show_cta=False) + f'''
  <section class="wrap thanks">
    <div class="thanks-grid">
      <div class="facts-card">
        <h2>What happens next</h2>
        <ol class="mini-steps">
          <li>We reply within {ph("response time")} to arrange a call.</li>
          <li>A free 15 minute call about how you take payments today.</li>
          <li>If a review is worthwhile, we tell you what we need and quote in writing.</li>
        </ol>
      </div>
      <div class="facts-card">
        <h2>Nothing opened?</h2>
        <p>Some browsers block email links. Write to us directly and include a few lines about your business.</p>
        <div class="actions">
          <a class="btn" href="mailto:onboarding@rumstar.eu?subject=Enquiry">Email onboarding@rumstar.eu</a>
          <a class="link" href="tel:+35797692104">Or call +357 97 692104</a>
        </div>
      </div>
      <div class="facts-card">
        <h2>While you wait</h2>
        <p>Gather your recent processing statements and current contract. They make the first call far more useful.</p>
        <p><a class="link" href="how-we-work.html#checklist">See what we need</a> &nbsp; <a class="link" href="guide.html">Read the payments guide</a></p>
      </div>
    </div>
  </section>'''
    return page("thank-you.html", "Thank you | Rumstar", "Your enquiry to Rumstar is ready to send.", body,
                "thanks-page", noindex=True, mobile_cta=False)


def not_found():
    body = hero("Error 404", "This page is not here.",
                "The address may be mistyped, or the page may have moved. These are good places to start.",
                show_cta=False) + '''
  <section class="wrap">
    <ul class="sector-strip">
      <li><a href="/"><b>Home</b><span>What Rumstar does, in two minutes</span></a></li>
      <li><a href="/services.html"><b>Expertise</b><span>Statement reviews, providers, approval rates and more</span></a></li>
      <li><a href="/guide.html"><b>Insights</b><span>How payment fees and rules actually work</span></a></li>
      <li><a href="/how-we-work.html"><b>Our Approach</b><span>From first call to signed contract</span></a></li>
      <li><a href="/faq.html"><b>FAQ</b><span>Questions, answered plainly</span></a></li>
      <li><a href="/contact.html"><b>Let&rsquo;s talk</b><span>Book a free 15 minute call</span></a></li>
    </ul>
  </section>'''
    return page("404.html", "Page not found | Rumstar", "This page could not be found.", body, "notfound-page", noindex=True)
