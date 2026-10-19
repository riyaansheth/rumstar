import re
from shell import page, hero, cta, ph, STAR

SRC = open('/Users/riyaansheth/rumstar/index.html').read()
ROUTER = re.search(r'    <figure class="router".*?</figure>', SRC, re.S).group(0)
ROUTER = ROUTER.replace('Card payment, €84.00, routed to lowest cost acquirer', 'Card payment routed to the lowest cost acquirer')
MARQUEE = re.search(r'  <div class="marquee".*?\n  </div>\n', SRC, re.S).group(0)


def home():
    body = f'''  <section class="hero wrap">
    <div class="hero-copy">
      <p class="kicker">Independent payment consultancy, Nicosia</p>
      <h1>
        <span class="line"><span>Pay less.</span></span>
        <span class="line"><span>Get paid more.</span></span>
      </h1>
      <p class="lede">We read your processing statements, find the fees you should not be paying and the payments you should not be losing, then fix both. We work for you, not for the providers.</p>
      <div class="actions">
        <a href="contact.html" class="btn">Book a free 15 minute call</a>
        <a href="#fees" class="link">See where your fee goes</a>
      </div>
    </div>

{ROUTER}
  </section>

{MARQUEE}
  <section id="fees" class="fees wrap">
    <div class="split-head">
      <h2>Where your rate actually goes.</h2>
      <p>Your provider shows you one blended rate. Underneath it are five different charges. Two are set by the card schemes. The other three are a negotiation nobody had on your behalf.</p>
    </div>

    <div class="fee-panel">
      <div class="fee-top">
        <div>
          <div class="fee-total">5</div>
          <div class="fee-sub">separate charges hidden inside one blended rate</div>
        </div>
        <div class="card3d" aria-hidden="true">
          <div class="card-shadow"></div>
          <div class="card-float">
            <div class="card-rot">
              <div class="lyr neg c" data-k="4" style="--z:0"><span>Extras</span></div>
              <div class="lyr neg b" data-k="3" style="--z:1"><span>Gateway</span></div>
              <div class="lyr neg" data-k="2" style="--z:2"><span>Acquirer margin</span></div>
              <div class="lyr fixed b" data-k="1" style="--z:3"><span>Scheme fees</span></div>
              <div class="lyr fixed" data-k="0" style="--z:4"><span>Interchange</span></div>
              <div class="lyr face" style="--z:5">
                <i class="chip"></i>
                <svg viewBox="0 0 32 32">{STAR}</svg>
                <b>•••• •••• •••• 2026</b>
                <em>One rate on your statement</em>
              </div>
            </div>
          </div>
        </div>
        <a href="guide.html#charges" class="link">How each charge works</a>
      </div>

      <div class="bar-wrap">
      <span class="fee-tip" aria-hidden="true"></span>
      <div class="bar" aria-hidden="true">
        <i class="seg fixed" data-v="3" data-k="0"></i>
        <i class="seg fixed b" data-v="1.4" data-k="1"></i>
        <i class="seg neg" data-v="8" data-k="2"></i>
        <i class="seg neg b" data-v="2.6" data-k="3"></i>
        <i class="seg neg c" data-v="2.8" data-k="4"></i>
      </div>
      </div>

      <ul class="legend">
        <li class="fixed" data-k="0" tabindex="0"><b>Interchange</b><em>Paid to the card issuer. Capped in the EEA for consumer cards.</em></li>
        <li class="fixed b" data-k="1" tabindex="0"><b>Scheme fees</b><em>Set by Visa and Mastercard. Passed through.</em></li>
        <li class="neg" data-k="2" tabindex="0"><b>Acquirer margin</b><em>Your provider's cut. Negotiable.</em></li>
        <li class="neg b" data-k="3" tabindex="0"><b>Gateway</b><em>Often bundled, often overpriced.</em></li>
        <li class="neg c" data-k="4" tabindex="0"><b>Extras</b><em>PCI, authorisation, refund and statement fees.</em></li>
      </ul>
      <p class="note">Bar proportions are illustrative. Your real numbers come from your statements.</p>
    </div>
  </section>

  <section id="services" class="services wrap">
    <div class="split-head">
      <h2>What we do for you.</h2>
      <p>We do not sell processing, software or terminals. We review, negotiate and oversee, so every recommendation is about what suits you. <a class="link" href="services.html">All services</a></p>
    </div>

    <div class="bench">
      <div class="tabs" role="tablist" aria-label="Services">
        <span class="tab-ind" aria-hidden="true"></span>
        <button role="tab" id="t0" aria-controls="panel" aria-selected="true">Statement Review</button>
        <button role="tab" id="t1" aria-controls="panel" aria-selected="false" tabindex="-1">Provider selection</button>
        <button role="tab" id="t2" aria-controls="panel" aria-selected="false" tabindex="-1">Approval rates</button>
        <button role="tab" id="t3" aria-controls="panel" aria-selected="false" tabindex="-1">Migration</button>
      </div>
      <div class="panel" id="panel" role="tabpanel" aria-labelledby="t0" tabindex="0">
        <h3>Every line of your statement, explained.</h3>
        <p>We take your recent statements and break down every charge: interchange, scheme fees, margin, gateway and the small extras that add up. You get a plain list of what you pay and what you should pay.</p>
        <ul><li>Statement teardown</li><li>Benchmark against the market</li><li>Findings in writing</li></ul>
      </div>
    </div>
  </section>

  <section id="industries" class="wrap">
    <div class="split-head">
      <h2>Built around how you sell.</h2>
      <p>A subscription business loses money in different places from a marketplace or an online shop. We start from your model. <a class="link" href="industries.html">All industries</a></p>
    </div>
    <ul class="sector-strip">
      <li><a href="industries.html#ecommerce"><b>Ecommerce and retail</b><span>Blended pricing, cross-border fees, false declines</span></a></li>
      <li><a href="industries.html#subscriptions"><b>Subscriptions and SaaS</b><span>Failed renewals and involuntary churn</span></a></li>
      <li><a href="industries.html#marketplaces"><b>Marketplaces and platforms</b><span>Split payments and seller payouts</span></a></li>
      <li><a href="industries.html#digital"><b>Digital goods</b><span>Fast fraud, low value disputes</span></a></li>
    </ul>
  </section>

  <section id="process" class="process wrap">
    <div class="split-head">
      <h2>Four steps. The first is free.</h2>
      <p>One call is normally enough to tell whether there is money to recover. If there is not, we say so. <a class="link" href="how-we-work.html">How we work</a></p>
    </div>
    <ol class="steps" data-progress>
      <li><span class="n">1</span><h3>Look</h3><p>A short call, then your statements. We come back with what you pay, what you should pay, and the gap.</p></li>
      <li><span class="n">2</span><h3>Recommend</h3><p>A written plan. Renegotiate with your current provider or move. Options ranked, trade-offs explained.</p></li>
      <li><span class="n">3</span><h3>Deliver</h3><p>We run the negotiation or the switch with the provider. You stay informed, not chasing.</p></li>
      <li><span class="n">4</span><h3>Keep watching</h3><p>Regular statement checks, so rates do not quietly creep back up.</p></li>
    </ol>
  </section>

  <section id="faq" class="faq wrap">
    <div class="split-head">
      <h2>Before you call.</h2>
      <p>The questions people ask first. <a class="link" href="faq.html">All questions</a></p>
    </div>
    <div class="qs">
      <details>
        <summary>How are you paid?<i aria-hidden="true"></i></summary>
        <p>Every engagement is quoted in writing before any work starts, and any commercial relationship we have with a provider is disclosed before you decide anything.</p>
      </details>
      <details>
        <summary>How long does a Statement Review take?<i aria-hidden="true"></i></summary>
        <p>It depends on how many providers and currencies are involved. We confirm a date as soon as we have your statements.</p>
      </details>
      <details>
        <summary>What do you need from us?<i aria-hidden="true"></i></summary>
        <p>Your recent processing statements, your current contract, and half an hour with whoever looks after payments. <a class="link" href="how-we-work.html#checklist">Full checklist</a></p>
      </details>
      <details>
        <summary>Will we have to switch providers?<i aria-hidden="true"></i></summary>
        <p>Often not. Renegotiating with the provider you already have is often the better route. We only recommend moving when the numbers clearly justify it.</p>
      </details>
      <details>
        <summary>Are you a payment provider?<i aria-hidden="true"></i></summary>
        <p>No. Rumstar advises only. We do not process payments, hold your money or approve accounts. Contracts are always between you and a licensed provider.</p>
      </details>
    </div>
  </section>

{cta()}'''
    return page("index.html", "Rumstar | Independent Payment Consultancy in Nicosia, Cyprus",
                "Independent payment consultancy in Nicosia. We find the fees you should not pay and the payments you should not lose, then fix both.",
                body, "home")


