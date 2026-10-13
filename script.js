const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
document.documentElement.classList.add('js');
const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];

// Navigation: highlight every link that points at the current page (header, menu, button, footer).
// Matches on the page name so it works with or without ".html" (Netlify serves both).
const pageName = (path) => (path.replace(/\/+$/, '').split('/').pop() || 'index').replace(/\.html$/, '');
const here = pageName(location.pathname);
$$('#site-nav a, .top .pill, .foot-explore a').forEach(a => {
  if (pageName(new URL(a.href).pathname) === here) a.setAttribute('aria-current', 'page');
  else a.removeAttribute('aria-current');
});

// Mobile menu
const menuBtn = $('.menu-btn');
const siteNav = $('#site-nav');
if (menuBtn && siteNav) {
  const setMenu = (open) => { siteNav.classList.toggle('open', open); menuBtn.setAttribute('aria-expanded', open); };
  menuBtn.addEventListener('click', () => setMenu(menuBtn.getAttribute('aria-expanded') !== 'true'));
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') setMenu(false); });
  siteNav.addEventListener('click', (e) => { if (e.target.closest('a')) setMenu(false); });
  $$('a', siteNav).forEach((a, i) => a.style.setProperty('--i', i));
}

// Hero routing: each illustrative example lights its route (input node -> output node)
// and sends one transaction along it. Runs only while the illustration is on screen.
const router = $('.router');
const readout = $('.readout');
const routes = [
  ['Card payment routed to the lowest cost acquirer', 0, 0],
  ['Apple Pay payment approved first time', 1, 1],
  ['Open banking payment, no card fees applied', 2, 1],
  ['Card payment screened for fraud before it reaches the acquirer', 0, 2],
  ['Declined card retried on a backup acquirer, approved', 0, 0],
  ['Subscription renewal, card details updated automatically', 0, 1],
];
if (router && readout) {
  const ins = $$('.paths path', router).slice(0, 3), outs = $$('.paths path', router).slice(3);
  const nodes = $$('.nodes > g', router);
  const [lineIn, lineOut] = $$('.route-line', router), [txIn, txOut] = $$('.tx', router);
  let ri = 0, timer = null;
  const show = (i) => {
    const [text, a, b] = routes[i];
    lineIn.setAttribute('d', ins[a].getAttribute('d')); txIn.setAttribute('d', ins[a].getAttribute('d'));
    lineOut.setAttribute('d', outs[b].getAttribute('d')); txOut.setAttribute('d', outs[b].getAttribute('d'));
    nodes.forEach((n, j) => n.classList.toggle('hot', j === a || j === 3 + b));
    router.classList.add('routing');
    router.classList.remove('fire'); void router.getBoundingClientRect(); router.classList.add('fire');
    readout.classList.add('swap');
    setTimeout(() => { readout.textContent = text; readout.classList.remove('swap'); }, 300);
  };
  const tick = () => { show(ri); ri = (ri + 1) % routes.length; };
  if (reduced) show(0);
  else new IntersectionObserver(([e]) => {
    clearInterval(timer); timer = null;
    if (e.isIntersecting) { tick(); timer = setInterval(tick, 3600); }
  }, { threshold: 0.3 }).observe(router);
}

// Fee bar: segments grow in once, then hover, focus or tap a charge to pick it out
const fee = $('.fee-panel');
if (fee) {
  const segs = $$('.seg', fee), items = $$('.legend li', fee), tip = $('.fee-tip', fee);
  segs.forEach((s, i) => s.style.setProperty('--k', i));
  new IntersectionObserver(([e], obs) => {
    if (!e.isIntersecting) return;
    const total = segs.reduce((sum, x) => sum + +x.dataset.v, 0);
    segs.forEach(s => s.style.width = (s.dataset.v / total * 100) + '%');
    obs.disconnect();
  }, { threshold: 0.35 }).observe(fee);
  let picked = null;
  const pick = (k) => {
    picked = k;
    fee.classList.toggle('picking', k !== null);
    segs.forEach(s => s.classList.toggle('on', s.dataset.k === k));
    items.forEach(li => li.classList.toggle('on', li.dataset.k === k));
    if (k === null) return;
    const seg = segs[k];
    tip.textContent = $('b', items[k]).textContent;
    tip.style.left = `${seg.offsetLeft + seg.offsetWidth / 2}px`;
  };
  [...segs, ...items].forEach(el => {
    el.addEventListener('pointerenter', (e) => { if (e.pointerType === 'mouse') pick(el.dataset.k); });
    el.addEventListener('pointerleave', (e) => { if (e.pointerType === 'mouse') pick(null); });
    el.addEventListener('click', () => pick(picked === el.dataset.k ? null : el.dataset.k));
  });
  items.forEach(li => {
    li.addEventListener('focus', () => pick(li.dataset.k));
    li.addEventListener('blur', () => pick(null));
  });
  document.addEventListener('click', (e) => { if (!fee.contains(e.target)) pick(null); });
}

