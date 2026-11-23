# Instructions for AI coding tools

This repository holds the Semaver Games website and **Dem**, the Semaver Games UI kit.

Before any interface work here, read `.claude/skills/dem-ui-skill/SKILL.md` and follow it. In short:

- `ui-kit-src/` is the source of the kit. `ui-kit/` is generated from it by `python3 ui-kit-src/build.py`. Never edit `ui-kit/` by hand.
- Start visual changes in `ui-kit-src/tokens.json`. Use tokens by name; do not hard-code colors, sizes or corner values.
- Read `ui-kit-src/GUIDELINES.md` and the component's own `README.md` before using or changing a component.
- After changing the kit, rebuild, check `ui-kit/index.html` at phone width, and commit source and generated files together.
- Open a pull request. Do not push to `main` directly.
- The kit, the skill file and this file are all open to improvement by the team. Change them the same way: edit, rebuild if the kit changed, pull request.
- The repository is public. No secrets, personal names or private notes.
- The kit page is deliberately not indexed (`noindex`, and AI crawlers are blocked in `robots.txt`). Keep it that way and do not link it from public pages.

The landing page is `index.html` at the root. It loads the kit's tokens and components from `/ui-kit/` and its copy is Turkish.
