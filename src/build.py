"""Builds the static site into ../public. Run: python3 src/build.py"""
import os, re
from layout import page, page_head, closing, redirect, ph, section_label, ARROW, SITE, STAR
from content import EXPERTISE, INDUSTRIES, PROCESS, ARTICLES, FAQ

ROOT = os.path.join(os.path.dirname(__file__), "..", "public")
EXP = {e["slug"]: e for e in EXPERTISE}
PAGES = []  # (path, priority) for the sitemap


def write(path, html, priority="0.7", sitemap=True):
    rel = path.strip("/")
    out = os.path.join(ROOT, rel, "index.html") if not rel.endswith(".html") else os.path.join(ROOT, rel)
    if path == "/":
        out = os.path.join(ROOT, "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as f:
        f.write(html)
    if sitemap:
        PAGES.append((path, priority))


def reading_time(html):
    words = len(re.sub(r"<[^>]+>", " ", html).split())
    return max(2, round(words / 220))


# ---------------------------------------------------------------- shared blocks

FEE_PARTS = [
    ("interchange", "Interchange", "fixed", 3,
     "Paid to the bank that issued your customer's card.",
     "The card schemes, within caps set by EU law for most consumer cards.",
     "No. It is passed through to the issuer.",
     "Whether your statement shows it separately, and how much of your volume is on uncapped cards."),
    ("scheme", "Scheme fees", "fixed", 2,
     "Charged by Visa, Mastercard and other networks for using their rails.",
     "The card schemes. Fees are numerous and change from time to time.",
     "No, but they should be passed through at cost, not marked up.",
     "Whether scheme fees are itemised, or quietly absorbed into a higher blended rate."),
    ("margin", "Acquirer margin", "neg", 6,
     "What your acquirer keeps for processing and settling your payments.",
     "Your contract with the acquirer or payment provider.",
     "Yes. This is the main subject of negotiation.",
     "How the margin compares with the market for a business of your size and card mix."),
    ("gateway", "Gateway charges", "neg", 2,
     "For the technology that connects your checkout to the acquirer.",
     "Your contract. Sometimes bundled, sometimes per transaction or per month.",
     "Yes, particularly at renewal or when changing provider.",
     "Whether you are paying twice for gateway services, or for features you do not use."),
    ("other", "Other processing costs", "neg", 2.5,
     "Authorisation, refund, chargeback, PCI, statement, currency conversion and minimum fees.",
     "Your contract, often in a separate schedule.",
     "Mostly. Many can be reduced or removed.",
     "The full fee schedule, including charges that only appear in some months."),
]


def anatomy():
    segs = "".join(
        f'<button type="button" class="seg seg-{k} {kind}" style="--w:{w}" data-part="{k}" aria-pressed="{str(i == 0).lower()}" aria-controls="anat-detail" aria-label="{n}"><span aria-hidden="true">{n.split()[0].replace("Acquirer", "Margin").replace("Other", "Other")}</span></button>'
        for i, (k, n, kind, w, *_r) in enumerate(FEE_PARTS))
    details = "".join(f'''
      <div class="anat-part" data-part="{k}"{"" if i == 0 else " hidden"}>
        <h3>{n}</h3>
        <p class="anat-what">{what}</p>
        <dl>
          <div><dt>Set by</dt><dd>{who}</dd></div>
          <div><dt>Negotiable</dt><dd>{neg}</dd></div>
          <div><dt>What we check</dt><dd>{check}</dd></div>
        </dl>
      </div>''' for i, (k, n, kind, w, what, who, neg, check) in enumerate(FEE_PARTS))
    return f'''<figure class="anatomy">
  <figcaption class="anat-cap"><span>Anatomy of a payment fee</span><span>Select a component</span></figcaption>
  <div class="anat-rate" aria-hidden="true">One rate on your statement</div>
  <div class="anat-bar" role="group" aria-label="Components of a card payment fee">{segs}</div>
  <div class="anat-key"><span class="k-fixed">Set by the card schemes</span><span class="k-neg">Set by your contract</span></div>
  <div class="anat-detail" id="anat-detail" aria-live="polite">{details}
  </div>
  <p class="fine">Proportions are illustrative and not to scale. The real mix depends on your card types, channels and contract.</p>
</figure>'''


def expertise_rows(link_text="Explore"):
    rows = "".join(f'''
  <a class="xrow" href="/expertise/{e["slug"]}/">
    <span class="xrow-num">{e["num"]}</span>
    <span class="xrow-title">{e["title"]}</span>
    <span class="xrow-text">{e["short"]}</span>
    <span class="xrow-go">{link_text} {ARROW}</span>
  </a>''' for e in EXPERTISE)
    return f'<div class="xrows">{rows}\n</div>'


def process_list(detailed=False):
    items = []
    for i, (name, what, get) in enumerate(PROCESS, 1):
        items.append(f'''
    <li class="step">
      <span class="step-num">{i:02d}</span>
      <h3>{name}</h3>
      <p>{what}</p>
      <p class="step-get"><span>You receive</span>{get}</p>
    </li>''')
    return f'<ol class="steps{" steps-v" if detailed else ""}">{"".join(items)}\n  </ol>'


def article_card(a, size=""):
    return f'''<article class="acard {size}">
    <a href="/insights/{a["slug"]}/">
      <p class="meta"><span class="cat">{a["cat"]}</span><time datetime="{a["iso"]}">{a["date"]}</time></p>
      <h3>{a["title"]}</h3>
      <p>{a["dek"]}</p>
      <span class="more">Read the guide {ARROW}</span>
    </a>
  </article>'''


# ---------------------------------------------------------------- home

def home():
    industries = "".join(f'''
      <li class="ind-row" data-ind="{i}">
        <a href="/industries/#{k}">
          <span class="ind-num">{i + 1:02d}</span>
          <span class="ind-name">{n}</span>
          <span class="ind-short">{probs}</span>
        </a>
      </li>''' for i, (k, n, probs, how, rel) in enumerate(INDUSTRIES))
    panels = "".join(f'''
        <div class="ind-panel" data-ind="{i}"{"" if i == 0 else " hidden"}>
          <p class="ind-panel-label">The challenge</p>
          <p class="ind-panel-prob">{probs}</p>
          <p class="ind-panel-label">How the work differs</p>
          <p class="ind-panel-text">{how}</p>
          <p class="ind-panel-rel">Most relevant: {", ".join(f'<a href="/expertise/{r}/">{EXP[r]["title"]}</a>' for r in rel)}</p>
        </div>''' for i, (k, n, probs, how, rel) in enumerate(INDUSTRIES))
    lead, a2, a3 = ARTICLES[0], ARTICLES[1], ARTICLES[5]
    body = f'''
<section class="hero wrap">
  <h1 class="hero-title">
    <span class="ln"><span>Your payment provider has a&nbsp;pricing&nbsp;team.</span></span>
    <span class="ln"><span><em>You should have someone on&nbsp;yours.</em></span></span>
  </h1>
  <div class="hero-foot">
    <p class="lead reveal">Independent advice on payment costs, providers and performance, built around your business, not the interests of a processor.</p>
    <div class="actions reveal">
      <a href="/contact/" class="btn">Book a consultation {ARROW}</a>
      <a href="/expertise/" class="tlink">Explore our expertise</a>
    </div>
  </div>
  <dl class="hero-facts reveal">
    <div><dt>Based in</dt><dd>Nicosia, Cyprus</dd></div>
    <div><dt>Role</dt><dd>Advisory only. Never in the flow of funds</dd></div>
    <div><dt>First conversation</dt><dd>Free, about fifteen minutes</dd></div>
  </dl>
</section>

<section class="problem wrap" id="problem">
  {section_label("01", "The payment problem")}
  <div class="problem-grid">
    <div class="problem-copy">
      <h2 class="h2 reveal">Payments are complicated. <em>Your decisions shouldn&rsquo;t be.</em></h2>
      <p>A card payment passes through several parties, and each takes a share. Your statement compresses all of that into one rate and a monthly total, spread over pages of codes few people read.</p>
      <p>Some of those charges are set by the card schemes and capped by law. Others are commercial terms agreed once and rarely revisited. Knowing which is which is the difference between accepting your costs and managing them.</p>
      <a href="/insights/anatomy-of-a-card-payment-fee/" class="tlink">Read the full guide</a>
    </div>
    {anatomy()}
  </div>
</section>

<section class="expertise wrap" id="expertise">
  {section_label("02", "Expertise")}
  <div class="sec-head">
    <h2 class="h2 reveal">Clarity where it <em>matters.</em></h2>
    <p>Four areas of work, from the first statement review to entering a new market.</p>
  </div>
  {expertise_rows()}
</section>

<section class="indep" id="independence">
  <div class="wrap">
    {section_label("03", "Independence")}
    <div class="indep-grid">
      <h2 class="indep-title reveal">Advice that starts with <em>your</em> interests.</h2>
      <div class="indep-copy">
        <p class="indep-lead">Payment providers employ people whose job is to price their services. Most businesses have no one doing the same job in the other direction. That is the role of an independent payment consultant.</p>
        <ul class="indep-points">
          <li><b>We act for the business.</b> We do not sell processing, terminals or software, and we do not approve accounts.</li>
          <li><b>Relationships are disclosed.</b> Any commercial relationship we have with a provider is disclosed before you decide anything. {ph("Rumstar to confirm its fee model and any provider relationships")}</li>
          <li><b>Contracts stay yours.</b> You sign directly with licensed providers. We never sit between you and your money.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="process wrap" id="process">
  {section_label("04", "The process")}
  <div class="sec-head">
    <h2 class="h2 reveal">A clearer way <em>forward.</em></h2>
    <p>Five steps. You approve each one before the next begins.</p>
  </div>
  {process_list()}
  <a href="/approach/" class="tlink">How we work, in detail</a>
</section>

<section class="industries wrap" id="industries">
  {section_label("05", "Industries")}
  <div class="sec-head">
    <h2 class="h2 reveal">Every model loses money <em>in its own places.</em></h2>
    <p>A subscription business, a travel company and a trading platform face different payment problems. We start from how you sell.</p>
  </div>
  <div class="ind-grid">
    <ol class="ind-list">{industries}
    </ol>
    <aside class="ind-side" aria-live="polite">{panels}
    </aside>
  </div>
</section>

<section class="insights wrap" id="insights">
  {section_label("06", "Insights")}
  <div class="sec-head">
    <h2 class="h2 reveal">Notes on how payments <em>really</em> work.</h2>
    <a href="/insights/" class="tlink">All insights</a>
  </div>
  <div class="agrid">
  {article_card(lead, "lead")}
  <div class="agrid-side">
  {article_card(a2)}
  {article_card(a3)}
  </div>
  </div>
</section>

{closing()}'''
    write("/", page("/", "Rumstar | Independent payment consultancy, Nicosia",
                    "Independent advice on payment costs, providers and performance for businesses that take card payments. Based in Nicosia, Cyprus.",
                    body, "home"), "1.0")


# ---------------------------------------------------------------- expertise

def expertise_index():
    groups = "".join(f'''
  <article class="xgroup" id="{e["slug"]}">
    <span class="xgroup-num">{e["num"]}</span>
    <div class="xgroup-main">
      <h2><a href="/expertise/{e["slug"]}/">{e["title"]}</a></h2>
      <p>{e["short"]}</p>
    </div>
    <ul class="xgroup-list">{"".join(f"<li>{s}</li>" for s in e["services"])}</ul>
    <a class="tlink xgroup-go" href="/expertise/{e["slug"]}/">Read more</a>
  </article>''' for e in EXPERTISE)
    body = page_head("Expertise", "Advice across the <em>whole</em> payment chain.",
                     "We do not sell processing, terminals or software. We review, recommend, negotiate and oversee, in four areas that cover how a business gets paid.") + f'''
<section class="wrap xgroups">{groups}
</section>
{closing()}'''
    write("/expertise/", page("/expertise/", "Expertise | Rumstar",
                              "Payment cost optimisation, acceptance and performance, provider selection and negotiation, and risk, compliance and global payments.",
                              body), "0.9")


def expertise_page(e):
    others = [x for x in EXPERTISE if x["slug"] != e["slug"]]
    evaluate = "".join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in e["evaluate"])
    steps = "".join(f'<li><span>{i:02d}</span><h3>{a}</h3><p>{b}</p></li>' for i, (a, b) in enumerate(e["steps"], 1))
    benefits = "".join(f"<li>{b}</li>" for b in e["benefits"])
    related = "".join(f'''
      <a class="rel" href="/expertise/{x["slug"]}/"><span>{x["num"]}</span><b>{x["title"]}</b>{ARROW}</a>''' for x in others)
    note = f'<p class="note">{e["note"]}</p>' if e.get("note") else ""
    body = page_head(f'<a href="/expertise/">Expertise</a><span>{e["num"]}</span>', e["title"], e["short"],
                     f'<ul class="phead-tags">{"".join(f"<li>{s}</li>" for s in e["services"])}</ul>') + f'''
<section class="wrap svc-sec">
  <div class="svc-side"><h2 class="label"><span>A</span>The problem</h2></div>
  <div class="svc-body prose">{"".join(f"<p>{p}</p>" for p in e["problem"])}</div>
</section>
<section class="wrap svc-sec">
  <div class="svc-side"><h2 class="label"><span>B</span>What we evaluate</h2></div>
  <dl class="svc-body eval">{evaluate}</dl>
</section>
<section class="wrap svc-sec">
  <div class="svc-side"><h2 class="label"><span>C</span>How we approach it</h2></div>
  <ol class="svc-body mini-steps">{steps}</ol>
</section>
<section class="wrap svc-sec">
  <div class="svc-side"><h2 class="label"><span>D</span>What it can mean for your business</h2></div>
  <div class="svc-body"><ul class="benefits">{benefits}</ul>{note}</div>
</section>
<section class="wrap svc-sec">
  <div class="svc-side"><h2 class="label"><span>E</span>Related expertise</h2></div>
  <div class="svc-body rels">{related}
  </div>
</section>
{closing("Start with a conversation.", "Fifteen minutes is usually enough to tell whether there is something worth changing.")}'''
    write(f'/expertise/{e["slug"]}/', page(f'/expertise/{e["slug"]}/', f'{e["title"]} | Rumstar', e["short"], body), "0.8")


