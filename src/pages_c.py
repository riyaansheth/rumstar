from shell import page, hero, cta, ph


def about():
    body = hero("About", "Independent advice on how you get paid.",
                "Rumstar is a payment consultancy based in Nicosia, Cyprus. We help businesses pay less to take payments, lose fewer of them, and understand the rules that apply.") + f'''
  <section class="wrap">
    <div class="about-grid">
      <div class="prose">
        <h2>Why we exist</h2>
        <p>Payment providers know their pricing far better than the businesses they charge. Statements are long, fees are split across dozens of lines, and contracts renew quietly. Most businesses never have anyone on their side read them.</p>
        <p>That is our job. We read the statements, compare the market, negotiate the terms and oversee the work, then keep checking so the gains last.</p>
        <h2>How we stay on your side</h2>
        <p>We recommend what suits your business. Any commercial relationship we have with a provider is disclosed to you before you decide anything.</p>
        <h2>What we are not</h2>
        <ul class="dashes">
          <li>We are not a payment institution or e-money institution.</li>
          <li>We do not process payments or hold client money.</li>
          <li>We do not approve or open accounts. Licensed providers do.</li>
          <li>We are not a law firm. Where a question needs legal advice, we say so.</li>
        </ul>
        <p>You can check any payment provider against the public registers kept by the <a class="link" href="https://www.centralbank.cy" rel="noopener">Central Bank of Cyprus</a>.</p>
      </div>
      <aside class="side-stack">
        <div class="person">
          <div class="avatar" aria-hidden="true">MV</div>
          <div>
            <h3>Michalis Vassiliou</h3>
            <p class="role">Director</p>
          </div>
        </div>
        <div class="facts-card">
          <h3>Company details</h3>
          <dl>
            <div><dt>Legal name</dt><dd>RUMSTAR LIMITED</dd></div>
            <div><dt>Company Registration No.</dt><dd>HE 498715</dd></div>
            <div><dt>Registered in</dt><dd>Republic of Cyprus</dd></div>
            <div><dt>Founded</dt><dd>2026</dd></div>
            <div><dt>Registered office</dt><dd>84 Larnakos, Pallouriotissa, 1046 Nicosia, Cyprus</dd></div>
          </dl>
        </div>
      </aside>
    </div>
  </section>

  <section class="wrap">
    <div class="split-head">
      <h2>What we believe.</h2>
      <p>Four principles that shape every engagement.</p>
    </div>
    <ul class="rules four">
      <li><b>Numbers before opinions.</b><span>Every recommendation starts from your statements, not from a sales pitch.</span></li>
      <li><b>Disclose everything.</b><span>If we have a relationship with a provider, you hear about it first.</span></li>
      <li><b>Write it down.</b><span>Findings and advice are in writing, so you can hold us to them.</span></li>
      <li><b>You sign, we read first.</b><span>Contracts are yours. We make sure you know what is in them.</span></li>
    </ul>
  </section>

{cta()}'''
    return page("about.html", "About Rumstar: Independent Payment Advice from Cyprus",
                "Rumstar Limited is an independent payment consultancy in Nicosia, Cyprus. Advisory only: not a payment institution, never in the flow of funds.",
                body)


