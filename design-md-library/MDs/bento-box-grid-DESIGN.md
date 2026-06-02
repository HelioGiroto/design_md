# Design System: Bento Box Grid

## 1. Definição do Estilo

- **Nome:** Bento Box Grid
- **Tipo:** Modular, Grid, Organized, Apple-Inspired
- **Keywords:** Modular cards, asymmetric grid, varied sizes, Apple-style, dashboard tiles, negative space, clean hierarchy, cards
- **Era:** 2020s Apple
- **Light/Dark:** ✓ Full / ✓ Full

## 2. Paleta de Cores

- **Primárias:** Neutral base + brand accent, #FFFFFF, #F5F5F5, brand primary
- **Secundárias:** Subtle gradients, shadow variations, accent highlights for interactive cards

## 3. Efeitos Visuais

grid-template with varied spans, rounded-xl (16px), subtle shadows, hover scale (1.02), smooth transitions

## 4. AI Prompt Keywords

Design a Bento Box grid layout. Use: modular cards with varied sizes (1x1, 2x1, 2x2), Apple-style aesthetic, rounded corners (16-24px), soft shadows, clean hierarchy, asymmetric grid, neutral backgrounds (#F5F5F7), hover effects.

## 5. CSS Technical

```css
display: grid, grid-template-columns: repeat(4, 1fr), grid-auto-rows: 200px, gap: 16px, border-radius: 24px, background: #FFFFFF, box-shadow: 0 4px 6px rgba(0,0,0,0.05)
```

## 6. Design System Variables

```css
--grid-gap: 16px, --card-radius: 24px, --card-bg: #FFFFFF, --page-bg: #F5F5F7, --shadow: 0 4px 6px rgba(0,0,0,0.05), --hover-scale: 1.02
```

## 7. Checklist de Implementação

- ☐ Grid responsive (4→2→1 cols)
- ☐ Card spans varied
- ☐ Rounded corners consistent
- ☐ Shadows subtle
- ☐ Content fits cards
- ☐ Hover scale (1.02)

## 8. Visual Theme & Atmosphere

Bento Box Grid — Design general com modular cards, asymmetric grid, varied sizes. Template e prompt pronto para IA. Estilo Bento Box Grid representa uma tendência moderna em design UI/UX web com foco em general.

- Density: 8/10 — Dense
- Variance: 7/10 — Dynamic
- Motion: 4/10 — Subtle

## 9. Color Palette & Roles

- **#FFFFFF** (#FFFFFF) — Primary surface or dominant color
- **#F5F5F5** (#F5F5F5) — Secondary surface or text color

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
- **Hero layout:** Asymmetric composition.
- **Feature sections:** Asymmetric grid with varied card sizes. No 3-equal-columns.
- **Mobile collapse:** All multi-column layouts collapse below 768px. No horizontal overflow.
- **z-index contract:** base (0) / sticky-nav (100) / overlay (200) / modal (300) / toast (500).

## 13. Motion & Interaction

- **Physics:** Ease-out curves, 200-300ms duration. Smooth and predictable.
- **Entry animations:** Fade + translate-Y (16px → 0) over 420ms ease-out. Staggered cascades for lists: 80ms between items.
- **Hover states:** Subtle color shift + shadow adjustment over 200ms.
- **Page transitions:** Fade only (200ms).
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

Estilo Bento Box Grid representa uma tendência moderna em design UI/UX web com foco em general.

## Caso de Uso

Landing pages, SaaS
