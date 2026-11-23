# Generates the Semaver Games logo files in logo/ and a preview sheet (preview.html).
# Run: python3 ui-kit-src/build.py --logos   (or python3 ui-kit-src/brand/build.py)
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

OUTER = "M77 44C77 82 92 100 92 122 92 142 76 152 78 172 79 187 88 196 120 196 152 196 161 187 162 172 164 152 148 142 148 122 148 100 163 82 163 44Z"
INNER = "M82.500 64C83.500 88 97.500 102 97.500 122 97.500 143 82 153 83.500 171 84.500 181 93 186 120 186 147 186 155.500 181 156.500 171 158 153 142.500 143 142.500 122 142.500 102 156.500 88 157.500 64Z"
OUTER_FILL = OUTER[:-1] + "A43 9 0 0 0 77 44Z"  # top edge follows the back of the rim, not a straight line
SPADE = "M120 143c-8.5 10-16 13.800-16 21.200a8 8 0 0 0 13.300 5.900L115.200 179h9.600l-2.100-8.900A8 8 0 0 0 136 164.200c0-7.400-7.500-11.200-16-21.200z"

import math
def wisp(x0, y0, y1, sway, drift, wmax, phase=0.0, n=40):
    """Tapered ribbon rising from (x0, y0) to y1: thin at both ends, widest a third of the way up."""
    left, right = [], []
    for i in range(n + 1):
        t = i / n
        x = x0 + drift * t + sway * math.sin(phase + t * 2 * math.pi * 0.95) * (0.35 + 0.65 * t)
        y = y0 + (y1 - y0) * t
        w = wmax * math.sin(math.pi * t ** 0.6)
        w = max(w, 0.15)
        left.append((x - w, y)); right.append((x + w, y))
    pts = left + right[::-1]
    return 'M' + ' L'.join(f'{x:.2f} {y:.2f}' for x, y in pts) + 'Z'

def defs(p, light):
    return f'''<defs>
<linearGradient id="{p}tea" gradientUnits="userSpaceOnUse" x1="78" y1="0" x2="162" y2="0"><stop offset="0" stop-color="#4a0a07"/><stop offset=".22" stop-color="#a81f18"/><stop offset=".5" stop-color="#e5562d"/><stop offset=".78" stop-color="#a81f18"/><stop offset="1" stop-color="#450906"/></linearGradient>
<linearGradient id="{p}teaV" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".28"/></linearGradient>
<radialGradient id="{p}top" cx=".42" cy=".4" r=".6"><stop offset="0" stop-color="#ffd0a0" stop-opacity=".6"/><stop offset=".55" stop-color="#f4955a" stop-opacity=".22"/><stop offset="1" stop-color="#f4955a" stop-opacity="0"/></radialGradient>
<linearGradient id="{p}glass" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity=".5"/><stop offset=".16" stop-color="#fff" stop-opacity=".1"/><stop offset=".84" stop-color="#fff" stop-opacity=".06"/><stop offset="1" stop-color="#fff" stop-opacity=".38"/></linearGradient>
<linearGradient id="{p}gold" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#b98f3c"/><stop offset=".35" stop-color="#f6dc98"/><stop offset=".65" stop-color="#d9b25a"/><stop offset="1" stop-color="#b98f3c"/></linearGradient>
<linearGradient id="{p}plate" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fffaf0"/><stop offset="1" stop-color="#ead9b2"/></linearGradient>
<radialGradient id="{p}well" cx=".5" cy=".35" r=".65"><stop offset="0" stop-color="#fff8e6"/><stop offset="1" stop-color="#d9c496"/></radialGradient>
<radialGradient id="{p}shadow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#000" stop-opacity="{'.28' if light else '.5'}"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>
<radialGradient id="{p}glow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#e5562d" stop-opacity=".55"/><stop offset="1" stop-color="#e5562d" stop-opacity="0"/></radialGradient>
<linearGradient id="{p}steam" gradientUnits="userSpaceOnUse" x1="0" y1="54" x2="0" y2="0"><stop offset="0" stop-color="{'#6b5540' if light else '#fff6de'}" stop-opacity=".12"/><stop offset=".3" stop-color="{'#6b5540' if light else '#fff6de'}" stop-opacity="{'.5' if light else '.7'}"/><stop offset=".7" stop-color="{'#6b5540' if light else '#fff6de'}" stop-opacity="{'.32' if light else '.45'}"/><stop offset="1" stop-color="{'#6b5540' if light else '#fff6de'}" stop-opacity="0"/></linearGradient>
<filter id="{p}soft" x="-40%" y="-10%" width="180%" height="120%"><feGaussianBlur stdDeviation=".7"/></filter>
<clipPath id="{p}in"><path d="{INNER}"/></clipPath>
<clipPath id="{p}out"><path d="{OUTER_FILL}"/></clipPath>
</defs>'''

