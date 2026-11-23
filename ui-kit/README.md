# Dem UI kit (generated)

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
