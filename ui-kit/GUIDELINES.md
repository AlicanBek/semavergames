The shared menu and shell UI for every Semaver Games title: lobby, shop, settings, rewards, modals. It does not cover gameplay (the table, cards in hand, turn indicators); each game owns that.

## Brand

- Semaver Games is the platform; each game is its own title under it. The platform logo is the tea glass on a striped saucer above the "SEMAVER GAMES" wordmark (Logos assets). Each game has its own logo on the shared red plaque (Game Logos assets).
- Inside a game, the game's logo leads: lobby header, loading screen, share images. The Semaver Games mark appears small, on the splash screen and in settings or the footer.
- On the platform's own surfaces (semavergames.com, the store publisher page, the game picker) the Semaver Games logo leads and game logos are the items being chosen.
- Use the logo files as they are. Never retype a wordmark or redraw an emblem.

## How to use it

- Load `tokens.css`, then `components.css`, then `components.js`. Components are plain HTML with `sg-` classes; the script only draws the faceted button shape.
- Read a component's README before using it. Each one says what you provide and what its colors mean.
- Set `lang="tr"` on the page. Labels are uppercased by CSS, and Turkish needs it to turn `i` into `İ`.
- Build for a phone held upright first (360px wide, 16px gutter from `space-4`), then let it widen. Nothing may run off the side of the screen.

## What the colors mean

The look is a card table: `bg-table` felt, `surface-panel` cream panels, `trim-gold` edges. On top of that, button color is a promise and never changes:

| Color | Token | Meaning |
|---|---|---|
| Red | `primary-` gradient | Moves the player forward: play, buy, claim, sign in. One per view. |
| Green | `confirm-` gradient | A positive state or an acknowledgement: on, equipped, OK. |
| Grey-brown | `neutral-` gradient | Secondary actions, opening a reference screen, the off state. |
| Outline red on cream | `text-heading` border | Destructive, always confirmed in a modal. |

- Text on the felt and on filled buttons is `text-on-dark`. Text on cream is `text-on-panel`, with `text-heading` for titles and `text-on-panel-muted` for hints.
- `trim-gold` is for borders only. For gold text on dark use `trim-gold-light`. Never set gold text on cream.
- `coin` is the coin face, not a text color. `status-online` is the live dot next to a player count.
- Keyboard focus is a 3px `focus-ring` outline with a 2px offset on every control.

## Type

One family, Montserrat, in three weights (600, 700, 900), loaded from Google Fonts.

- `display`, `title`, `heading` and `label` are uppercase with a little letter spacing. Use them for names of things and for buttons.
- `body` and `caption` are sentence case. Anything the player reads as a sentence goes here.
- `numeric` is for coin amounts and prices, with tabular figures.

## Writing

- Turkish, informal second person singular: "Hediyen seni bekliyor", "İlerlemeni kaydet".
- Buttons are a verb or verb phrase of one to three words: "Oyna", "Satın Al", "Ödülü Al", "Masa Kur".
- Hints are one short sentence without a full stop: "Kart, sıra ve bitiş sesleri".
- Numbers use the Turkish thousands dot: 1.500, 12.400. Coins are called "para" and never carry a money symbol.
- Labels are never truncated. If a label does not fit, shorten the word, not the box.

## Shape and depth

- Corners: `radius-md` on buttons and tiles, `radius-lg` on panels and modals, `radius-xl` on lobby cards, `radius-pill` on pills, switches and badges, `radius-sm` on tabs and chips. No other corner sizes.
- Every filled button has one finish: a three-stop vertical gradient (`primary-`, `confirm-` or `neutral-` with `-top`, `-mid`, `-bottom`), a 2px `trim-gold` border, and a 4px lip in the matching `-lip` color. It moves down 2px when pressed. No gloss, no inner lines.
- The faceted button (`sg-btn--hex`) and the play banner are that same finish with pointed ends. The shape alone marks entering a game from the lobby, and it is not used anywhere else.
- Panels resting on the felt use `shadow-card`; anything floating above it uses `shadow-panel`.
- The diamond rule (`sg-rule`) sits under a panel or modal title, once per surface.

## Behavior rules

- One unprompted modal per session start at most. Waiting rewards show as a badge.
- Every modal can be closed with its close button, Escape, or a tap outside.
- A setting that is on or off is a `Switch`. A button never doubles as a state display.
- The bottom nav holds at most five items.
- Touch targets are at least 44px tall; small buttons (36px) are only for rows inside a panel.

## Themes

`yanik` is the first and default theme. A new game adds a theme that overrides only the `primary-` stops and the `action-primary` family and, if it wants its own table, `bg-table` and `bg-table-deep`. Panels, text, gold, green and neutral stay the same across games so the menus feel like one platform.

## Iconography and art

- The bottom nav uses 24px line icons, 2px stroke, round caps, in the label's color.
- The suit glyphs in `GameCard` and the plain card backs in `ShopItem` are placeholders. Each game supplies its own illustrations for those slots.
- The logo is the tea glass mark above the "SEMAVER GAMES" wordmark, in the Logos assets (`logo-stacked-on-dark.svg`, `logo-stacked-on-light.svg`). Use the mark on its own (`mark-on-dark.svg`, `mark-on-light.svg`) where the name is already present, and the small versions under 64px. Never retype the wordmark; use the files.
- No emoji in the UI.

## Intentional changes from the first Yanık build

- `Switch` replaces the Açık / Kapalı buttons in settings.
- Green and red buttons now have one meaning each, as in the table above.
- Seven corner sizes became five.
- Playfair Display and Oswald are dropped; only Montserrat is loaded.
- The bottom nav went from six items to five so labels fit on a phone.
- Layout is phone-upright first.
