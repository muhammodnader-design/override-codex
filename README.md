# Override Zone — Codex & Reader

An interactive codex and online reader for the **Override Zone** original
novel universe: 36 characters, 4 novels, 9 factions, and 44 illustrations.
Built as a college project to demonstrate frontend skills.

## Features

- **Home:** universe overview, stats, faction preview.
- **Characters:** searchable/filterable gallery (by name, faction, quote), detail
  view with all quotes, favorites, prev/next navigation, random character.
- **Novels:** 4 full novels readable online with progress bar, font-size
  controls, search-in-text, bookmarks, and .docx download.
- **Gallery:** 44 illustrations with folder filter, lightbox, and download.
- **Lore:** factions and the universe disclaimer.
- **About:** tech and credits.
- Dark/light theme, responsive layout, keyboard-friendly, deep links via URL hash.

## Tech stack

- HTML5, CSS3 (custom properties, responsive grid), vanilla JavaScript (no framework, no build step).
- Data: JSON generated from `.docx` (python-docx) + `character_lines.txt`.
- Storage: `localStorage` (favorites, theme, bookmarks, reading position).
- Deployable to any static host (GitHub Pages, Netlify, Vercel).

## Run locally

```bash
python -m http.server 8000
# then open http://localhost:8000
```

(Any static server works; `fetch()` requires http, not `file://`.)

## Regenerate data

```bash
pip install python-docx
python build_data.py
```

Reads from `D:\writing\override_zone` (adjust `BASE` in the script) and writes
`data/*.json` plus copies illustrations into `assets/illustrations/`.

## Project structure

```
override-codex/
  index.html
  css/style.css
  js/app.js
  data/            # characters.json, novels.json, novel_*.json, lore.json, gallery.json
  assets/
    illustrations/ # 44 images
    novels/        # .docx originals for download
  build_data.py
  README.md
  LICENSE
```

## License

MIT — see [LICENSE](LICENSE). Text and illustrations © Muhammad Nader.
