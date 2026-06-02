# Design System: HUD / Sci-Fi FUI

## 1. Definição do Estilo

- **Nome:** HUD / Sci-Fi FUI
- **Tipo:** Sci-Fi, Technical, Dark, Interface-Driven
- **Keywords:** Futuristic, technical, wireframe, neon, data, transparency, iron man, sci-fi, interface
- **Era:** 2010s Sci-Fi
- **Light/Dark:** ✓ Low / ✓ Full

## 2. Paleta de Cores

- **Primárias:** Neon Cyan #00FFFF, Holographic Blue #0080FF, Alert Red #FF0000
- **Secundárias:** Transparent Black, Grid Lines #333333

## 3. Efeitos Visuais

Glow effects, scanning animations, ticker text, blinking markers, fine line drawing

## 4. AI Prompt Keywords

Design a futuristic HUD (Heads Up Display) or FUI. Use: thin lines (1px), neon cyan/blue on black, technical markers, decorative brackets, data visualization, monospaced tech fonts, glowing elements, transparency.

## 5. CSS Technical

```css
border: 1px solid rgba(0,255,255,0.5), color: #00FFFF, background: transparent or rgba(0,0,0,0.8), font-family: monospace, text-shadow: 0 0 5px cyan
```

## 6. Design System Variables

```css
--hud-color: #00FFFF, --bg-color: rgba(0,10,20,0.9), --line-width: 1px, --glow: 0 0 5px, --font: monospace
```

## 7. Checklist de Implementação

- ☐ Fine lines 1px
- ☐ Neon glow text/borders
- ☐ Monospaced font
- ☐ Dark/Transparent BG
- ☐ Decorative tech markers
- ☐ Holographic feel

## 8. Visual Theme & Atmosphere

HUD / Sci-Fi FUI — Design general com futuristic, technical, wireframe. Template e prompt pronto para IA. Estilo HUD / Sci-Fi FUI representa uma tendência moderna em design UI/UX web com foco em general.

- Density: 7/10 — Compact
- Variance: 4/10 — Moderate
- Motion: 6/10 — Expressive

## 9. Color Palette & Roles

- **Neon Cyan** (#00FFFF) — Accent highlight, links and focus states
- **Holographic Blue** (#0080FF) — Accent highlight, links and focus states
- **Alert Red** (#FF0000) — Error states, destructive actions
- **Grid Lines** (#333333) — Extended palette, decorative use

## 10. Typography Rules

- **Display / Hero:** monospace — Weight 700, tight tracking, used for headline impact
- **Body:** monospace — Weight 400, 16px/1.6 line-height, max 72ch per line
- **UI Labels / Captions:** monospace — 0.875rem, weight 500, slight letter-spacing
- **Monospace:** monospace — Used for code, metadata, and technical values

Scale:
- Hero: clamp(2.5rem, 5vw, 4rem)
- H1: 2.25rem
- H2: 1.5rem
- Body: 1rem / 1.6
- Small: 0.875rem

## 11. Component Stylings

- **Primary Button:** Subtly rounded (0.5rem) shape. Accent color fill. Hover: 8% darken + subtle lift shadow. Active: -1px translate tactile press. Font weight 600. No outer glows.
- **Secondary / Ghost Button:** Outline variant. 1.5px border in muted color. Text in primary color. Hover: subtle background fill.
- **Cards:** Subtly rounded (0.5rem) corners. Surface background. Subtle shadow (0 2px 12px rgba(0,0,0,0.06)). 1px border stroke.
- **Inputs:** Label above input. 1px border stroke. Focus ring: 2px accent color offset 2px. Error text below in semantic red. No floating labels.
- **Navigation:** Primary surface background. Active item: accent color indicator. Font weight 500 when active.
- **Skeletons:** Shimmer animation matching component dimensions. No circular spinners.
- **Empty States:** Icon-based composition with descriptive text and action button.

## 12. Layout Principles

- **Grid:** CSS Grid primary. Max-width containment: 1280px centered with 1.5rem side padding.
- **Spacing rhythm:** Balanced. Base unit: 0.5rem (8px).
- **Section vertical gaps:** clamp(4rem, 8vw, 8rem).
- **Hero layout:** Split-screen (text left, visual right).
- **Feature sections:** Zig-zag alternating text+image rows. No 3-equal-columns.
- **Mobile collapse:** All multi-column layouts collapse below 768px. No horizontal overflow.
- **z-index contract:** base (0) / sticky-nav (100) / overlay (200) / modal (300) / toast (500).

## 13. Motion & Interaction

- **Physics:** Spring — stiffness 120, damping 20. Confident, weighted transitions.
- **Entry animations:** Fade + translate-Y (16px → 0) over 480ms ease-out. Staggered cascades for lists: 100ms between items.
- **Hover states:** Scale(1.03) + shadow lift over 200ms.
- **Page transitions:** Fade + slide (300ms).
- **Performance:** Only transform and opacity animated. No layout-triggering properties.

## 14. Anti-Patterns (Banned)

- No emojis in UI — use icon system only (Lucide, Heroicons)
- No pure white (#FFFFFF) backgrounds — use off-white or dark surfaces
- No oversaturated accent colors (saturation cap: 80%)
- No 3-column equal-width feature layouts — use zig-zag or asymmetric grid
- No `h-screen` — use `min-h-[100dvh]`
- No AI copywriting clichés: "Elevate", "Seamless", "Unleash", "Next-Gen"
- No broken external image links — use picsum.photos or inline SVG
- No generic lorem ipsum in demos

## Contexto Histórico

Estilo HUD / Sci-Fi FUI representa uma tendência moderna em design UI/UX web com foco em general.

## Caso de Uso

Landing pages, SaaS