def mark(p, light=False):
    edge = '#3a2a1c' if light else '#fff6de'
    edge_op = '.55' if light else '.75'
    body_tint = f'<path d="{OUTER_FILL}" fill="#3a2a1c" opacity=".07"/>' if light else ''
    return f'''{defs(p, light)}
<ellipse cx="120" cy="226" rx="104" ry="17" fill="url(#{p}shadow)"/>
<ellipse cx="120" cy="208" rx="92" ry="24" fill="#c9b27c"/>
<ellipse cx="120" cy="204" rx="92" ry="24" fill="url(#{p}plate)"/>
<g transform="translate(120 204) scale(1 .261)"><circle r="77" fill="none" stroke="#c0261f" stroke-width="19" stroke-dasharray="15.120 15.120"/></g>
<ellipse cx="120" cy="204" rx="92" ry="24" fill="none" stroke="url(#{p}gold)" stroke-width="3"/>
<ellipse cx="120" cy="203" rx="63" ry="15" fill="url(#{p}well)" stroke="#d9b25a" stroke-width="1"/>
<ellipse cx="120" cy="200" rx="46" ry="10" fill="url(#{p}glow)"/>
<ellipse cx="120" cy="199" rx="33" ry="6" fill="#000" opacity=".22"/>
{body_tint}
<g clip-path="url(#{p}out)"><rect x="70" y="32" width="100" height="170" fill="#fff" opacity="{'.25' if light else '.09'}"/></g>
<g clip-path="url(#{p}in)">
<rect x="76" y="60" width="88" height="130" fill="url(#{p}tea)"/>
<rect x="76" y="60" width="88" height="130" fill="url(#{p}teaV)"/>
<ellipse cx="120" cy="182" rx="32" ry="5" fill="#f4955a" opacity=".3"/>
</g>
<ellipse cx="120" cy="64" rx="37.500" ry="7.500" fill="url(#{p}tea)"/>
<ellipse cx="120" cy="64" rx="37.500" ry="7.500" fill="url(#{p}top)"/>
<path d="M83 63.500A37.500 7.500 0 0 1 157 63.500" fill="none" stroke="#ffd9b0" stroke-opacity=".35" stroke-width="1"/>
<path d="{SPADE}" fill="#3a0806" opacity=".35" transform="translate(1.500 2)"/>
<path d="{SPADE}" fill="#fff6de"/>
<path d="{OUTER_FILL}" fill="url(#{p}glass)"/>
<path d="{OUTER[:-1]}" fill="none" stroke="{edge}" stroke-opacity="{edge_op}" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
<path d="{INNER[:-1]}" fill="none" stroke="#fff" stroke-opacity=".2" stroke-width="1.200"/>
<path d="M83 52C83 82 95.500 101 95.500 122 95.500 140 81 152 82 170" fill="none" stroke="#fff" stroke-opacity=".62" stroke-width="4.500" stroke-linecap="round"/>
<path d="M157 76C154.500 92 144.500 106 144.500 122 144.500 138 156.500 150 157.500 166" fill="none" stroke="#fff" stroke-opacity=".3" stroke-width="2.600" stroke-linecap="round"/>
<path d="M93 191Q120 198.500 147 191" fill="none" stroke="#fff" stroke-opacity=".45" stroke-width="2.400" stroke-linecap="round"/>
<path d="M77 44A43 9 0 0 1 163 44" fill="none" stroke="url(#{p}gold)" stroke-width="2.400" opacity=".8"/>
<g fill="url(#{p}steam)" filter="url(#{p}soft)">
<path d="{wisp(108, 53, 3, 6.500, -3, 2.900, 0.300)}"/>
<path d="{wisp(131, 54, 9, 5.500, -2, 2.500, 0.900)}"/>
</g>
<path d="M77 44A43 9 0 0 0 163 44" fill="none" stroke="url(#{p}gold)" stroke-width="3" stroke-linecap="round"/>'''

def svg(body, vb="0 0 240 250", w=480, h=500, title="Semaver Games"):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="{w}" height="{h}" role="img" aria-label="{title}"><title>{title}</title>\n{body}\n</svg>\n'

