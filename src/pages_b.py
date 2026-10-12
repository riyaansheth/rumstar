from shell import page, hero, cta, ph


def how():
    body = hero("How we work", "A clear process, from first call to signed contract.",
                "You stay the decision maker throughout. We do the reading, the comparing and the chasing, and we put everything in writing.") + f'''
  <section class="wrap flow">
    <div class="flow-head">
      <h2>Five steps, in order.</h2>
      <p>Most engagements follow this path. Some stop after step three, when the written recommendation is all a business needs.</p>
      <a class="btn" href="contact.html">Start with step one</a>
    </div>
    <ol class="timeline">
      <li>
        <span class="n">1</span>
        <div><h2>First call</h2>
        <p>Fifteen minutes, free. We ask how you take payments today, who your providers are and what is bothering you. By the end you know whether a review is worth doing.</p></div>
      </li>
      <li>
        <span class="n">2</span>
        <div><h2>Statement Review</h2>
        <p>You send your recent statements and contracts. We break down every charge, check your pricing model and benchmark it. We confirm the turnaround as soon as we have your documents.</p></div>
      </li>
      <li>
        <span class="n">3</span>
        <div><h2>Written recommendation</h2>
        <p>A plain report: what you pay, what you should pay, and how to get there. Renegotiate, move, or change how payments are routed. Options are ranked and every trade-off is explained.</p></div>
      </li>
      <li>
        <span class="n">4</span>
        <div><h2>Delivery</h2>
        <p>We run the negotiation, the tender or the migration with the providers. You approve every decision and sign contracts directly with the provider. We never sit between you and your money.</p></div>
      </li>
      <li>
        <span class="n">5</span>
        <div><h2>Keep watching</h2>
        <p>Regular statement checks and renewal date tracking, so rates do not creep back up and contracts do not roll over unnoticed.</p></div>
      </li>
    </ol>
  </section>

  <section class="wrap" id="checklist">
    <div class="split-head">
      <h2>What we need from you.</h2>
      <p>The more complete this is, the faster and sharper the review. Send what you have. We will ask for anything missing.</p>
    </div>
    <div class="check-grid">
      <div class="check-card">
        <h3>For a Statement Review</h3>
        <ul class="ticks">
          <li>Your last three months of processing statements, from every provider</li>
          <li>Your current contracts and pricing schedules</li>
          <li>Chargeback and fraud reports, if you have them</li>
          <li>Your website and a description of your checkout</li>
          <li>Half an hour with whoever looks after payments</li>
        </ul>
      </div>
      <div class="check-card">
        <h3>For a new account application</h3>
        <ul class="ticks">
          <li>Company registration documents</li>
          <li>Identity documents for directors and main shareholders</li>
          <li>Proof of business address</li>
          <li>Processing history, where you have it</li>
          <li>Any licences your sector requires</li>
          <li>Your website, with terms, refund policy and contact details visible</li>
        </ul>
      </div>
    </div>
    <p class="share-note"><b>Sharing documents safely.</b> We agree a secure way to transfer statements and contracts before you send them, and a redacted summary is often enough to start. Never send card numbers, CVVs, passwords or bank login details, to us or anyone else.</p>
  </section>

  <section class="wrap">
    <div class="split-head">
      <h2>Ground rules.</h2>
      <p>How we behave on every engagement, whatever its size.</p>
    </div>
    <ul class="rules">
      <li><b>You decide.</b><span>We recommend. You approve every change and sign every contract yourself.</span></li>
      <li><b>Disclosed, always.</b><span>Any commercial relationship we have with a provider is disclosed before you decide anything.</span></li>
      <li><b>In writing.</b><span>Findings, recommendations and offers are written down, so you can check them and keep them.</span></li>
      <li><b>Confidential.</b><span>Your statements and contracts stay private. We sign a confidentiality agreement on request.</span></li>
      <li><b>Never in the money flow.</b><span>We do not process payments or hold funds. Your money moves only between you, your customers and your licensed providers.</span></li>
      <li><b>Honest about the gap.</b><span>If there is not enough to gain, we tell you after the first call, including when that means not hiring us.</span></li>
    </ul>
  </section>

{cta()}'''
    return page("how-we-work.html", "How We Work: From First Call to Signed Contract | Rumstar",
                "Rumstar's process: a free first call, a Statement Review, a written recommendation, delivery and ongoing review. Plus the documents we need from you.",
                body)


