# Builds the browsable Dem UI kit (../ui-kit/) from the source in this folder.
#
#   python3 ui-kit-src/build.py            rebuild the page, tokens.css and copies
#   python3 ui-kit-src/build.py --logos    also regenerate the logo SVGs first (after editing brand/build.py)
#
# Needs only Python 3.9+. Never edit files in ../ui-kit/ by hand; they are overwritten here.
import json, os, re, shutil, html, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = HERE
BRAND = os.path.join(HERE, 'brand', 'logo')
OUT = os.path.join(HERE, '..', 'ui-kit')
os.makedirs(os.path.join(OUT, 'logos'), exist_ok=True)

if '--logos' in sys.argv:
    subprocess.run([sys.executable, os.path.join(HERE, 'brand', 'build.py')], check=True)

tokens = json.load(open(os.path.join(SRC, 'tokens.json')))

# ---------- copies that other projects consume ----------
shutil.copy(os.path.join(SRC, 'tokens.json'), os.path.join(OUT, 'tokens.json'))
shutil.copy(os.path.join(SRC, 'components', 'bundle.css'), os.path.join(OUT, 'components.css'))
shutil.copy(os.path.join(SRC, 'components', 'bundle.js'), os.path.join(OUT, 'components.js'))
guide = open(os.path.join(SRC, 'GUIDELINES.md')).read().replace('`components/bundle.css`', '`components.css`').replace('`components/bundle.js`', '`components.js`')
open(os.path.join(OUT, 'GUIDELINES.md'), 'w').write(guide)
open(os.path.join(OUT, 'README.md'), 'w').write("""# Dem UI kit (generated)

Everything in this folder is generated from `ui-kit-src/` by `python3 ui-kit-src/build.py`. Do not edit these files by hand; your changes will be overwritten.

| File | What it is |
|---|---|
| `index.html` | The browsable kit, at semavergames.com/ui-kit/. Not indexed by search engines. |
| `tokens.json` | Colors, type, spacing, radius and shadows, each with a usage note. |
| `tokens.css` | The same tokens as CSS custom properties. |
| `components.css` | The `sg-` component classes. |
| `components.js` | Draws the pointed outline of the faceted button and play banner. |
| `GUIDELINES.md` | The rules: brand, what colors mean, type, writing, behavior. |
| `logos/` | Semaver Games logos, game logos and emblems as SVG. |

On the web, load `tokens.css`, `components.css` and `components.js`, and set `lang="tr"` on the page. In the React Native app, read values from `tokens.json` and treat `components.css` as the visual spec.
""")
for f in sorted(os.listdir(BRAND)):
    if f.endswith('.svg'):
        shutil.copy(os.path.join(BRAND, f), os.path.join(OUT, 'logos', f))

css = ['/* Dem, the Semaver Games UI kit. Generated from ui-kit-src/tokens.json, do not edit by hand. */', ':root {']
for fam in ('color', 'spacing', 'radius', 'shadow'):
    css.append(f'  /* {fam} */')
    for t in tokens[fam]['tokens']:
        css.append(f"  --{t['name']}: {t['value']};")
css += ['  /* type */', f"  --font-sans: {tokens['type']['families']['sans']};", '}']
for g in tokens['type']['groups']:
    for s in g['styles']:
        ls = f" letter-spacing: {s['letterSpacing']};" if 'letterSpacing' in s else ''
        css.append(f".{s['name']} {{ font-family: var(--font-sans); font-size: {s['fontSize']}; line-height: {s['lineHeight']}; font-weight: {s['fontWeight']};{ls} }}")
open(os.path.join(OUT, 'tokens.css'), 'w').write('\n'.join(css) + '\n')

# ---------- tiny markdown to HTML (paragraphs, lists, tables, headings, inline code) ----------
def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    return t

