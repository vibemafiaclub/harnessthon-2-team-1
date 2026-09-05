# design.md — 디자인 가이드 (Apple 웹 디자인 언어)

> **이 파일은 사람이 준 가이드입니다. 에이전트는 읽기만 하며, 본문(§Overview~§Known Gaps)을 수정하지 않습니다.**
> 에이전트가 결정할 수 있는 범위는 맨 아래 **부록 C "에이전트 결정 권한 경계"** 표에 한정됩니다.
>
> **하네스 셋업 시 복원한 깨진 참조(원문 복붙 중 손상된 부분, 문맥상 명백한 것만):**
> `{colors.pri #0071e3)` → `{colors.primary-focus}` · hero-display 행 weight 600 / line-height 1.07 · `{colors.pr}` → `{colors.primary-focus}` · `{typography.display-egative` → `{typography.display-lg}` + negative letter-spacing · `{typography.hero-displayhy.display-lg}` → `{typography.hero-display}` → `{typography.display-lg}` · Small phone 행 `≤ 419px` · Elevation 표 헤더 · 기타 단어 잘림("retaie", "ptographic" 등).
> 원문에 참조되지만 정의가 없던 토큰 두 개를 §Colors에 추가: `{colors.on-dark}` = #ffffff, `{colors.on-primary}` = #ffffff.

## Overview

Apple's web presence is a masterclass in **reverent product photography framed by near-invisible UI**. Every page is a stack of edge-to-edge product "tiles" — alternating light and dark canvases, each centered on a hero headline, a one-line tagline, two tiny blue pill CTAs, and an impossibly crisp product render. Nothing competes with the product. Typography is confident but quiet; color is either pure white, an off-white parchment, or a near-black tile; interactive elements are a single, quiet blue.

Density is unusually low even by contemporary SaaS standards. Each tile occupies roughly one viewport, and there is no decorative chrome — no borders, no gradients, no decorative frames, no shadows on headlines. Elevation appears only when a product image rests on a surface (a single soft `rgba(0, 0, 0, 0.22) 3px 5px 30px` drop for visual weight). The result is a catalog that feels more like a museum gallery: the wall disappears and the artifact takes over.

Store and shop surfaces retain the same chassis but switch modes. The product configurator (iPhone 17 Pro, accessories grid) introduces a tight grid of white utility cards at `{rounded.lg}` (18px) radius with a thin border, paired with a persistent thin sub-nav strip. The environment page leans darker and more editorial. Across all five surfaces the typographic system, spacing rhythm, and the single blue accent are consistent — this is one design language expressed at different volumes.

**Key Characteristics:**

