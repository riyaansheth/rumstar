const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];

// Mobile menu
const menuBtn = $('.menu-btn');
const siteNav = $('#site-nav');
if (menuBtn && siteNav) {
  const setMenu = (open) => { siteNav.classList.toggle('open', open); menuBtn.setAttribute('aria-expanded', open); };
  menuBtn.addEventListener('click', () => setMenu(menuBtn.getAttribute('aria-expanded') !== 'true'));
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') setMenu(false); });
  siteNav.addEventListener('click', (e) => { if (e.target.closest('a')) setMenu(false); });
}

// Hero readout: cycles through illustrative routing examples
const readout = $('.readout');
const lines = [
  'Card payment routed to the lowest cost acquirer',
  'Apple Pay payment approved first time',
  'Open banking payment, no card fees applied',
  'Declined card retried on a backup acquirer, approved',
  'Subscription renewal, card details updated automatically',
];
let li = 0;
if (readout && !reduced) setInterval(() => {
  readout.classList.add('swap');
  setTimeout(() => { li = (li + 1) % lines.length; readout.textContent = lines[li]; readout.classList.remove('swap'); }, 350);
}, 3200);

// Animate the fee bar and process line once, when scrolled into view
const fee = $('.fee-panel');
const steps = $('.steps');
$$('.steps li').forEach((el, i) => el.style.setProperty('--i', i));
const io = new IntersectionObserver((entries) => entries.forEach(e => {
  if (!e.isIntersecting) return;
  if (e.target === fee) {
    const segs = $$('.seg', fee);
    const total = segs.reduce((sum, x) => sum + +x.dataset.v, 0);
    segs.forEach(s => s.style.width = (s.dataset.v / total * 100) + '%');
  } else e.target.classList.add('in');
  io.unobserve(e.target);
}), { threshold: 0.35 });
if (fee) io.observe(fee);
if (steps) io.observe(steps);

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
function select(i, focus) {
  tabs.forEach((t, j) => { t.setAttribute('aria-selected', j === i); t.tabIndex = j === i ? 0 : -1; });
  const [h, p, tags] = services[i];
  panel.setAttribute('aria-labelledby', tabs[i].id);
  panel.innerHTML = `<h3>${h}</h3><p>${p}</p><ul>${tags.map(t => `<li>${t}</li>`).join('')}</ul>`;
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
}

// CTA glow follows the cursor
const cta = $('.cta');
if (cta) cta.addEventListener('pointermove', (e) => {
  const r = cta.getBoundingClientRect();
  cta.style.setProperty('--x', `${e.clientX - r.left}px`);
  cta.style.setProperty('--y', `${e.clientY - r.top}px`);
});

// Contact form: three steps, then opens the visitor's email app with the answers filled in.
// ponytail: mailto has no server side, swap for a form endpoint once one exists
const form = $('#intake');
if (form) {
  const fieldsets = $$('fieldset', form);
  const back = $('[data-back]', form), next = $('[data-next]', form), submit = $('[data-submit]', form);
  const err = $('.form-error', form), bar = $('.progress i', form), count = $('.step-count b', form);
  let step = 0;
  const show = (n) => {
    step = n;
    fieldsets.forEach((f, i) => f.hidden = i !== n);
    back.hidden = n === 0;
    next.hidden = n === fieldsets.length - 1;
    submit.hidden = n !== fieldsets.length - 1;
    bar.style.width = ((n + 1) / fieldsets.length * 100) + '%';
    count.textContent = n + 1;
    err.textContent = '';
    $('input, textarea', fieldsets[n])?.focus({ preventScroll: true });
  };
  const valid = () => {
    let ok = true;
    $$('input[required]', fieldsets[step]).forEach(i => {
      const bad = !i.value.trim() || (i.type === 'email' && !i.checkValidity());
      i.setAttribute('aria-invalid', bad);
      if (bad && ok) { i.focus(); ok = false; }
    });
    if (!ok) err.textContent = 'Please fill in your name, a valid work email and your company.';
    return ok;
  };
  next.addEventListener('click', () => { if (valid()) show(step + 1); });
  back.addEventListener('click', () => show(step - 1));
  form.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && e.target.tagName === 'INPUT' && step < fieldsets.length - 1) { e.preventDefault(); next.click(); }
  });
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const data = new FormData(form);
    const out = {};
    for (const [k, v] of data) if (String(v).trim()) out[k] = out[k] ? `${out[k]}, ${v}` : v;
    const body = Object.entries(out).map(([k, v]) => `${k}: ${v}`).join('\n');
    const subject = `Enquiry from ${out.Company || out.Name || 'website'}`;
    location.href = `mailto:onboarding@rumstar.eu?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    const done = $('.done', form);
    done.hidden = false;
    done.focus();
  });
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