# ---------------------------------------------------------------- industries

def industries():
    index = "".join(f'<li><a href="#{k}">{n}</a></li>' for k, n, *_ in INDUSTRIES)
    blocks = "".join(f'''
  <article class="sector" id="{k}">
    <p class="sector-num">{i:02d}</p>
    <h2>{n}</h2>
    <div class="sector-cols">
      <div><h3>The challenge</h3><p>{probs}</p></div>
      <div><h3>How our work differs</h3><p>{how}</p></div>
    </div>
    <p class="sector-rel">{" ".join(f'<a class="chip" href="/expertise/{r}/">{EXP[r]["title"]}</a>' for r in rel)}</p>
  </article>''' for i, (k, n, probs, how, rel) in enumerate(INDUSTRIES, 1))
    body = page_head("Industries", "Different businesses, <em>different</em> payment problems.",
                     "We start from how you sell, then look at what you pay. These are the sectors we work with most, and what tends to matter in each.") + f'''
<section class="wrap sectors">
  <nav class="sector-index" aria-label="Industries on this page"><p>Sectors</p><ol>{index}</ol></nav>
  <div class="sector-list">{blocks}
    <aside class="aside-note">
      <h2>A note on higher risk sectors</h2>
      <p>Some sectors need a licence before any provider will consider them, and providers make their own approval decisions. We tell you early if your model raises a licensing question, so it reaches your legal advisers before it costs you time.</p>
    </aside>
    <aside class="aside-note">
      <h2>Based in Nicosia</h2>
      <p>Cyprus is home to many trading, gaming and fintech businesses. We are based here and focused on the questions EU and Cypriot rules raise for them, while working with businesses wherever they sell.</p>
    </aside>
  </div>
</section>
{closing()}'''
    write("/industries/", page("/industries/", "Industries | Rumstar",
                               "Payment advice for ecommerce, subscriptions, travel, iGaming, forex and trading, marketplaces, digital goods and other specialist sectors.",
                               body), "0.8")


