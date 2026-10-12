"""Legal pages (from Rumstar's policy drafts of 9 October 2026), thank-you page and 404."""
from shell import page, hero, ph

# Bracketed instructions from the drafts are shown as visible placeholders until counsel approves them.
DRAFT_NOTE = (f"Effective date: {ph('approved date')}. "
              "Draft for review by Rumstar's Cyprus counsel. Not yet in effect.")

LEGAL_TITLES = {
    "privacy.html": "Privacy Notice | Rumstar Limited",
    "terms.html": "Website Terms and Conditions | Rumstar Limited",
    "cookies.html": "Cookie and Local Storage Notice | Rumstar Limited",
    "complaints.html": "Complaints and Concerns Policy | Rumstar Limited",
}


def legal(file, kicker, title, lede, sections, description):
    toc = "\n".join(f'        <li><a href="#{i}">{h}</a></li>' for i, h, _ in sections)
    body_secs = "\n".join(f"""      <section class="g-sec" id="{i}">
        <h2>{h}</h2>
{c}
      </section>""" for i, h, c in sections)
    body = hero(kicker, title, lede, show_cta=False) + f"""
  <section class="doc wrap">
    <aside class="toc" aria-label="Contents">
      <p>Contents</p>
      <ol>
{toc}
      </ol>
    </aside>
    <div class="doc-body prose legal-body">
      <p class="legal-meta">{DRAFT_NOTE}</p>
{body_secs}
    </div>
  </section>"""
    return page(file, LEGAL_TITLES[file], description, body, "legal-page")


def ul(items):
    return '        <ul class="dashes">\n' + "\n".join(f"          <li>{i}</li>" for i in items) + "\n        </ul>"


def terms():
    secs = [
        ("scope", "Who we are and scope", f"""        <p>rumstar.eu is operated by RUMSTAR LIMITED, registered in the Republic of Cyprus under number HE 498715, with registered office at 84 Larnakos, Pallouriotissa, 1046 Nicosia, Cyprus. Contact <a href="mailto:support@rumstar.eu">support@rumstar.eu</a> or <a href="tel:+35797692104">+357 97 692104</a>. {ph("Confirm operator and details; add VAT number if applicable")}</p>
        <p>These terms govern use of our website. They do not create a paid consultancy engagement, authorise us to act for you or permit us to enter provider contracts on your behalf. Paid work requires a separate written agreement accepted by you and Rumstar.</p>"""),
        ("services", "Our services and website information", f"""        <p>We describe independent business consultancy concerning payment costs, provider options, commercial negotiations and migration planning. This website is directed at businesses and people acting in a business capacity. {ph("Confirm business-to-business only scope")}</p>
        <p>Our consultancy is distinct from your payment provider's services. This website does not offer payment execution, custody of funds or access to your bank account. Legal, tax, investment and regulatory advice is outside its scope. Any engagement involving regulated activities requires separate assessment of its scope and applicable authorisation.</p>
        <p>Examples, fee breakdowns, estimates and timelines are general information, not an individual quotation or guarantee of savings, approvals, settlement, acceptance rates or availability. Results depend on your records, business, market conditions and provider decisions. A written proposal states its own assumptions, scope, fees and schedule. Check important information with us before relying on it for a business decision.</p>"""),
        ("documents", "Enquiries and safe document sharing", """        <p>An email, telephone enquiry or introductory call does not create paid work. Do not send CVVs, full card details, passwords, bank login credentials or unnecessary personal data. Ask for the agreed secure transfer method before supplying statements or contracts. Redact information not needed for review and ensure you are entitled to share it.</p>
        <p>Sending records does not authorise us to disclose them to providers, contact providers for you or make commitments for your business. That authority must be agreed separately.</p>"""),
        ("use", "Website use and ownership", """        <p>You may read and download material for lawful business evaluation. Unless a different licence is stated, Rumstar or its licensors own the website content. Do not sell, republish or present it as your own without permission, except where law permits. Third-party marks belong to their owners and do not imply partnership or endorsement.</p>
        <p>Do not introduce malicious code, seek unauthorised access, disrupt the site, impersonate others or harvest personal data. You may lawfully report security concerns to <a href="mailto:support@rumstar.eu">support@rumstar.eu</a> without sending sensitive client records.</p>"""),
        ("links", "Privacy, links and availability", """        <p>External sites have their own terms and privacy practices; a link is not a guarantee or endorsement. Our <a href="/privacy.html">Privacy Notice</a> explains data use and our <a href="/cookies.html">Cookie and Local Storage Notice</a> explains browser storage. Browsing is not consent to marketing or nonessential tracking.</p>
        <p>We may update or suspend website content for maintenance, security or business reasons. Continuous website availability is not guaranteed. Separately agreed client-service obligations remain governed by the engagement.</p>"""),
        ("law", "Responsibility, law and changes", f"""        <p>To the extent the law permits, we are not responsible for loss caused by treating general website information as personalised advice. Nothing excludes fraud, fraudulent misrepresentation or liability that cannot lawfully be excluded or limited. These terms do not set a consultancy engagement's liability cap.</p>
        <p>{ph("Governing law and courts for website disputes, to be selected with Cyprus counsel")} Mandatory rights and jurisdiction protections remain unaffected. Changes apply to subsequent website use from the stated date, not retrospectively to existing engagements. Questions may be sent to <a href="mailto:support@rumstar.eu">support@rumstar.eu</a>.</p>"""),
    ]
    return legal("terms.html", "Terms and Conditions", "The terms for using this website.",
                 "How rumstar.eu may be used. Paid consultancy work is always covered by a separate written agreement.", secs,
                 "Website terms and conditions for rumstar.eu, operated by Rumstar Limited, Nicosia, Cyprus.")


