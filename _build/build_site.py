#!/usr/bin/env python3
"""Build the Dahab Guest App specification site (plain HTML + CSS).

Usage:
    python3 _build/build_site.py            # run from the repository root

Reads   _build/content/*.md  (module specs)  and  _build/issues.json  (issues tracker)
Writes  index.html, issues.html and one HTML page per module into the repository root.
Needs   pandoc (3.x) on the PATH. Screenshots are expected at images/<frame-id>.png and
        thumbnails at images/thumbs/<frame-id>.jpg (see _build/make_thumbs.py).
"""
import html
import json
import os
import re
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(ROOT, "_build")
CONTENT = os.path.join(BUILD, "content")
FIGMA_FILE = "https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-2"
BPS = {"Desktop": "desktop", "Tablet": "tablet", "Mobile Web": "mobile", "Native App": "native"}
BP_WEIGHT = {"Desktop": 2, "Tablet": 2, "Mobile Web": 1, "Native App": 1}
PRIO_CLASS = {"Blocker": "b-blocker", "High": "b-high", "Medium": "b-medium", "Low": "b-low"}

esc = html.escape


# ---------------------------------------------------------------- helpers
def inline_md(s):
    s = esc(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    return s


def pandoc(md):
    r = subprocess.run(["pandoc", "-f", "gfm", "-t", "html5", "--wrap=none"],
                       input=md, capture_output=True, text=True, check=True)
    return r.stdout


def cells(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def slug_of(fn):
    return fn[:-3]


# ---------------------------------------------------------------- screenshot grids
def shot_block(state, header, imgs, links):
    cols = header
    tmpl = " ".join(f"{BP_WEIGHT[c]}fr" for c in cols)
    out = []
    if state:
        out.append(f'<div class="state-title">{inline_md(state)}</div>')
    out.append(f'<div class="shot-grid" style="grid-template-columns:{tmpl}">')
    for bp, img, link in zip(cols, imgs, links):
        m = re.search(r'images/([\w-]+)\.png', img)
        fid = m.group(1) if m else ""
        lm = re.search(r"\[Figma ([^\]]+)\]\(([^)]+)\)", link)
        node, url = (lm.group(1), lm.group(2)) if lm else ("", "#")
        rtl = '<span class="rtl">Arabic · RTL</span>' if "RTL" in link else ""
        alt = esc(f"{state or 'Screen'} – {bp}")
        out.append(
            f'<figure class="shot bp-{BPS[bp]}">'
            f'<figcaption><span class="bp-ico">{bp}</span>{rtl}</figcaption>'
            f'<a class="frame" href="images/{fid}.png" target="_blank" rel="noopener">'
            f'<img loading="lazy" src="images/thumbs/{fid}.jpg" alt="{alt}"></a>'
            f'<a class="figma" href="{url}" target="_blank" rel="noopener">Open in Figma · {esc(node)}</a>'
            f'</figure>')
    out.append("</div>")
    return "\n".join(out)


def expand_shots(md):
    lines = md.split("\n")
    out, i, first_desktop = [], 0, None
    while i < len(lines):
        line = lines[i]
        state = None
        j = i
        m = re.match(r"^\*\*State: (.+)\*\*\s*$", line)
        if m:
            state = m.group(1)
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
        if j + 3 < len(lines) and lines[j].startswith("|") and cells(lines[j]) and \
                all(c in BPS for c in cells(lines[j])) and "images/" in lines[j + 2]:
            header = cells(lines[j])
            imgs, links = cells(lines[j + 2]), cells(lines[j + 3])
            if first_desktop is None and header[0] == "Desktop":
                fm = re.search(r'images/([\w-]+)\.png', imgs[0])
                first_desktop = fm.group(1) if fm else None
            out += ["", shot_block(state, header, imgs, links), ""]
            i = j + 4
            continue
        out.append(line)
        i += 1
    return "\n".join(out), first_desktop


# ---------------------------------------------------------------- html polish
def polish(h):
    h = re.sub(r"<table>", '<div class="table-wrap"><table>', h)
    h = h.replace("</table>", "</table></div>")

    def td(m):
        attrs, val = m.group(1), m.group(2).strip()
        badge = {
            "H": '<span class="badge b-high">High</span>',
            "M": '<span class="badge b-medium">Medium</span>',
            "L": '<span class="badge b-low">Low</span>',
            "✅": '<span class="badge b-mvp">MVP ✓</span>',
            "Later": '<span class="badge b-later">Later</span>',
        }.get(val)
        if badge is None and re.fullmatch(r"[A-Z0-9]{2,6}-\d+( \(tech\))?", val):
            badge = f'<span class="badge b-key">{val}</span>'
        if badge is None and re.fullmatch(r"G\d+", val):
            badge = f'<span class="badge b-gap">{val}</span>'
        return f"<td{attrs}>{badge or m.group(2)}</td>"

    h = re.sub(r"<td([^>]*)>([^<]{1,20})</td>", td, h)
    return h


def toc_of(h):
    items = []
    for m in re.finditer(r'<h([23]) id="([^"]+)"[^>]*>(.*?)</h\1>', h):
        text = re.sub(r"<[^>]+>", "", m.group(3))
        items.append(f'<li class="l{m.group(1)}"><a href="#{m.group(2)}">{text}</a></li>')
    return "\n".join(items)


# ---------------------------------------------------------------- page shell
def page(title, active, body, modules, toc=""):
    side = ['<div class="side-label">Overview</div><ul>',
            f'<li><a href="index.html"{" class=active" if active == "index" else ""}>'
            f'<span class="num alt">★</span>Home</a></li>',
            f'<li><a href="issues.html"{" class=active" if active == "issues" else ""}>'
            f'<span class="num alt">!</span>Issues tracker</a></li></ul>',
            '<div class="side-label">Guest app modules</div><ul>']
    for mod in modules:
        cls = " class=active" if mod["slug"] == active else ""
        side.append(f'<li><a href="{mod["slug"]}.html"{cls}><span class="num">{mod["num"]}</span>{esc(mod["name"])}</a></li>')
    side.append("</ul>")
    toc_html = (f'<aside class="toc"><div class="side-label">On this page</div><ul>{toc}</ul></aside>'
                if toc else "")
    layout_cls = "layout" if toc else "layout no-toc"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} · Dahab Guest App Specs</title>
<link rel="icon" href="assets/logo.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Noto+Sans+Arabic:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="topbar">
  <label for="nav-toggle" class="nav-btn" aria-label="Menu"><span></span><span></span><span></span></label>
  <a class="brand" href="index.html">
    <img src="assets/logo.svg" alt="">
    <span><span class="brand-name">DAHAB<span class="ar">• دهب</span></span>
    <span class="brand-sub">Guest App · Product Specification</span></span>
  </a>
  <nav class="topbar-links">
    <a href="index.html"{' class="active"' if active == "index" else ""}>Modules</a>
    <a href="issues.html"{' class="active"' if active == "issues" else ""}>Issues</a>
    <a href="{FIGMA_FILE}" target="_blank" rel="noopener">Figma ↗</a>
  </nav>
</header>
<input type="checkbox" id="nav-toggle">
<div class="{layout_cls}">
<nav class="sidebar">{''.join(side)}</nav>
<main class="content">
{body}
</main>
{toc_html}
</div>
<footer class="site-footer">
  <span><b style="color:#fff">DAHAB • دهب</b> — Reservations • Touring • Trips · Guest App specification</span>
  <span>Sources: SRS v1.0 · Figma “Dahab” → page <a href="{FIGMA_FILE}" target="_blank" rel="noopener">New</a> · Prepared 23 Sep 2026</span>
</footer>
<script src="assets/app.js" defer></script>
</body>
</html>
"""


# ---------------------------------------------------------------- modules
def load_modules():
    readme = open(os.path.join(CONTENT, "00-README.md"), encoding="utf-8").read()
    index_rows = {}
    for line in readme.split("\n"):
        m = re.match(r"\|\s*(\d\d)\s*\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|(.*)\|(.*)\|(.*)\|", line)
        if m:
            index_rows[m.group(1)] = dict(sections=m.group(4).strip(), frames=m.group(5).strip(),
                                          epic=m.group(6).strip())
    mods = []
    for fn in sorted(os.listdir(CONTENT)):
        if not re.match(r"\d\d-", fn) or fn.startswith("00-"):
            continue
        md = open(os.path.join(CONTENT, fn), encoding="utf-8").read()
        lines = md.split("\n")
        title = lines[0].lstrip("# ").strip()
        tm = re.match(r"(\d\d)\s*·\s*(.+?)(?:\s+—\s+Guest App)?$", title)
        num, name = tm.group(1), tm.group(2)
        # meta table directly under the title
        meta, k = [], 1
        while k < len(lines) and not lines[k].startswith("|"):
            k += 1
        while k < len(lines) and lines[k].startswith("|"):
            c = cells(lines[k])
            if len(c) >= 2 and c[0] and not set(c[0]) <= set("-: "):
                meta.append((c[0].strip("* "), c[1]))
            k += 1
        while k < len(lines) and lines[k].strip() in ("", "---"):
            k += 1
        rest = "\n".join(lines[k:])
        sm = re.search(r"## 1\. Module summary\s*\n\s*\n(.+?)\n", rest)
        summary = sm.group(1) if sm else ""
        first = re.split(r"(?<=[.!?])\s", summary, maxsplit=1)[0]
        mods.append(dict(file=fn, slug=slug_of(fn), num=num, name=name, meta=meta, body=rest,
                         lead=first, **index_rows.get(num, {})))
    return mods


def module_page(mod, mods, idx):
    body_md, first_desktop = expand_shots(mod["body"])
    mod["thumb"] = first_desktop
    mod["frame_ids"] = set(re.findall(r"images/([\w-]+)\.png", body_md))
    h = polish(pandoc(body_md))
    meta = "".join(f"<div><dt>{esc(k)}</dt><dd>{inline_md(v)}</dd></div>" for k, v in mod["meta"])
    hero = f"""<section class="hero">
  <div class="eyebrow"><span class="hero-num">{mod['num']}</span> Guest App · Module</div>
  <h1>{esc(mod['name'])}</h1>
  <p class="lead">{inline_md(mod['lead'])}</p>
  <dl class="meta">{meta}</dl>
  <div class="hero-waves"></div>
</section>"""
    prev_ = mods[idx - 1] if idx > 0 else None
    next_ = mods[idx + 1] if idx + 1 < len(mods) else None
    pager = '<nav class="pager">'
    if prev_:
        pager += f'<a href="{prev_["slug"]}.html"><small>← Previous</small><b>{prev_["num"]} · {esc(prev_["name"])}</b></a>'
    if next_:
        pager += f'<a class="next" href="{next_["slug"]}.html"><small>Next →</small><b>{next_["num"]} · {esc(next_["name"])}</b></a>'
    pager += "</nav>"
    body = f'{hero}<article class="doc">{h}</article>{pager}'
    return page(f"{mod['num']} {mod['name']}", mod["slug"], body, mods, toc_of(h))


# ---------------------------------------------------------------- home
def home_page(mods, issues):
    readme = open(os.path.join(CONTENT, "00-README.md"), encoding="utf-8").read()
    findings = readme.split("## Top findings", 1)[1].split("## How to use", 1)[0]
    findings_html = polish(pandoc("## Top findings" + findings))
    frames = len({f for m in mods for f in m.get("frame_ids", [])})
    high = sum(1 for i in issues if i["Priority"] in ("High", "Blocker"))
    cards = []
    for m in mods:
        if m.get("thumb"):
            thumb = (f'<div class="card-thumb"><span class="num">{m["num"]}</span>'
                     f'<img loading="lazy" src="images/thumbs/{m["thumb"]}.jpg" alt=""></div>')
        else:
            thumb = f'<div class="card-thumb empty"><span class="num">{m["num"]}</span>Designs in Stitch · not in Figma yet</div>'
        n_issues = sum(1 for i in issues if i["Module"].startswith(m["num"] + " "))
        fr = m.get("frames", "")
        fr_n = re.sub(r"\D.*", "", fr) or "0"
        cards.append(f"""<a class="card" href="{m['slug']}.html">{thumb}
  <div class="card-body"><h3>{esc(m['name'])}</h3><p>{inline_md(m.get('sections', ''))}</p>
  <div class="card-foot"><span class="badge b-low">{fr_n} frames</span>
  <span class="badge b-high">{n_issues} issues</span>
  <span class="badge b-cat">{esc(m.get('epic', ''))}</span></div></div></a>""")
    body = f"""<section class="hero">
  <div class="eyebrow">Dahab Reservations · Touring · Trips</div>
  <h1>Guest App — Product Specification</h1>
  <p class="lead">Every guest-app module described from the business requirements (SRS v1.0) and the final Figma design:
  screens for all four breakpoints, UI elements, step-by-step flows, states, business rules, Jira story candidates and open issues.</p>
  <div class="stats">
    <div class="stat"><b>{len(mods)}</b><span>Modules</span></div>
    <div class="stat"><b>{frames}</b><span>Figma frames</span></div>
    <div class="stat"><b>4</b><span>Breakpoints</span></div>
    <div class="stat"><b>{len(issues)}</b><span>Open issues</span></div>
    <div class="stat"><b>{high}</b><span>High / blocker</span></div>
  </div>
  <div class="stats"><a class="btn" href="01-account-authentication.html">Start reading →</a>
  <a class="btn ghost" href="issues.html">Open issues tracker</a></div>
  <div class="hero-waves"></div>
</section>

<h2 class="section-title">Modules</h2>
<p class="section-sub">Each module becomes one Jira epic. Open a module to see its screens, flows and stories.</p>
<div class="cards">{''.join(cards)}</div>

<h2 class="section-title">How to read a module page</h2>
<div class="howto">
  <div><b>Summary & SRS</b><span>What the module does and which requirements (FR / NFR) it covers, with priority and MVP flag.</span></div>
  <div><b>Screens</b><span>Every state in Desktop · Tablet · Mobile Web · Native. Click a screen to open it full size, or jump to the Figma frame.</span></div>
  <div><b>Flows & rules</b><span>UI elements, step-by-step tables (guest action → system response), states, errors and business rules.</span></div>
  <div><b>Stories & gaps</b><span>Jira story candidates with acceptance criteria, then the gaps and decisions still needed.</span></div>
</div>

<article class="doc">{findings_html}</article>
"""
    return page("Home", "index", body, mods)


# ---------------------------------------------------------------- issues
def issues_page(mods, issues):
    order = ["Blocker", "High", "Medium", "Low"]
    counts = {p: sum(1 for i in issues if i["Priority"] == p) for p in order}
    colors = {"Blocker": "var(--error)", "High": "var(--error)", "Medium": "var(--warning)", "Low": "var(--teal)"}
    bars = "".join(f'<div><b style="color:{colors[p]}">{counts[p]}</b><span>{p}</span></div>' for p in order)
    modules = sorted({i["Module"] for i in issues})
    cats = sorted({i["Category"] for i in issues})
    opt = lambda vals: "".join(f'<option value="{esc(v)}">{esc(v)}</option>' for v in vals)
    rows = []
    for i in issues:
        p = i["Priority"] or ""
        rows.append(
            f'<tr data-mod="{esc(i["Module"])}" data-prio="{esc(p)}" data-cat="{esc(i["Category"] or "")}">'
            f'<td class="id">{esc(i["ID"])}</td>'
            f'<td><span class="badge {PRIO_CLASS.get(p, "b-later")}">{esc(p)}</span></td>'
            f'<td><div class="mod">{esc(i["Module"])}</div>{esc(i["Screen / area"] or "")}</td>'
            f'<td><span class="badge b-cat">{esc(i["Category"] or "")}</span></td>'
            f'<td>{esc(i["Finding"] or "")}</td>'
            f'<td class="sugg">{esc(i["Suggested decision"] or "")}</td>'
            f'<td>{esc(i["Suggested owner"] or "")}</td>'
            f'<td><span class="badge b-open">{esc(i["Status"] or "")}</span></td></tr>')
    body = f"""<section class="hero">
  <div class="eyebrow">Decisions needed</div>
  <h1>Issues tracker</h1>
  <p class="lead">Every gap, inconsistency and open question found by comparing the SRS with the Figma design.
  Decide the High and Blocker items before the related stories enter a sprint.</p>
  <div class="stats"><a class="btn" href="downloads/Guest-App-Issues-Tracker.xlsx">Download Excel tracker</a></div>
  <div class="hero-waves"></div>
</section>
<div class="prio-bars">{bars}<div><b>{len(issues)}</b><span>Total open</span></div></div>
<div class="filters">
  <input id="f-q" type="search" placeholder="Search issues…" aria-label="Search issues">
  <select id="f-mod" aria-label="Module"><option value="">All modules</option>{opt(modules)}</select>
  <select id="f-prio" aria-label="Priority"><option value="">All priorities</option>{opt(order)}</select>
  <select id="f-cat" aria-label="Category"><option value="">All categories</option>{opt(cats)}</select>
  <span class="count" id="f-count">{len(issues)} issues</span>
</div>
<div class="doc"><div class="table-wrap"><table class="issues">
<thead><tr><th>ID</th><th>Priority</th><th>Module / screen</th><th>Category</th><th>Finding</th><th>Suggested decision</th><th>Owner</th><th>Status</th></tr></thead>
<tbody>{''.join(rows)}</tbody></table></div></div>"""
    return page("Issues tracker", "issues", body, mods)


# ---------------------------------------------------------------- main
def main():
    mods = load_modules()
    issues = json.load(open(os.path.join(BUILD, "issues.json"), encoding="utf-8"))
    for idx, mod in enumerate(mods):
        with open(os.path.join(ROOT, mod["slug"] + ".html"), "w", encoding="utf-8") as f:
            f.write(module_page(mod, mods, idx))
        print("built", mod["slug"] + ".html")
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(home_page(mods, issues))
    with open(os.path.join(ROOT, "issues.html"), "w", encoding="utf-8") as f:
        f.write(issues_page(mods, issues))
    print("built index.html, issues.html")


if __name__ == "__main__":
    main()