FAQ = [
    ("Working with us", [
        ("How are you paid?", f"Every engagement is quoted in writing before any work starts."),
        ("Do you take commission from providers?", f"Any commercial relationship we have with a provider is disclosed to you in writing before you decide anything."),
        ("What does the first call cost?", "Nothing. It takes about fifteen minutes and tells you whether a review is worth doing."),
        ("How long does a Statement Review take?", "It depends on how many providers and currencies are involved. We confirm a date as soon as we have your documents."),
        ("What do you need from us?", 'Your recent processing statements, current contracts and pricing schedules, and half an hour with whoever looks after payments. <a class="link" href="how-we-work.html#checklist">See the full checklist</a>.'),
        ("Is our information kept confidential?", "Yes. Your statements and contracts are used only for your engagement, and we sign a confidentiality agreement on request."),
        ("Will we have to switch providers?", "Often not. Renegotiating with your current provider is frequently the better route. We only recommend moving when the gain clearly outweighs the disruption."),
        ("Do you work with small businesses?", "Yes, when there is enough at stake for a review to be worthwhile. The first call tells you whether that is the case."),
        ("Where do you work?", "We are based in Nicosia, Cyprus, and work with businesses across Europe and beyond."),
    ]),
    ("About payments", [
        ("What is interchange?", 'The fee your acquirer pays to the bank that issued your customer\'s card. In the EEA it is capped for most consumer cards. <a class="link" href="guide.html#caps">More in our guide</a>.'),
        ("What is the difference between blended and itemised pricing?", 'Blended pricing is one rate for every card. Itemised pricing, often called interchange plus plus, passes interchange and scheme fees through at cost and adds a visible margin. <a class="link" href="guide.html#pricing-models">More in our guide</a>.'),
        ("Can I ask my provider for itemised statements?", "In the EEA, yes. The Interchange Fee Regulation requires acquirers to itemise charges by card category and brand unless you ask in writing for blended pricing."),
        ("Can I add a surcharge for card payments?", "Not for consumer cards covered by the EEA interchange caps. Where surcharging is allowed, it cannot exceed your direct cost, and national rules vary."),
        ("Why are good payments declined?", "Expired cards, temporary bank decisions, authentication problems and fraud rules that are too strict. Many of these can be reduced. <a class=\"link\" href=\"guide.html#declines\">More in our guide</a>."),
        ("What is a rolling reserve?", "A share of your takings that a provider holds back for a period to cover future chargebacks. Common in higher risk sectors, and negotiable."),
        ("What makes a business high-risk?", "Sectors with higher dispute, fraud or regulatory exposure, such as gaming, trading, travel and nutraceuticals. Fewer providers accept them, and terms are stricter."),
    ]),
    ("About Rumstar", [
        ("Are you regulated?", "Rumstar is an advisory business. We are not a payment institution or e-money institution, and we do not process payments or hold client funds. Your contracts are always with licensed providers."),
        ("Do you approve merchant accounts?", "No. Providers make their own approval decisions. We prepare a strong application and help you approach providers with the right appetite."),
        ("Are you a law firm?", "No. We explain the payment rules that affect you, and we tell you when a question needs a lawyer."),
    ]),
]


def faq():
    groups = []
    for title, qs in FAQ:
        items = "\n".join(f'''        <details>
          <summary>{q}<i aria-hidden="true"></i></summary>
          <p>{a}</p>
        </details>''' for q, a in qs)
        groups.append(f'''    <div class="faq-group">
      <h2>{title}</h2>
      <div class="qs">
{items}
      </div>
    </div>''')
    body = hero("FAQ", "Questions, answered plainly.",
                "What people ask before working with us, and the payments questions we hear most often.") + f'''
  <section class="wrap faq-page">
{chr(10).join(groups)}
  </section>

{cta("Still have a question?", "Ask us directly. The first call is free.")}'''
    return page("faq.html", "Payment Consultancy FAQ: Fees, Providers, Regulation | Rumstar",
                "Answers about working with Rumstar, how payment fees work, surcharging, declines, reserves and our regulatory status.",
                body)


def chips(name, options, kind="radio"):
    return "".join(
        f'<label class="chip"><input type="{kind}" name="{name}" value="{o}"><span>{o}</span></label>' for o in options)