# ---------------------------------------------------------------- approach

def approach():
    body = page_head("Our Approach", "From first conversation to <em>signed</em> contract.",
                     "You remain the decision maker throughout. We do the reading, comparing and chasing, and we put everything in writing.") + f'''
<section class="wrap approach-steps">
  <h2 class="sr">The five steps</h2>
  {process_list(detailed=True)}
</section>

<section class="wrap principles">
  {section_label("A", "Method")}
  <div class="sec-head"><h2 class="h2 reveal">How we work, <em>on every engagement.</em></h2></div>
  <dl class="pgrid">
    <div><dt>Numbers before opinions</dt><dd>Every recommendation starts from your statements and contracts, not from a provider's pitch.</dd></div>
    <div><dt>Disclosed, always</dt><dd>Any commercial relationship we have with a provider is disclosed before you decide anything.</dd></div>
    <div><dt>In writing</dt><dd>Findings, recommendations and offers are written down, so you can check them and keep them.</dd></div>
    <div><dt>Confidential</dt><dd>Your documents are used only for your engagement. We sign a confidentiality agreement on request.</dd></div>
    <div><dt>Never in the money flow</dt><dd>We do not process payments or hold funds. Money moves only between you, your customers and licensed providers.</dd></div>
    <div><dt>Honest about the gap</dt><dd>If there is not enough to gain, we say so after the first conversation, including when that means not hiring us.</dd></div>
  </dl>
</section>

<section class="wrap docs" id="documents">
  {section_label("B", "What we need")}
  <div class="docs-grid">
    <div>
      <h2 class="h3">For a cost or performance review</h2>
      <ul class="dash">
        <li>Your last three months of processing statements, from every provider</li>
        <li>Your current contracts and pricing schedules</li>
        <li>Chargeback, fraud and decline reports, if available</li>
        <li>Your website and a description of your checkout</li>
        <li>Time with whoever looks after payments</li>
      </ul>
    </div>
    <div>
      <h2 class="h3">For a new account application</h2>
      <ul class="dash">
        <li>Company registration documents</li>
        <li>Identity documents for directors and main shareholders</li>
        <li>Proof of business address</li>
        <li>Processing history, where you have it</li>
        <li>Any licences your sector requires</li>
        <li>Your website, with terms, refund policy and contact details visible</li>
      </ul>
    </div>
  </div>
</section>

<section class="wrap scenarios">
  {section_label("C", "Practical examples")}
  <div class="sec-head">
    <h2 class="h2 reveal">What an engagement <em>can look like.</em></h2>
    <p>Illustrative scenarios showing how the process applies. They are not client cases.</p>
  </div>
  <div class="scen">
    <article>
      <h3>A subscription business losing renewals</h3>
      <p><b>Discover.</b> Renewals fail more often than expected, and customers are lost without cancelling.</p>
      <p><b>Analyse.</b> Decline reasons, card updater coverage, retry timing and the exemptions requested on renewals.</p>
      <p><b>Recommend.</b> Network tokens, retry logic within scheme rules, and correct flagging of merchant initiated payments.</p>
    </article>
    <article>
      <h3>An online retailer on an old blended rate</h3>
      <p><b>Discover.</b> One rate agreed years ago, never reviewed, with a contract that renews automatically.</p>
      <p><b>Analyse.</b> Card mix, pass-through costs, margin and the full fee schedule against the market.</p>
      <p><b>Recommend.</b> Itemised pricing, a renegotiation with the current provider and a tender as the fallback.</p>
    </article>
    <article>
      <h3>A trading platform needing a new provider</h3>
      <p><b>Discover.</b> A provider has given notice, and the sector limits the options.</p>
      <p><b>Analyse.</b> Licences, processing history, website compliance and the controls providers will ask about.</p>
      <p><b>Recommend.</b> A complete application file and a shortlist of providers with appetite for the sector.</p>
    </article>
  </div>
</section>
{closing()}'''
    write("/approach/", page("/approach/", "Our Approach | Rumstar",
                             "How Rumstar works: discover, analyse, recommend, implement and review. Plus our method, the documents we need and illustrative examples.",
                             body), "0.8")