SERVICES = [
    ("statement-review", "Statement Review",
     "Every charge on your processing statements, explained and benchmarked.",
     "Most businesses have never had their statements checked by someone on their side. We go through them line by line, separate the fixed costs from the negotiable ones and compare what you pay with what comparable businesses pay.",
     ["A breakdown of interchange, scheme fees, acquirer margin, gateway and extras",
      "A check of whether you are on blended or itemised pricing",
      "A benchmark against the market for a business like yours",
      "A written summary of what you should be paying"],
     "Any business whose rates were set years ago, or never questioned."),
    ("provider-selection", "Provider selection and tender",
     "The right acquirer, gateway or payment provider for how you actually sell.",
     "We turn your markets, currencies, payment methods, volumes and risk profile into clear requirements, then run a structured tender. Your current provider is invited too, so you see a fair comparison.",
     ["A requirements document in plain language",
      "A shortlist of providers that fit, and why",
      "Offers compared like for like, not headline rate against headline rate",
      "A ranked recommendation with the trade-offs explained"],
     "New businesses, businesses entering new markets, and anyone unhappy with their provider."),
    ("negotiation", "Contract negotiation",
     "Better terms, with or without switching.",
     "Pricing is only part of a payments contract. Minimum fees, termination charges, automatic renewals, reserves and settlement times all cost money. We negotiate the whole thing. You sign, we read it first.",
     ["Renegotiation with your current provider",
      "Review of pricing schedules and small print",
      "Fixes for auto renewal and exit terms",
      "A summary of what changed and what it is worth"],
     "Businesses approaching a renewal date, or tied to terms nobody remembers agreeing."),
    ("approval-rates", "Approval rates and declines",
     "A declined payment is a lost customer. Many of them should have gone through.",
     "We look at why your payments fail: by decline reason, card type, issuing country and channel. Then we fix what can be fixed with routing, retries, authentication settings and card updating services.",
     ["Decline analysis by reason, issuer and country",
      "Retry and routing logic that follows scheme rules",
      "Network tokens and account updater services",
      "3D Secure and strong customer authentication settings tuned to your traffic"],
     "Online businesses, subscriptions, and anyone selling across borders."),
    ("fraud-chargebacks", "Fraud and chargebacks",
     "Stop the losses without blocking good customers.",
     "Too little fraud control costs you chargebacks and can put your account at risk. Too much turns good customers away. We review your fraud rules, dispute handling and chargeback levels against card scheme monitoring programmes.",
     ["Chargeback monitoring against scheme thresholds",
      "A review of fraud rules and false positives",
      "A dispute process that wins more of what it should",
      "Early warning before a provider steps in"],
     "Digital goods, subscriptions and other businesses with high dispute exposure."),
    ("routing", "Routing and multiple providers",
     "When one provider is not enough.",
     "A second acquirer can lower costs, lift approval rates and keep you trading when a provider has an outage. It also adds work. We tell you whether it is worth it and, if so, how to set it up, with or without an orchestration layer.",
     ["An honest view on whether you need more than one provider",
      "Cost based and approval based routing rules",
      "Failover planning",
      "Orchestration platform selection if it makes sense"],
     "Growing businesses with meaningful volume in several markets."),
    ("migration", "Migration",
     "Switch provider without losing a day of trading.",
     "We plan the move, coordinate the providers' teams, move stored card tokens where possible and test before go live. Your customers should not notice anything changed.",
     ["A migration plan with owners and dates",
      "Token and stored card data transfer",
      "Testing and parallel running",
      "Go live support and a post move check"],
     "Anyone who has agreed better terms elsewhere and needs the switch done properly."),
    ("compliance", "Compliance and risk",
     "Know what applies to you and what does not.",
     "PCI DSS, strong customer authentication under PSD2, the EU Interchange Fee Regulation and surcharging rules all affect how you take payments. We explain what applies, what you can stop paying for, and what to fix first. We work alongside your legal advisers, not instead of them.",
     ["PCI DSS scope and how to reduce it",
      "Strong customer authentication and exemptions",
      "Your right to itemised statements in the EEA",
      "Surcharging and steering rules"],
     "Businesses that are unsure what their obligations are, or suspect they are overpaying for compliance."),
    ("new-markets", "New markets and payment methods",
     "Take the payment methods your new customers already use.",
     "Cards are not the default everywhere. We help you add the local methods, currencies and acquiring that matter in the markets you are entering, from bank payments and wallets to buy now pay later.",
     ["Payment method coverage by country",
      "Local acquiring and currency options",
      "Open banking and account to account payments",
      "A rollout order based on where your customers are"],
     "Businesses expanding into new countries."),
    ("ongoing", "Ongoing review",
     "Keep the savings you have won.",
     "Rates drift and providers add new fees quietly. We check your statements regularly, flag anything that has changed and keep track of contract renewal dates so nothing rolls over by accident.",
     ["Regular statement checks",
      "Alerts when rates or fees change",
      "Renewal date tracking",
      "A short written update each review"],
     "Every client, once the first piece of work is done."),
]