# small flat version, 64 grid
S_GLASS = "M19.500 9C19.500 20 24.500 25 24.500 31.500 24.500 37.500 19 40.500 19.500 46.500 20 51 23.500 53.500 32 53.500 40.500 53.500 44 51 44.500 46.500 45 40.500 39.500 37.500 39.500 31.500 39.500 25 44.500 20 44.500 9Z"
S_SPADE = "M32 34.500c-3.200 3.800-6 5.200-6 8a3 3 0 0 0 5 2.200L30.200 48h3.600l-.8-3.300A3 3 0 0 0 38 42.500c0-2.800-2.800-4.200-6-8z"
def small(light=False):
    line = '#3a2a1c' if light else '#fff6de'
    return f'''<ellipse cx="32" cy="54.500" rx="25" ry="6" fill="#fbf0d8" stroke="#d9b25a" stroke-width="1.500"/>
<g transform="translate(32 54.500) scale(1 .24)"><circle r="20.500" fill="none" stroke="#c0261f" stroke-width="6" stroke-dasharray="8.050 8.050"/></g>
<path d="{S_GLASS}" fill="#b3261e"/>
<path d="M19.500 9H44.500C44.500 12 44.200 14.500 43.600 16.500H20.400C19.800 14.500 19.500 12 19.500 9Z" fill="{'#fbf0d8' if light else '#17301f'}" opacity=".85"/>
<path d="{S_SPADE}" fill="#fff6de"/>
<path d="{S_GLASS}" fill="none" stroke="{line}" stroke-width="2.800" stroke-linejoin="round"/>
<path d="M19.500 9H44.500" stroke="#d9b25a" stroke-width="3" stroke-linecap="round"/>'''

files = {
 'logo/mark-on-dark.svg': svg(mark('d')),
 'logo/mark-on-light.svg': svg(mark('l', True)),
 'logo/mark-small-on-dark.svg': svg(small(), "0 0 64 64", 256, 256),
 'logo/mark-small-on-light.svg': svg(small(True), "0 0 64 64", 256, 256),
 'logo/app-icon.svg': svg('<defs><radialGradient id="bg" cx=".5" cy=".36" r=".75"><stop offset="0" stop-color="#2a6140"/><stop offset=".6" stop-color="#17301f"/><stop offset="1" stop-color="#0a2f1c"/></radialGradient></defs><rect width="1024" height="1024" fill="url(#bg)"/><g transform="translate(152 122) scale(3)">' + mark('a') + '</g>', "0 0 1024 1024", 1024, 1024, "Semaver Games app icon"),
 'logo/favicon.svg': svg('<rect width="64" height="64" rx="14" fill="#17301f"/><g transform="translate(5 4) scale(.84)">' + small() + '</g>', "0 0 64 64", 64, 64, "Semaver Games"),
}
# stacked logo: mark above, SEMAVER, then GAMES between two rules (text is outlined, no font needed)
import json
WM = json.load(open('wordmark-paths.json'))
def stacked(p, light):
    name, sub, rule = ('#8e1b14', '#3a2a1c', '#c9a24e') if light else ('#fff6de', '#e9c97a', '#d9b25a')
    return (f'<g transform="translate(84 0) scale(.55)">{mark(p, light)}</g>'
            f'<path transform="translate(40.48 176) scale(.4)" d="{WM["semaver"]}" fill="{name}"/>'
            f'<path transform="translate(108.810 197) scale(.15)" d="{WM["games"]}" fill="{sub}"/>'
            f'<rect x="64" y="190.750" width="34" height="2" rx="1" fill="{rule}"/>'
            f'<rect x="202" y="190.750" width="34" height="2" rx="1" fill="{rule}"/>')
files['logo/logo-stacked-on-dark.svg'] = svg(stacked('sd', False), "0 0 300 206", 600, 412)
files['logo/logo-stacked-on-light.svg'] = svg(stacked('sl', True), "0 0 300 206", 600, 412)

# ---- game logos: the plaque from the Yanık Masası build, the game name, and the game's emblem on both sides
PLAQUE = ('<path d="M24 9.5 Q86 0.5 148 9.5 L162 27.5 L148 45.5 Q86 52.5 24 45.5 L10 27.5 Z" fill="#450906"/>'
          '<path d="M24 6 Q86 -3 148 6 L162 24 L148 42 Q86 49 24 42 L10 24 Z" fill="url(#{p}body)" stroke="#D9B25A" stroke-width="1.5" stroke-linejoin="round"/>'
          '<path d="M26 9 Q86 0.5 146 9 L157 24 L146 39 Q86 45.5 26 39 L15 24 Z" fill="none" stroke="rgba(243,213,138,0.5)" stroke-width="0.8"/>'
          '<path d="M27 8.5 Q86 0.5 145 8.5 L153 19 Q86 11 19 19 Z" fill="url(#{p}gloss)"/>')
