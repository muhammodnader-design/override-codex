const DOCX = {
  novel_1: "1_0override zone-the dark maiden.docx",
  novel_2: "2_0 The 'Hart' that shall beat.docx",
  novel_3: "3_0Override Zone the blood tournament.docx",
  novel_4: "4_0Override Zone Cobalt Knight.docx",
};
const state = {
  characters: [],
  novels: [],
  novelCache: {},
  lore: null,
  gallery: [],
  favorites: new Set(JSON.parse(localStorage.getItem('oz_favs') || '[]')),
  theme: localStorage.getItem('oz_theme') || 'dark',
  reader: { font: 18, pos: {} },
};

document.documentElement.setAttribute('data-theme', state.theme);

async function loadAll() {
  const [chars, novels, lore, gallery] = await Promise.all([
    fetch('data/characters.json').then(r=>r.json()),
    fetch('data/novels.json').then(r=>r.json()),
    fetch('data/lore.json').then(r=>r.json()),
    fetch('data/gallery.json').then(r=>r.json()),
  ]);
  state.characters = chars;
  state.novels = novels;
  state.lore = lore;
  state.gallery = gallery;
}

const $app = () => document.getElementById('app');

function slug(s){ return s.toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,''); }

// ---------- Router ----------
window.addEventListener('hashchange', route);
window.addEventListener('DOMContentLoaded', async () => {
  await loadAll();
  document.getElementById('themeToggle').addEventListener('click', toggleTheme);
  document.getElementById('searchToggle').addEventListener('click', openSearch);
  document.getElementById('globalSearch').addEventListener('input', doSearch);
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') closeSearch();
    if ((e.ctrlKey||e.metaKey) && e.key.toLowerCase()==='k') { e.preventDefault(); openSearch(); }
  });
  route();
});

