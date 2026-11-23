# Dem UI kit, source

Dem is the Semaver Games UI kit: brand, tokens and menu components shared by every game. This folder is the source of truth. The browsable kit in `../ui-kit/` (live at semavergames.com/ui-kit/) is generated from it.

## Layout

| Path | What it is |
|---|---|
| `tokens.json` | Every color, type style, spacing step, corner size and shadow, each with a usage note. Start here for any visual change. |
| `GUIDELINES.md` | The rules: brand, what each color means, type, writing, shape, behavior. |
| `components/bundle.css` | The `sg-` component classes. Published as `ui-kit/components.css`. |
| `components/bundle.js` | Draws the pointed outline of the faceted button. Published as `ui-kit/components.js`. |
| `components/<Name>/preview.html` | A small live example of one component. |
| `components/<Name>/README.md` | What the component is for, what you provide, do and don't. |
| `assets/Logos/README.md`, `assets/Game Logos/README.md` | Logo and game logo rules. |
| `brand/build.py` | Generates every logo SVG into `brand/logo/`. |
| `brand/wordmark-paths.json` | The outlined lettering used in the logos (made with `brand/outline.html`). |
| `build.py` | Builds `../ui-kit/` from all of the above. |

## Changing the kit

1. Edit the source here. Never edit `../ui-kit/` by hand.
2. If a color, size or font is involved, change `tokens.json` first and give every new token a usage note.
3. For a new or changed component, update its `preview.html` and `README.md` together. A new component also needs a line in the `COMPONENTS` list in `build.py`.
4. Rebuild:

   ```bash
   python3 ui-kit-src/build.py
   ```

   Add `--logos` if you changed `brand/build.py`.
5. Open `ui-kit/index.html` through a local server and check it at phone width (about 375px). Nothing may scroll sideways.
6. Commit the source and the regenerated `ui-kit/` files together, and open a pull request.

A GitHub check fails the pull request if `ui-kit/` does not match what the build produces.

## Not automated

- `apple-touch-icon.png` and `assets/og.png` at the site root are PNG renders of `brand/logo/app-icon.svg` and `brand/og-source.svg`. Re-render them by hand when the logo changes.
- The private design system page is a mirror of this folder and is refreshed on request.