SECTORS = [
    ("ecommerce", "Ecommerce and retail",
     ["Blended pricing that hides what each card really costs",
      "Cross-border and currency conversion fees on foreign customers",
      "Good payments declined by overcautious fraud rules"],
     "Statement Review, approval rate work, local payment methods for new markets."),
    ("subscriptions", "Subscriptions and SaaS",
     ["Renewals failing on expired or replaced cards",
      "Customers lost to failed payments rather than cancellations",
      "Authentication friction on recurring charges"],
     "Retry logic, card updater services, network tokens and the right exemptions for recurring payments."),
    ("travel", "Travel and hospitality",
     ["Long gaps between payment and delivery, so providers see higher risk",
      "Rolling reserves that tie up cash",
      "Chargebacks when plans change"],
     "Provider selection, reserve negotiation, dispute handling and multi-currency setups."),
    ("igaming", "iGaming and betting",
     ["Few providers willing to accept the sector",
      "Licence checks country by country",
      "Fast, reliable payouts expected by players"],
     "Complete application files, providers with appetite, payout methods and local payment options."),
    ("trading", "Forex, CFD and trading",
     ["Card deposits treated as high risk",
      "Withdrawals and refunds that must go back the right way",
      "Regulatory expectations on where client money sits"],
     "Provider shortlists, bank transfer and open banking options, and clean onboarding files."),
    ("marketplaces", "Marketplaces and platforms",
     ["Collecting for sellers and paying them out",
      "Checking sellers before they can be paid",
      "Questions about whether your model needs a licence"],
     "Platform payment models, provider selection, and early flags on licensing questions for your lawyers."),
    ("digital", "Digital goods and gaming",
     ["Instant delivery, so fraud arrives fast",
      "High dispute rates on low value items",
      "Customers in many countries with different payment habits"],
     "Fraud rule tuning, chargeback controls, wallets and local methods."),
    ("other-high-risk", "Other specialist sectors",
     ["Nutraceuticals, dating, ticketing and similar sectors",
      "Accounts refused or closed with little explanation",
      "Reserves and terms that are hard to compare"],
     "Application files, provider shortlists and plain explanations of the terms on offer."),
]


def industries():
    cards = []
    for i, t, probs, help_ in SECTORS:
        pl = "".join(f"<li>{p}</li>" for p in probs)
        cards.append(f'''      <article class="sector" id="{i}">
        <svg class="sector-star" viewBox="0 0 32 32" aria-hidden="true"><path d="M16 1 C17.5 11 21 14.5 31 16 C21 17.5 17.5 21 16 31 C14.5 21 11 17.5 1 16 C11 14.5 14.5 11 16 1Z"/></svg>
        <h2>{t}</h2>
        <h3>Common problems</h3>
        <ul class="dashes">{pl}</ul>
        <h3>Where we help</h3>
        <p>{help_}</p>
      </article>''')
    body = hero("Industries", "Different businesses, different payment problems.",
                "A subscription business loses money in different places from a travel agent or a trading platform. We start from how you sell, then look at what you pay.") + f'''
  <section class="wrap">
    <div class="sector-grid">
{chr(10).join(cards)}
    </div>
  </section>

  <section class="wrap">
    <div class="callout wide">
      <h3>A note on high-risk sectors</h3>
      <p>Some sectors need a licence before any provider will consider them, and providers make their own approval decisions. We tell you early if your model raises a licensing question, so you can take it to your legal advisers before it costs you time.</p>
    </div>
  </section>

  <section class="wrap">
    <div class="split-head">
      <h2>Based in Nicosia.</h2>
      <p>Cyprus is home to a large number of trading, gaming and fintech businesses. We are based here and focused on the questions EU and Cypriot rules raise for them, while working with businesses wherever they sell.</p>
    </div>
  </section>

{cta()}'''
    return page("industries.html", "Payment Advice for Ecommerce, iGaming and Forex | Rumstar",
                "Payment advice for ecommerce, subscriptions, travel, iGaming, forex and trading, marketplaces, digital goods and other specialist sectors.",
                body)