# ---------------------------------------------------------------- insights

def insights_index():
    cats = sorted({a["cat"] for a in ARTICLES})
    filters = '<button type="button" aria-pressed="true" data-cat="all">All</button>' + "".join(
        f'<button type="button" aria-pressed="false" data-cat="{c}">{c}</button>' for c in cats)
    rows = "".join(f'''
  <li class="arow" data-cat="{a["cat"]}">
    <a href="/insights/{a["slug"]}/">
      <span class="arow-meta"><span class="cat">{a["cat"]}</span><time datetime="{a["iso"]}">{a["date"]}</time></span>
      <span class="arow-title">{a["title"]}</span>
      <span class="arow-dek">{a["dek"]}</span>
      <span class="arow-time">{reading_time(a["body"])} min read</span>
    </a>
  </li>''' for a in ARTICLES)
    body = page_head("Insights", "Notes on how payments <em>really</em> work.",
                     "Plain guides to fees, pricing, regulation, performance and risk. Written for the people who sign the contracts.") + f'''
<section class="wrap ilist">
  <div class="filters" role="group" aria-label="Filter by topic">{filters}</div>
  <ol class="arows">{rows}
  </ol>
</section>
{closing()}'''
    write("/insights/", page("/insights/", "Insights | Rumstar",
                             "Guides to card payment fees, pricing models, EU payment regulation, approval rates, chargebacks and reserves.",
                             body), "0.8")