def privacy():
    secs = [
        ("controller", "Controller and contact", f"""        <p>RUMSTAR LIMITED, HE 498715, 84 Larnakos, Pallouriotissa, 1046 Nicosia, Cyprus, is the controller of personal data used to manage its website, business enquiries and own client relationships. Contact <a href="mailto:support@rumstar.eu">support@rumstar.eu</a> for privacy questions and rights requests. {ph("Confirm operator, monitored contact and any required DPO or representative details")}</p>
        <p>Where we process personal data in client records solely on the client's instructions, the client is the controller and our agreed data-processing terms govern our processor role. This notice does not replace that client's privacy information. Roles are assessed for each engagement.</p>"""),
        ("data", "Data and sources", f"""        <p>We may receive your name, business contact details, role, company and message when you contact us. An engagement may involve contracts, invoices, processing statements and correspondence containing information about staff, sole traders or customers. Limit and redact records before sharing them.</p>
        <p>The enquiry form on this website does not send anything to our servers. It opens your own email application with your answers filled in, and nothing reaches us until you press send.</p>
        <p>Your browser sends technical information to servers delivering the website. {ph("Confirm host and CDN log content, such as IP address, time, page and browser")} The site serves its fonts from its own server and can save an optional theme preference, and a record that you have seen the cookie notice, in your browser's local storage.</p>
        <p>Information comes directly from you and, where relevant, authorised colleagues or business contacts. {ph("Insert any other actual sources")} For indirectly obtained personal data, we provide the required information within the applicable GDPR timeframe unless a lawful exception applies.</p>"""),
        ("purposes", "Purposes and legal bases", f"""        <p><b>Business enquiries and relationships.</b> We use business-contact information to answer requests, prepare proposals and manage communications. For company representatives, our proposed basis is legitimate interests in responding to business requests and managing commercial relationships, balanced against their rights. When you personally contract, for example as a sole trader, necessary pre-contract steps you request and contract performance may instead apply. {ph("Approve these bases against actual practice")}</p>
        <p><b>Consultancy.</b> The engagement identifies necessary records and our data role. As a processor, we follow the controller's documented instructions under a data-processing agreement. For any controller use of client records, we identify the specific purpose and lawful basis. A business contract alone does not authorise every use of its customers' data. {ph("Complete any engagement-specific controller purposes and bases before collection")}</p>
        <p><b>Billing and compliance.</b> Relevant contact and transaction records are used for invoicing, accounting and applicable legal duties. Contract performance may apply for individual clients and legal obligation for statutory record-keeping. {ph("Confirm the applicable duties")}</p>
        <p><b>Security and legal claims.</b> Necessary records may be used to protect systems, investigate misuse or establish, exercise or defend claims, based on legitimate interests in security and legal rights, with appropriate limits.</p>
        <p><b>Optional tracking or marketing.</b> {ph("Confirm whether any tracking or marketing is used; remove this paragraph if not")} Consent-dependent tracking runs only after consent. An enquiry is not promotional-email consent. Any marketing must have an appropriate lawful basis, comply with electronic-marketing rules and offer a clear opt-out.</p>"""),
        ("recipients", "Recipients and international transfers", f"""        <p>We use service providers for business email (Google Workspace), domain name services (Cloudflare) and website hosting. {ph("Insert remaining providers and functions: secure files, CRM or calendar, accounting and advisers")} Access is limited to people who need it for the relevant purpose, subject to appropriate confidentiality and contractual arrangements.</p>
        <p>Relevant records may be shared with payment providers or other counterparties only within the engagement's agreed scope and applicable data rules, or when legally required or necessary for legal claims. {ph("Confirm other recipients, including any advertising or sale of data")}</p>
        <p>The website does not load fonts or other resources from Google; fonts are served from our own server.</p>
        <p>{ph("Insert actual non-EEA countries, adequacy decisions or other safeguards, and how to obtain details or copies")}</p>"""),
        ("retention", "Retention", f"""        <p>We keep data only as long as needed for the stated purpose, applicable legal duties and justified claims, then delete or anonymise it under the applicable schedule.</p>
{ul([f"Enquiries not becoming engagements: {ph('period or criteria')}",
     f"Raw statements and working files: {ph('period or criteria, and client return or deletion instructions where we are a processor')}",
     f"Deliverables and correspondence: {ph('period or criteria')}",
     f"Contracts, invoices and statutory records: {ph('verified legal period and start event')}",
     f"Technical and security logs: {ph('period')}; backups: {ph('expiry cycle')}",
     f"Consent and opt-out evidence, if applicable: {ph('period or criteria')}"])}
        <p>Necessary legal holds may pause routine deletion of relevant records. Theme and cookie-notice storage remains until changed or cleared in your browser.</p>"""),
        ("rights", "Rights and complaints", """        <p>Subject to GDPR conditions and exceptions, you may request access, correction, erasure, restriction or portability and object to processing. You may object to legitimate-interest processing on grounds relating to your situation and to direct marketing at any time. Where consent applies, you may withdraw it without affecting earlier lawful processing.</p>
        <p>Contact <a href="mailto:support@rumstar.eu">support@rumstar.eu</a>. We may ask for proportionate identity verification. We respond without undue delay, normally within one month, and explain any lawful extension within that first month. Requests are normally free, subject to GDPR rules on manifestly unfounded or excessive requests.</p>
        <p>You may complain to the Cyprus Commissioner for Personal Data Protection at <a href="https://www.dataprotection.gov.cy/" rel="noopener">dataprotection.gov.cy</a> or, where applicable, the authority in your country of habitual residence, work or alleged infringement. You need not complain to us first.</p>"""),
        ("other", "Information requirements, automation and updates", f"""        <p>Enquiry information is voluntary, but missing contact details may prevent a response. An engagement may require records for the agreed review; we explain requirements before collection. Do not supply special-category data or unnecessary customer-level records unless expressly agreed and lawfully justified.</p>
        <p>{ph("Confirm any solely automated decisions or profiling, and any AI-assisted analysis and its providers")}</p>
        <p>The website is directed at business users, not children. We update this notice when processing changes and provide further information or obtain consent where required. The effective date identifies the version.</p>"""),
    ]
    return legal("privacy.html", "Privacy Notice", "How we handle personal data.",
                 "Who controls your data, what we collect, why, who receives it, how long we keep it, and your rights.", secs,
                 "Rumstar Limited's privacy notice: personal data from enquiries, client work and website use, legal bases and your GDPR rights.")


