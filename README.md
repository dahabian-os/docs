<p align="center"><img src="assets/logo.svg" width="96" alt="Dahab logo"></p>

<h1 align="center">DAHAB • دهب — Guest App Specification</h1>
<p align="center"><b>Reservations • Touring • Trips</b><br>Business requirements (SRS v1.0) + final Figma design, as a browsable website for the team.</p>

---

## What is inside

| Page | What you get |
|---|---|
| `index.html` | Home: all 10 guest-app modules as cards, top findings across modules |
| `01-…html` → `10-…html` | One page per module: SRS coverage, every screen state in Desktop · Tablet · Mobile Web · Native, UI elements, step-by-step flows, business rules, Jira story candidates, open issues |
| `issues.html` | All 117 open issues with search and filters (module, priority, category) |
| `downloads/` | The Excel issues tracker |
| `images/` | 162 Figma screenshots (full size) + `images/thumbs/` previews |

## Open it

- **Locally:** double-click `index.html`. No server or install needed.
- **On GitHub Pages:** push the repository, then go to **Settings → Pages → Build and deployment**, choose **Deploy from a branch**, branch `main`, folder `/ (root)`. The site will be live at `https://<org>.github.io/<repo>/`.

## Update the content

The pages are generated from the Markdown files in `_build/content/`.

```bash
python3 _build/make_thumbs.py   # after adding/replacing screenshots in images/  (needs Pillow)
python3 _build/build_site.py    # rebuild all HTML pages                       (needs pandoc 3.x)
```

- Screenshot file name = Figma frame ID (`16-635.png` = node `16:635`).
- Issues come from `_build/issues.json` (exported from the Excel tracker).
- Styling lives in `assets/style.css` (brand colours: Terracotta `#D05D3F`, Deep Sea Teal `#0F4C5C`, Sand `#FAF8F5`; font Plus Jakarta Sans).

## Sources

- SRS v1.0 — `dahab_platform_srs.md`
- Figma file **Dahab** → page **New** (162 frames, 25 sections)
- Prepared 23 September 2026