def article(a, i):
    related = [x for x in ARTICLES if x["cat"] == a["cat"] and x is not a][:2]
    if len(related) < 2:
        related += [x for x in ARTICLES if x is not a and x not in related][:2 - len(related)]
    prev_a, next_a = ARTICLES[i - 1] if i > 0 else None, ARTICLES[i + 1] if i < len(ARTICLES) - 1 else None
    body_html = a["body"].replace("<table>", '<div class="tbl"><table>').replace("</table>", "</table></div>")
    toc = re.findall(r"<h2>(.*?)</h2>", a["body"])
    toc_html = "".join(f'<li><a href="#s{n}">{t}</a></li>' for n, t in enumerate(toc, 1))
    n = iter(range(1, 100))
    body_html = re.sub(r"<h2>", lambda m: f'<h2 id="s{next(n)}">', body_html)
    pager = "".join([
        f'<a class="pg prev" href="/insights/{prev_a["slug"]}/"><span>Previous</span><b>{prev_a["title"]}</b></a>' if prev_a else "<span></span>",
        f'<a class="pg next" href="/insights/{next_a["slug"]}/"><span>Next</span><b>{next_a["title"]}</b></a>' if next_a else "<span></span>",
    ])
    body = f'''
<article class="art">
  <header class="art-head wrap">
    <p class="crumb"><a href="/insights/">Insights</a><span>{a["cat"]}</span></p>
    <h1 class="art-title reveal">{a["title"]}</h1>
    <p class="lead reveal">{a["dek"]}</p>
    <p class="art-meta"><time datetime="{a["iso"]}">{a["date"]}</time><span>{reading_time(a["body"])} min read</span><span>Rumstar</span></p>
  </header>
  <div class="art-grid wrap">
    <aside class="art-toc"><p>In this guide</p><ol>{toc_html}</ol></aside>
    <div class="art-body prose">{body_html}
      <div class="art-cta">
        <p>Want to know how this applies to your business?</p>
        <a class="tlink" href="/contact/">Talk to Rumstar</a>
      </div>
    </div>
  </div>
  <nav class="pager wrap" aria-label="More guides">{pager}</nav>
</article>
<section class="wrap related">
  <p class="label"><span>&nbsp;</span>Related guides</p>
  <div class="agrid-2">{"".join(article_card(x) for x in related)}</div>
</section>'''
    write(f'/insights/{a["slug"]}/', page(f'/insights/{a["slug"]}/', f'{a["title"]} | Rumstar Insights', a["dek"], body, "article-page"), "0.7")