def cookies():
    secs = [
        ("inventory", "Scope and inventory", f"""        <p>Cookies are small browser files. Similar technologies include localStorage and sessionStorage. This notice concerns rumstar.eu, operated by RUMSTAR LIMITED. Contact <a href="mailto:support@rumstar.eu">support@rumstar.eu</a>.</p>
        <div class="tbl"><table>
          <thead><tr><th>Name</th><th>Type</th><th>Purpose</th><th>Set when</th><th>Kept until</th></tr></thead>
          <tbody>
            <tr><td>theme</td><td>First-party localStorage</td><td>Remembers your light or dark display choice. It does not identify you for advertising.</td><td>You switch theme</td><td>You change or clear it</td></tr>
            <tr><td>cookie-notice</td><td>First-party localStorage</td><td>Remembers that you have dismissed the cookie notice, so it is not shown again.</td><td>You press OK on the notice</td><td>You clear it</td></tr>
          </tbody>
        </table></div>
        <p>The site sets no cookies of its own and runs no analytics or advertising scripts. Fonts are served from our own server, so no font provider receives your details. {ph("Confirm the complete inventory, including anything set by the host or CDN, and the exemption position under Cyprus law")}</p>"""),
        ("consent", "Consent and controls", """        <p>Any legally exempt storage is used only for the relevant transmission or strictly necessary requested-service purpose. Consent-dependent tracking must not run before agreement.</p>
        <p>If nonessential tracking is introduced, users must be able to reject it, select purposes and withdraw consent as easily as they give it, while retaining basic content access. Continuing to browse is not consent.</p>
        <p>Your browser's site-data controls can clear cookies and localStorage. Clearing theme storage removes the saved preference. Blocking storage can prevent preferences being remembered. These controls supplement, not replace, required consent controls. You can show the cookie notice again with the link in the footer. We update this notice when the inventory changes and gate any new consent-dependent technology before collection.</p>"""),
    ]
    return legal("cookies.html", "Cookie and Local Storage Notice", "What this site stores on your device.",
                 "No cookies, no analytics, no advertising. Two small preferences, both set by your own actions.", secs,
                 "Rumstar's cookie and local storage notice: no cookies or tracking, two first-party preferences stored in your browser.")


