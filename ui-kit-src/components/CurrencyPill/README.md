Shows a balance: coins or scratch tickets.

A dark pill with the currency mark, the amount, and an optional `+` that opens the shop. Use `sg-pill--static` without the `+` on screens that are already the shop.

You provide: the amount, formatted with the Turkish thousands dot (1.500, 12.400) and no decimals. Above 999.999 abbreviate (1,2 Mn).

`sg-coin` is the coin mark on its own; use it next to prices in `ShopItem` and amounts in `RewardTile`. Coins are play money: never show a currency symbol or the word "TL" next to a coin amount.