def contact():
    body = hero("Contact", "Tell us how you take payments today.",
                "Three short steps. We use your answers to prepare for the first call, so it is useful from the first minute.", show_cta=False) + f'''
  <section class="wrap contact-grid">
    <form class="intake" id="intake" novalidate>
      <div class="progress" aria-hidden="true"><i></i></div>
      <p class="step-count" aria-live="polite">Step <b>1</b> of 3</p>

      <fieldset class="step" data-step="1">
        <legend>About you</legend>
        <div class="fields">
          <label class="field"><span>Full name</span><input name="Name" autocomplete="name" required aria-describedby="err-name"><small class="ferr" id="err-name">Please enter your name.</small></label>
          <label class="field"><span>Work email</span><input name="Email" type="email" autocomplete="email" required aria-describedby="err-email"><small class="ferr" id="err-email" data-empty="Please enter your email address." data-bad="That email address does not look right. Check it includes @ and a domain.">Please enter your email address.</small></label>
          <label class="field"><span>Company</span><input name="Company" autocomplete="organization" required aria-describedby="err-company"><small class="ferr" id="err-company">Please enter your company name.</small></label>
          <label class="field"><span>Website <em>optional</em></span><input name="Website" type="url" inputmode="url" placeholder="https://" aria-describedby="err-web"><small class="ferr" id="err-web">Enter the full address, starting with https://</small></label>
          <label class="field"><span>Phone <em>optional</em></span><input name="Phone" type="tel" autocomplete="tel"></label>
        </div>
      </fieldset>

      <fieldset class="step" data-step="2" hidden>
        <legend>Your business</legend>
        <p class="q">What kind of business is it?</p>
        <div class="chips">{chips("Business type", ["Ecommerce or retail", "Subscriptions or SaaS", "Travel or hospitality", "iGaming or betting", "Forex or trading", "Marketplace or platform", "Digital goods", "Other"])}</div>
        <p class="q">What would you like help with? <em>Choose any</em></p>
        <div class="chips">{chips("Help with", ["Lower fees", "A new provider", "Fewer declines", "Chargebacks or fraud", "Switching provider", "Compliance questions", "A high-risk account", "Not sure yet"], "checkbox")}</div>
      </fieldset>

      <fieldset class="step" data-step="3" hidden>
        <legend>Your payments</legend>
        <div class="fields">
          <label class="field"><span>Current provider or providers <em>optional</em></span><input name="Current providers"></label>
          <label class="field"><span>Approximate monthly card volume <em>optional, a rough figure is fine</em></span><input name="Monthly volume"></label>
        </div>
        <p class="q">Where are most of your customers?</p>
        <div class="chips">{chips("Markets", ["Cyprus", "Rest of the EU", "United Kingdom", "Middle East", "Worldwide"], "checkbox")}</div>
        <label class="field"><span>Anything else we should know? <em>optional</em></span><textarea name="Message" rows="4"></textarea></label>
      </fieldset>

      <div class="step-nav">
        <button type="button" class="btn-ghost" data-back hidden>Back</button>
        <button type="button" class="btn" data-next>Continue</button>
        <button type="submit" class="btn" data-submit hidden><span class="btn-label">Send enquiry</span><span class="spinner" aria-hidden="true"></span></button>
      </div>
      <p class="form-error" role="alert" aria-live="assertive"></p>
      <p class="fine">Sending opens your email app with your answers filled in, addressed to onboarding@rumstar.eu. We use your details to reply to your enquiry, as explained in our <a class="link" href="privacy.html">Privacy Notice</a>. Please do not include card numbers, CVVs, passwords or bank login details.</p>

    </form>

    <aside class="side-stack">
      <div class="facts-card">
        <h3>Talk to us directly</h3>
        <dl>
          <div><dt>New enquiries</dt><dd><a href="mailto:onboarding@rumstar.eu">onboarding@rumstar.eu</a></dd></div>
          <div><dt>Existing clients</dt><dd><a href="mailto:support@rumstar.eu">support@rumstar.eu</a></dd></div>
          <div><dt>Phone</dt><dd><a href="tel:+35797692104">+357 97 692104</a></dd></div>
          <div><dt>Office</dt><dd>84 Larnakos, Pallouriotissa, 1046 Nicosia, Cyprus</dd></div>
        </dl>
      </div>
      <div class="facts-card">
        <h3>What happens next</h3>
        <ol class="mini-steps">
          <li>We reply to arrange a call.</li>
          <li>A free 15 minute call about how you take payments today.</li>
          <li>If a review is worthwhile, we tell you what we need and quote in writing.</li>
        </ol>
      </div>
      <div class="facts-card">
        <h3>Have these ready</h3>
        <p>Your recent processing statements and current contract make the first call far more useful. Do not email them yet: we will agree a secure way to share them, and a redacted summary is often enough to start. <a class="link" href="how-we-work.html#checklist">Full checklist</a></p>
      </div>
    </aside>
  </section>'''
    return page("contact.html", "Contact Rumstar: Book a Free 15 Minute Payments Call",
                "Tell Rumstar how you take payments today. Book a free 15 minute call about fees, providers, declines or compliance.",
                body, "contact-page", mobile_cta=False)