FLAME_CARD = ('<path d="M9 54C2 41 8 30 13 23C13 30 16 33.500 19.500 34.500C17 22 23 11 32 2C31 11 35 17.500 39.500 21.500C41.500 17.500 41.500 13.500 40.500 9.500C49 18 55 30 53 45C52 51 50 55 47 59L13 59Z" fill="url(#{p}f1)"/>'
              '<path d="M15 53C10.500 44 14.500 36 18 31.500C19 36.500 21 38.500 24 38.500C22 28 27 20 32.500 13.500C32.500 20 35.500 25 38.500 28C40.500 26 41.500 23 41.500 21C46.500 28 48.500 36.500 46.500 46.500L44.500 57L16 57Z" fill="url(#{p}f2)"/>'
              '<path d="M20.500 53C18.500 47 20.500 41.500 23.500 38.500C24.500 42.500 26.500 43.500 28.500 42.500C27.500 35.500 30.500 30.500 33.500 26.500C33.500 31.500 36.500 34.500 38.500 37.500C41.500 40.500 42.500 45.500 40.500 53Z" fill="url(#{p}f3)"/>'
              '<rect x="12.800" y="37.300" width="36" height="46" rx="5" fill="#000" opacity=".28"/>'
              '<rect x="12" y="36" width="36" height="46" rx="5" fill="url(#{p}card)" stroke="#d9b25a" stroke-width="1"/>'
              '<path transform="translate(-21.200 -9.500) scale(1.600)" d="M32 34.500c-3.200 3.800-6 5.200-6 8a3 3 0 0 0 5 2.200L30.200 48h3.600l-.8-3.300A3 3 0 0 0 38 42.500c0-2.800-2.800-4.200-6-8z" fill="#1c1410"/>')
def game_logo(p, line1, line2):
    d = (f'<defs><linearGradient id="{p}body" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#C8322A"/><stop offset=".55" stop-color="#8E1B14"/><stop offset="1" stop-color="#5E0D09"/></linearGradient>'
         f'<linearGradient id="{p}gloss" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".34"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>'
         f'<linearGradient id="{p}f1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f4722e"/><stop offset="1" stop-color="#c0261f"/></linearGradient>'
         f'<linearGradient id="{p}f2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffb23e"/><stop offset="1" stop-color="#f0602b"/></linearGradient>'
         f'<linearGradient id="{p}f3" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffe9a3"/><stop offset="1" stop-color="#ffb627"/></linearGradient>'
         f'<linearGradient id="{p}card" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fffaf0"/><stop offset="1" stop-color="#ead9b2"/></linearGradient></defs>')
    def word(key, y):
        d0 = WM[key]
        import re
        nums = re.findall(r'-?\d+\.?\d*', d0)
        xv = [float(n) for n in nums[0::2]]
        x1, x2 = min(xv), max(xv)
        k = 0.143
        tx = 120 - (x2 - x1) * k / 2 - x1 * k
        return (f'<path transform="translate({tx:.2f} {y + 0.8:.2f}) scale({k})" d="{d0}" fill="#4a0a07"/>'
                f'<path transform="translate({tx:.2f} {y:.2f}) scale({k})" d="{d0}" fill="#fff6de"/>')
    plaque = '<g transform="translate(34 18)">' + PLAQUE.replace('{p}', p) + '</g>'
    card = FLAME_CARD.replace('{p}', p)
    left = f'<g transform="translate(20 6) rotate(-9 30 60) scale(.82)">{card}</g>'
    right = f'<g transform="translate(220 6) scale(-1 1) rotate(-9 30 60) scale(.82)">{card}</g>'
    return d + plaque + word(line1, 37.450) + word(line2, 56.550) + left + right
def emblem_defs(p):
    return (f'<defs><linearGradient id="{p}f1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f4722e"/><stop offset="1" stop-color="#c0261f"/></linearGradient>'
            f'<linearGradient id="{p}f2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffb23e"/><stop offset="1" stop-color="#f0602b"/></linearGradient>'
            f'<linearGradient id="{p}f3" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffe9a3"/><stop offset="1" stop-color="#ffb627"/></linearGradient>'
            f'<linearGradient id="{p}card" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fffaf0"/><stop offset="1" stop-color="#ead9b2"/></linearGradient></defs>')
files['logo/emblem-yanik-card-left.svg'] = svg(emblem_defs('el') + '<g transform="translate(6 2) rotate(-9 30 60)">' + FLAME_CARD.replace('{p}', 'el') + '</g>', "0 0 64 90", 256, 360, "Yanık flaming card, left")
files['logo/emblem-yanik-card-right.svg'] = svg(emblem_defs('er') + '<g transform="translate(58 2) scale(-1 1) rotate(-9 30 60)">' + FLAME_CARD.replace('{p}', 'er') + '</g>', "0 0 64 90", 256, 360, "Yanık flaming card, right")
files['logo/game-yanik-masasi.svg'] = svg(game_logo('ym', 'yanik', 'masasi'), "0 0 240 84", 720, 252, "Yanık Masası")

