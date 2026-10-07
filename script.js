const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;

// Hero readout: cycles through illustrative routing examples
const readout = document.querySelector('.readout');
const lines = [
  'Card payment, €84.00, routed to lowest cost acquirer',
  'Apple Pay, €12.50, approved first time',
  'Open Banking, €1,240.00, no card fees applied',
  'Declined card retried on backup acquirer, approved',
  'Subscription renewal, €29.00, card details auto updated',
];
let li = 0;
if (readout && !reduced) setInterval(() => {
  readout.classList.add('swap');
  setTimeout(() => { li = (li + 1) % lines.length; readout.textContent = lines[li]; readout.classList.remove('swap'); }, 350);
}, 3200);

// Fee breakdown bar: segments grow and the total counts up when scrolled into view
const fee = document.querySelector('.fee-panel');
const segs = [...fee.querySelectorAll('.seg')];
const totalEl = fee.querySelector('[data-total]');
const TOTAL = segs.reduce((sum, x) => sum + +x.dataset.v, 0);

function showFees() {
  segs.forEach(s => s.style.width = (s.dataset.v / TOTAL * 100) + '%');
  if (reduced) return;
  const t0 = performance.now();
  const tick = (t) => {
    const k = Math.min(1, (t - t0) / 1100), e = 1 - Math.pow(1 - k, 3);
    totalEl.textContent = (TOTAL * e).toFixed(2);
    if (k < 1) requestAnimationFrame(tick);
  };
  requestAnimationFrame(tick);
}

// Animate bar and process line once, when scrolled into view
document.querySelectorAll('.steps li').forEach((li, i) => li.style.setProperty('--i', i));
const io = new IntersectionObserver((entries) => entries.forEach(e => {
  if (!e.isIntersecting) return;
  if (e.target === fee) showFees(); else e.target.classList.add('in');
  io.unobserve(e.target);
}), { threshold: 0.35 });
io.observe(fee);
io.observe(document.querySelector('.steps'));

// Services tabs
const services = [
  ['Every line of your statement, explained.', 'We take three months of statements and break down every charge: interchange, scheme fees, margin, gateway and the small extras that add up. You get a plain list of what you pay and what you should pay.', ['Statement teardown', 'Benchmark against market rates', 'Savings figure in writing']],
  ['The right provider, on the right terms.', 'We shortlist acquirers, gateways and payment providers that fit your volumes, markets and checkout, run the tender and negotiate the contract. You sign it. We read it first.', ['Shortlist and tender', 'Contract negotiation', 'Small print review']],
  ['Stop losing sales to declines.', 'A declined payment is a lost customer. We find out why yours are failing and fix it with smarter routing, retries, card updater services and the right authentication settings.', ['Decline analysis', 'Routing and retries', '3D Secure tuning']],
  ['Switch provider without losing a day of trading.', 'We plan the move, manage the provider\'s team and test everything before go live. Your customers should not notice anything changed.', ['Migration plan', 'Token and data transfer', 'Go live support']],
  ['Know what applies and what does not.', 'PCI DSS, strong customer authentication, chargebacks and fraud rules. We tell you exactly what you need to do, and what you are paying for that you do not need.', ['PCI DSS', 'Chargebacks', 'Fraud rules']],
];
const tabs = [...document.querySelectorAll('[role=tab]')];
const panel = document.getElementById('panel');
function select(i, focus) {
  tabs.forEach((t, j) => { t.setAttribute('aria-selected', j === i); t.tabIndex = j === i ? 0 : -1; });
  const [h, p, tags] = services[i];
  panel.setAttribute('aria-labelledby', tabs[i].id);
  panel.innerHTML = `<h3>${h}</h3><p>${p}</p><ul>${tags.map(t => `<li>${t}</li>`).join('')}</ul>`;
  if (focus) tabs[i].focus();
}
tabs.forEach((t, i) => {
  t.addEventListener('click', () => select(i));
  t.addEventListener('keydown', (e) => {
    const n = { ArrowDown: i + 1, ArrowRight: i + 1, ArrowUp: i - 1, ArrowLeft: i - 1, Home: 0, End: tabs.length - 1 }[e.key];
    if (n === undefined) return;
    e.preventDefault();
    select((n + tabs.length) % tabs.length, true);
  });
});

// CTA glow follows the cursor
const cta = document.querySelector('.cta');
cta.addEventListener('pointermove', (e) => {
  const r = cta.getBoundingClientRect();
  cta.style.setProperty('--x', `${e.clientX - r.left}px`);
  cta.style.setProperty('--y', `${e.clientY - r.top}px`);
});

// Theme toggle: light by default, choice remembered, circular reveal where supported
const themeBtn = document.querySelector('.theme');
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
