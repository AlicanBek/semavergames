# Semaver Games UI Kit

Shared menu and shell UI for every Semaver Games title (lobby, shop, settings, rewards, modals). Gameplay UI is not covered.

| File | What it is |
|---|---|
| `tokens.json` | Source of truth for colors, type, spacing, radius and shadows. Each token has a usage note. |
| `tokens.css` | The same tokens as CSS custom properties, generated from `tokens.json`. |
| `components.css` | The `sg-` component classes (buttons, switch, tabs, cards, modal, shop item, settings rows, nav). |
| `components.js` | Draws the pointed outline of the faceted button and play banner as SVG. |
| `GUIDELINES.md` | The rules: what each color means, type, copy, behavior. |

On the web, load `tokens.css`, `components.css` and `components.js`, and set `lang="tr"` on the page. In the React Native app, read values from `tokens.json` and treat `components.css` as the visual spec.

Change `tokens.json` first, then regenerate `tokens.css`. Do not edit `tokens.css` by hand.