def complaints():
    secs = [
        ("status", "About this process", f"""        <p>This is a voluntary process for complaints about Rumstar's consultancy service. It is not a regulated payment-provider complaints procedure. {ph("Approve contact, staffing and targets before publication")}</p>"""),
        ("how", "How to complain", """        <p>Email <a href="mailto:support@rumstar.eu">support@rumstar.eu</a> or write to RUMSTAR LIMITED, 84 Larnakos, Pallouriotissa, 1046 Nicosia, Cyprus. Include your contact details, engagement reference, what happened and the outcome sought. Do not include card details, passwords or unnecessary customer data.</p>"""),
        ("timing", "What happens and when", """        <p>We aim to acknowledge complaints within five working days and provide a substantive response within twenty working days. If more time is needed, we explain why and give a revised date. These targets do not restrict legal rights or deadlines.</p>"""),
        ("review", "Review and escalation", f"""        <p>We review relevant records and explain findings and any proposed remedy. If you disagree, request further review and explain why. Where practicable, someone not directly involved will review it. {ph("Confirm a feasible escalation process")}</p>"""),
        ("other", "Other routes", """        <p>Privacy complaints may also go directly to the relevant authority, such as the Cyprus Commissioner for Personal Data Protection. Issues with a payment provider's processing or settlement should also be raised with that provider; this process does not replace its statutory procedures. You need not delay seeking legal advice or exercising rights.</p>"""),
    ]
    return legal("complaints.html", "Complaints", "Raising a concern with us.",
                 "How to complain about our service, what to include, and when to expect a reply.", secs,
                 "How to raise a complaint or concern about Rumstar's consultancy service, and our response targets.")


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