function route() {
  const hash = location.hash || '#/';
  const parts = hash.replace(/^#\/?/, '').split('/').filter(Boolean);
  const [page, ...rest] = parts;
  closeSearch();
  switch (page) {
    case '': case 'home': renderHome(); break;
    case 'characters': renderCharacters(); break;
    case 'character': renderCharacter(rest.join('/')); break;
    case 'novels': renderNovels(); break;
    case 'read': renderReader(rest.join('/')); break;
    case 'gallery': renderGallery(); break;
    case 'lore': renderLore(); break;
    case 'chat': renderChat(rest); break;
    case 'about': renderAbout(); break;
    default: renderHome();
  }
  window.scrollTo(0,0);
}

function toggleTheme() {
  state.theme = state.theme === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', state.theme);
  localStorage.setItem('oz_theme', state.theme);
}

// ---------- Search ----------
function openSearch() { document.getElementById('searchOverlay').classList.remove('hidden'); document.getElementById('globalSearch').focus(); }
function closeSearch() { document.getElementById('searchOverlay').classList.add('hidden'); document.getElementById('globalSearch').value=''; document.getElementById('searchResults').innerHTML=''; }
function doSearch(e) {
  const q = e.target.value.trim().toLowerCase();
  const box = document.getElementById('searchResults');
  if (!q) { box.innerHTML=''; return; }
  const res = [];
  state.characters.forEach(c => {
    if (c.name.toLowerCase().includes(q) || c.faction.toLowerCase().includes(q) || c.quotes.some(qq=>qq.toLowerCase().includes(q))) {
      res.push({type:'Character', title:c.name, sub:c.faction, action:()=>location.hash='#/character/'+slug(c.name)});
    }
  });
  state.novels.forEach(n => {
    if (n.title.toLowerCase().includes(q)) {
      res.push({type:'Novel', title:n.title, sub:n.paragraphs+' paragraphs', action:()=>location.hash='#/read/'+n.id});
    }
  });
  state.gallery.forEach(g => {
    if (g.name.toLowerCase().includes(q) || g.folder.toLowerCase().includes(q)) {
      res.push({type:'Image', title:g.name, sub:g.folder, action:()=>location.hash='#/gallery'});
    }
  });
  box.innerHTML = res.slice(0,30).map((r,i)=>`<div class="item" data-i="${i}"><div class="t">${r.title}</div><div class="s">${r.type} · ${r.sub}</div></div>`).join('') || '<div class="empty">No matches.</div>';
  box.querySelectorAll('.item').forEach((el,i)=> el.addEventListener('click', ()=>{ res[i].action(); closeSearch(); }));
}

// ---------- Home ----------
function renderHome() {
  const favCount = state.favorites.size;
  $app().innerHTML = `
    <section class="hero">
      <h1>Override Zone</h1>
      <p class="sub">An original universe — characters, factions, novels, and illustrations. Explore the codex, read the stories, and browse the art.</p>
      <div class="stats">
        <div class="stat"><strong>${state.characters.length}</strong><span>Characters</span></div>
        <div class="stat"><strong>${state.novels.length}</strong><span>Novels</span></div>
        <div class="stat"><strong>${state.gallery.length}</strong><span>Illustrations</span></div>
        <div class="stat"><strong>${state.lore.factions.length}</strong><span>Factions</span></div>
        <div class="stat"><strong>${favCount}</strong><span>Favorites</span></div>
      </div>
      <div style="margin-top:28px; display:flex; gap:10px; justify-content:center; flex-wrap:wrap;">
        <a class="btn primary" href="#/characters">Browse Characters</a>
        <a class="btn" href="#/novels">Read Novels</a>
        <a class="btn" href="#/gallery">View Gallery</a>
      </div>
    </section>
    <h2 class="section-title">Factions</h2>
    <div class="grid cols-3">
      ${state.lore.factions.slice(0,6).map(f=>`<div class="card"><h3>${f.name}</h3><p class="meta">${f.desc}</p></div>`).join('')}
    </div>
    <div style="margin-top:16px;"><a class="btn" href="#/lore">All factions & disclaimer →</a></div>
  `;
}

// ---------- Characters ----------
function renderCharacters() {
  const factions = [...new Set(state.characters.map(c=>c.faction))].sort();
  $app().innerHTML = `
    <h2 class="section-title">Characters (${state.characters.length})</h2>
    <div class="controls">
      <input id="charSearch" type="search" placeholder="Search name, faction, quote…" />
      <select id="factionFilter"><option value="">All factions</option>${factions.map(f=>`<option>${f}</option>`).join('')}</select>
      <button class="btn" id="randomChar">Random</button>
    </div>
    <div id="charGrid" class="grid cols-4"></div>
  `;
  const grid = document.getElementById('charGrid');
  function draw() {
    const q = document.getElementById('charSearch').value.trim().toLowerCase();
    const f = document.getElementById('factionFilter').value;
    const list = state.characters.filter(c => {
      if (f && c.faction !== f) return false;
      if (!q) return true;
      return c.name.toLowerCase().includes(q) || c.faction.toLowerCase().includes(q) || c.quotes.some(qq=>qq.toLowerCase().includes(q));
    });
    grid.innerHTML = list.map(c => `
      <div class="card" data-slug="${slug(c.name)}" style="cursor:pointer;">
        ${c.image ? `<img src="${c.image}" alt="${c.name}" loading="lazy" />` : `<div style="aspect-ratio:3/4;background:var(--bg-2);border-radius:8px;display:flex;align-items:center;justify-content:center;color:var(--muted);">no portrait</div>`}
        <h3>${c.name}</h3>
        <div class="meta">${c.title ? c.title+' · ' : ''}${c.faction}</div>
        <div class="quote">"${(c.quotes[0]||'').slice(0,90)}${(c.quotes[0]||'').length>90?'…':''}"</div>
      </div>
    `).join('') || '<div class="empty">No characters match.</div>';
    grid.querySelectorAll('.card').forEach(card => {
      card.addEventListener('click', () => location.hash = '#/character/' + card.dataset.slug);
    });
  }
  document.getElementById('charSearch').addEventListener('input', draw);
  document.getElementById('factionFilter').addEventListener('change', draw);
  document.getElementById('randomChar').addEventListener('click', () => {
    const c = state.characters[Math.floor(Math.random()*state.characters.length)];
    location.hash = '#/character/' + slug(c.name);
  });
  draw();
}

function renderCharacter(s) {
  const c = state.characters.find(x => slug(x.name) === s);
  if (!c) { $app().innerHTML = '<div class="empty">Character not found. <a href="#/characters">Back</a></div>'; return; }
  const idx = state.characters.indexOf(c);
  const prev = state.characters[(idx-1+state.characters.length)%state.characters.length];
  const next = state.characters[(idx+1)%state.characters.length];
  const isFav = state.favorites.has(c.name);
  $app().innerHTML = `
    <div style="display:flex; gap:10px; margin-bottom:16px; flex-wrap:wrap;">
      <a class="btn" href="#/characters">← All characters</a>
      <button class="btn" id="prevChar">◀ ${prev.name}</button>
      <button class="btn" id="nextChar">${next.name} ▶</button>
    </div>
    <div class="card" style="display:grid; grid-template-columns: 260px 1fr; gap:24px; align-items:start;">
      <div>
        ${c.image ? `<img src="${c.image}" alt="${c.name}" style="width:100%;border-radius:8px;" />` : `<div style="aspect-ratio:3/4;background:var(--bg-2);border-radius:8px;display:flex;align-items:center;justify-content:center;color:var(--muted);">no portrait</div>`}
        ${c.image ? `<a class="btn sm" style="margin-top:8px;" href="${c.image}" download>Download portrait</a>` : ''}
      </div>
      <div>
        <h2 style="font-family:var(--font-head); margin:0 0 4px;">${c.name}</h2>
        ${c.title ? `<div style="color:var(--accent-2); font-size:14px; margin-bottom:6px;">${c.title}</div>` : ''}
        <div class="meta" style="margin-bottom:12px;">${c.faction}${c.role ? ' · '+c.role : ''}</div>
        ${c.aliases && c.aliases.length ? `<div class="meta" style="margin-bottom:8px;"><strong>Aliases:</strong> ${c.aliases.join(', ')}</div>` : ''}
        ${c.bio ? `<p style="margin:12px 0;">${c.bio}</p>` : ''}
        ${c.first_appearance ? `<p class="meta" style="margin-top:8px;"><strong>First appearance:</strong> ${c.first_appearance}</p>` : ''}
        ${c.novels && c.novels.length ? `<p class="meta"><strong>Appears in:</strong> ${c.novels.join(', ')}</p>` : ''}
        <button class="btn sm" id="favBtn">${isFav ? '★ Favorited' : '☆ Favorite'}</button>
      <a class="btn sm" href="#/chat/${slug(c.name)}">💬 Chat with ${c.name.split(' ')[0]}</a>
        <h3 style="margin-top:16px;">Quotes</h3>
        <ul style="padding-left:18px;">
          ${c.quotes.map(q=>`<li style="margin-bottom:8px; font-style:italic;">"${q}"</li>`).join('')}
        </ul>
      </div>
    </div>
  `;
  document.getElementById('prevChar').addEventListener('click', ()=>location.hash='#/character/'+slug(prev.name));
  document.getElementById('nextChar').addEventListener('click', ()=>location.hash='#/character/'+slug(next.name));
  document.getElementById('favBtn').addEventListener('click', () => {
    if (state.favorites.has(c.name)) state.favorites.delete(c.name); else state.favorites.add(c.name);
    localStorage.setItem('oz_favs', JSON.stringify([...state.favorites]));
    renderCharacter(s);
  });
}

// ---------- Novels ----------
function renderNovels() {
  $app().innerHTML = `
    <h2 class="section-title">Novels</h2>
    <div class="grid cols-3">
      ${state.novels.map(n=>`
        <div class="card">
          <h3>${n.title}</h3>
          <div class="meta">${n.paragraphs} paragraphs</div>
          <div style="margin-top:12px; display:flex; gap:8px; flex-wrap:wrap;">
            <a class="btn primary" href="#/read/${n.id}">Read online</a>
            <a class="btn" href="assets/novels/${encodeURIComponent(DOCX[n.id])}" download>Download .docx</a>
          </div>
        </div>
      `).join('')}
    </div>
    <h2 class="section-title" style="margin-top:32px;">Other documents</h2>
    <div class="card">
      <p class="meta">Dossiers, rankings, and side stories are in <code>assets/novels/</code> and can be downloaded directly.</p>
      <div style="display:flex; gap:8px; flex-wrap:wrap; margin-top:8px;">
        ${['Niro Hart - Ivory Board Brief.docx','ranking.docx','the kurogane heir_01.docx','VeilNet_lives.docx','Weavers - Complete Dossier.docx','Weavers - Past Dossier.docx'].map(f=>`<a class="btn sm" href="assets/novels/${encodeURIComponent(f)}" download>${f}</a>`).join('')}
      </div>
    </div>
  `;
  // fix download links: actual filenames
}

// ---------- Reader ----------
async function loadNovel(id) {
  if (state.novelCache[id]) return state.novelCache[id];
  const meta = state.novels.find(n=>n.id===id);
  if (!meta) return null;
  const data = await fetch('data/'+meta.file).then(r=>r.json());
  state.novelCache[id] = data;
  return data;
}

async function renderReader(id) {
  const data = await loadNovel(id);
  if (!data) { $app().innerHTML = '<div class="empty">Novel not found.</div>'; return; }
  const saved = state.reader.pos[id] || 0;
  $app().innerHTML = `
    <div class="reader">
      <a class="btn" href="#/novels">← Novels</a>
      <h1>${data.title}</h1>
      <div class="meta">${data.paragraphs.length} paragraphs</div>
      <div class="reader-toolbar">
        <button class="btn sm" id="fontDown">A-</button>
        <button class="btn sm" id="fontUp">A+</button>
        <button class="btn sm" id="bmSave">Bookmark here</button>
        <button class="btn sm" id="bmGo">Go to bookmark</button>
        <input id="readerSearch" type="search" placeholder="Find in text…" style="flex:1;min-width:120px;" />
        <span id="searchCount" class="muted" style="font-size:12px;"></span>
      </div>
      <div class="progress"><div id="readProgress"></div></div>
      <div id="readerBody"></div>
    </div>
  `;
  const body = document.getElementById('readerBody');
  body.style.fontSize = state.reader.font + 'px';
  // render paragraphs; empty string = scene break
  body.innerHTML = data.paragraphs.map((p,i) => {
    if (p === '') return `<div class="scene-break">* * *</div>`;
    return `<p class="para" data-i="${i}">${escapeHtml(p)}</p>`;
  }).join('');

  // progress
  const prog = document.getElementById('readProgress');
  function updateProgress() {
    const h = document.documentElement;
    const scrolled = h.scrollTop || document.body.scrollTop;
    const total = (h.scrollHeight - h.clientHeight) || 1;
    prog.style.width = Math.min(100, (scrolled/total*100)) + '%';
  }
  window.addEventListener('scroll', updateProgress);
  // store cleanup? simple: re-add each render; acceptable

  // restore scroll
  if (saved) setTimeout(()=>window.scrollTo(0,saved), 50);

  // font
  document.getElementById('fontDown').addEventListener('click', ()=>{ state.reader.font=Math.max(14,state.reader.font-2); body.style.fontSize=state.reader.font+'px'; });
  document.getElementById('fontUp').addEventListener('click', ()=>{ state.reader.font=Math.min(26,state.reader.font+2); body.style.fontSize=state.reader.font+'px'; });

  // bookmark
  document.getElementById('bmSave').addEventListener('click', ()=>{ state.reader.pos[id]=window.scrollY; localStorage.setItem('oz_pos',JSON.stringify(state.reader.pos)); alert('Bookmark saved.'); });
  document.getElementById('bmGo').addEventListener('click', ()=>{ const y=state.reader.pos[id]||0; window.scrollTo(0,y); });

  // search
  const rc = document.getElementById('readerSearch');
  const cnt = document.getElementById('searchCount');
  rc.addEventListener('input', () => {
    const q = rc.value.trim().toLowerCase();
    // clear highlights
    body.querySelectorAll('p.para').forEach(p=>{ p.innerHTML = escapeHtml(data.paragraphs[+p.dataset.i]); });
    if (!q) { cnt.textContent=''; return; }
    let n=0;
    body.querySelectorAll('p.para').forEach(p => {
      const i = +p.dataset.i;
      const txt = data.paragraphs[i];
      if (txt.toLowerCase().includes(q)) {
        p.innerHTML = escapeHtml(txt).replace(new RegExp('('+escapeReg(q)+')','gi'), '<mark>$1</mark>');
        n++;
      }
    });
    cnt.textContent = n ? n+' match'+(n>1?'es':'') : 'no matches';
  });
}

function escapeHtml(s){ return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function escapeReg(s){ return s.replace(/[.*+?^${}()|[\]\\]/g,'\\$&'); }

// ---------- Gallery ----------
function renderGallery() {
  const folders = [...new Set(state.gallery.map(g=>g.folder))];
  $app().innerHTML = `
    <h2 class="section-title">Illustrations (${state.gallery.length})</h2>
    <div class="controls">
      <input id="galSearch" type="search" placeholder="Search filename…" />
      <select id="galFolder"><option value="">All folders</option>${folders.map(f=>`<option>${f}</option>`).join('')}</select>
    </div>
    <div id="galGrid" class="grid cols-4"></div>
  `;
  const grid = document.getElementById('galGrid');
  function draw() {
    const q = document.getElementById('galSearch').value.trim().toLowerCase();
    const f = document.getElementById('galFolder').value;
    const list = state.gallery.filter(g => {
      if (f && g.folder !== f) return false;
      if (q && !g.name.toLowerCase().includes(q)) return false;
      return true;
    });
    grid.innerHTML = list.map(g=>`
      <div style="position:relative;">
        <img class="gallery-img" src="${g.path}" alt="${g.name}" loading="lazy" data-path="${g.path}" data-name="${g.name}" />
        <div style="display:flex; justify-content:space-between; align-items:center; margin-top:4px;">
          <span class="meta" style="font-size:11px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">${g.name}</span>
          <a class="btn sm" href="${g.path}" download>↓</a>
        </div>
      </div>
    `).join('') || '<div class="empty">No images.</div>';
    grid.querySelectorAll('.gallery-img').forEach(img => {
      img.addEventListener('click', () => openImage(img.dataset.path, img.dataset.name));
    });
  }
  document.getElementById('galSearch').addEventListener('input', draw);
  document.getElementById('galFolder').addEventListener('change', draw);
  draw();
}

function openImage(path, name) {
  const bd = document.createElement('div');
  bd.className = 'modal-backdrop';
  bd.innerHTML = `<div class="modal"><button class="close">×</button><img src="${path}" alt="${name}" /><div style="text-align:center;"><a class="btn" href="${path}" download>Download</a> <span class="muted" style="margin-left:8px;">${name}</span></div></div>`;
  document.body.appendChild(bd);
  bd.querySelector('.close').addEventListener('click', ()=>bd.remove());
  bd.addEventListener('click', e=>{ if(e.target===bd) bd.remove(); });
}

// ---------- Lore ----------
function renderLore() {
  const L = state.lore;
  $app().innerHTML = `
    <h2 class="section-title">Lore & World</h2>
    <div class="controls" style="margin-bottom:8px;">
      <a class="btn sm" href="#lore-factions">Factions</a>
      <a class="btn sm" href="#lore-concepts">Concepts</a>
      <a class="btn sm" href="#lore-locations">Locations</a>
      <a class="btn sm" href="#lore-events">Events</a>
      <a class="btn sm" href="#lore-rankings">Rankings</a>
      <a class="btn sm" href="#lore-relationships">Relationships</a>
      <a class="btn sm" href="#lore-quotes">Quotes</a>
      <a class="btn sm" href="#lore-dossiers">Dossiers</a>
      <a class="btn sm" href="#lore-disclaimer">Disclaimer</a>
    </div>

    <h3 id="lore-factions" class="section-title" style="font-size:20px;">Factions</h3>
    ${L.factions.map(f=>`<div class="faction-card"><h3>${f.name}</h3><p>${f.desc}</p></div>`).join('')}

    <h3 id="lore-concepts" class="section-title" style="font-size:20px; margin-top:24px;">Concepts & Terms</h3>
    <div class="grid cols-3">
      ${L.concepts.map(c=>`<div class="card"><h3 style="font-size:15px;">${c.term}</h3><p class="meta">${c.desc}</p></div>`).join('')}
    </div>

    <h3 id="lore-locations" class="section-title" style="font-size:20px; margin-top:24px;">Locations (${L.locations.length})</h3>
    <div class="grid cols-3">
      ${L.locations.map(l=>`<div class="card"><h3 style="font-size:15px;">${l.name}</h3><p class="meta">${l.desc||''}</p></div>`).join('')}
    </div>

    <h3 id="lore-events" class="section-title" style="font-size:20px; margin-top:24px;">Events & Timeline (${L.events.length})</h3>
    ${L.events.map(e=>`<div class="card" style="margin-bottom:10px;"><h3 style="font-size:15px;">${e.title} <span class="meta" style="font-size:11px;">(${e.novel||''})</span></h3><p class="meta">${e.summary||''}</p>${e.participants&&e.participants.length?`<p class="meta" style="margin-top:4px;"><strong>Participants:</strong> ${e.participants.join(', ')}</p>`:''}</div>`).join('')}

    <h3 id="lore-rankings" class="section-title" style="font-size:20px; margin-top:24px;">Power Rankings (fan tier list)</h3>
    ${L.rankings.map(r=>`<div class="card" style="margin-bottom:10px;"><h3 style="font-size:15px;">${r.tier}</h3><p class="meta">${r.names.join(' · ')}</p></div>`).join('')}

    <h3 id="lore-relationships" class="section-title" style="font-size:20px; margin-top:24px;">Weaver Relationships</h3>
    <div class="grid cols-3">
      ${L.relationships.map(r=>`<div class="card"><h3 style="font-size:14px;">${r.pair}</h3><p class="meta">${r.note}</p></div>`).join('')}
    </div>
    <div class="card" style="margin-top:12px;">
      <h3 style="font-size:15px;">Trust clusters</h3>
      <p class="meta"><strong>High:</strong> ${L.trust.high.join(' · ')}</p>
      <p class="meta" style="margin-top:6px;"><strong>Friction:</strong> ${L.trust.low.join(' · ')}</p>
    </div>

    <h3 id="lore-quotes" class="section-title" style="font-size:20px; margin-top:24px;">Iconic Quotes (${L.quotes.length})</h3>
    <div id="quoteList">
      ${L.quotes.slice(0,40).map(q=>`<div class="card" style="margin-bottom:8px;"><p style="font-style:italic; margin:0 0 4px;">"${q.quote}"</p><div class="meta">— ${q.speaker}</div></div>`).join('')}
    </div>
    ${L.quotes.length>40?`<button class="btn" id="loadMoreQuotes" style="margin-top:8px;">Load more (${L.quotes.length-40} remaining)</button>`:''}

    <h3 id="lore-dossiers" class="section-title" style="font-size:20px; margin-top:24px;">Dossiers & Broadcasts</h3>
    ${L.dossiers.map(d=>`<div class="card" style="margin-bottom:10px;"><h3 style="font-size:15px;">${d.title}</h3><p class="meta">${d.summary}</p></div>`).join('')}

    <h3 id="lore-disclaimer" class="section-title" style="font-size:20px; margin-top:24px;">Disclaimer</h3>
    <div class="card"><p style="white-space:pre-wrap;">${escapeHtml(L.disclaimer)}</p></div>
  `;
  // load more quotes
  const btn = document.getElementById('loadMoreQuotes');
  if (btn) {
    let shown = 40;
    btn.addEventListener('click', () => {
      shown += 40;
      const list = document.getElementById('quoteList');
      list.innerHTML = L.quotes.slice(0,shown).map(q=>`<div class="card" style="margin-bottom:8px;"><p style="font-style:italic; margin:0 0 4px;">"${q.quote}"</p><div class="meta">— ${q.speaker}</div></div>`).join('');
      if (shown >= L.quotes.length) btn.remove();
      else btn.textContent = `Load more (${L.quotes.length-shown} remaining)`;
    });
  }
  // smooth scroll for anchor links
  $app().querySelectorAll('a[href^="#lore-"]').forEach(a => {
    a.addEventListener('click', e => {
      e.preventDefault();
      const el = document.getElementById(a.getAttribute('href').slice(1));
      if (el) el.scrollIntoView({behavior:'smooth'});
    });
  });
}

// ---------- Chat ----------
state.chat = state.chat || { charSlug: null, messages: [] };

function renderChat(rest) {
  const slugParam = (rest && rest[0]) ? rest.join('/') : null;
  if (slugParam && slugParam !== state.chat.charSlug) {
    state.chat.charSlug = slugParam;
    state.chat.messages = [];
  }
  if (!state.chat.charSlug && state.characters.length) {
    state.chat.charSlug = slug(state.characters[0].name);
  }
  const c = state.characters.find(x => slug(x.name) === state.chat.charSlug);
  $app().innerHTML = `
    <h2 class="section-title">Ask the Codex</h2>
    <p class="meta" style="margin-bottom:12px;">Chat with a character. Powered by free AI (Pollinations). No API key needed. Responses are fictional and may hallucinate.</p>
    <div class="controls">
      <select id="chatChar">${state.characters.map(ch=>`<option value="${slug(ch.name)}" ${slug(ch.name)===state.chat.charSlug?'selected':''}>${ch.name}</option>`).join('')}</select>
      <button class="btn" id="chatClear">Clear chat</button>
    </div>
    <div id="chatWindow" style="background:var(--card); border:1px solid var(--border); border-radius:var(--radius); padding:16px; min-height:300px; max-height:60vh; overflow:auto; margin-bottom:12px;"></div>
    <div style="display:flex; gap:8px;">
      <input id="chatInput" type="text" placeholder="Ask ${c?c.name:'...'} something…" style="flex:1; padding:10px 12px; border-radius:8px; border:1px solid var(--border); background:var(--bg-2); color:var(--text); font-family:inherit;" />
      <button class="btn primary" id="chatSend">Send</button>
    </div>
    <p class="meta" style="margin-top:8px; font-size:12px;">Tip: try "What do you want most?" or "Tell me about your past."</p>
  `;
  const win = document.getElementById('chatWindow');
  function renderMsgs() {
    win.innerHTML = state.chat.messages.map(m => `
      <div style="margin-bottom:12px; ${m.role==='user'?'text-align:right;':''}">
        <div style="display:inline-block; max-width:85%; padding:8px 12px; border-radius:10px; ${m.role==='user'?'background:var(--accent); color:#fff;':'background:var(--bg-2);'}">
          <div style="font-size:11px; opacity:.7; margin-bottom:2px;">${m.role==='user'?'You': (c?c.name:'Character')}</div>
          <div style="white-space:pre-wrap;">${escapeHtml(m.content)}</div>
        </div>
      </div>
    `).join('') || '<div class="empty">Start a conversation.</div>';
    win.scrollTop = win.scrollHeight;
  }
  renderMsgs();

  document.getElementById('chatChar').addEventListener('change', e => {
    state.chat.charSlug = e.target.value;
    state.chat.messages = [];
    renderChat([]);
  });
  document.getElementById('chatClear').addEventListener('click', () => {
    state.chat.messages = [];
    renderMsgs();
  });

  async function send() {
    const input = document.getElementById('chatInput');
    const text = input.value.trim();
    if (!text) return;
    input.value = '';
    state.chat.messages.push({role:'user', content:text});
    renderMsgs();
    const thinking = {role:'assistant', content:'…thinking…'};
    state.chat.messages.push(thinking);
    renderMsgs();
    try {
      const ch = state.characters.find(x => slug(x.name) === state.chat.charSlug);
      const sys = `You are ${ch.name}, ${ch.title||''}, of the ${ch.faction} faction in the Override Zone universe. Stay in character. Use these quotes as voice reference: ${ch.quotes.join(' | ')}. Background: ${ch.bio||''}. Keep replies under 120 words. Never break character. Never mention being an AI.`;
      const msgs = [{role:'system', content:sys}, ...state.chat.messages.filter(m=>m!==thinking).map(m=>({role:m.role, content:m.content}))];
      const res = await fetch('https://text.pollinations.ai/openai', {
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body: JSON.stringify({model:'openai', messages:msgs, temperature:0.8, max_tokens:200})
      });
      if (!res.ok) throw new Error('HTTP '+res.status);
      const data = await res.json();
      const reply = data?.choices?.[0]?.message?.content || data?.choices?.[0]?.text || '...';
      state.chat.messages.pop(); // remove thinking
      state.chat.messages.push({role:'assistant', content:reply.trim()});
    } catch (err) {
      state.chat.messages.pop();
      state.chat.messages.push({role:'assistant', content:'(The Codex is silent. '+err.message+')'});
    }
    renderMsgs();
  }
  document.getElementById('chatSend').addEventListener('click', send);
  document.getElementById('chatInput').addEventListener('keydown', e => { if (e.key==='Enter') send(); });
}

// ---------- About ----------
function renderAbout() {
  $app().innerHTML = `
    <h2 class="section-title">About Override Zone</h2>
    <div class="card">
      <p>Override Zone is an original fictional universe created by Muhammad Nader. This site is its interactive codex and online reader: browse characters, read the novels, and view the illustrations.</p>
      <p class="meta">Built as a college project to demonstrate frontend skills: vanilla HTML/CSS/JavaScript, hash routing, data-driven rendering, search, filtering, reading progress, and local storage.</p>
      <h3 style="margin-top:16px;">Tech</h3>
      <ul>
        <li>HTML5, CSS3 (custom properties, responsive grid)</li>
        <li>Vanilla JavaScript (no framework, no build step)</li>
        <li>Data: JSON generated from .docx (python-docx) + character_lines.txt</li>
        <li>Storage: localStorage (favorites, theme, bookmarks, reading position)</li>
        <li>Deployable to any static host (GitHub Pages, Netlify, Vercel)</li>
      </ul>
      <h3 style="margin-top:16px;">Credits</h3>
      <p class="meta">Text and illustrations © Muhammad Nader. Character lines are original and voice-matched; not quoted from source.</p>
    </div>
  `;
}
