The one button for every menu action, in five meanings that never swap.

| Class | Meaning | Examples |
|---|---|---|
| `sg-btn` (primary, red) | Moves the player forward. One per view. | Oyna, Satın Al, Ödülü Al, Giriş Yap |
| `sg-btn--confirm` (green) | Acknowledges or shows a positive state. | Tamam, Takılı |
| `sg-btn--secondary` (gold) | Secondary action or opening a reference screen. | Yanık Öğren, Kuralları Aç, Tak |
| `sg-btn--alt` (muted blue) | Optional alternative. Not part of the default set. | Arkadaş Davet Et |
| `sg-btn--ghost` | Navigation on the felt. | Geri |
| `sg-btn--danger` | Destructive. Always followed by a confirm modal. | Hesabı Sil |

The muted blue `sg-btn--alt` is kept as an alternative for cases where a screen needs a third filled button that is neither the main action (red) nor the plain secondary (gold), such as a social action. It is the only cool color among the buttons, so use it rarely and never as the main action.

Every filled button has the same finish: a three-stop vertical gradient, a 2px `trim-gold` border and a lip in the color's darkest shade. Red reads `primary-top`, `primary-mid`, `primary-bottom` and `primary-lip`; green and gold have the same four stops under `confirm-` and `secondary-`. Gold takes a dark label. A `disabled` button switches to the `locked-` stops.

The faceted button, `sg-btn sg-btn--hex`, is that same finish with pointed ends. Use it where the player enters a game or a destination from the lobby: the button on a `GameCard` ("Oyna", "Masa Kur", "Giriş Yap") and the `PlayBanner`. Everywhere else (modals, shop, settings) use the rounded button. The pointed outline is drawn by `components/bundle.js`, which finds every `sg-btn--hex` on the page; call `Semaver.init()` after adding buttons later.

Sizes: `sg-btn--sm` (36px), default (44px), `sg-btn--lg` (56px). `sg-btn--block` fills its container.

Labels are set in the `label` style: Montserrat 700, uppercase. Do not make them heavier.

You provide: the label, in Turkish, as a verb or verb phrase of one to three words. Write it in normal case; CSS uppercases it, and the page must carry `lang="tr"` so `i` becomes `İ`.

Do:
- Keep the default height on phones; 44px is the minimum touch target.
- Use `disabled` for locked items and say why in the label ("5. Seviye").

Don't:
- Use the faceted button inside modals, shop items or settings rows, or put two of them next to each other outside a row of game cards.
- Put two primary buttons side by side. Pair primary with secondary or ghost.
- Use green for buying or playing, or red for on/off state. A setting that turns on and off is a `Switch`.
