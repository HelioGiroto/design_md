# Design System: Swiss Modernism 2.0

## 1. Definição do Estilo

- **Nome:** Swiss Modernism 2.0
- **Tipo:** Grid-Based, Typographic, Functional, Modern
- **Keywords:** Grid system, Helvetica, modular, asymmetric, international style, rational, clean, mathematical spacing
- **Era:** 1950s Swiss + 2020s
- **Light/Dark:** ✓ Full / ✓ Full

## 2. Paleta de Cores

- **Primárias:** #000000, #FFFFFF, #F5F5F5, single vibrant accent only
- **Secundárias:** Minimal secondary, accent for emphasis only, no gradients

## 3. Efeitos Visuais

display: grid, grid-template-columns: repeat(12 1fr), gap: 1rem, mathematical ratios, clear hierarchy

## 4. AI Prompt Keywords

Design with Swiss Modernism 2.0. Use: strict grid system (12 columns), Helvetica/Inter fonts, mathematical spacing, asymmetric balance, high contrast, minimal decoration, clean hierarchy, single accent color.

## 5. CSS Technical

```css
display: grid, grid-template-columns: repeat(12, 1fr), gap: 1rem (8px base unit), font-family: Inter/Helvetica, font-weight: 400-700, color: #000/#FFF, single accent
```

## 6. Design System Variables

```css
--grid-columns: 12, --grid-gap: 1rem, --base-unit: 8px, --font-primary: Inter, --color-text: #000000, --color-bg: #FFFFFF, --accent: single vibrant
```

## 7. Checklist de Implementação

- ☐ 12-column grid strict
- ☐ Spacing mathematical
- ☐ Typography hierarchy clear
- ☐ Single accent only
- ☐ No decorations
- ☐ High contrast verified

## 8. Visual Theme & Atmosphere

Swiss Modernism 2.0 — Design general com grid system, helvetica, modular. Template e prompt pronto para IA. Estilo Swiss Modernism 2.0 representa uma tendência moderna em design UI/UX web com foco em general.

- Density: 3/10 — Airy
- Variance: 7/10 — Dynamic
- Motion: 4/10 — Subtle

## 9. Color Palette & Roles

- **#000000** (#000000) — Primary surface or dominant color
- **#FFFFFF** (#FFFFFF) — Secondary surface or text color
- **#F5F5F5** (#F5F5F5) — Supporting palette color

## 10. Typography Rules

- **Display / Hero:** Inter/Helvetica — Weight 700, tight tracking, used for headline impact
- **Body:** Inter/Helvetica — Weight 400, 16px/1.6 line-height, max 72ch per line
- **UI Labels / Captions:** Inter/Helvetica — 0.875rem, weight 500, slight letter-spacing
- **Monospace:** JetBrains Mono — Used for code, metadata, and technical values

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

Estilo Swiss Modernism 2.0 representa uma tendência moderna em design UI/UX web com foco em general.

## Caso de Uso

Landing pages, SaaS
