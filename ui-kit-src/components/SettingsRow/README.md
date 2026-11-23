A cream panel of settings: each row is a name, a one-line hint and exactly one control on the right.

The control tells the player what kind of row it is:

- `Switch` for anything that is on or off.
- Secondary small `Button` ("Aç") for rows that open another screen.
- `sg-code` chip for a value to read or copy, like the friend code.
- Danger small `Button` for destructive rows, always last in the panel.

You provide: the panel title, and per row the name (sentence case), the hint (wraps fully, never truncated) and the control.

Panels stack in one column on phones and sit two across from 720px. Maximum panel width 420px.
