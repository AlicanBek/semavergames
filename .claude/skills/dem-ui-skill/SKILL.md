---
name: dem-ui-skill
description: Dem, the Semaver Games UI kit. Use for any Semaver Games interface work, in any game or on the website - building or changing menus, lobby, shop, settings, modals, buttons, logos, colors or copy - and for changing the kit itself (tokens, components, guidelines, logos).
---

# Dem, the Semaver Games UI kit

Dem is the single source for how every Semaver Games title looks and reads outside of gameplay: brand, colors, type, spacing and the menu components. Each game owns its own table and gameplay UI; everything around it comes from Dem.

## Always read the current kit first

The kit changes. Do not rely on values quoted here or remembered from earlier; read the current files before you write any UI.

Inside the `semavergames` repository, read the source:

- `ui-kit-src/GUIDELINES.md` - the rules
- `ui-kit-src/tokens.json` - every token with its usage note
- `ui-kit-src/components/<Name>/README.md` - one component's contract
- `ui-kit-src/components/bundle.css` - the component styles

In any other repository (a game app, another site), fetch the published kit:

- https://semavergames.com/ui-kit/GUIDELINES.md
- https://semavergames.com/ui-kit/tokens.json
- https://semavergames.com/ui-kit/components.css
- https://semavergames.com/ui-kit/logos/ (file names are listed in GUIDELINES.md and on the kit page)

If a fetch fails, say so and stop. Do not guess token values.

## Using the kit to build UI

- Use tokens by name. Never hard-code a color, font size, spacing value or corner radius that a token covers. If nothing fits, propose a new token; do not invent a one-off value.
- On the web: load `tokens.css`, then `components.css`, then `components.js` from `https://semavergames.com/ui-kit/`, and use the `sg-` classes as documented.
- In the React Native app: map `tokens.json` into the app's theme at build time and treat `components.css` and the component READMEs as the visual spec. Do not copy CSS values by hand into components.
- Read a component's README before using it. Button colors carry meaning and are not interchangeable.
- Build for a phone held upright first (about 360px wide), then let it widen. Nothing may run off the side of the screen.
- UI text is Turkish. Set `lang="tr"` so uppercase conversion handles `i` and `İ` correctly, and follow the writing rules in GUIDELINES.md.
- Use the logo files as they are. Never retype a wordmark, redraw an emblem or recolor a mark.

## Changing the kit

Only in the `semavergames` repository.

1. Read `ui-kit-src/README.md` and follow it.
2. Edit the source in `ui-kit-src/`. Never edit `ui-kit/` by hand; it is generated.
3. Change `tokens.json` first when a color, size or font is involved, with a usage note on every new token.
4. Update a component's `preview.html` and `README.md` together. Update `GUIDELINES.md` when a rule changes.
5. Run `python3 ui-kit-src/build.py` (add `--logos` after editing `ui-kit-src/brand/build.py`).
6. Check `ui-kit/index.html` locally at phone width.
7. Commit source and generated files together and open a pull request. Do not push to `main` directly.

Keep changes in the spirit of the kit: one meaning per color, one finish for all buttons, few sizes. A change that adds a second way to do something the kit already does needs a reason in the pull request.

## Changing this skill

This file is part of the kit and is meant to be improved by the team. If an instruction here is wrong, missing or out of date, edit `.claude/skills/dem-ui-skill/SKILL.md` and mirror the change in `AGENTS.md` at the repository root, which gives the same guidance to tools that do not load skills. Keep it short, keep it pointing at the live kit files instead of copying values into it, and send the change as a pull request like any other.

## Do not

- Do not make the kit page indexable or link it from public pages. It carries `noindex` on purpose.
- Do not add gambling language or imagery. Coins are play money and never carry a currency symbol.
- Do not put secrets, personal names or private notes in this repository; it is public.