// Process lines: fill with scroll position, light each step once it is reached
const progressLists = $$('[data-progress]');
if (progressLists.length) {
  let queued = false;
  const update = () => {
    queued = false;
    const anchor = innerHeight * 0.7;
    progressLists.forEach(list => {
      const r = list.getBoundingClientRect(), lis = $$(':scope > li', list), n = lis.length;
      const horizontal = lis.length > 1 && lis[0].offsetTop === lis[1].offsetTop;
      const p = reduced ? 1 : Math.min(1, Math.max(0, (anchor - r.top) / r.height));
      list.style.setProperty('--p', p);
      let now = -1;
      lis.forEach((li, i) => {
        const on = reduced || (horizontal ? p * n > i : li.getBoundingClientRect().top < anchor);
        li.classList.toggle('on', on);
        li.style.setProperty('--f', Math.min(1, Math.max(0, p * n - i)));
        if (on) now = i;
      });
      lis.forEach((li, i) => li.classList.toggle('now', i === now && p < 1));
    });
  };
  const queue = () => { if (!queued) { queued = true; requestAnimationFrame(update); } };
  addEventListener('scroll', queue, { passive: true });
  addEventListener('resize', queue);
  update();
}

// Services tabs (home page)
const services = [
  ['Every line of your statement, explained.', 'We take your recent statements and break down every charge: interchange, scheme fees, margin, gateway and the small extras that add up. You get a plain list of what you pay and what you should pay.', ['Statement teardown', 'Benchmark against the market', 'Findings in writing']],
  ['The right provider, on the right terms.', 'We shortlist acquirers, gateways and payment providers that fit your volumes, markets and checkout, run the tender and negotiate the contract. You sign it. We read it first.', ['Shortlist and tender', 'Contract negotiation', 'Small print review']],
  ['Stop losing sales to declines.', 'A declined payment is a lost customer. We find out why yours are failing and fix it with smarter routing, retries, card updater services and the right authentication settings.', ['Decline analysis', 'Routing and retries', '3D Secure tuning']],
  ['Switch provider without losing a day of trading.', 'We plan the move, coordinate the providers\' teams and test everything before go live. Your customers should not notice anything changed.', ['Migration plan', 'Token and data transfer', 'Go live support']],
  ['Stronger applications for specialist sectors.', 'Gaming, trading, travel and other high-risk sectors face fewer willing providers. We prepare a complete application file and help you approach providers with the right appetite.', ['Application file', 'Provider shortlist', 'Terms explained']],
];
const tabs = $$('[role=tab]');
const panel = $('#panel');
const tabInd = $('.tab-ind');
let current = 0, swapTimer;
const moveInd = () => {
  if (!tabInd) return;
  const t = tabs[current];
  tabInd.style.transform = `translateY(${t.offsetTop}px)`;
  tabInd.style.height = `${t.offsetHeight}px`;
};
if (tabInd && tabs.length) {
  tabInd.parentElement.classList.add('has-ind');
  moveInd();
  addEventListener('resize', moveInd);
  document.fonts?.ready.then(moveInd);
}
function select(i, focus) {
  if (i === current && !focus) return;
  current = i;
  tabs.forEach((t, j) => { t.setAttribute('aria-selected', j === i); t.tabIndex = j === i ? 0 : -1; });
  moveInd();
  const [h, p, tags] = services[i];
  panel.setAttribute('aria-labelledby', tabs[i].id);
  clearTimeout(swapTimer);
  panel.classList.add('leaving');
  swapTimer = setTimeout(() => {
    panel.innerHTML = `<h3>${h}</h3><p>${p}</p><ul>${tags.map(t => `<li>${t}</li>`).join('')}</ul>`;
    panel.classList.remove('leaving');
  }, reduced ? 0 : 140);
  if (focus) tabs[i].focus();
}
if (panel) tabs.forEach((t, i) => {
  t.addEventListener('click', () => select(i));
  t.addEventListener('keydown', (e) => {
    const n = { ArrowDown: i + 1, ArrowRight: i + 1, ArrowUp: i - 1, ArrowLeft: i - 1, Home: 0, End: tabs.length - 1 }[e.key];
    if (n === undefined) return;
    e.preventDefault();
    select((n + tabs.length) % tabs.length, true);
  });
});

