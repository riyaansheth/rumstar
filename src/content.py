"""All site copy that is shared between pages. British English, no em dashes."""
from layout import ph

EXPERTISE = [
    {
        "slug": "payment-cost-optimisation",
        "num": "01",
        "title": "Payment Cost Optimisation",
        "short": "A line by line reading of what you pay to accept payments, what you should be paying, and how to close the gap.",
        "services": ["Statement Review", "Pricing model review", "Contract renegotiation on price", "Ongoing statement monitoring"],
        "problem": [
            "Most businesses see one blended rate and a monthly total. Underneath sit interchange, scheme fees, the acquirer's margin, gateway charges and a long tail of smaller fees. Some are fixed by the card schemes. Others are commercial terms that were never seriously negotiated.",
            "Pricing also drifts. Scheme fees change, new line items appear, introductory rates expire and contracts renew automatically. Without someone reading the statements regularly, costs rise without anyone deciding they should.",
        ],
        "evaluate": [
            ("Your statements", "Every charge, separated into pass-through costs and provider margin."),
            ("Your pricing model", "Whether you are on blended or itemised pricing, and which suits your card mix."),
            ("Your card mix", "Debit, credit, commercial, domestic and cross-border cards, and how each is priced."),
            ("Your contract", "Minimum fees, renewal terms, termination charges and price change clauses."),
            ("The market", "What comparable businesses pay for the same profile."),
            ("The small print", "Authorisation, refund, chargeback, PCI and statement fees that add up."),
        ],
        "steps": [
            ("Collect", "We take your recent statements and contracts from every provider you use."),
            ("Separate", "We split fixed pass-through costs from the negotiable ones and rebuild your real effective rate."),
            ("Benchmark", "We compare your terms with the market for a business of your size and profile."),
            ("Act", "You receive a written summary and, if you choose, we renegotiate on your behalf."),
        ],
        "benefits": [
            "A clear view of what you actually pay, by charge and by card type",
            "Lower processing costs where the market supports it",
            "Itemised statements that make future changes visible",
            "Contract terms that no longer renew or rise by default",
        ],
    },
    {
        "slug": "acceptance-and-performance",
        "num": "02",
        "title": "Acceptance and Performance",
        "short": "Fewer good payments declined, smoother authentication and routing that keeps sales flowing.",
        "services": ["Decline and approval rate analysis", "Retry and routing logic", "Authentication and 3D Secure settings", "Multi-provider and failover set-ups"],
        "problem": [
            "A declined payment is usually a lost customer. Some declines are correct. Many are not: expired cards, temporary issuer decisions, authentication friction or fraud rules set too tightly.",
            "Approval rates are rarely reported clearly, and the causes sit across several parties: your checkout, your provider, the card schemes and the issuing banks. Improving them means looking at all of them together.",
        ],
        "evaluate": [
            ("Decline reasons", "Which codes you receive, how often, and which are recoverable."),
            ("Issuers and countries", "Where approval rates differ, and why."),
            ("Authentication", "How strong customer authentication and 3D Secure are applied, and which exemptions are used."),
            ("Stored cards", "Whether network tokens and account updater services keep saved cards current."),
            ("Retries", "When and how failed payments are retried, within scheme rules."),
            ("Routing", "Whether a second provider or local acquiring would help."),
        ],
        "steps": [
            ("Measure", "We establish your real approval rate by channel, card type and country."),
            ("Diagnose", "We trace declines to their causes and separate the recoverable from the final."),
            ("Prioritise", "We rank fixes by effort and likely effect."),
            ("Implement", "We work with your provider and developers to put the changes live, then measure again."),
        ],
        "benefits": [
            "More completed sales from the same traffic",
            "Fewer customers lost to failed renewals",
            "Checkout friction applied where it is needed, not everywhere",
            "Resilience if a provider has an outage",
        ],
    },
    {
        "slug": "provider-selection-and-negotiation",
        "num": "03",
        "title": "Provider Selection and Negotiation",
        "short": "The right acquirer, gateway or payment provider on terms you understand, and a switch that does not interrupt trading.",
        "services": ["Requirements and shortlisting", "Structured tender", "Contract negotiation", "Migration planning and support"],
        "problem": [
            "Providers are usually chosen once, often on a recommendation from a bank or a developer, and then left in place for years. The market moves on. Pricing, payment methods, coverage and service levels all change.",
            "Comparing offers is harder than it looks. Headline rates hide differences in pricing models, reserves, settlement times, minimums and exit terms. And when a better offer exists, moving provider carries real operational risk.",
        ],
        "evaluate": [
            ("Your requirements", "Markets, currencies, payment methods, volumes, channels and risk profile."),
            ("Provider fit", "Which acquirers, gateways and platforms genuinely suit your business."),
            ("Total cost", "Offers compared like for like, not headline rate against headline rate."),
            ("Contract terms", "Reserves, settlement times, liability, minimums, renewals and exit."),
            ("Integration effort", "What a change would mean for your checkout and your team."),
            ("Migration risk", "Stored card data, recurring payments and the go-live plan."),
        ],
        "steps": [
            ("Define", "We turn how you sell into a clear set of requirements."),
            ("Tender", "We invite a shortlist of providers, including your current one, to bid."),
            ("Negotiate", "We negotiate pricing and terms. You sign directly with the provider."),
            ("Move", "If you switch, we plan and oversee the migration so trading continues."),
        ],
        "benefits": [
            "A provider chosen for fit, not for a sales pitch",
            "A fair comparison you can explain to your board",
            "Better terms, whether you move or stay",
            "A switch planned around your trading, not the provider's timetable",
        ],
    },
    {
        "slug": "risk-compliance-and-global-payments",
        "num": "04",
        "title": "Risk, Compliance and Global Payments",
        "short": "Chargebacks, fraud, regulatory obligations, higher risk sectors and expansion into new markets.",
        "services": ["Fraud and chargeback review", "PCI DSS, SCA and EU payment rules", "High-risk and specialist sector applications", "New markets and local payment methods"],
        "problem": [
            "Payment rules are spread across EU regulation, national law, card scheme rules and your own provider's terms. Businesses either overpay for compliance they do not need or discover a gap only when a provider steps in.",
            "Higher risk sectors face fewer willing providers, stricter checks and rolling reserves. Businesses expanding abroad find that cards are not the default everywhere. Both need preparation before the first conversation with a provider.",
        ],
        "evaluate": [
            ("Chargebacks", "Your dispute levels against card scheme monitoring programmes."),
            ("Fraud controls", "Rules that stop fraud without turning away good customers."),
            ("Obligations", "PCI DSS scope, strong customer authentication and surcharging rules that apply to you."),
            ("Statement rights", "Your right in the EEA to itemised pricing information."),
            ("Application readiness", "For specialist sectors, the documents and controls providers will expect."),
            ("New markets", "The payment methods, currencies and local acquiring your new customers use."),
        ],
        "steps": [
            ("Review", "We map the rules, programmes and terms that apply to your business."),
            ("Prepare", "We close gaps and, for new accounts, assemble a complete application file."),
            ("Approach", "We help you approach providers with the right appetite for your sector or market."),
            ("Monitor", "We keep watching dispute levels, rule changes and renewal terms."),
        ],
        "benefits": [
            "Fewer chargebacks and fewer surprises from your provider",
            "Compliance effort spent where it is required",
            "Stronger applications in specialist sectors",
            "Payment options that match how customers pay in each market",
        ],
        "note": "Providers make their own decisions on approving accounts. Rumstar is not a law firm; where a question needs legal advice, we say so and work alongside your advisers.",
    },
]