for f, s in files.items(): open(f, 'w').write(s)

sheet = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Semaver Games logo sheet</title><meta name="robots" content="noindex">
<style>
body{margin:0;padding:24px 16px;background:#101613;color:#d9e6d2;font:14px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
h1{font-size:18px;margin:0 0 16px;color:#fff6de}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;max-width:1000px}
figure{margin:0;border-radius:14px;padding:16px;text-align:center}
figcaption{margin-top:8px;font-size:13px}
.felt{background:#17301f}.cream{background:#fbf0d8;color:#6b5540}.white{background:#fff;color:#555}.night{background:#140c0a}
img{max-width:100%;height:auto}
.row{display:flex;flex-wrap:wrap;gap:18px;align-items:flex-end;justify-content:center}
.icon{border-radius:22.5%}
</style></head><body>
<h1>Semaver Games logo and mark</h1>
<div class="grid">
<figure class="felt"><img src="logo/game-yanik-masasi.svg" width="320" alt="Yanık Masası logo"><figcaption>Yanık Masası game logo on felt</figcaption></figure>
<figure class="cream"><img src="logo/game-yanik-masasi.svg" width="320" alt=""><figcaption>Yanık Masası game logo on cream</figcaption></figure>
<figure class="felt"><div class="row"><img src="logo/emblem-yanik-card-left.svg" width="110" alt="Flaming card, left"><img src="logo/emblem-yanik-card-right.svg" width="110" alt="Flaming card, right"></div><figcaption>Yanık flaming cards, left and right</figcaption></figure>
<figure class="felt"><img src="logo/logo-stacked-on-dark.svg" width="300" alt="Stacked logo on felt"><figcaption>Stacked logo on felt</figcaption></figure>
<figure class="cream"><img src="logo/logo-stacked-on-light.svg" width="300" alt="Stacked logo on cream"><figcaption>Stacked logo on cream</figcaption></figure>
<figure class="night"><img src="logo/logo-stacked-on-dark.svg" width="150" alt=""><figcaption>Stacked logo at 150px wide</figcaption></figure>
<figure class="white"><img src="logo/logo-stacked-on-light.svg" width="150" alt=""><figcaption>Stacked logo at 150px on white</figcaption></figure>
<figure class="felt"><img src="logo/mark-on-dark.svg" width="260" alt="Mark on felt"><figcaption>Full mark on felt</figcaption></figure>
<figure class="night"><img src="logo/mark-on-dark.svg" width="260" alt="Mark on dark"><figcaption>Full mark on near-black</figcaption></figure>
<figure class="cream"><img src="logo/mark-on-light.svg" width="260" alt="Mark on cream"><figcaption>Light-background version on cream</figcaption></figure>
<figure class="white"><img src="logo/mark-on-light.svg" width="260" alt="Mark on white"><figcaption>Light-background version on white</figcaption></figure>
<figure class="white"><div class="row"><img class="icon" src="logo/app-icon.svg" width="140" alt="App icon"><img class="icon" src="logo/app-icon.svg" width="90" alt=""><img class="icon" src="logo/app-icon.svg" width="48" alt=""></div><figcaption>App icon at 140, 90 and 48px</figcaption></figure>
<figure class="felt"><div class="row"><img src="logo/mark-small-on-dark.svg" width="96" alt="Small mark"><img src="logo/mark-small-on-dark.svg" width="48" alt=""><img src="logo/mark-small-on-dark.svg" width="24" alt=""></div><figcaption>Simplified mark at 96, 48 and 24px</figcaption></figure>
<figure class="cream"><div class="row"><img src="logo/mark-small-on-light.svg" width="96" alt="Small mark, light"><img src="logo/mark-small-on-light.svg" width="48" alt=""><img src="logo/mark-small-on-light.svg" width="24" alt=""></div><figcaption>Simplified mark on cream</figcaption></figure>
<figure class="white"><div class="row"><img src="logo/favicon.svg" width="64" alt="Favicon"><img src="logo/favicon.svg" width="32" alt=""><img src="logo/favicon.svg" width="16" alt=""></div><figcaption>Favicon at 64, 32 and 16px</figcaption></figure>
</div></body></html>'''
open('preview.html', 'w').write(sheet)
print('built', sorted(os.listdir('logo')))
