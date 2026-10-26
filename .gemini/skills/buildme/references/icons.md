# Icons: Material Symbols

BuildMe ships a curated set of Material Symbols icons so that every build uses the same icon family without a network call or a package install.

## What is bundled

- Location: `assets/icons/` (relative to the `buildme` skill folder).
- Set: Material Symbols, **Outlined**, 24px, default weight (400), grade 0, fill 0.
- Count: 58 common UI icons (navigation, actions, status, account, commerce, media, and so on). Names follow Material Symbols, for example `arrow_back.svg`, `check_circle.svg`, `shopping_cart.svg`.
- Source and license: Apache License 2.0. See `assets/icons/LICENSE` and `assets/icons/NOTICE.md`. Keep both files with the bundled icons.

## Use the bundled icons first

1. Look for an existing name in `assets/icons/` before adding a new icon.
2. Inline the SVG, or copy it into the project's asset folder, and style it with `currentColor`:

```html
<svg class="icon" aria-hidden="true" focusable="false" viewBox="0 -960 960 960" width="24" height="24" fill="currentColor">
  <path d="M240-200h120v-240h240v240h120v-360L480-740 240-560v360Zm-80 80v-480l320-240 320 240v480H520v-240h-80v240H160Zm320-350Z"/>
</svg>
```

The source files already contain `height`, `width` and `viewBox`. Keep the `viewBox`. Add `fill="currentColor"` (or set `fill: currentColor` in CSS) so that the icon follows the text colour.

3. Size icons with the design system's tokens, for example `1em` or a 20px / 24px step. Do not scale the path by hand.

## Accessibility (required)

- **Decorative icon** (the text already says what it means): `aria-hidden="true"` and `focusable="false"`.
- **Meaningful icon with no visible text** (icon-only button, status icon): give the interactive element an accessible name, such as `<button aria-label="Close dialog">`, and keep the icon `aria-hidden="true"`. Use `role="img"` plus `aria-label` on the SVG only when the icon is not inside a labelled control.
- Icon-only controls need a visible focus state and a hit area of at least 44 × 44 CSS px (the Mandatory UX laws and the perf/a11y audit check this).
- Do not convey state by colour alone. Pair status icons with text.

## Adding an icon that is not bundled

Copy it from the upstream repository (commit recorded in `assets/icons/NOTICE.md` or newer):

```
symbols/web/<name>/materialsymbolsoutlined/<name>_24px.svg
```

- Only use the **Outlined 24px default** variant unless the design calls for another style. Mixing Outlined, Rounded and Sharp in one product breaks the visual system.
- Add the copied file to `assets/icons/` and keep the original `LICENSE` and an updated `NOTICE.md` entry for it.
- The full upstream set is about 2 million files. Do not copy the whole folder into a project.

## Other options

- **Material Symbols web font** (Google Fonts): fine for a project that already loads Google Fonts. Use `font-variation-settings` for weight, fill and grade only when the design needs them.
- **npm package** `material-symbols` (maintained by a third party, not by Google): usable, but it is not vetted by Google. Pin the version and check its licence before use.

## Brands and logos

Do not use third-party logos from this icon set. The upstream project does not include them for legal reasons. Use the brand's official press kit or assets supplied by the client.

## Checklist for the quality gates

- [ ] Every icon comes from `assets/icons/` or a documented addition.
- [ ] All icons use one style (Outlined 24px default) unless the design brief says otherwise.
- [ ] Decorative icons are hidden from assistive technology; icon-only controls have an accessible name.
- [ ] `LICENSE` and `NOTICE.md` are kept with the bundled icons.
- [ ] No third-party brand logos were taken from the icon set.