INDUSTRIES = [
    ("ecommerce", "Ecommerce and retail",
     "Blended pricing that hides what each card costs, cross-border fees on foreign customers, and good payments declined by cautious fraud rules.",
     "Here the work usually starts with cost: a Statement Review and a check of the pricing model, followed by approval rate work and local payment methods for new markets.",
     ["payment-cost-optimisation", "acceptance-and-performance"]),
    ("subscriptions", "Subscriptions and SaaS",
     "Renewals failing on expired or replaced cards, customers lost to failed payments rather than cancellations, and authentication friction on recurring charges.",
     "The focus is retention: retry logic within scheme rules, network tokens, account updater services and the correct use of exemptions for merchant initiated payments.",
     ["acceptance-and-performance", "payment-cost-optimisation"]),
    ("travel", "Travel and hospitality",
     "Long gaps between payment and delivery, rolling reserves that tie up cash, and chargebacks when plans change.",
     "Provider selection and reserve terms matter most, alongside dispute handling and multi-currency set-ups.",
     ["provider-selection-and-negotiation", "risk-compliance-and-global-payments"]),
    ("igaming", "iGaming and betting",
     "Few providers willing to accept the sector, licence checks country by country, and players who expect fast, reliable payouts.",
     "Preparation is everything: a complete application file, providers with genuine appetite, payout methods and local payment options.",
     ["risk-compliance-and-global-payments", "provider-selection-and-negotiation"]),
    ("trading", "Forex, CFD and trading",
     "Card deposits treated as high risk, withdrawals that must return the right way, and regulatory expectations on where client money sits.",
     "We shortlist providers with appetite for the sector, look at bank transfer and open banking options, and make onboarding files complete from the start.",
     ["risk-compliance-and-global-payments", "provider-selection-and-negotiation"]),
    ("marketplaces", "Marketplaces and platforms",
     "Collecting on behalf of sellers and paying them out, checking sellers before they can be paid, and open questions about whether the model needs a licence.",
     "We look at platform payment models and provider fit, and flag licensing questions early so they reach your lawyers before they cost you time.",
     ["provider-selection-and-negotiation", "risk-compliance-and-global-payments"]),
    ("digital", "Digital goods and gaming",
     "Instant delivery, so fraud arrives fast; high dispute rates on low value items; and customers in many countries with different payment habits.",
     "Fraud rule tuning and chargeback controls come first, followed by wallets and local methods that suit each market.",
     ["risk-compliance-and-global-payments", "acceptance-and-performance"]),
    ("specialist", "Other specialist sectors",
     "Nutraceuticals, dating, ticketing and similar sectors face accounts refused or closed with little explanation, and reserves and terms that are hard to compare.",
     "We prepare application files, build provider shortlists and explain the terms on offer in plain language before anything is signed.",
     ["risk-compliance-and-global-payments", "provider-selection-and-negotiation"]),
]