def md(text):
    out, lines, i = [], text.strip().split('\n'), 0
    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            i += 1; continue
        if ln.startswith('#'):
            level = min(len(ln) - len(ln.lstrip('#')) + 2, 5)
            out.append(f'<h{level}>{inline(ln.lstrip("# "))}</h{level}>'); i += 1; continue
        if ln.startswith('|') and i + 1 < len(lines) and re.match(r'^\|[\s:|-]+\|$', lines[i + 1].strip()):
            head = [c.strip() for c in ln.strip().strip('|').split('|')]
            i += 2; rows = []
            while i < len(lines) and lines[i].startswith('|'):
                rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')]); i += 1
            out.append('<div class="tablewrap"><table><thead><tr>' + ''.join(f'<th>{inline(c)}</th>' for c in head) + '</tr></thead><tbody>' +
                       ''.join('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>' for r in rows) + '</tbody></table></div>')
            continue
        if ln.startswith('- '):
            items = []
            while i < len(lines) and lines[i].startswith('- '):
                items.append(lines[i][2:]); i += 1
            out.append('<ul>' + ''.join(f'<li>{inline(x)}</li>' for x in items) + '</ul>'); continue
        para = []
        while i < len(lines) and lines[i].strip() and not lines[i].startswith(('#', '- ', '|')):
            para.append(lines[i]); i += 1
        out.append(f'<p>{inline(" ".join(para))}</p>')
    return '\n'.join(out)

def first_sentence(text):
    para = text.strip().split('\n\n')[0].replace('\n', ' ')
    m = re.match(r'(.+?[.!?])(\s|$)', para)
    return m.group(1) if m else para

# ---------- sections ----------
LOGOS = [
    ('logo-stacked-on-dark.svg', 'Logo, on dark', 'felt', 260),
    ('logo-stacked-on-light.svg', 'Logo, on light', 'cream', 260),
    ('mark-on-dark.svg', 'Mark, on dark', 'felt', 170),
    ('mark-on-light.svg', 'Mark, on light', 'cream', 170),
    ('mark-small-on-dark.svg', 'Small mark, on dark', 'felt', 72),
    ('mark-small-on-light.svg', 'Small mark, on light', 'cream', 72),
    ('app-icon.svg', 'App icon', 'plain', 120),
    ('favicon.svg', 'Favicon', 'plain', 48),
]
GAME_LOGOS = [('game-yanik-masasi.svg', 'Yanık Masası', 'felt', 300), ('game-yanik-masasi.svg', 'Yanık Masası, on light', 'cream', 300),
              ('emblem-yanik-card-left.svg', 'Yanık emblem, left', 'felt', 110), ('emblem-yanik-card-right.svg', 'Yanık emblem, right', 'felt', 110)]

def tiles(items):
    out = []
    for f, label, ground, w in items:
        cls = ' class="appicon"' if f == 'app-icon.svg' else ''
        out.append(f'<figure class="tile tile--{ground}"><div class="tile__art"><img src="logos/{f}" width="{w}" alt="{html.escape(label)}"{cls}></div>'
                   f'<figcaption>{html.escape(label)}<a href="logos/{f}" target="_blank" rel="noopener">{f}</a></figcaption></figure>')
    return '<div class="tiles">' + ''.join(out) + '</div>'

def color_groups():
    order = [('Table and surfaces', ('bg-', 'surface-')), ('Button gradients', ('primary-', 'confirm-', 'neutral-', 'locked-')),
             ('Flat fills and marks', ('action-', 'coin', 'status-', 'play-')), ('Gold trim', ('trim-',)), ('Text', ('text-',)), ('Focus', ('focus-',))]
    used, out = set(), []
    for title, prefixes in order:
        toks = [t for t in tokens['color']['tokens'] if t['name'].startswith(prefixes) and t['name'] not in used]
        used.update(t['name'] for t in toks)
        if not toks: continue
        out.append(f'<h3>{title}</h3><div class="swatches">' + ''.join(
            f'<div class="swatch"><span class="swatch__chip" style="background:{t["value"]}"></span><div><code>{t["name"]}</code><span class="swatch__val">{t["value"]}</span><p>{html.escape(t["usage"])}</p></div></div>'
            for t in toks) + '</div>')
    return '\n'.join(out)

def type_rows():
    rows = []
    for g in tokens['type']['groups']:
        for s in g['styles']:
            upper = 'text-transform:uppercase;' if s['name'] in ('display', 'title', 'heading', 'label') else ''
            ls = f"letter-spacing:{s['letterSpacing']};" if 'letterSpacing' in s else ''
            rows.append(f'<div class="typerow"><div class="typerow__meta"><code>{s["name"]}</code><span>{s["fontSize"]} / {s["lineHeight"]} · {s["fontWeight"]}</span></div>'
                        f'<div class="typerow__sample" lang="tr" style="font-size:{s["fontSize"]};line-height:{s["lineHeight"]};font-weight:{s["fontWeight"]};{ls}{upper}">{html.escape(s.get("sample", ""))}</div>'
                        f'<p>{html.escape(s.get("usage", ""))}</p></div>')
    return '\n'.join(rows)