# ---------------------------------------------------------------- about, faq, contact, legal

def about():
    body = page_head("About", "An independent voice on <em>how you get paid.</em>",
                     "Rumstar is a payment consultancy based in Nicosia, Cyprus, founded in 2026 to help businesses pay less to take payments, lose fewer of them and understand the rules that apply.") + f'''
<section class="wrap about">
  <div class="about-story prose">
    <h2>Why Rumstar exists</h2>
    <p>Payment providers know their pricing far better than the businesses they charge. Statements are long, fees are spread across dozens of lines, and contracts renew quietly. Most businesses never have anyone on their side read them.</p>
    <p>Rumstar was set up to do that job: to read the statements, compare the market, negotiate the terms and oversee the work, then keep checking so the gains last.</p>
    <h2>How we stay on your side</h2>
    <p>We recommend what suits your business. Any commercial relationship we have with a provider is disclosed to you before you decide anything. {ph("Rumstar to confirm its fee model and any provider relationships")}</p>
    <h2>What we are not</h2>
    <ul>
      <li>We are not a payment institution or e-money institution.</li>
      <li>We do not process payments or hold client money.</li>
      <li>We do not approve or open accounts. Licensed providers do.</li>
      <li>We are not a law firm. Where a question needs legal advice, we say so.</li>
    </ul>
    <p>You can check any payment provider against the public registers kept by the <a href="https://www.centralbank.cy" rel="noopener">Central Bank of Cyprus</a>.</p>
  </div>
  <aside class="about-side">
    <div class="person">
      <p class="label"><span>&nbsp;</span>Leadership</p>
      <h2>Michalis Vassiliou</h2>
      <p class="role">Director</p>
      <p>{ph("Biography and payments background")}</p>
    </div>
    <dl class="company">
      <p class="label"><span>&nbsp;</span>Company</p>
      <div><dt>Legal name</dt><dd>RUMSTAR LIMITED</dd></div>
      <div><dt>Registration no.</dt><dd>HE 498715</dd></div>
      <div><dt>Registered in</dt><dd>Republic of Cyprus</dd></div>
      <div><dt>Founded</dt><dd>2026</dd></div>
      <div><dt>Registered office</dt><dd>84 Larnakos, Pallouriotissa, 1046 Nicosia, Cyprus</dd></div>
    </dl>
  </aside>
</section>
{closing()}'''
    write("/about/", page("/about/", "About | Rumstar",
                          "Rumstar Limited is an independent payment consultancy in Nicosia, Cyprus. Advisory only: not a payment institution and never in the flow of funds.",
                          body), "0.7")