// Highlight the current section in a page's contents list
const tocLinks = $$('.toc a');
if (tocLinks.length) {
  const byId = new Map(tocLinks.map(a => [a.hash.slice(1), a]));
  const spy = new IntersectionObserver((entries) => entries.forEach(e => {
    if (!e.isIntersecting) return;
    tocLinks.forEach(a => a.classList.remove('active'));
    byId.get(e.target.id)?.classList.add('active');
  }), { rootMargin: '-20% 0px -70% 0px' });
  byId.forEach((_, id) => { const el = document.getElementById(id); if (el) spy.observe(el); });
  tocLinks.forEach(a => a.addEventListener('click', () => {
    tocLinks.forEach(x => x.classList.remove('active'));
    a.classList.add('active');
  }));
  const list = $('.toc ol');
  const marker = document.createElement('span');
  marker.className = 'toc-marker';
  marker.setAttribute('aria-hidden', 'true');
  list.appendChild(marker);
  const move = () => {
    const a = $('.toc a.active');
    if (!a || !matchMedia('(min-width: 1000px)').matches) { marker.style.opacity = 0; return; }
    marker.style.top = `${a.offsetTop}px`;
    marker.style.height = `${a.offsetHeight}px`;
    marker.style.opacity = 1;
  };
  new MutationObserver(move).observe(list, { subtree: true, attributes: true, attributeFilter: ['class'] });
  addEventListener('resize', move);
}

// Industry cards: staggered entrance, then a pointer spotlight and gentle tilt
const sectorGrid = $('.sector-grid');
if (sectorGrid) {
  const cards = $$('.sector', sectorGrid);
  cards.forEach((c, i) => c.style.setProperty('--i', i));
  new IntersectionObserver(([e], obs) => {
    if (!e.isIntersecting) return;
    sectorGrid.classList.add('in');
    setTimeout(() => sectorGrid.classList.add('settled'), cards.length * 90 + 1000);
    obs.disconnect();
  }, { threshold: 0.1 }).observe(sectorGrid);
  const canHover = matchMedia('(hover: hover)').matches;
  cards.forEach(c => {
    c.addEventListener('pointermove', (e) => {
      const r = c.getBoundingClientRect();
      const x = (e.clientX - r.left) / r.width, y = (e.clientY - r.top) / r.height;
      c.style.setProperty('--mx', `${x * 100}%`);
      c.style.setProperty('--my', `${y * 100}%`);
      if (reduced || !canHover) return;
      c.classList.add('live');
      c.style.transform = `rotateX(${(0.5 - y) * 6}deg) rotateY(${(x - 0.5) * 8}deg) translateY(-4px)`;
    });
    c.addEventListener('pointerleave', () => { c.classList.remove('live'); c.style.transform = ''; });
  });
}

// Guide page: 3D card follows the pointer, sections tilt in, reading progress, contents marker
if (document.body.classList.contains('guide-page')) {
  const rot = $('.stack-rot');
  if (rot && !reduced && matchMedia('(hover: hover)').matches) {
    addEventListener('pointermove', (e) => {
      const x = e.clientX / innerWidth - 0.5, y = e.clientY / innerHeight - 0.5;
      rot.style.setProperty('--rz', `${-34 + x * 24}deg`);
      rot.style.setProperty('--rx', `${56 - y * 18}deg`);
    }, { passive: true });
  }
  const secs = $$('.g-sec');
  secs.forEach(sec => $$('.terms div', sec).forEach((d, i) => d.style.setProperty('--i', i)));
  const reveal = new IntersectionObserver((entries) => entries.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('in'); reveal.unobserve(e.target); }
  }), { threshold: 0.08 });
  secs.forEach(sec => reveal.observe(sec));
  const bar = $('.read-progress i');
  const onScroll = () => {
    const max = document.documentElement.scrollHeight - innerHeight;
    bar.style.setProperty('--p', max > 0 ? scrollY / max : 0);
  };
  addEventListener('scroll', onScroll, { passive: true });
  onScroll();
  // Fee layers: the keys under the card and the rows in "What you actually pay" both pick a layer
  const stack = $('.stack3d'), cap = $('.lyr-cap');
  if (stack && cap) {
    const keys = $$('.lyr-key', stack), rows = $$('.terms div[data-k]');
    const text = Object.fromEntries(rows.map(r => [r.dataset.k, `${$('dt', r).textContent}: ${$('dd', r).textContent}`]));
    const idle = cap.textContent;
    let picked = null;
    const pick = (k) => {
      picked = k;
      stack.classList.toggle('picking', k !== null);
      $$('.lyr', stack).forEach(l => l.classList.toggle('on', l.dataset.k === k));
      keys.forEach(b => b.setAttribute('aria-pressed', b.dataset.k === k));
      rows.forEach(r => r.classList.toggle('on', r.dataset.k === k));
      cap.classList.add('swap');
      setTimeout(() => { cap.textContent = k ? text[k] : idle; cap.classList.remove('swap'); }, reduced ? 0 : 150);
    };
    keys.forEach(b => b.addEventListener('click', () => pick(picked === b.dataset.k ? null : b.dataset.k)));
    rows.forEach(r => {
      r.addEventListener('pointerenter', (e) => { if (e.pointerType === 'mouse') pick(r.dataset.k); });
      r.addEventListener('pointerleave', (e) => { if (e.pointerType === 'mouse') pick(null); });
    });
  }
}

