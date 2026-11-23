An on/off control for settings, replacing the Açık / Kapalı buttons.

A `button` with `role="switch"` and `aria-checked`. Green track means on, neutral means off; the knob position carries the state too, so it does not rely on color alone.

You provide: an `aria-label` or a visible label in a `SettingsRow`, and a click handler that flips `aria-checked` and saves the setting immediately. No separate save step.

Use it for: sound, chat sound, vibration, notifications.

Don't use it for actions that open something or change more than one value (theme picker, sign in). Those are a `Button`.