def faq():
    groups = "".join(f'''
  <div class="faq-group">
    <h2 class="h3">{title}</h2>
    <div class="qs">{"".join(f"""
      <details><summary>{q}<i aria-hidden="true"></i></summary><p>{a}</p></details>""" for q, a in qs)}
    </div>
  </div>''' for title, qs in FAQ)
    body = page_head("Questions", "Questions, <em>answered plainly.</em>",
                     "What people ask before working with us, and the payment questions we hear most often.") + f'''
<section class="wrap faq">{groups}
</section>
{closing()}'''
    write("/faq/", page("/faq/", "Questions | Rumstar",
                        "Answers about working with Rumstar, payment fees, surcharging, declines, reserves and our regulatory status.", body), "0.6")


def contact():
    opts = lambda name, items, kind="radio": "".join(
        f'<label class="opt"><input type="{kind}" name="{name}" value="{o}"><span>{o}</span></label>' for o in items)
    body = page_head("Contact", "Start a <em>conversation.</em>",
                     "Tell us a little about how you take payments today. We will reply to arrange a first conversation, which is free and takes about fifteen minutes.") + f'''
<section class="wrap contact">
  <form class="cform" id="cform" novalidate>
    <div class="fgrid">
      <label class="f"><span>Full name <b aria-hidden="true">*</b></span><input name="Name" autocomplete="name" required><em class="ferr">Please enter your name.</em></label>
      <label class="f"><span>Work email <b aria-hidden="true">*</b></span><input name="Email" type="email" autocomplete="email" required><em class="ferr">Please enter a valid email address.</em></label>
      <label class="f"><span>Company <b aria-hidden="true">*</b></span><input name="Company" autocomplete="organization" required><em class="ferr">Please enter your company name.</em></label>
      <label class="f"><span>Website</span><input name="Website" type="url" inputmode="url" placeholder="https://"><em class="ferr">Please enter a full address, starting with https://</em></label>
    </div>
    <fieldset class="fs">
      <legend>Type of business</legend>
      <div class="opts">{opts("Business type", ["Ecommerce or retail", "Subscriptions or SaaS", "Travel or hospitality", "iGaming or betting", "Forex or trading", "Marketplace or platform", "Digital goods", "Other"])}</div>
    </fieldset>
    <fieldset class="fs">
      <legend>What would you like help with?</legend>
      <div class="opts">{opts("Help with", ["Payment costs", "Approval rates", "Choosing a provider", "Changing provider", "Chargebacks or fraud", "Compliance", "A higher risk account", "Not sure yet"], "checkbox")}</div>
    </fieldset>
    <label class="f f-wide"><span>Anything else we should know?</span><textarea name="Message" rows="5"></textarea></label>
    <div class="cform-foot">
      <button type="submit" class="btn">Send enquiry {ARROW}</button>
      <p class="fine">Sending opens your email application with your enquiry addressed to onboarding@rumstar.eu. We use your details only to reply.</p>
    </div>
    <p class="form-msg" role="status" tabindex="-1" hidden></p>
  </form>
  <aside class="contact-side">
    <dl>
      <div><dt>New enquiries</dt><dd><a href="mailto:onboarding@rumstar.eu">onboarding@rumstar.eu</a></dd></div>
      <div><dt>Existing clients</dt><dd><a href="mailto:support@rumstar.eu">support@rumstar.eu</a></dd></div>
      <div><dt>Telephone</dt><dd><a href="tel:+35797692104">+357 97 692104</a></dd></div>
      <div><dt>Office</dt><dd>84 Larnakos, Pallouriotissa<br>1046 Nicosia, Cyprus</dd></div>
      <div><dt>Response</dt><dd>We reply within {ph("response time")}</dd></div>
    </dl>
    <p class="contact-tip">Having recent processing statements to hand makes the first conversation far more useful. <a class="tlink" href="/approach/#documents">What we need</a></p>
  </aside>
</section>'''
    write("/contact/", page("/contact/", "Contact | Rumstar",
                            "Start a conversation with Rumstar about payment costs, providers, approval rates or compliance.", body, "contact-page"), "0.8")


