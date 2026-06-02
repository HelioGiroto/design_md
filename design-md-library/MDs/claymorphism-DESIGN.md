# Design System: Claymorphism

## 1. Definição do Estilo

- **Nome:** Claymorphism
- **Tipo:** Soft, Playful, Rounded, Colorful
- **Keywords:** Soft 3D, chunky, playful, toy-like, bubbly, thick borders (3-4px), double shadows, rounded (16-24px)
- **Era:** 2020s Modern
- **Light/Dark:** ✓ Full / ◐ Partial

## 2. Paleta de Cores

- **Primárias:** Pastel: Soft Peach #FDBCB4, Baby Blue #ADD8E6, Mint #98FF98, Lilac #E6E6FA, light BG
- **Secundárias:** Soft gradients (pastel-to-pastel), light/dark variations (20-30%), gradient subtle

## 3. Efeitos Visuais

Inner+outer shadows (subtle, no hard lines), soft press (200ms ease-out), fluffy elements, smooth transitions

## 4. AI Prompt Keywords

Design a playful, toy-like interface with soft 3D, chunky elements, bubbly aesthetic, rounded edges (16-24px), thick borders (3-4px), double shadows (inner + outer), pastel colors, smooth animations. Perfect for children's apps and creative tools.

## 5. CSS Technical

```css
border-radius: 16-24px, border: 3-4px solid, box-shadow: inset -2px -2px 8px, 4px 4px 8px, background: pastel-gradient, animation: soft bounce (cubic-bezier 0.34, 1.56)
```

## 6. Design System Variables

```css
--border-radius: 20px, --border-width: 3-4px, --shadow-inner: inset -2px -2px 8px, --shadow-outer: 4px 4px 8px, --color-palette: pastels, --animation: bounce
```

## 7. Checklist de Implementação

- ☐ Border-radius 16-24px
- ☐ Thick borders 3-4px
- ☐ Double shadows (inner+outer)
- ☐ Pastel colors used
- ☐ Soft bounce animations
- ☐ Playful interactions

## 8. Visual Theme & Atmosphere

Design brinquedo, bubbly, pastéis suaves e bordas chunky. Ideal para apps infantis e creative tools. Prompt playful. 2021+ movimento ludic design, inspirado em Clay.io e Adobe XD. Rejeita corporate severity — celebra diversão, bubbly, toy-like.

- Density: 5/10 — Balanced
- Variance: 4/10 — Moderate
- Motion: 8/10 — Cinematic

## 9. Color Palette & Roles

- **Soft Peach** (#FDBCB4) — Primary surface or dominant color
- **Baby Blue** (#ADD8E6) — Accent highlight, links and focus states
- **Mint** (#98FF98) — Supporting palette color
- **Lilac** (#E6E6FA) — Supporting palette color

## 10. Typography Rules

- **Display / Hero:** System UI stack (-apple-system, sans-serif) — Weight 700, tight tracking, used for headline impact
- **Body:** System UI stack (-apple-system, sans-serif) — Weight 400, 16px/1.6 line-height, max 72ch per line
- **UI Labels / Captions:** System UI stack (-apple-system, sans-serif) — 0.875rem, weight 500, slight letter-spacing
- **Monospace:** JetBrains Mono — Used for code, metadata, and technical values

Scale:
- Hero: clamp(2.5rem, 5vw, 4rem)
- H1: 2.25rem
- H2: 1.5rem
- Body: 1rem / 1.6
- Small: 0.875rem

## 11. Component Stylings

- **Primary Button:** Generously rounded (1.5rem) shape. Accent color fill. Hover: 8% darken + subtle lift shadow. Active: -1px translate tactile press. Font weight 600. No outer glows.
- **Secondary / Ghost Button:** Outline variant. 1.5px border in muted color. Text in primary color. Hover: subtle background fill.
- **Cards:** Generously rounded (1.5rem) corners. Surface background. Subtle shadow (0 2px 12px rgba(0,0,0,0.06)). 1px border stroke.
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
- **Entry animations:** Fade + translate-Y (16px → 0) over 540ms ease-out. Staggered cascades for lists: 120ms between items.
- **Hover states:** Scale(1.03) + shadow lift over 200ms.
- **Page transitions:** Fade + slide (300ms).
- **Performance:** Only transform and opacity animated. No layout-triggering properties.

## 14. Anti-Patterns (Banned)

- No emojis in UI — use icon system only (Lucide, Heroicons)
- No pure black (#000000) — use off-black or charcoal variants
- No oversaturated accent colors (saturation cap: 80%)
- No 3-column equal-width feature layouts — use zig-zag or asymmetric grid
- No `h-screen` — use `min-h-[100dvh]`
- No AI copywriting clichés: "Elevate", "Seamless", "Unleash", "Next-Gen"
- No broken external image links — use picsum.photos or inline SVG
- No generic lorem ipsum in demos

## Contexto Histórico

2021+ movimento ludic design, inspirado em Clay.io e Adobe XD. Rejeita corporate severity — celebra diversão, bubbly, toy-like.

## Caso de Uso

Apps infantis, Creative tools, Educação, Jogos interativos
