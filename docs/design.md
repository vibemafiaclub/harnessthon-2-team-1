# Design System Guide

Primitive → Semantic Variable Structure | Self-contained Design Token System

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. COLOR FOUNDATION

1.1 Primitive Colors
Raw color values — the single source of truth for all design tokens.

[Primary]
active-red #EA1917
light-gray-2 #F0ECE4 (WSG: Warm Gray)
black #000000
white #FFFFFF
logo-gray #6B6B6B
white-60 #FFFFFF 60%

[Gray Scale]
light-gray-0 #F6F6F6
light-gray-1 #F6F3EB
light-gray-2 #F0ECE4
light-gray-3 #E6E1D6
mid-gray-1 #CBC8C2
mid-gray-2 #646464
mid-gray-3 #4A4946
dark-gray-1 #333333
dark-gray-2 #262626
dark-gray-3 #1A1A1A

[Functional / State]
heritage-red #A50034
green-1 #287D00
green-2 #316D15
yellow-1 #F7B500
yellow-2 #EEB404
teal-1 #006A63
toast-gray #303030
bright-red #FF3224
ad-red #FD312E
near-black #141414

[Badge Gradient]
#FF3224 → #EA1917 → #A50034
Color Style: gradient/badge (gradient stop variable binding not supported — raw hex)
⚠ Primitive value changes are NOT auto-reflected in gradients; manual sync required.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1.2 Semantic Tokens
Context-based aliases referencing Primitive values — enables theming & consistent usage.

[Background]
bg/default ← white #FFFFFF
bg/warm ← light-gray-2 #F0ECE4
bg/subtle ← light-gray-1 #F6F3EB
bg/elevated ← white #FFFFFF
bg/light ← light-gray-0 #F6F6F6

[Surface]
surface/card ← white #FFFFFF
surface/toast-error ← toast-gray #303030
surface/toast-warning ← yellow-2 #EEB404
surface/toast-info ← teal-1 #006A63
surface/inverse ← dark-gray-1 #333333 — GNB promo bar etc.
surface/blur-blind ← white-60 #FFFFFF 60%

[Text]
text/primary ← black #000000
text/secondary ← dark-gray-1 #333333
text/tertiary ← mid-gray-2 #646464
text/disabled ← mid-gray-1 #CBC8C2
text/inverse ← white #FFFFFF — On dark images/backgrounds
text/brand ← active-red #EA1917
text/disclaimer ← black #000000 — Disclaimer on light bg
text/disclaimer-inverse ← white #FFFFFF — Disclaimer on dark bg
text/on-toast-error ← white #FFFFFF
text/on-toast-warning ← black #000000
text/on-toast-info ← white #FFFFFF

[Border]
border/default ← light-gray-3 #E6E1D6
border/strong ← mid-gray-1 #CBC8C2
border/focus ← black #000000 — WCAG accessibility
border/inverse ← white #FFFFFF — On dark backgrounds

[Brand]
brand/primary ← active-red #EA1917
brand/logo ← heritage-red #A50034 — LG logo on light bg
brand/logo-inverse ← white #FFFFFF — LG logo on dark bg
brand/secondary ← logo-gray #6B6B6B

[State]
state/success ← green-1 #287D00
state/success-on-warm ← green-2 #316D15 — Valid input on bg/warm
state/warning ← yellow-2 #EEB404
state/error ← active-red #EA1917
state/error-on-warm ← heritage-red #A50034 — Error on bg/warm
state/info ← teal-1 #006A63

[Review]
review/star ← active-red #EA1917

[Icon]
icon/default ← black #000000
icon/active ← active-red #EA1917
icon/muted ← mid-gray-2 #646464
icon/white ← white #FFFFFF — On dark backgrounds

[Flag]
flag/general ← black #000000
flag/promotion ← active-red #EA1917