GUIDE = [
    ("charges", "What you actually pay", '''
      <p>Every card payment carries several charges, usually rolled into one rate on your statement.</p>
      <dl class="terms">
        <div><dt>Interchange</dt><dd>Paid by your acquirer to the bank that issued the customer's card. Set by the card schemes and, in the EEA, capped for most consumer cards.</dd></div>
        <div><dt>Scheme fees</dt><dd>Charged by Visa, Mastercard and others for using their networks. Many separate line items, often updated. Not capped.</dd></div>
        <div><dt>Acquirer margin</dt><dd>What your acquirer keeps for processing and settling your payments. This is where most negotiation happens.</dd></div>
        <div><dt>Gateway fees</dt><dd>For the technology that connects your checkout to the acquirer. Sometimes bundled, sometimes charged per transaction.</dd></div>
        <div><dt>Extras</dt><dd>Authorisation fees, refund fees, chargeback fees, PCI fees, statement fees, currency conversion and minimum monthly charges.</dd></div>
      </dl>'''),
    ("pricing-models", "Blended or itemised pricing", '''
      <p>On <b>blended</b> pricing you pay one rate whatever the card. It is simple, but you cannot see how much is margin. On <b>itemised</b> pricing, often called interchange plus plus, interchange and scheme fees are passed through at cost and the provider adds a visible margin.</p>
      <p>In the EEA, the Interchange Fee Regulation (Regulation (EU) 2015/751, Article 9) requires acquirers to show merchant service charges separately for each card category and brand, unless you ask in writing for blended pricing. If your statement does not itemise charges, you can ask for it to.</p>'''),
    ("caps", "Interchange caps in the EEA", '''
      <p>For consumer cards issued and used in the EEA, interchange is capped at 0.2% of the transaction for debit cards and 0.3% for credit cards (Regulation (EU) 2015/751, Articles 3 and 4).</p>
      <p>Cards issued outside the EEA are covered by separate commitments Visa and Mastercard gave the European Commission in 2019, with higher caps for online payments.</p>
      <p>Not capped: commercial and business cards, scheme fees, acquirer margin and gateway fees. Three party schemes such as American Express are treated differently. This is why two businesses with the same headline rate can be paying very different real costs.</p>'''),
    ("surcharging", "Surcharging", '''
      <p>Under PSD2 (Directive (EU) 2015/2366, Article 62), you cannot add a surcharge for consumer cards covered by the interchange caps, or for SEPA transfers and direct debits. Where a surcharge is allowed, it cannot exceed your direct cost. Rules can vary between countries, so check before you add one.</p>'''),
    ("sca", "Strong customer authentication and 3D Secure", '''
      <p>PSD2 requires strong customer authentication for most online card payments in the EEA, usually through 3D Secure. Exemptions exist for low value payments, low risk transactions assessed by your provider, and merchant initiated payments such as subscriptions after the first one. Payments where the card or the acquirer is outside the EEA are handled differently.</p>
      <p>Applying exemptions well reduces friction at checkout. Applying them badly increases declines and fraud.</p>'''),
    ("declines", "Approval rates and declines", '''
      <p>Some declines are final, such as a stolen card. Many are not: an expired card, a temporary bank decision, an authentication problem or a fraud rule that was too strict. These are often called false declines, and they turn good customers away.</p>
      <p>Common fixes include retrying at the right moment and in line with scheme rules, network tokens and account updater services that keep stored cards current, better authentication settings, and routing payments to a local acquirer.</p>'''),
    ("chargebacks", "Chargebacks and reserves", '''
      <p>A chargeback is a payment reversed by the customer's bank, usually after a dispute. You can contest it with evidence. The card schemes run monitoring programmes, and businesses whose dispute or fraud levels stay too high face fines and can lose their account.</p>
      <p>A rolling reserve is a share of your takings that a provider holds back for a period, to cover future chargebacks. It is common in higher risk sectors and is negotiable, so read the terms before you sign.</p>'''),
    ("regulated", "Who is regulated, and who is not", '''
      <p>In Cyprus, payment institutions and e-money institutions are authorised and supervised by the Central Bank of Cyprus, under the laws that bring PSD2 into Cypriot law. The Central Bank keeps public registers of authorised firms, and you should check any provider you deal with against them.</p>
      <p>Advisers such as Rumstar are a different thing. We do not process payments, hold funds or act for a provider in the payment flow. Your contract is always with a licensed provider.</p>'''),
    ("changes", "What is changing", '''
      <p>The EU has agreed a new payments package: a revised directive, known as PSD3, and a new Payment Services Regulation. It is expected to apply from around late 2027, with transition periods for licensing. Expected changes include checks that a payee's name matches their account, more protection against fraud for consumers, and e-money institutions being brought into the payment institution regime.</p>
      <p>Dates and details may still change before the rules apply.</p>'''),
]