def legal(path, title):
    body = page_head("Legal", title, "This page is being prepared.") + f'''
<section class="wrap prose legal">
  <p>{ph(f"{title} to be provided by Rumstar's legal adviser")}</p>
  <p>Questions in the meantime can be sent to <a href="mailto:support@rumstar.eu">support@rumstar.eu</a>.</p>
</section>'''
    write(path, page(path, f"{title} | Rumstar", f"{title} for rumstar.eu.", body, noindex=True), sitemap=False)


def not_found():
    body = page_head("Page not found", "This page <em>has moved</em> or no longer exists.",
                     "The site was recently reorganised. These are good places to start.",
                     '<div class="actions"><a class="btn" href="/">Home</a><a class="tlink" href="/expertise/">Expertise</a><a class="tlink" href="/insights/">Insights</a></div>')
    with open(os.path.join(ROOT, "404.html"), "w") as f:
        f.write(page("/404.html", "Page not found | Rumstar", "Page not found.", body, noindex=True))


def build():
    home()
    expertise_index()
    for e in EXPERTISE:
        expertise_page(e)
    industries()
    approach()
    insights_index()
    for i, a in enumerate(ARTICLES):
        article(a, i)
    about()
    faq()
    contact()
    legal("/privacy/", "Privacy policy")
    legal("/terms/", "Terms of use")
    legal("/cookies/", "Cookie policy")
    not_found()
    # Old single-file URLs from the previous site
    for old, new in {"services.html": "/expertise/", "how-we-work.html": "/approach/", "industries.html": "/industries/",
                     "guide.html": "/insights/", "about.html": "/about/", "faq.html": "/faq/", "contact.html": "/contact/"}.items():
        with open(os.path.join(ROOT, old), "w") as f:
            f.write(redirect(new))
    urls = "".join(f"<url><loc>{SITE}{p}</loc><priority>{pr}</priority></url>" for p, pr in PAGES)
    with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    with open(os.path.join(ROOT, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    with open(os.path.join(ROOT, "favicon.svg"), "w") as f:
        f.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" fill="#F5F3EE"/><g fill="#762F3C" transform="translate(4 4) scale(.75)">{STAR}</g></svg>')
    # Copy guard: no em dashes or banned phrases in any generated page
    banned = re.compile(r"—|\bseamless|\belevate|\bunlock|\bempower|\bleverag|cutting.edge|next.generation|holistic|synergy|\bsolutions?\b|\btransform|\bjourney|\becosystem|\brobust|\binnovative", re.I)
    for dirpath, _, files in os.walk(ROOT):
        for name in files:
            if name.endswith(".html"):
                text = re.sub(r"<[^>]+>", " ", open(os.path.join(dirpath, name)).read())
                hits = set(banned.findall(text))
                if hits:
                    print("COPY CHECK", os.path.join(dirpath, name), hits)
    print(f"built {len(PAGES)} indexed pages")


if __name__ == "__main__":
    build()