def scale(fam, kind):
    out = []
    for t in tokens[fam]['tokens']:
        if kind == 'space':
            demo = f'<span class="bar" style="width:{t["value"]}"></span>'
        else:
            demo = f'<span class="corner" style="border-radius:{t["value"]}"></span>'
        out.append(f'<div class="scale">{demo}<code>{t["name"]}</code><span class="swatch__val">{t["value"]}</span><p>{html.escape(t["usage"])}</p></div>')
    return '\n'.join(out)

COMPONENTS = [
    ('Actions', ['Button', 'PlayBanner', 'Switch', 'Tabs']),
    ('Status', ['Badge', 'CurrencyPill']),
    ('Navigation', ['TopBar', 'BottomNav']),
    ('Surfaces', ['GameCard', 'Modal', 'ShopItem', 'SettingsRow', 'RewardTile']),
]
def component(name):
    prev = open(os.path.join(SRC, 'components', name, 'preview.html')).read()
    m = re.search(r'<body class="([^"]*)"[^>]*>(.*)</body>', prev, re.S)
    body = re.sub(r'<script>.*?</script>', '', m.group(2), flags=re.S)
    body = re.sub(r'\bid="[^"]*"', '', body)
    readme = open(os.path.join(SRC, 'components', name, 'README.md')).read()
    return (f'<article class="comp" id="c-{name.lower()}"><header><h4>{name}</h4><p>{inline(first_sentence(readme))}</p></header>'
            f'<div class="{m.group(1)} comp__stage" lang="tr">{body}</div>'
            f'<details><summary>Usage notes</summary><div class="prose">{md(readme)}</div></details></article>')

comp_html = ''
for group, names in COMPONENTS:
    comp_html += f'<h3>{group}</h3>' + ''.join(component(n) for n in names)

logos_readme = open(os.path.join(SRC, 'assets', 'Logos', 'README.md')).read()
games_readme = open(os.path.join(SRC, 'assets', 'Game Logos', 'README.md')).read()