def services():
    toc = "\n".join(f'        <li><a href="#{i}">{t}</a></li>' for i, t, *_ in SERVICES)
    blocks = []
    for n, (i, t, tag, text, gets, good) in enumerate(SERVICES, 1):
        items = "".join(f"<li>{g}</li>" for g in gets)
        blocks.append(f'''      <article class="svc" id="{i}">
        <span class="svc-n">{n:02d}</span>
        <div>
          <h2>{t}</h2>
          <p class="svc-tag">{tag}</p>
          <p>{text}</p>
          <div class="svc-cols">
            <div><h3>What you get</h3><ul class="ticks">{items}</ul></div>
            <div><h3>Good for</h3><p>{good}</p></div>
          </div>
        </div>
      </article>''')
    body = hero("Services", "Advice on every part of how you get paid.",
                "We do not sell processing, terminals or software. We review, recommend, negotiate and oversee. Take one service, or let us run the whole thing.") + f'''
  <section class="doc wrap">
    <aside class="toc" aria-label="Services on this page">
      <p>On this page</p>
      <ol>
{toc}
      </ol>
    </aside>
    <div class="doc-body">
{chr(10).join(blocks)}
      <div class="callout">
        <h3>How engagements are priced</h3>
        <p>Every engagement is quoted in writing before any work starts.</p>
      </div>
    </div>
  </section>

{cta()}'''
    return page("services.html", "Payment Consulting: Fees, Providers, Approvals | Rumstar",
                "Statement reviews, provider selection, contract negotiation, approval rates, chargebacks, migrations and compliance for merchants.",
                body)