[Action]
action/primary ← active-red #EA1917 — Web CTA (Buy Now, etc.)
action/promo ← ad-red #FD312E — Ad/promo CTA
action/primary-label ← white #FFFFFF — Primary button text
action/secondary ← white #FFFFFF — Secondary button bg
action/secondary-label ← black #000000 — Secondary button text
action/secondary-border ← mid-gray-2 #646464 — Secondary button border
action/disabled ← mid-gray-1 #CBC8C2 — Disabled button

[Shadow]
shadow/disclaimer ← white #FFFFFF — Halo for black text on light bg
shadow/disclaimer-inverse ← black #000000 — Halo for white text on dark bg

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

2. TYPOGRAPHY FOUNDATION

Font Family: LGEIHeadline + LGEIText Dual System

2.1 Typography Primitives
font-family, font-size, font-weight variable definitions — Typography collection

[Font Family]
font-family/headline STRING "LGEIHeadline"
font-family/text STRING "LGEIText"

[Font Size]
font-size/12 12
font-size/14 14
font-size/16 16
font-size/20 20
font-size/24 24
font-size/32 32
font-size/36 36
font-size/56 56
font-size/60 60
font-size/80 80

[Font Weight]
font-weight/regular 400
font-weight/semibold 600

2.2 Text Styles
13 local Text Styles — variable binding, weight correction, Vertical Trim (Cap Height) applied

Style Name Size/LH Weight Font Family Usage
title/xlarge 80/80 600 SemiBold LGEIHeadline Large headline
title/large 60/60 600 SemiBold LGEIHeadline Hero headline
title/medium 56/60 600 SemiBold LGEIHeadline Section title
title/small 32/36 600 SemiBold LGEIHeadline Card/block title
subtitle/large 36/42 400 Regular LGEIText Hero sub-copy
subtitle/medium 24/28 400 Regular LGEIText Section sub-copy
subtitle/medium-strong 24/28 600 SemiBold LGEIText Emphasized sub-copy
body/default 16/20 400 Regular LGEIText Body text
body/default-strong 16/20 600 SemiBold LGEIText Body emphasis
cta/medium 16/16 600 SemiBold LGEIText Button label
nav/menu 20/24 400 Regular LGEIText Navigation menu
badge/small 12/14 400 Regular LGEIText Badge / label
body/small 14/16 400 Regular LGEIText Secondary body

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

3. SPACING SCALE

Spacing, Layout, Radius — 4-based multiplier token system

3.1 Spacing
Multiples of 4, 10 steps. Bound to auto-layout gap & padding.

Variable px WSG Reference
spacing/4 4
spacing/8 8 WSG Title Guide — Headline ↔ SubTitle
spacing/12 12
spacing/16 16
spacing/20 20 WSG Layout Common Principle — Title ↔ Content (Desktop)
spacing/24 24 Grid gutter / Body → Button
spacing/32 32 WSG Card Common Principle — Card margin (Desktop)
spacing/40 40
spacing/48 48 WSG Layout — Section top margin
spacing/64 64 WSG Layout — Section bottom margin (with title)

3.2 Layout
Layout structure tokens. Viewport, banner, container, and layout area width definitions.

Variable px Usage
layout/viewport 1920 Full viewport width
layout/banner 1600 Banner area max width
layout/container 1440 Content container max width
layout/gutter 24 Grid column gap
layout/viewport-inset 240 Viewport L/R margin (=(1920-1440)/2)
layout/banner-inset 160 Banner L/R margin (=(1920-1600)/2)
layout/banner-padding 80 Banner internal padding
layout/filter-width 240 Filter panel width

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

4. RADIUS SCALE

Corner rounding tokens — default rounding values per component type.

Variable px Applied To
radius/4 4 Badge, Chip
radius/6 6 Button small (Contained), Text Field
radius/8 8 Button medium (Contained), Input
radius/12 12 Button large, frame element rounding
radius/28 28 Card (Desktop) — WSG Card Common
radius/full 9999 Pill — Box Button, Toast (fully rounded)