PROCESS = [
    ("Discover", "A first conversation about how you take payments today, who your providers are and what is not working.",
     "A clear view of whether a review is worthwhile. The first conversation is free and takes about fifteen minutes."),
    ("Analyse", "We read your statements and contracts, separate fixed costs from negotiable ones and look at approvals, disputes and terms.",
     f"A written analysis, delivered within {ph('X')} working days of receiving your documents."),
    ("Recommend", "We set out the options: renegotiate, change provider, adjust routing or authentication, or leave things as they are.",
     "A ranked recommendation with the trade-offs explained, in writing."),
    ("Implement", "With your approval, we run the negotiation, tender or migration with the providers involved.",
     "Agreed terms and a working set-up. You sign directly with the provider."),
    ("Review", "Rates drift and providers add fees. We keep reading your statements and tracking renewal dates.",
     "A short written update at each review, and early warning of anything that has changed."),
]

ARTICLES = [
    {
        "slug": "anatomy-of-a-card-payment-fee", "cat": "Pricing", "date": "12 October 2026", "iso": "2026-10-12",
        "title": "The anatomy of a card payment fee",
        "dek": "Every card payment carries several charges, usually rolled into a single rate. Here is what each one is, who sets it and which ones can be negotiated.",
        "body": """
<p>When a customer pays by card, your statement usually shows one number: a percentage, sometimes with a fixed amount per transaction. That number is a bundle. Understanding what is inside it is the first step to knowing whether you are paying the right price.</p>
<h2>The five components</h2>
<table>
<thead><tr><th>Charge</th><th>Who receives it</th><th>Who sets it</th><th>Negotiable?</th></tr></thead>
<tbody>
<tr><td>Interchange</td><td>The bank that issued the card</td><td>The card schemes, within regulatory caps</td><td>No</td></tr>
<tr><td>Scheme fees</td><td>Visa, Mastercard and other networks</td><td>The card schemes</td><td>No</td></tr>
<tr><td>Acquirer margin</td><td>Your acquirer or payment provider</td><td>Your contract</td><td>Yes</td></tr>
<tr><td>Gateway fees</td><td>The gateway provider</td><td>Your contract</td><td>Yes</td></tr>
<tr><td>Other charges</td><td>Usually your provider</td><td>Your contract</td><td>Mostly</td></tr>
</tbody>
</table>
<h3>Interchange</h3>
<p>Interchange is paid by your acquirer to the customer's card issuer. It varies by card type, whether the card is consumer or commercial, whether the card was present, and where the card was issued. In the EEA it is capped for most consumer cards.</p>
<h3>Scheme fees</h3>
<p>The card schemes charge for using their networks. These fees appear as many separate items and change from time to time. They are not capped.</p>
<h3>Acquirer margin</h3>
<p>This is what your acquirer keeps for processing and settling your payments. It is the main subject of negotiation, and on blended pricing it is the part you cannot see.</p>
<h3>Gateway fees</h3>
<p>The gateway connects your checkout to the acquirer. Some providers bundle it into the rate, others charge per transaction or per month.</p>
<h3>Other charges</h3>
<p>Authorisation fees, refund fees, chargeback fees, PCI compliance fees, statement fees, currency conversion and minimum monthly charges. Individually small, together often significant.</p>
<h2>What to do with this</h2>
<p>Ask your provider for an itemised statement if you do not already receive one. Then separate the pass-through costs from the margin. That margin, plus the smaller charges, is what a negotiation can change.</p>
""",
    },
    {
        "slug": "blended-or-interchange-plus-plus", "cat": "Pricing", "date": "12 October 2026", "iso": "2026-10-12",
        "title": "Blended or interchange plus plus: which pricing are you on?",
        "dek": "Two businesses with the same headline rate can pay very different amounts. The pricing model is often the reason.",
        "body": """
<p>Card processing is usually priced in one of two ways. The choice affects both what you pay and what you can see.</p>
<h2>Blended pricing</h2>
<p>You pay a single rate for every card, whatever it costs your provider. It is simple to understand and easy to forecast. The drawback is that you cannot see how much of the rate is the provider's margin, and cheaper cards subsidise more expensive ones.</p>
<h2>Interchange plus plus</h2>
<p>Interchange and scheme fees are passed through at cost, and the provider adds a stated margin on top. Statements are longer, but every component is visible, and changes in interchange or scheme fees flow through rather than being absorbed into a fixed rate.</p>
<h2>Your right to itemised information in the EEA</h2>
<p>Under the Interchange Fee Regulation (Regulation (EU) 2015/751, Article 9), acquirers must show merchant service charges separately for each category and brand of card, unless the merchant asks in writing for blended pricing. If your statement does not break charges down, you can ask for it to.</p>
<h2>Which is better?</h2>
<p>It depends on your card mix and volumes. Businesses with many debit cards and domestic customers often benefit from itemised pricing. Very small businesses sometimes prefer the simplicity of a blended rate. The only way to know is to model your own transactions under both.</p>
""",
    },
    {
        "slug": "interchange-caps-in-the-eea", "cat": "Regulation", "date": "12 October 2026", "iso": "2026-10-12",
        "title": "Interchange caps in the EEA, explained",
        "dek": "The EU caps the largest single component of most card fees. What is covered, what is not, and why it matters for your rate.",
        "body": """
<p>Interchange is the fee paid to the bank that issued your customer's card. In the European Economic Area, it is capped by law for most consumer cards.</p>
<h2>The caps</h2>
<table>
<thead><tr><th>Card</th><th>Cap</th><th>Source</th></tr></thead>
<tbody>
<tr><td>Consumer debit, issued and used in the EEA</td><td>0.2% of the transaction</td><td>Regulation (EU) 2015/751, Article 3</td></tr>
<tr><td>Consumer credit, issued and used in the EEA</td><td>0.3% of the transaction</td><td>Regulation (EU) 2015/751, Article 4</td></tr>
</tbody>
</table>
<p>Cards issued outside the EEA and used at EEA merchants are covered by separate commitments that Visa and Mastercard gave the European Commission in 2019, with different levels for card present and online payments.</p>
<h2>What is not capped</h2>
<ul>
<li>Commercial and business cards</li>
<li>Scheme fees</li>
<li>Your acquirer's margin and gateway fees</li>
<li>Three party schemes, such as American Express, which are treated differently</li>
</ul>
<h2>Why this matters</h2>
<p>Because interchange is capped and published, the remaining parts of your rate are where real differences between providers appear. Knowing your card mix, and how much of it is capped, tells you how much room there is to negotiate.</p>
<p class="fine">General information, not legal advice. Rules and their application depend on your circumstances.</p>
""",
    },
    {
        "slug": "surcharging-card-payments-in-the-eu", "cat": "Regulation", "date": "12 October 2026", "iso": "2026-10-12",
        "title": "Can you surcharge card payments in the EU?",
        "dek": "Passing card costs on to customers is tightly restricted. A short guide to what the rules allow.",
        "body": """
<p>Many businesses would like to pass some of their payment costs on to customers. In the EU, the scope to do so is limited.</p>
<h2>What PSD2 says</h2>
<p>Under the second Payment Services Directive (Directive (EU) 2015/2366, Article 62), merchants may not add a surcharge for consumer cards covered by the interchange caps, or for SEPA credit transfers and direct debits.</p>
<p>Where a surcharge is allowed, it must not exceed the direct cost the merchant bears for that payment method.</p>
<h2>National differences</h2>
<p>Member States can restrict surcharging further, and scheme rules apply on top. Before adding any surcharge, check the rules in each country where you sell.</p>
<h2>Alternatives</h2>
<p>Steering customers towards cheaper payment methods, through checkout design or by offering open banking payments, is often more effective and less risky than surcharging.</p>
<p class="fine">General information, not legal advice.</p>
""",
    },
    {
        "slug": "strong-customer-authentication-exemptions", "cat": "Performance", "date": "12 October 2026", "iso": "2026-10-12",
        "title": "Strong customer authentication: the exemptions that matter",
        "dek": "Authentication protects against fraud but adds friction. Applying the exemptions well is one of the most effective ways to lift approval rates.",
        "body": """
<p>PSD2 requires strong customer authentication for most online card payments in the EEA, usually delivered through 3D Secure. Done badly, it costs sales. Done well, it is close to invisible for genuine customers.</p>
<h2>The main exemptions</h2>
<ul>
<li><b>Low value payments</b>, below thresholds set in the regulatory technical standards.</li>
<li><b>Transaction risk analysis</b>, where your provider assesses a payment as low risk within permitted fraud levels.</li>
<li><b>Merchant initiated transactions</b>, such as subscription renewals after the first authenticated payment.</li>
<li><b>Trusted beneficiaries</b>, where a customer has added your business to an allow list with their bank.</li>
</ul>
<h2>Out of scope payments</h2>
<p>Payments where the card issuer or the acquirer is outside the EEA, and mail or telephone orders, are treated differently.</p>
<h2>What to check</h2>
<p>Which exemptions your provider requests, how often issuers accept them, and how your authentication rate compares across countries and card types. The answers are usually available from your provider's reporting, if someone asks for them.</p>
""",
    },
    {
        "slug": "why-good-payments-get-declined", "cat": "Performance", "date": "12 October 2026", "iso": "2026-10-12",
        "title": "Why good payments get declined",
        "dek": "Not every decline is fraud. Many are recoverable, and each one is a customer who wanted to pay.",
        "body": """
<p>Some declines are correct: a stolen card, a closed account, a customer with no funds. Many are not. These are often called false declines, and they are among the most expensive problems in payments because the cost is invisible.</p>
<h2>Common causes</h2>
<ul>
<li>Expired or replaced cards stored on file</li>
<li>Temporary decisions by the issuing bank</li>
<li>Authentication failures or abandoned 3D Secure challenges</li>
<li>Fraud rules set more tightly than your risk requires</li>
<li>Cross-border transactions treated cautiously by issuers</li>
</ul>
<h2>Common fixes</h2>
<ul>
<li><b>Network tokens and account updater services</b> keep stored cards current.</li>
<li><b>Retry logic</b> tries again at the right time, within card scheme rules.</li>
<li><b>Authentication tuning</b> uses exemptions where they apply.</li>
<li><b>Local acquiring</b> processes payments in the customer's country.</li>
</ul>
<h2>Where to start</h2>
<p>Ask your provider for declines broken down by reason code, card type and issuing country. The pattern usually points to the cause.</p>
""",
    },
    {
        "slug": "chargebacks-and-rolling-reserves", "cat": "Risk", "date": "12 October 2026", "iso": "2026-10-12",
        "title": "Chargebacks and rolling reserves",
        "dek": "Two of the most misunderstood terms in a payments contract, and how they affect your cash flow.",
        "body": """
<p>A chargeback is a payment reversed by the customer's bank, usually after a dispute. A rolling reserve is a share of your takings held back by your provider to cover future chargebacks. Both can have a large effect on cash flow.</p>
<h2>How chargebacks work</h2>
<p>The customer disputes a payment with their bank. The bank reverses it and your provider debits your account, usually with a fee. You can contest the dispute with evidence, and you win some of them back.</p>
<h2>Scheme monitoring programmes</h2>
<p>The card schemes run programmes that monitor dispute and fraud levels. Businesses that stay above the thresholds face fines and can lose their account. Your provider will usually act before the schemes do.</p>
<h2>Rolling reserves</h2>
<p>Common in travel, gaming, trading and other higher risk sectors. The percentage held and the holding period are commercial terms, which means they can be negotiated, especially with a clean processing history.</p>
<h2>What to check before signing</h2>
<ul>
<li>The reserve percentage and holding period</li>
<li>When and how the reserve is reviewed</li>
<li>The fees charged per chargeback</li>
<li>What happens to the reserve if you leave</li>
</ul>
""",
    },
    {
        "slug": "psd3-and-the-payment-services-regulation", "cat": "Regulation", "date": "12 October 2026", "iso": "2026-10-12",
        "title": "PSD3 and the Payment Services Regulation: what is changing",
        "dek": "The EU has agreed a new payments package. What businesses that take payments should know now.",
        "body": """
<p>The EU has agreed a revised Payment Services Directive, known as PSD3, and a new Payment Services Regulation. Together they replace much of PSD2.</p>
<h2>Timing</h2>
<p>The new rules are expected to apply from around late 2027, with transition periods for licensing. Dates and details may still change before they take effect.</p>
<h2>Expected changes</h2>
<ul>
<li>Checks that a payee's name matches the account being paid</li>
<li>More protection for consumers against certain types of fraud</li>
<li>E-money institutions brought into the payment institution regime</li>
<li>Clarifications to strong customer authentication</li>
</ul>
<h2>What it means for merchants</h2>
<p>Most of the obligations fall on payment providers, but the effects reach merchants: changes to authentication flows, refund handling and provider contracts. It is worth asking your provider how they are preparing.</p>
<p class="fine">General information, not legal advice. This article will be updated as the rules are finalised.</p>
""",
    },
    {
        "slug": "checking-a-payment-provider-in-cyprus", "cat": "Risk", "date": "12 October 2026", "iso": "2026-10-12",
        "title": "How to check a payment provider is authorised in Cyprus",
        "dek": "Before you sign with any provider, confirm it is allowed to do what it is offering.",
        "body": """
<p>In Cyprus, payment institutions and e-money institutions are authorised and supervised by the Central Bank of Cyprus, under the laws that bring PSD2 into Cypriot law.</p>
<h2>Use the public registers</h2>
<p>The Central Bank of Cyprus publishes registers of authorised payment and e-money institutions. Check the provider's name, its registration status and the services it is authorised for.</p>
<h2>Passported firms</h2>
<p>Firms authorised elsewhere in the EEA can provide services in Cyprus through passporting. Check the register in the firm's home country as well.</p>
<h2>Agents and distributors</h2>
<p>Some firms act as agents of an authorised institution. Agents should appear in the relevant register, linked to the institution they act for.</p>
<h2>Advisers</h2>
<p>Advisers such as Rumstar are different. We do not process payments, hold funds or act for a provider in the payment flow. Your contract is always with the licensed provider.</p>
""",
    },
]