page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Dem UI Kit | Semaver Games</title>
<meta name="description" content="Brand, tokens and menu components shared by every Semaver Games title.">
<meta name="robots" content="noindex">
<link rel="icon" href="logos/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700;800;900&display=swap">
<link rel="stylesheet" href="tokens.css">
<link rel="stylesheet" href="components.css">
<style>
  * {{ box-sizing: border-box; }}
  html {{ scroll-behavior: smooth; scroll-padding-top: 64px; }}
  body {{ margin: 0; background: #0d1a13; color: #d9e6d2; font: 500 15px/1.65 Montserrat, "Helvetica Neue", Arial, sans-serif; }}
  a {{ color: #e9c97a; }}
  code {{ font: 600 12.5px/1.4 ui-monospace, SFMono-Regular, Menlo, monospace; background: rgba(255,255,255,.08); color: #fff6de; padding: 1px 5px; border-radius: 4px; }}
  .nav {{ position: sticky; top: 0; z-index: 20; background: rgba(13,26,19,.94); border-bottom: 1px solid rgba(217,178,90,.35); backdrop-filter: blur(6px); }}
  .nav__in {{ max-width: 1040px; margin: 0 auto; padding: 10px 16px; display: flex; align-items: center; gap: 16px; overflow-x: auto; white-space: nowrap; scrollbar-width: none; }}
  .nav__brand {{ display: flex; align-items: center; gap: 8px; color: #fff6de; font-weight: 700; text-decoration: none; letter-spacing: .02em; }}
  .nav__brand img {{ width: 26px; height: 26px; }}
  .nav a.link {{ color: #d9e6d2; text-decoration: none; font-weight: 600; font-size: 14px; }}
  .nav a.link:hover {{ color: #e9c97a; }}
  main {{ max-width: 1040px; margin: 0 auto; padding: 28px 16px 80px; }}
  .hero {{ display: flex; flex-wrap: wrap; align-items: center; gap: 24px; padding: 20px 0 8px; }}
  .hero img {{ width: 200px; height: auto; }}
  .hero h1 {{ margin: 0 0 6px; color: #fff6de; font-size: clamp(24px, 4.5vw, 30px); line-height: 1.2; font-weight: 700; }}
  .hero p {{ margin: 0; max-width: 56ch; }}
  section {{ padding-top: 40px; }}
  h2 {{ margin: 0 0 4px; color: #fff6de; font-size: 21px; line-height: 1.3; font-weight: 700; }}
  h2 + p {{ margin: 0 0 16px; max-width: 70ch; }}
  h3 {{ margin: 28px 0 10px; color: #e9c97a; font-size: 15px; font-weight: 600; }}
  .tiles {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px; }}
  .tile {{ margin: 0; border-radius: 14px; overflow: hidden; border: 1px solid rgba(217,178,90,.25); display: flex; flex-direction: column; }}
  .tile__art {{ flex: 1; display: flex; align-items: center; justify-content: center; min-height: 190px; padding: 20px; }}
  .tile__art img {{ max-width: 100%; height: auto; }}
  .tile--felt .tile__art {{ background: #17301f; }}
  .tile--cream .tile__art {{ background: #fbf0d8; }}
  .tile--plain .tile__art {{ background: #f4f2ec; }}
  .appicon {{ border-radius: 22.5%; }}
  .tile figcaption {{ display: flex; flex-wrap: wrap; justify-content: space-between; gap: 4px 12px; padding: 10px 12px; background: #12241a; font-size: 13px; font-weight: 600; color: #fff6de; }}
  .tile figcaption a {{ font-weight: 500; font-size: 12px; }}
  .swatches {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 10px; }}
  .swatch {{ display: flex; gap: 12px; padding: 10px; background: #12241a; border-radius: 12px; min-width: 0; }}
  .swatch__chip {{ flex: none; width: 48px; height: 48px; border-radius: 10px; border: 1px solid rgba(255,255,255,.22); }}
  .swatch__val {{ margin-left: 8px; font-size: 12px; color: #b5c4b9; font-variant-numeric: tabular-nums; }}
  .swatch p, .scale p, .typerow p {{ margin: 4px 0 0; font-size: 12.5px; line-height: 1.45; color: #b5c4b9; }}
  .typerow {{ padding: 14px 0; border-top: 1px solid rgba(255,255,255,.1); }}
  .typerow__meta {{ display: flex; flex-wrap: wrap; gap: 10px; align-items: baseline; font-size: 12px; color: #b5c4b9; }}
  .typerow__sample {{ margin-top: 6px; color: #fff6de; font-family: Montserrat, "Helvetica Neue", Arial, sans-serif; overflow-wrap: anywhere; }}
  .scales {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 10px; }}
  .scale {{ padding: 12px; background: #12241a; border-radius: 12px; }}
  .bar {{ display: block; height: 14px; margin-bottom: 8px; background: #d9b25a; border-radius: 3px; }}
  .corner {{ display: block; width: 72px; height: 48px; margin-bottom: 8px; background: #fbf0d8; border: 2px solid #d9b25a; }}
  .comp {{ margin: 0 0 16px; border: 1px solid rgba(217,178,90,.25); border-radius: 14px; overflow: hidden; background: #12241a; }}
  .comp > header {{ padding: 12px 14px; }}
  .comp h4 {{ margin: 0; color: #fff6de; font-size: 16px; font-weight: 700; }}
  .comp > header p {{ margin: 2px 0 0; font-size: 13.5px; color: #b5c4b9; }}
  .comp__stage {{ padding: 20px 16px 22px; overflow-x: auto; }}
  .comp__stage.sg-stage--stack > * {{ max-width: 100%; }}
  details {{ border-top: 1px solid rgba(255,255,255,.1); }}
  summary {{ padding: 10px 14px; cursor: pointer; font-weight: 600; font-size: 14px; color: #e9c97a; }}
  .prose {{ padding: 0 14px 14px; font-size: 14px; }}
  .prose p, .prose ul {{ margin: 0 0 10px; }}
  .prose ul {{ padding-left: 20px; }}
  .prose h3, .prose h4, .prose h5 {{ margin: 16px 0 6px; color: #fff6de; font-size: 14px; letter-spacing: 0; text-transform: none; }}
  .tablewrap {{ overflow-x: auto; margin: 0 0 12px; }}
  table {{ border-collapse: collapse; width: 100%; font-size: 13.5px; }}
  th, td {{ text-align: left; vertical-align: top; padding: 7px 10px; border-bottom: 1px solid rgba(255,255,255,.1); }}
  th {{ color: #fff6de; font-weight: 700; }}
  .guide {{ background: #12241a; border-radius: 14px; padding: 6px 16px 10px; }}
  .guide h4 {{ margin: 22px 0 8px; color: #fff6de; font-size: 16px; font-weight: 700; }}
  footer {{ margin-top: 48px; padding-top: 16px; border-top: 1px solid rgba(255,255,255,.1); font-size: 13px; color: #b5c4b9; }}
</style>
</head>
<body>
<nav class="nav" aria-label="Sections"><div class="nav__in">
  <a class="nav__brand" href="#top"><img src="logos/mark-small-on-dark.svg" alt="">Dem</a>
  <a class="link" href="#brand">Brand</a>
  <a class="link" href="#colors">Colors</a>
  <a class="link" href="#type">Type</a>
  <a class="link" href="#scales">Spacing</a>
  <a class="link" href="#components">Components</a>
  <a class="link" href="#guidelines">Guidelines</a>
</div></nav>
<main id="top">
<div class="hero">
  <img src="logos/logo-stacked-on-dark.svg" alt="Semaver Games">
  <div><h1>Dem UI Kit</h1><p>Brand, tokens and menu components shared by every Semaver Games title. Gameplay UI is not covered; each game owns its table.</p></div>
</div>

<section id="brand">
<h2>Brand</h2>
<p>The platform logo, then each game's own logo. Click a file name to open the SVG.</p>
<h3>Semaver Games</h3>
{tiles(LOGOS)}
<details class="comp" style="margin-top:12px"><summary>Logo rules</summary><div class="prose">{md(logos_readme)}</div></details>
<h3>Game logos</h3>
{tiles(GAME_LOGOS)}
<details class="comp" style="margin-top:12px"><summary>Game logo pattern</summary><div class="prose">{md(games_readme)}</div></details>
</section>

<section id="colors">
<h2>Colors</h2>
<p>Every color has one job. Token names are the CSS variable names in <code>tokens.css</code>.</p>
{color_groups()}
</section>

<section id="type">
<h2>Type</h2>
<p>One family, Montserrat. Weight 900 is for large text only.</p>
{type_rows()}
</section>

<section id="scales">
<h2>Spacing and corners</h2>
<p>Six spacing steps and five corner sizes. No other values.</p>
<h3>Spacing</h3>
<div class="scales">{scale('spacing', 'space')}</div>
<h3>Corners</h3>
<div class="scales">{scale('radius', 'corner')}</div>
</section>

<section id="components">
<h2>Components</h2>
<p>Live, built from <code>components.css</code>. Open "Usage notes" under each one for what it needs and what its colors mean.</p>
{comp_html}
</section>

<section id="guidelines">
<h2>Guidelines</h2>
<p>The full rules: what colors mean, type, writing, shape and behavior.</p>
<div class="guide prose">{md(guide)}</div>
</section>

<footer>Files: <a href="tokens.json" target="_blank" rel="noopener">tokens.json</a> · <a href="tokens.css" target="_blank" rel="noopener">tokens.css</a> · <a href="components.css" target="_blank" rel="noopener">components.css</a> · <a href="components.js" target="_blank" rel="noopener">components.js</a> · <a href="GUIDELINES.md" target="_blank" rel="noopener">GUIDELINES.md</a></footer>
</main>
<script src="components.js"></script>
<script>
  // demo behaviour for the previews
  document.querySelectorAll('.sg-switch:not([disabled])').forEach(function (s) {{
    s.addEventListener('click', function () {{ s.setAttribute('aria-checked', s.getAttribute('aria-checked') === 'true' ? 'false' : 'true'); }});
  }});
  document.querySelectorAll('.sg-tabs').forEach(function (tabs) {{
    tabs.querySelectorAll('.sg-tab').forEach(function (t) {{
      t.addEventListener('click', function () {{ tabs.querySelectorAll('.sg-tab').forEach(function (o) {{ o.setAttribute('aria-selected', o === t ? 'true' : 'false'); }}); }});
    }});
  }});
  // links that open in a new tab get a scripted fallback
  document.querySelectorAll('a[target="_blank"]').forEach(function (a) {{
    a.addEventListener('click', function (e) {{ var w = window.open(a.href, '_blank', 'noopener'); if (w) e.preventDefault(); }});
  }});
</script>
</body>
</html>
'''
open(os.path.join(OUT, 'index.html'), 'w').write(page)
print('built ui-kit/:', ', '.join(sorted(os.listdir(OUT))))