// CTA glow follows the cursor
const cta = $('.cta');
if (cta) cta.addEventListener('pointermove', (e) => {
  const r = cta.getBoundingClientRect();
  cta.style.setProperty('--x', `${e.clientX - r.left}px`);
  cta.style.setProperty('--y', `${e.clientY - r.top}px`);
});

// Contact form: three steps with per-field errors, a loading state, then the thank-you page.
// The enquiry is handed to the visitor's email app, addressed to onboarding@rumstar.eu.
// ponytail: mailto has no server side, swap for a form endpoint once one exists
const form = $('#intake');
if (form) {
  const fieldsets = $$('fieldset', form);
  const back = $('[data-back]', form), next = $('[data-next]', form), submit = $('[data-submit]', form);
  const err = $('.form-error', form), bar = $('.progress i', form), count = $('.step-count b', form);
  let step = 0;
  const show = (n) => {
    form.classList.toggle('back', n < step);
    step = n;
    fieldsets.forEach((f, i) => f.hidden = i !== n);
    back.hidden = n === 0;
    next.hidden = n === fieldsets.length - 1;
    submit.hidden = n !== fieldsets.length - 1;
    bar.style.setProperty('--p', (n + 1) / fieldsets.length);
    count.textContent = n + 1;
    count.style.animation = 'none'; void count.offsetWidth; count.style.animation = '';
    err.textContent = '';
    $('input, textarea', fieldsets[n])?.focus({ preventScroll: true });
  };
  // Returns true when the field is acceptable, and shows or clears its message
  const check = (input) => {
    const v = input.value.trim(), msg = input.parentElement.querySelector('.ferr');
    let bad = false;
    if (input.required && !v) bad = true;
    else if (v && (input.type === 'email' || input.type === 'url') && !input.checkValidity()) bad = true;
    if (msg && input.type === 'email') msg.textContent = v ? msg.dataset.bad : msg.dataset.empty;
    input.parentElement.classList.toggle('invalid', bad);
    input.parentElement.classList.toggle('valid', !bad && !!v);
    input.setAttribute('aria-invalid', bad);
    return !bad;
  };
  const checkable = (scope) => $$('input[required], input[type=email], input[type=url]', scope);
  checkable(form).forEach(i => {
    i.addEventListener('blur', () => { if (i.value.trim() || i.parentElement.classList.contains('invalid')) check(i); });
    i.addEventListener('input', () => { if (i.parentElement.classList.contains('invalid')) check(i); });
  });
  const valid = () => {
    const bad = checkable(fieldsets[step]).filter(i => !check(i));
    err.textContent = bad.length ? `Please fix ${bad.length === 1 ? 'the highlighted field' : `the ${bad.length} highlighted fields`} to continue.` : '';
    if (bad.length) bad[0].focus();
    return !bad.length;
  };
  next.addEventListener('click', () => { if (valid()) show(step + 1); });
  back.addEventListener('click', () => show(step - 1));
  form.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && e.target.tagName === 'INPUT' && step < fieldsets.length - 1) { e.preventDefault(); next.click(); }
  });
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (!valid()) return;
    const out = {};
    for (const [k, v] of new FormData(form)) if (String(v).trim()) out[k] = out[k] ? `${out[k]}, ${v}` : String(v).trim();
    const body = Object.entries(out).map(([k, v]) => `${k}: ${v}`).join('\n');
    const subject = `Enquiry from ${out.Company || out.Name}`;
    submit.classList.add('is-loading');
    submit.setAttribute('aria-busy', 'true');
    $('.btn-label', submit).textContent = 'Opening your email';
    location.href = `mailto:onboarding@rumstar.eu?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    setTimeout(() => { location.href = '/thank-you.html'; }, 1200);
  });
  // Coming back with the Back button restores the page from cache: reset the button
  addEventListener('pageshow', () => {
    submit.classList.remove('is-loading');
    submit.removeAttribute('aria-busy');
    $('.btn-label', submit).textContent = 'Send enquiry';
  });
}

// Cookie notice: informational only (no tracking cookies), remembered once dismissed
const note = $('.cookie-note');
if (note) {
  let seen = false;
  try { seen = localStorage.getItem('cookie-notice') === 'ok'; } catch (e) {}
  if (!seen) note.hidden = false;
  $('.cookie-ok', note).addEventListener('click', () => {
    note.hidden = true;
    try { localStorage.setItem('cookie-notice', 'ok'); } catch (e) {}
  });
  $('.cookie-reopen')?.addEventListener('click', () => { note.hidden = false; $('.cookie-ok', note).focus(); });
}

// Sticky call button on phones: appears after the hero, steps aside for the footer
const mcta = $('.mcta');
if (mcta) {
  const foot = $('.foot');
  let footerVisible = false;
  const update = () => mcta.classList.toggle('show', scrollY > innerHeight * 0.6 && !footerVisible);
  new IntersectionObserver(([e]) => { footerVisible = e.isIntersecting; update(); }).observe(foot);
  addEventListener('scroll', update, { passive: true });
  update();
}

// Theme toggle: light by default, choice remembered, circular reveal where supported
const themeBtn = $('.theme');
const syncLabel = () => themeBtn.setAttribute('aria-label', document.documentElement.dataset.theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
syncLabel();
themeBtn.addEventListener('click', (e) => {
  const next = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
  const apply = () => {
    if (next === 'dark') document.documentElement.dataset.theme = 'dark';
    else delete document.documentElement.dataset.theme;
    try { localStorage.setItem('theme', next); } catch (err) {}
    syncLabel();
  };
  if (!document.startViewTransition || reduced) return apply();
  const r = Math.hypot(Math.max(e.clientX, innerWidth - e.clientX), Math.max(e.clientY, innerHeight - e.clientY));
  document.startViewTransition(apply).ready.then(() => {
    document.documentElement.animate(
      { clipPath: [`circle(0 at ${e.clientX}px ${e.clientY}px)`, `circle(${r}px at ${e.clientX}px ${e.clientY}px)`] },
      { duration: 650, easing: 'cubic-bezier(.2,.7,.1,1)', pseudoElement: '::view-transition-new(root)' }
    );
  });
});


// FAQ: animate details open and closed. Native details still works without this.
$$('details').forEach(d => {
  const summary = $('summary', d);
  let anim = null;
  summary.addEventListener('click', (e) => {
    if (reduced || !d.animate) return;
    e.preventDefault();
    anim?.cancel();
    const start = d.offsetHeight;
    const opening = !d.open;
    if (opening) { d.open = true; d.classList.add('opening'); }
    const end = opening ? d.scrollHeight : summary.offsetHeight + 1;
    anim = d.animate({ height: [`${start}px`, `${end}px`] }, { duration: opening ? 280 : 220, easing: 'cubic-bezier(.22,1,.36,1)' });
    anim.onfinish = () => { if (!opening) d.open = false; d.classList.remove('opening'); anim = null; };
  });
});

// Quiet scroll reveals on the main blocks of each page
if (!reduced) {
  const blocks = $$('.split-head, .fee-panel, .bench, .sector-strip, .steps, .qs, .cta, .svc, .check-card, .rules, .share-note, .faq-group, .about-grid, .thanks-grid, .flow-head');
  const rv = new IntersectionObserver((entries) => entries.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('in'); rv.unobserve(e.target); }
  }), { rootMargin: '0px 0px -8% 0px' });
  blocks.forEach(b => {
    // anything already on screen, or scrolled past, shows straight away
    if (b.getBoundingClientRect().top < innerHeight) return;
    b.classList.add('rv');
    rv.observe(b);
  });
}