- Photography-first presentation; UI recedes so the product can speak.
- Alternating full-bleed tile sections: white/parchment ↔ near-black, with the color change itself acting as the section divider.
- Single blue accent (`{colors.primary}` — #0066cc) carries every interactive element. No second brand color exists.
- Two button grammars: tiny blue pill CTAs (`{rounded.pill}`) and compact utility rects (`{rounded.sm}`).
- SF Pro Display + SF Pro Text — negative letter-spacing at display sizes for the signature "Apple tight" feel.
- Whisper-soft elevation used only when a product image needs to breathe — exactly one drop-shadow in the entire system.
- Tight two-row nav: slim `{component.global-nav}` + product-specific `{component.sub-nav-frosted}` with persistent right-aligned primary CTA.
- Section rhythm across multiple pages: light hero → dark product tile → light utility tile → dark tile → parchment footer — a predictable pulse.

## Colors

> **Source pages analyzed:** homepage, environment, store, iPhone 17 Pro buy page, accessories index. The color system is identical across all five surfaces; only the surface-mode mix differs.

### Brand & Accent

- **Action Blue** (`{colors.primary}` — #0066cc): The single brand-level interactive color. All text links, all blue pill CTAs ("Learn more", "Buy"), and the focus ring root. This is Apple's quiet but universal "click me" signal. Press state shifts to a slightly darker variant via the active scale transform rather than a hex change.
- **Focus Blue** (`{colors.primary-focus}` — #0071e3): A marginally brighter sibling of Action Blue, reserved for the keyboard focus ring on buttons (`outline: 2px solid`).
- **Sky Link Blue** (`{colors.primary-on-dark}` — #2997ff): A brighter blue used on dark surfaces for in-copy links and inline callouts, where Action Blue would disappear against the tile background.
- **On Primary** (`{colors.on-primary}` — #ffffff): Text/icon color on top of `{colors.primary}`. _(하네스 추가 — 원문에서 참조만 되고 정의 없음)_

### Surface

- **Pure White** (`{colors.canvas}` — #ffffff): The dominant canvas. Content, utility cards, store tiles, configurator grids.
- **Parchment** (`{colors.canvas-parchment}` — #f5f5f7): The signature Apple off-white. Used for alternating light tiles, footer region, and the default page canvas in store utility sections. Just different enough from white to create rhythm.
- **Pearl Button** (`{colors.surface-pearl}` — #fafafc): A near-white used as the fill for secondary "ghost" buttons — lighter than the parchment canvas so the button still reads as a button against `{colors.canvas-parchment}`.
- **Near-Black Tile 1** (`{colors.surface-tile-1}` — #272729): The prime surface on the homepage product grid.
- **Near-Black Tile 2** (`{colors.surface-tile-2}` — #2a2a2c): A micro-step lighter — used where a dark tile sits directly above or below Tile 1 to create the faintest separation.
- **Near-Black Tile 3** (`{colors.surface-tile-3}` — #252527): A micro-step darker — used at the bottom of the stack and in embedded video/player frames.
- **Pure Black** (`{colors.surface-black}` — #000000): Reserved for true void — video player backgrounds, edge-to-edge photographic overlays, the global nav bar background.
- **Translucent Chip Gray** (`{colors.surface-chip-translucent}` — #d2d2d7): The base hex of the translucent gray chip used over photography for circular control buttons. In production, applied at ~64% alpha as `rgba(210, 210, 215, 0.64)`.

### Text

- **Near-Black Ink** (`{colors.ink}` — #1d1d1f): The voice of every headline, every body paragraph, and the dark utility button's fill. Chosen instead of pure black to keep the page feeling photographic rather than printed.
- **Body** (`{colors.body}` — #1d1d1f): Same hex as ink — Apple uses one near-black tone for all text on light surfaces.
- **Body On Dark** (`{colors.body-on-dark}` — #ffffff): All text on dark tiles and on the global nav bar.
- **On Dark** (`{colors.on-dark}` — #ffffff): Alias of body-on-dark, used by component specs. _(하네스 추가)_
- **Body Muted** (`{colors.body-muted}` — #cccccc): Secondary copy on dark tiles where pure white would be too loud.
- **Ink Muted 80** (`{colors.ink-muted-80}` — #333333): Body text on the white Pearl Button surface — slightly softer than pure black.
- **Ink Muted 48** (`{colors.ink-muted-48}` — #7a7a7a): Disabled button text and legal fine-print.

### Hairlines & Borders

- **Divider Soft** (`{colors.divider-soft}` — #f0f0f0): The "border" tone on secondary buttons — functions as a ring shadow rather than a hard line. In production, often applied as `rgba(0, 0, 0, 0.04)`.
- **Hairline** (`{colors.hairline}` — #e0e0e0): The 1px hairline border on store utility cards and configurator chips.

### Brand Gradient

**No decorative gradients.** Atmospheric depth on product renders (iPhone 17 Pro camera plate, the Apple Watch bands, AirPods reflections) is inherent to the imagery, not a CSS gradient overlay. The environment page's hero uses photographic atmosphere (mountain vista at dawn) but no gradient tokens are defined. Apple is the rare luxury-brand site with zero gradient-based design tokens.

## Typography

### Font Family

- **Display**: `SF Pro Display, system-ui, -apple-system, sans-serif` — Apple's proprietary display face, optimized for sizes ≥ 19px. Defines the voice of every headline.
- **Body / UI**: `SF Pro Text, system-ui, -apple-system, sans-serif` — the text-optimized variant used for body copy, captions, buttons, and links below 20px.
- **OpenType features**: `font-variant-numeric: numerator` is enabled on numeric links (pricing tables, spec sheets). Display sizes rely on tight tracking rather than contextual ligatures.

### Hierarchy

| Token                         | Size | Weight | Line Height | Letter Spacing | Use                                                    |
| ----------------------------- | ---- | ------ | ----------- | -------------- | ------------------------------------------------------ |
| `{typography.hero-display}`   | 56px | 600    | 1.07        | -0.28px        | Hero headline; the signature "Apple tight" tracking    |
| `{typography.display-lg}`     | 40px | 600    | 1.10        | 0              | Tile headlines atop every product tile                 |
| `{typography.display-md}`     | 34px | 600    | 1.47        | -0.374px       | Section heads (SF Pro Text at display proportions)     |
| `{typography.lead}`           | 28px | 400    | 1.14        | 0.196px        | Product tile subcopy                                   |
| `{typography.lead-airy}`      | 24px | 300    | 1.5         | 0              | Environment-page lead paragraphs (the rare weight 300) |
| `{typography.tagline}`        | 21px | 600    | 1.19        | 0.231px        | Sub-tile tagline; sub-nav category name                |
| `{typography.body-strong}`    | 17px | 600    | 1.24        | -0.374px       | Inline strong emphasis                                 |
| `{typography.body}`           | 17px | 400    | 1.47        | -0.374px       | Default paragraph                                      |
| `{typography.dense-link}`     | 17px | 400    | 2.41        | 0              | Footer / store utility link lists (relaxed leading)    |
| `{typography.caption}`        | 14px | 400    | 1.43        | -0.224px       | Secondary captions, button text                        |
| `{typography.caption-strong}` | 14px | 600    | 1.29        | -0.224px       | Emphasized captions                                    |
| `{typography.button-large}`   | 18px | 300    | 1.0         | 0              | Store hero CTAs (the rare weight 300)                  |
| `{typography.button-utility}` | 14px | 400    | 1.29        | -0.224px       | Utility/nav button labels                              |
| `{typography.fine-print}`     | 12px | 400    | 1.0         | -0.12px        | Fine-print, footer body                                |
| `{typography.micro-legal}`    | 10px | 400    | 1.3         | -0.08px        | Micro legal disclaimers                                |
| `{typography.nav-link}`       | 12px | 400    | 1.0         | -0.12px        | Global nav menu items                                  |

### Principles

- **Negative letter-spacing at display sizes.** Every headline at 17px and up carries a slight tracking tighten (`-0.12 → -0.374px`). This produces the iconic "Apple tight" headline cadence. Never used at 12px or below.
- **Body copy at 17px, not 16px.** Apple breaks the SaaS convention and runs paragraph text at 17px. The extra pixel gives the page an unmistakable "reading, not scanning" pace.
- **Weight 300 is real and rare.** Used deliberately on a handful of large-size reads (`{typography.button-large}` at 18px/300 and `{typography.lead-airy}` at 24px/300). It's not an accident — it's a light-atmosphere cue reserved for moments where the content should feel airy.
- **Weight 600, not 700, for headlines.** Apple's headlines sit at weight 600. Weight 700 is used sparingly for `{typography.tagline}` (21px) when a touch more assertion is needed.
- **Line-height is context-specific.** Display sizes use 1.07–1.19 (tight). Body uses 1.47. Utility link stacks in the footer/store use an unusually relaxed 2.41 (`{typography.dense-link}`). The 2.41 is not a bug — it's how the footer's dense link columns breathe.
- **Weight 500 is deliberately absent.** The ladder is 300 / 400 / 600 / 700. Mid-weight readings always use 600.

### Note on Font Substitutes

SF Pro is Apple's proprietary system font. When building off-system:

- Use `system-ui, -apple-system, BlinkMacSystemFont` as the first stack entry — on macOS/iOS/Safari this resolves to the real SF Pro.
- For non-Apple platforms, **Inter** (Google Fonts, variable) is the closest open-source equivalent. Inter at weight 600 with `font-feature-settings: "ss03"` approximates SF Pro's rounded "a" character.
- Nudge `letter-spacing` down by `-0.01em` on display sizes to re-create the Apple tight feel; Inter's default tracking runs slightly wider than SF Pro.
- For body text, tighten line-height by `0.03` (from 1.47 → 1.44) when substituting Inter — Inter's taller x-height needs less leading.

## Layout

### Spacing System

- **Base unit:** 8px. Sub-base values (2, 4, 5, 6, 7) are used for tight typographic adjustments; structural layout snaps to 8/12/16/20/24.
- **Tokens:** `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px · `{spacing.md}` 17px · `{spacing.lg}` 24px · `{spacing.xl}` 32px · `{spacing.xxl}` 48px · `{spacing.section}` 80px.
- **Section vertical padding:** `{spacing.section}` (80px) inside a product tile; tiles stack edge-to-edge with 0 gap (the color change provides the break).
- **Card padding:** `{spacing.lg}` (24px) inside utility grid cards.
- **Button padding:** 8–11px vertical, 15–22px horizontal.
- **Universal rhythm constants:** the 17px body line-height multiplier (~25px line) and 21px tagline size show up on every analyzed page.

### Grid & Container

- **Max content width:** ~980px on text-heavy sections (environment), ~1440px on product grids (store, accessories), full-bleed for product tiles (homepage).
- **Column patterns:** 3 to 5 column utility card grid on store/accessories; 2-column side-by-side tiles on homepage occasional sections; single-column centered stack on product tile heroes.
- **Gutters:** 20–24px between cards in a utility grid.

### Whitespace Philosophy

Apple's whitespace is the product's pedestal. Every tile begins with at least 64px of air above its headline and 48–64px below. Product renders are never crowded; the nearest content to a product image is at least 40px away. The footer is the only area that breaks this — there, Apple goes deliberately dense to make the full information architecture visible at a glance.

## Elevation & Depth

| Level          | Treatment                                   | Use                                                                         |
| -------------- | ------------------------------------------- | --------------------------------------------------------------------------- |
| Flat           | No shadow, no border                        | Full-bleed tiles, global nav, footer, body sections                         |
| Soft hairline  | 1px `rgba(0, 0, 0, 0.08)` border            | Utility cards, sub-nav frosted-glass separator                              |
| Backdrop blur  | `backdrop-filter: blur(N)` on Parchment 80% | Sub-nav and the iPhone buy floating sticky bar                              |
| Product shadow | `rgba(0, 0, 0, 0.22) 3px 5px 30px 0`        | Product renders resting on a surface (the only true "shadow" in the system) |

**Shadow philosophy.** Apple uses **exactly one** drop-shadow, and it is applied to photographic product imagery — never to cards, never to buttons, never to text. Elevation in the UI comes from (a) surface-color change (light tile ↔ dark tile) and (b) backdrop-blur on sticky bars. The single shadow is about giving the product weight, not about UI hierarchy.

### Decorative Depth

- **Atmospheric imagery** on the environment page (photographic vista) supplies mood; no CSS gradient involved.
- **Edge-to-edge tile alternation** creates rhythm without borders or shadows — the color change itself is the divider.
- **Backdrop-filter blur** on `{component.sub-nav-frosted}` and `{component.floating-sticky-bar}` creates a "floating over content" effect that's functional, not decorative.

## Shapes

### Border Radius Scale

| Token            | Value        | Use                                                                                                            |
| ---------------- | ------------ | -------------------------------------------------------------------------------------------------------------- |
| `{rounded.none}` | 0px          | Full-bleed product tiles (no corner rounding)                                                                  |
| `{rounded.xs}`   | 5px          | Inline links when styled as subtle chips (rare)                                                                |
| `{rounded.sm}`   | 8px          | Dark utility buttons (Sign In, Bag), inline card imagery                                                       |
| `{rounded.md}`   | 11px         | White Pearl Button capsules                                                                                    |
| `{rounded.lg}`   | 18px         | Store utility cards, accessories grid cards                                                                    |
| `{rounded.pill}` | 9999px       | Primary blue pill CTAs, sub-nav buy button, configurator option chips, search input — the signature Apple pill |
| `{rounded.full}` | 9999px / 50% | Circular control chips floating over photography                                                               |

### Photography Geometry

- **Hero imagery**: full-bleed, 21:9 or taller on the homepage; 16:9 on environment and shop pages. Product renders are photographic-realistic, often shot on a tinted surface that becomes the tile background.
- **Product renders**: PNG/WebP with transparency; rest on a surface tile and pick up the system shadow.
- **Accessory grid**: square 1:1 crops at `{rounded.lg}` (18px) radius, light neutral backgrounds, product centered with 20–40px internal padding.
- **No rounded imagery in hero tiles** — images are full-bleed rectangular. Rounding (`{rounded.sm}`, `{rounded.lg}`) appears only on inline card imagery.
- Lazy-loading via responsive `srcset` and `sizes` across all breakpoints; CDN-optimized WebP.

## Components

### Top Navigation

**`global-nav`** — Persistent, ultra-thin black nav bar pinned to the top of every page. Background `{colors.surface-black}`, height 44px, text `{colors.on-dark}` in `{typography.nav-link}` (12px / 400 / -0.12px tracking). Links are quiet, spaced ~20px apart, running edge-to-edge across the top. Right-aligned cluster: Search, Bag icons — always visible. On mobile, collapses to hamburger and the Apple logo centers.

**`sub-nav-frosted`** — Surface-specific nav that sticks below the global nav. Background `{colors.canvas-parchment}` at 80% opacity with backdrop-filter blur, creating a frosted-glass effect. Height 52px. Content on left: product category name ("iPhone", "Store", "Accessories") in `{typography.tagline}` (21px / 600). Content right: inline nav links in `{typography.button-utility}` (14px), ending in a persistent `{component.button-primary}` ("Buy") or a utility link.

### Buttons

**`button-primary`** — The signature Apple action. Background `{colors.primary}` (Action Blue #0066cc), text `{colors.on-primary}` in `{typography.body}` (SF Pro Text 17px / 400), rounded `{rounded.pill}` (full pill — capsule-shaped), padding 11px × 22px. The full-pill radius IS the brand action signal.

- Active state: `{component.button-primary-active}` — `transform: scale(0.95)` (the system-wide micro-interaction).
- Focus state: `{component.button-primary-focus}` — 2px solid `{colors.primary-focus}` outline.

**`button-secondary-pill`** — Used as the second CTA when two blue pills appear together ("Learn more" / "Buy"). Background transparent, text `{colors.primary}`, 1px solid `{colors.primary}` border, rounded `{rounded.pill}`, padding 11px × 22px. Reads as a "ghost pill."

**`button-dark-utility`** — Global nav actions (Sign In, Bag, language selector). Background `{colors.ink}` (#1d1d1f), text `{colors.on-dark}` in `{typography.button-utility}` (14px / 400 / -0.224px tracking), rounded `{rounded.sm}` (8px), padding 8px × 15px. Active state shrinks via `transform: scale(0.95)`.

**`button-pearl-capsule`** — Product-card secondary button. Background `{colors.surface-pearl}` (#fafafc), text `{colors.ink-muted-80}` in `{typography.caption}` (14px), 3px solid `{colors.divider-soft}` border (functions as a soft ring rather than a visible line), rounded `{rounded.md}` (11px), padding 8px × 14px.

**`button-store-hero`** — A larger primary CTA used on store hero surfaces. Same Action Blue + Pill as `{component.button-primary}`, but with `{typography.button-large}` (18px / 300 — note the rare weight 300) and slightly more padding (14px × 28px). Used sparingly on the store landing.

**`button-icon-circular`** — Floats over photography. 44 × 44px, background `{colors.surface-chip-translucent}` at ~64% alpha, icon in `{colors.ink}`, rounded `{rounded.full}`. Used for carousel controls, close buttons, and in-image controls (product image thumbnails on the iPhone buy page).

**`text-link`** — Inline body links in `{colors.primary}` (Action Blue). Underlined or non-underlined per context.

**`text-link-on-dark`** — Inline body links on dark tiles in `{colors.primary-on-dark}` (Sky Link Blue #2997ff) — Action Blue would disappear against `{colors.surface-tile-1}`.

### Cards & Containers

**`product-tile-light`** — Full-bleed light tile. Background `{colors.canvas}` (white), text `{colors.ink}`, rounded `{rounded.none}` (0 — tiles touch edges), vertical padding `{spacing.section}` (80px). Content stack: product name in `{typography.display-lg}` (40px / 600) → one-line tagline in `{typography.lead}` (28px / 400) → two `{component.button-primary}` CTAs ("Learn more" / "Buy") → product render resting on the surface with the system shadow.

**`product-tile-parchment`** — Same as `{component.product-tile-light}` but on `{colors.canvas-parchment}` (#f5f5f7). Used to break two consecutive white tiles.

**`product-tile-dark`** — Full-bleed dark tile. Background `{colors.surface-tile-1}` (#272729), text `{colors.on-dark}`, rounded `{rounded.none}`, vertical padding `{spacing.section}` (80px). Same content stack as the light tile but with `{component.text-link-on-dark}` for inline copy and `{component.button-primary}` (Action Blue still works on the dark surface). Used on the homepage product grid as the alternating dark band.

**`product-tile-dark-2`** — Variant on `{colors.surface-tile-2}` (#2a2a2c). Used where a dark tile sits directly above or below `{component.product-tile-dark}` to create the faintest separation through micro-step lightness change.

**`product-tile-dark-3`** — Variant on `{colors.surface-tile-3}` (#252527). Used at the bottom of the stack and in embedded video/player frames.

**`store-utility-card`** — Used in store grid and accessories grid. Background `{colors.canvas}` (white), 1px solid `{colors.hairline}` border, rounded `{rounded.lg}` (18px), padding `{spacing.lg}` (24px). Top: product image (1:1 crop with `{rounded.sm}` (8px) inner image radius). Below: product name in `{typography.body-strong}` (17px / 600), price in `{typography.body}` (17px / 400), and a `{component.text-link}` ("Buy" or "Learn more"). No shadow by default; product render itself carries the system product-shadow.

**`configurator-option-chip`** — Pill-shaped tappable cell used in the iPhone 17 Pro buy page. Background `{colors.canvas}`, text `{colors.ink}` in `{typography.caption}`, rounded `{rounded.pill}`, padding 12px × 16px. Contains a small product thumbnail + label + price delta. Arranged in a grid of 4–5 per row.

**`configurator-option-chip-selected`** — Selected state. Border upgrades to 2px solid `{colors.primary-focus}`. Same shape, same content.

**`environment-quote-card`** — A photographic-canvas hero specific to the environment page. Dark photographic backdrop (mountain vista at dawn) with `{colors.surface-tile-1}` as the fallback color, centered white-text headline in `{typography.display-lg}` (40px), small green "Apple 2030" pictographic logo above the headline, single `{component.button-primary}` below. Padding `{spacing.section}` (80px).

**`floating-sticky-bar`** — Floats at the bottom of the viewport on the iPhone 17 Pro buy page during scroll. Background `{colors.canvas-parchment}` at 80% opacity with `backdrop-filter: blur(N)`, height 64px, padding 12px × 32px. Left: running price total in `{typography.body}`. Right: `{component.button-primary}` ("Add to Bag").

### Inputs & Forms

**`search-input`** — The accessories search input. Background `{colors.canvas}`, text `{colors.ink}` in `{typography.body}` (17px), 1px solid `rgba(0, 0, 0, 0.08)` border, rounded `{rounded.pill}` (full pill — search is also pill-shaped, matching the CTA grammar), padding 12px × 20px, height 44px. Leading icon: search glyph at 14px, muted tint.

Error and validation states were not surfaced in the analyzed pages.

### Footer

**`footer`** — Background `{colors.canvas-parchment}` (#f5f5f7), text `{colors.ink-muted-80}`. Link columns in `{typography.dense-link}` (17px / 400 / 2.41 line-height — the relaxed leading is what makes the dense columns scannable). Column headings in `{typography.caption-strong}` (14px / 600). Legal row at the very bottom in `{typography.fine-print}` (12px / 400) with `{colors.ink-muted-48}` text. Vertical padding 64px.

## Do's and Don'ts

### Do

- Use `{colors.primary}` (Action Blue #0066cc) for every interactive element — links, pill CTAs, focus signals — and nothing else. The single accent is non-negotiable.
- Set headlines in `{typography.hero-display}` or `{typography.display-lg}` with negative letter-spacing (`-0.28 → -0.374px`) to get the signature "Apple tight" cadence.
- Run body copy at `{typography.body}` (17px / 400 / 1.47 / -0.374px) — not 16px. The extra pixel defines the brand's reading pace.
- Alternate `{component.product-tile-light}` (or parchment) and `{component.product-tile-dark}` for full-bleed section rhythm. The color change IS the divider.
- Reserve `{rounded.pill}` for the primary blue CTA and any other element that should read as an "action" (configurator chips, search input, sticky bar CTA).
- Apply the single product-shadow (`rgba(0, 0, 0, 0.22) 3px 5px 30px`) only to product renders resting on a surface — never on cards, buttons, or text.
- Use `transform: scale(0.95)` as the active/press state on every button — it's the system-wide micro-interaction.
- Keep the global nav `{colors.surface-black}` (true black) — it's the only place pure black appears on most pages.

### Don't

- Don't introduce a second accent color; every "click me" signal is `{colors.primary}` (Action Blue).
- Don't add shadows to cards, buttons, or text — shadow is reserved for product imagery.
- Don't use gradients as decorative backgrounds; atmosphere comes from photography.
- Don't set body copy at weight 500 — Apple's ladder is 300 / 400 / 600 / 700, with 500 deliberately absent. Body is always 400; strong inline is 600; display is 600.
- Don't round full-bleed tiles — tiles are rectangular and edge-to-edge; the color change is the divider.
- Don't tighten line-height below 1.47 for body copy — the editorial leading is part of the brand.
- Don't mix radii grammars — use `{rounded.sm}` for compact utility, `{rounded.lg}` for utility cards, `{rounded.pill}` for pills, and nothing in between (except the rare `{rounded.md}` Pearl Button).
- Don't use `{colors.primary-on-dark}` (Sky Link Blue) on light surfaces — it's the dark-tile-only variant. Action Blue is for light surfaces.

## Responsive Behavior

### Breakpoints

| Name             | Width       | Key Changes                                                                                               |
| ---------------- | ----------- | --------------------------------------------------------------------------------------------------------- |
| Small phone      | ≤ 419px     | Single-column tiles; sub-nav collapses to category name + primary CTA only; hero typography drops to 28px |
| Phone            | 420–640px   | Single-column stack; product renders scale to 80% of tile width; hero h1 drops to 34px                    |
| Large phone      | 641–735px   | Tiles transition to tighter padding (48px vertical vs 80px); fine-print wraps                             |
| Tablet portrait  | 736–833px   | Global nav collapses to hamburger; sub-nav hides category chips, keeps primary CTA                        |
| Tablet landscape | 834–1023px  | Global nav returns fully expanded; 3-column utility grids become 2-column                                 |
| Small desktop    | 1024–1068px | Product tiles use 2/3 width with margin gutters; hero h1 stays at 40px                                    |
| Desktop          | 1069–1440px | Full layout; 4–5 column store grids; 1440px content max                                                   |
| Wide desktop     | ≥ 1441px    | Content locks at 1440px, margins absorb extra width                                                       |

The structural breakpoints that matter for agents: 1440px (content lock), 1068px (small-desktop), 833px (tablet landscape switch), 734px (tablet portrait), 640px (phone), 480px (small phone).

### Touch Targets

- Minimum 44 × 44px. `{component.button-primary}` lands at ~44 × 100px (with the full-pill radius making the visible hit area more generous than the label suggests).
- `{component.button-icon-circular}` is exactly 44 × 44px.
- Global nav utility links are smaller (~32 × 80px) — they deliberately sit at a tighter target because they're precision desktop actions, and the mobile hamburger replaces them at ≤ 833px.

### Collapsing Strategy

- **Global nav**: full horizontal link row on desktop → collapses to Apple logo + hamburger + bag icon at 834px and below.
- **Sub-nav**: category name + inline links + primary CTA → category name + primary CTA only at mobile; inline links move into a hamburger tray.
- **Product tiles**: stack from 2-column to 1-column at 834px; vertical padding tightens from 80px → 48px at small-phone.
- **Utility grids** (store, accessories): 5-col → 4-col (1440px) → 3-col (1068px) → 2-col (834px) → 1-col (640px).
- **Hero typography**: `{typography.hero-display}` (56px) → `{typography.display-lg}` (40px) at 1068px → 34px at 640px → 28px at 419px.

### Image Behavior

- All product imagery uses responsive `srcset` with breakpoint-matched crops.
- Hero photography may switch art direction at mobile (e.g., the environment page's vista crops to a taller aspect ratio on mobile, framing the subject differently).
- Product renders maintain their 1:1 or 4:3 aspect ratios across breakpoints; only scale changes.
- Lazy-loading is default; the above-fold hero loads eagerly.

## Iteration Guide

1. Focus on ONE component at a time. Reference its YAML key directly (`{component.product-tile-dark}`, `{component.search-input}`).
2. Variants of an existing component (`-active`, `-focus`, `-2`, `-3`) live as separate entries in `components:`.
3. Use `{token.refs}` everywhere — never inline hex.
4. Never document hover. Default and Active/Pressed states only.
5. Display headlines stay SF Pro Display 600 with negative letter-spacing. Body stays SF Pro Text 400 at 17px. The boundary is unbreakable.
6. The single drop-shadow (`rgba(0, 0, 0, 0.22) 3px 5px 30px`) is reserved for product photography only.
7. When in doubt about emphasis: alternate surface (light → dark tile) before adding chrome.

## Known Gaps

- Form validation and error states were not surfaced on the analyzed pages; only the neutral search input is documented.
- The homepage's embedded video/player frame uses `{colors.surface-black}`; interior player controls are not documented (they're a platform widget, not a web-design token).
- Some component imagery is dynamic (rotating product hero) and its specific copy varies per surface — component specs name the structure, not the rotating content.
- Dark-mode counterparts for store and accessories utility cards were not surfaced on the analyzed pages; the system documented is the daytime/light-dominant variant Apple ships by default.
- Atmospheric photography (environment page mountain vista) is a content asset, not a design token; the documented `{component.environment-quote-card}` describes structural surface only.
- The exact backdrop-filter blur radius on `{component.sub-nav-frosted}` and `{component.floating-sticky-bar}` is platform-dependent; production CSS uses `saturate(180%) blur(20px)` as a typical baseline but the value isn't formalized as a token.

---

---

# 부록 (하네스 추가 — 본문에서 유도한 규칙. 본문과 충돌 시 본문이 우선)

## 부록 A. 모바일 앱 적용 규칙

본문은 데스크탑 웹 기준이다. 이 프로젝트는 **모바일 앱 고정**이므로 §Responsive Behavior의 ≤640px 규칙에서 아래 값을 유도한다. 에이전트는 이 표의 값만 쓴다.

### A-1. 프레임

| 항목                  | 값                  | 근거                                                                   |
| --------------------- | ------------------- | ---------------------------------------------------------------------- |
| `{frame.width}`       | 390px               | Phone(420–640) 하한 근처 대표 기기                                     |
| `{frame.height}`      | 844px               | 위와 동일 기기 세로. 콘텐츠가 길면 프레임을 세로로 늘린다(스크롤 화면) |
| `{frame.safe-top}`    | 47px                | 상태바 영역. 헤더 배경색으로 채움                                      |
| `{frame.safe-bottom}` | 34px                | 홈 인디케이터. 탭바/스티키바 배경색으로 채움                           |
| `{frame.side-margin}` | `{spacing.lg}` 24px | Whitespace Philosophy — "product pedestal"                             |

### A-2. 타이포 다운스케일 (Collapsing Strategy §Hero typography 준용)

| 역할                  | 토큰                       | 모바일 값             |
| --------------------- | -------------------------- | --------------------- |
| 화면 대제목(1개/화면) | `{typography.display-md}`  | 34px / 600 / -0.374px |
| 섹션 헤드             | `{typography.tagline}`     | 21px / 600            |
| 카드·리스트 제목      | `{typography.body-strong}` | 17px / 600            |
| 본문                  | `{typography.body}`        | 17px / 400 / 1.47     |
| 보조·메타             | `{typography.caption}`     | 14px / 400            |
| 라벨·탭바             | `{typography.nav-link}`    | 12px / 400            |
| 법적 고지             | `{typography.fine-print}`  | 12px / 400            |

`{typography.hero-display}`, `{typography.display-lg}`, `{typography.lead}`는 모바일에서 **사용하지 않는다** (온보딩/빈 상태 1회성 히어로 제외 — 그때도 display-md 이하).

### A-3. 간격

| 항목                                        | 값                                                              |
| ------------------------------------------- | --------------------------------------------------------------- |
| `{spacing.section-mobile}` (섹션 세로 패딩) | `{spacing.xxl}` 48px — Large phone 규칙 "80→48"                 |
| 섹션 간 간격                                | 0 (색 전환이 구분자) 또는 `{spacing.xl}` 32px (같은 색 연속 시) |
| 리스트 행 세로 패딩                         | `{spacing.sm}` 12px ~ `{spacing.md}` 17px                       |
| 카드 내부 패딩                              | `{spacing.md}` 17px (본문 24px의 모바일 축소)                   |
| 카드 간 간격                                | `{spacing.sm}` 12px                                             |
| 버튼 그룹 간격                              | `{spacing.xs}` 8px                                              |

### A-4. 모바일 전용 컴포넌트 (본문 컴포넌트에서 유도)

| 키                              | 유도 원본                   | 스펙                                                                                                                                                                                                                                          |
| ------------------------------- | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `{component.mobile-header}`     | `sub-nav-frosted`           | 높이 52px + safe-top. 배경 `{colors.canvas-parchment}` 80% + blur. 좌: 화면 제목 `{typography.tagline}` 또는 뒤로가기 `{component.button-icon-circular}`(32px 축소 허용). 우: `{component.button-primary}`(compact: 8px×15px) 또는 아이콘 1개 |
| `{component.mobile-tab-bar}`    | `global-nav` 모바일 축약    | 높이 49px + safe-bottom. 배경 `{colors.surface-black}`. 탭 3~5개, 아이콘 24px + `{typography.nav-link}`. 활성 탭 `{colors.on-dark}`, 비활성 `{colors.ink-muted-48}`                                                                           |
| `{component.mobile-sticky-cta}` | `floating-sticky-bar`       | 높이 64px + safe-bottom. 배경 parchment 80% blur. 좌: 요약 텍스트 `{typography.body}`, 우: `{component.button-primary}`                                                                                                                       |
| `{component.list-row}`          | `store-utility-card` 평면화 | 배경 `{colors.canvas}`, 하단 1px `{colors.hairline}`, 세로 패딩 12px, 좌: 제목 body-strong + 메타 caption, 우: 상태 텍스트 caption 또는 chevron. 그림자 없음                                                                                  |
| `{component.status-chip}`       | `configurator-option-chip`  | `{rounded.pill}`, 1px `{colors.hairline}`, 패딩 4px×12px, `{typography.caption}`. **색으로 상태 구분 금지**(단일 액센트 원칙) — 텍스트 라벨과 선택 시 2px `{colors.primary-focus}` 테두리로만 구분                                            |
| `{component.card}`              | `store-utility-card`        | 그대로. 패딩만 17px                                                                                                                                                                                                                           |
| `{component.input}`             | `search-input`              | 그대로. 높이 44px                                                                                                                                                                                                                             |
| `{component.section-dark}`      | `product-tile-dark`         | 세로 패딩 48px, 좌우 24px. 강조 섹션(요약/히어로)에만 1화면 1개 이하                                                                                                                                                                          |
| `{component.empty-state}`       | `product-tile-parchment`    | parchment 배경, 중앙 정렬. 제목 `{typography.tagline}` + 본문 `{typography.body}` + `{component.button-primary}` 1개                                                                                                                          |

### A-5. 터치 타깃

- 모든 탭 가능 요소 최소 44×44px (§Touch Targets). 리스트 행은 높이 ≥ 44px.

## 부록 B. 목데이터 규칙

에이전트가 유일하게 자유 생성하는 것이 목데이터다. 아래를 만족해야 한다.

1. **도메인 사실감**: 한국어 실명풍 이름(예: 김서연, 박준호), 관계 그룹은 PRD §3에서 온 것(대학 동기·직장 동료·동네 친구·가족·양가). "홍길동", "Lorem ipsum", "테스트1" 금지.
2. **규모 사실감**: 지인 40~~60명, 모임 12~~20개, 주말당 2~~3건, 모임당 3~~6명 + 1:1 모임 존재.
3. **PRD §3 엣지케이스 필수 포함** (각 최소 1건, `mock-data.json`의 `edgeCases` 필드에 어느 레코드가 어느 케이스인지 명시):
   - 한 사람이 2개 이상 그룹에 소속
   - 회신 마감이 지났는데 미회신인 사람
   - 같은 날짜에 겹치는 모임 2건
   - 1:1로 따로 만나야 하는 관계(직장 상사)
   - 양가가 같이 나가는 모임(상견례)
   - 결혼식 2주 전 급하게 잡힌 모임
4. **상태 4종 모두 존재**: 회신 대기 / 확정 대기 / 확정 / 완료.
5. **빈 상태 1개 이상**: 예) 아직 모임이 없는 그룹.
6. **긴 텍스트 1개 이상**: 예) 15자 이상 이름 또는 30자 이상 메모 — 잘림/줄바꿈 검증용.
7. **날짜 일관성**: 결혼식 날짜 1개를 정하고(예: 2026-12-12), 모든 모임은 그 3개월 전~2주 전 사이 주말 위주.
8. **두 사람 관점**: 지인마다 `side: "bride" | "groom" | "both"` 필드.

## 부록 C. 에이전트 결정 권한 경계

| 에이전트가 **결정해도 되는 것**                                                                   | 에이전트가 **결정하면 안 되는 것** (사람 게이트 필요)     |
| ------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| 목데이터 내용 (부록 B 범위 내)                                                                    | design.md 본문의 어떤 값이든 변경                         |
| 화면 내 섹션 순서, 리스트 정렬 기준                                                               | 새 색상·새 폰트·새 radius 도입                            |
| 부록 A 컴포넌트를 조합해 새 복합 컴포넌트 만들기 (단, 토큰만 사용하고 `work/figma-log.md`에 기록) | 두 번째 액센트 색, 그림자(제품 이미지 외), 그라디언트     |
| 아이콘 선택 (SF Symbols 스타일 단색 라인 아이콘, `{colors.ink}` 또는 `{colors.on-dark}`)          | IA 구조(탭 개수·이름) — 01-planner 게이트에서 사람이 선택 |
| 마이크로카피 문구 (한국어, 존댓말, 짧게)                                                          | 화면 추가/삭제 — 02-wireframer 게이트에서 사람이 선택     |
| 빈 상태·에러 상태의 문구                                                                          | 플랫폼 변경 (모바일 고정)                                 |
