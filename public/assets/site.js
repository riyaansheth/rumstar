(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Header: hairline once the page scrolls
  const hdr = $('.hdr');
  const onScroll = () => hdr.classList.toggle('scrolled', scrollY > 8);
  addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Mobile menu
  const menu = $('.menu'), nav = $('#nav');
  const setMenu = (open) => {
    menu.setAttribute('aria-expanded', open);
    nav.classList.toggle('open', open);
    document.body.classList.toggle('menu-open', open);
    menu.querySelector('.menu-word').textContent = open ? 'Close' : 'Menu';
  };
  menu.addEventListener('click', () => setMenu(menu.getAttribute('aria-expanded') !== 'true'));
  addEventListener('keydown', (e) => { if (e.key === 'Escape' && nav.classList.contains('open')) { setMenu(false); menu.focus(); } });
  matchMedia('(min-width: 1081px)').addEventListener('change', (m) => { if (m.matches) setMenu(false); });

  // Restrained entrances: elements fade up once, process lines draw once
  $$('.steps .step').forEach((s, i) => s.style.setProperty('--i', i));
  const targets = $$('.reveal, .hero-title, .steps');
  if (reduced || !('IntersectionObserver' in window)) targets.forEach(t => t.classList.add('in'));
  else {
    const io = new IntersectionObserver((entries) => entries.forEach(e => {
      if (!e.isIntersecting) return;
      e.target.classList.add('in');
      io.unobserve(e.target);
    }), { threshold: 0, rootMargin: '0px 0px -8% 0px' });
    targets.forEach(t => io.observe(t));
    // Never leave content hidden: anything already scrolled past is shown immediately
    const sweep = () => targets.forEach(t => { if (!t.classList.contains('in') && t.getBoundingClientRect().top < innerHeight) t.classList.add('in'); });
    addEventListener('scroll', () => requestAnimationFrame(sweep), { passive: true });
    addEventListener('load', sweep);
  }

  // Anatomy of a payment fee
  const anat = $('.anatomy');
  if (anat) {
    const segs = $$('.seg', anat), parts = $$('.anat-part', anat);
    const pick = (key) => {
      segs.forEach(s => s.setAttribute('aria-pressed', s.dataset.part === key));
      parts.forEach(p => p.hidden = p.dataset.part !== key);
    };
    segs.forEach((s, i) => {
      s.addEventListener('click', () => pick(s.dataset.part));
      s.addEventListener('keydown', (e) => {
        const d = { ArrowRight: 1, ArrowLeft: -1 }[e.key];
        if (!d) return;
        e.preventDefault();
        const n = segs[(i + d + segs.length) % segs.length];
        n.focus(); pick(n.dataset.part);
      });
    });
  }

  // Home industries: the side panel follows the hovered or focused row
  const rows = $$('.ind-row');
  if (rows.length) {
    const panels = $$('.ind-panel');
    const show = (i) => {
      rows.forEach(r => r.classList.toggle('active', r.dataset.ind === i));
      panels.forEach(p => p.hidden = p.dataset.ind !== i);
    };
    rows.forEach(r => {
      r.addEventListener('mouseenter', () => show(r.dataset.ind));
      r.addEventListener('focusin', () => show(r.dataset.ind));
    });
    show('0');
  }

  // Current-section highlight for sticky indexes (industries page, article contents)
  const indexLinks = $$('.sector-index a, .art-toc a');
  if (indexLinks.length && 'IntersectionObserver' in window) {
    const byId = new Map(indexLinks.map(a => [decodeURIComponent(a.hash.slice(1)), a]));
    const spy = new IntersectionObserver((entries) => entries.forEach(e => {
      if (!e.isIntersecting) return;
      indexLinks.forEach(a => a.classList.remove('active'));
      byId.get(e.target.id)?.classList.add('active');
    }), { rootMargin: '-25% 0px -65% 0px' });
    byId.forEach((_, id) => { const el = document.getElementById(id); if (el) spy.observe(el); });
  }

  // Insights topic filter
  const filters = $$('.filters button');
  filters.forEach(b => b.addEventListener('click', () => {
    filters.forEach(x => x.setAttribute('aria-pressed', x === b));
    $$('.arow').forEach(r => r.hidden = b.dataset.cat !== 'all' && r.dataset.cat !== b.dataset.cat);
  }));

  // Contact form: validate, then hand the enquiry to the visitor's email app.
  // ponytail: no server-side handler exists on this static host; swap for a form endpoint when one is chosen
  const form = $('#cform');
  if (form) {
    const msg = $('.form-msg', form);
    const check = (input) => {
      const v = input.value.trim();
      let ok = true;
      if (input.required && !v) ok = false;
      else if (v && (input.type === 'email' || input.type === 'url')) ok = input.checkValidity();
      input.closest('.f').classList.toggle('invalid', !ok);
      input.setAttribute('aria-invalid', !ok);
      return ok;
    };
    const fields = $$('input[required], input[type=url]', form);
    fields.forEach(i => i.addEventListener('blur', () => { if (i.value || i.closest('.f').classList.contains('invalid')) check(i); }));
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const bad = fields.filter(i => !check(i));
      if (bad.length) { bad[0].focus(); return; }
      const out = {};
      for (const [k, v] of new FormData(form)) if (String(v).trim()) out[k] = out[k] ? `${out[k]}, ${v}` : String(v).trim();
      const body = Object.entries(out).map(([k, v]) => `${k}: ${v}`).join('\n');
      const subject = `Enquiry from ${out.Company || out.Name}`;
      location.href = `mailto:onboarding@rumstar.eu?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
      msg.hidden = false;
      msg.innerHTML = 'Your email application should now be open with your enquiry ready to send. If nothing opened, write to <a href="mailto:onboarding@rumstar.eu">onboarding@rumstar.eu</a> directly.';
      msg.focus();
    });
  }
})();