GLOSSARY = [
    ("Acquirer", "The provider that processes card payments for a business and pays the money into its account."),
    ("Issuer", "The bank or provider that issued the customer's card."),
    ("Payment service provider (PSP)", "A company offering payment processing to businesses, often combining acquiring, a gateway and other services."),
    ("Gateway", "The technology that passes payment details from your checkout to the acquirer."),
    ("Orchestration", "A layer that connects several providers and decides where each payment is sent."),
    ("Interchange plus plus (IC++)", "Pricing where interchange and scheme fees are passed through at cost, plus a stated provider margin."),
    ("MCC", "Merchant category code. A four digit code that tells the card schemes what kind of business you are."),
    ("MID", "Merchant ID. The identifier for your account with an acquirer."),
    ("BIN", "The first digits of a card number. They identify the issuer, card type and country."),
    ("3D Secure", "The card schemes' system for authenticating online payments, used to meet strong customer authentication rules."),
    ("Tokenisation", "Replacing card details with a token, so stored cards are safer and can be kept up to date."),
    ("Account updater", "A service that refreshes stored card details when a card is replaced or expires."),
    ("Rolling reserve", "A share of your takings held back by a provider for a period to cover future chargebacks."),
    ("PCI DSS", "The card industry's security standard for any business that handles card data."),
    ("APM", "Alternative payment method. Anything other than a card, such as wallets, bank payments or buy now pay later."),
    ("Settlement", "When the money from your sales is actually paid into your bank account."),
]


def guide():
    toc = "\n".join(f'        <li><a href="#{i}">{t}</a></li>' for i, t, _ in GUIDE)
    secs = "\n".join(f'''      <section class="g-sec" id="{i}">
        <h2>{t}</h2>{c}
      </section>''' for i, t, c in GUIDE)
    gl = "\n".join(f'        <div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in GLOSSARY)
    layers = [("Extras", "neg c"), ("Gateway", "neg b"), ("Acquirer margin", "neg"), ("Scheme fees", "fixed b"), ("Interchange", "fixed")]
    lyr = "\n".join(f'          <div class="lyr {c}" style="--z:{n}"><span>{t}</span></div>' for n, (t, c) in enumerate(layers))
    stack = f'''    <div class="stack3d" aria-hidden="true">
      <div class="stack-shadow"></div>
      <div class="stack-rot">
{lyr}
          <div class="lyr face" style="--z:5">
            <i class="chip"></i>
            <svg viewBox="0 0 32 32"><path d="M16 1 C17.5 11 21 14.5 31 16 C21 17.5 17.5 21 16 31 C14.5 21 11 17.5 1 16 C11 14.5 14.5 11 16 1Z"/></svg>
            <b>•••• •••• •••• 2026</b>
            <em>One rate on your statement</em>
          </div>
      </div>
    </div>
'''
    body = hero("Payments guide", "How payment fees and rules actually work.",
                "A plain guide to what you pay, why payments fail and which rules apply in the EU. Read it before you talk to any provider, including us.", stack) + f'''
  <div class="read-progress" aria-hidden="true"><i></i></div>
  <section class="doc wrap">
    <aside class="toc" aria-label="Guide contents">
      <p>Contents</p>
      <ol>
{toc}
        <li><a href="#glossary">Glossary</a></li>
      </ol>
    </aside>
    <div class="doc-body prose">
{secs}
      <section class="g-sec" id="glossary">
        <h2>Glossary</h2>
        <dl class="terms glossary">
{gl}
        </dl>
      </section>
      <p class="fine">General information about payments in the EU, last reviewed October 2026. It is not legal advice. Rules change and their application depends on your circumstances.</p>
    </div>
  </section>

{cta("Want to know what this means for you?", "Send us your statements and we will show you where your money goes.")}'''
    return page("guide.html", "Payments Guide: Card Fees, Interchange and EU Rules | Rumstar",
                "A plain guide to card fees, interchange caps, surcharging, 3D Secure, declines, chargebacks and payment regulation in the EU and Cyprus.",
                body, "guide-page")
