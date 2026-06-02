# Design System: Pixel Art

## 1. Definição do Estilo

- **Nome:** Pixel Art
- **Tipo:** Pixelated, Retro, Colorful, Nostalgic
- **Keywords:** Retro, 8-bit, 16-bit, gaming, blocky, nostalgic, pixelated, arcade
- **Era:** 1980s Arcade
- **Light/Dark:** ✓ Full / ✓ Full

## 2. Paleta de Cores

- **Primárias:** Primary colors (NES Palette), brights, limited palette
- **Secundárias:** Black outlines, shading via dithering or block colors

## 3. Efeitos Visuais

Frame-by-frame sprite animation, blinking cursor, instant transitions, marquee text

## 4. AI Prompt Keywords

Design a pixel art inspired interface. Use: pixelated fonts, 8-bit or 16-bit aesthetic, sharp edges (image-rendering: pixelated), limited color palette, blocky UI elements, retro gaming feel.

## 5. CSS Technical

```css
font-family: 'Press Start 2P', image-rendering: pixelated, box-shadow: 4px 0 0 #000 (pixel border), no anti-aliasing
```

## 6. Design System Variables

```css
--pixel-size: 4px, --font: pixel font, --border-style: pixel-shadow, --anti-alias: none
```

## 7. Checklist de Implementação

- ☐ Pixelated fonts loaded
- ☐ Images sharp (no blur)
- ☐ CSS box-shadow for pixel borders
- ☐ Retro palette
- ☐ Blocky layout

## 8. Visual Theme & Atmosphere

Pixel Art — Design general com retro, 8-bit, 16-bit. Template e prompt pronto para IA. Estilo Pixel Art representa uma tendência moderna em design UI/UX web com foco em general.

- Density: 5/10 — Balanced
- Variance: 7/10 — Dynamic
- Motion: 6/10 — Expressive

## 9. Color Palette & Roles

- Palette derived from style keywords and era context

## 10. Typography Rules

- **Display / Hero:** Press Start 2P — Weight 700, tight tracking, used for headline impact
- **Body:** Press Start 2P — Weight 400, 16px/1.6 line-height, max 72ch per line
- **UI Labels / Captions:** Press Start 2P — 0.875rem, weight 500, slight letter-spacing
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

- **Physics:** Spring — stiffness 120, damping 20. Confident, weighted transitions.
- **Entry animations:** Fade + translate-Y (16px → 0) over 480ms ease-out. Staggered cascades for lists: 100ms between items.
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

Estilo Pixel Art representa uma tendência moderna em design UI/UX web com foco em general.

## Caso de Uso

Landing pages, SaaS