FAQ = [
    ("Working with Rumstar", [
        ("How are you paid?", f"{ph('Rumstar to confirm its fee model')} Every engagement is quoted in writing before any work starts."),
        ("Do you receive commission from providers?", f"{ph('Rumstar to confirm')} Whatever the arrangement, any commercial relationship with a provider is disclosed to you before you decide anything."),
        ("What does the first conversation cost?", "Nothing. It takes about fifteen minutes and tells you whether a review is worth doing."),
        ("How long does a review take?", f"{ph('X')} working days from receiving your documents. Set-ups with several providers or currencies take longer."),
        ("What do you need from us?", 'Recent processing statements, your current contracts and pricing schedules, and some time with whoever looks after payments. <a href="/approach/#documents">See the full list</a>.'),
        ("Is our information kept confidential?", "Yes. Your statements and contracts are used only for your engagement. We sign a confidentiality agreement on request."),
        ("Will we have to change provider?", "Often not. Renegotiating with your current provider is frequently the better route. We only recommend moving when the gain clearly outweighs the disruption."),
        ("Do you work with smaller businesses?", "Yes, where there is enough at stake for a review to be worthwhile. The first conversation tells you whether that is the case."),
        ("Where do you work?", "We are based in Nicosia, Cyprus, and work with businesses across Europe and beyond."),
    ]),
    ("About payments", [
        ("What is interchange?", 'The fee your acquirer pays to the bank that issued your customer\'s card. In the EEA it is capped for most consumer cards. <a href="/insights/interchange-caps-in-the-eea/">Read more</a>.'),
        ("What is the difference between blended and itemised pricing?", 'Blended pricing is one rate for every card. Itemised pricing passes interchange and scheme fees through at cost and adds a visible margin. <a href="/insights/blended-or-interchange-plus-plus/">Read more</a>.'),
        ("Can I ask my provider for itemised statements?", "In the EEA, yes. The Interchange Fee Regulation requires acquirers to itemise charges by card category and brand unless you ask in writing for blended pricing."),
        ("Can I add a surcharge for card payments?", 'Not for consumer cards covered by the EEA caps. Where surcharging is allowed, it cannot exceed your direct cost. <a href="/insights/surcharging-card-payments-in-the-eu/">Read more</a>.'),
        ("Why are good payments declined?", 'Expired cards, temporary issuer decisions, authentication problems and fraud rules that are too strict. <a href="/insights/why-good-payments-get-declined/">Read more</a>.'),
        ("What is a rolling reserve?", "A share of your takings held back by a provider for a period, to cover future chargebacks. Common in higher risk sectors, and negotiable."),
    ]),
    ("About Rumstar", [
        ("Are you regulated?", "Rumstar is an advisory business. We are not a payment institution or e-money institution, and we do not process payments or hold client funds. Your contracts are always with licensed providers."),
        ("Do you approve merchant accounts?", "No. Providers make their own decisions. We prepare strong applications and help you approach providers with the right appetite."),
        ("Are you a law firm?", "No. We explain the payment rules that affect you and tell you when a question needs a lawyer."),
    ]),
]
