# Design System: Memphis Design

## 1. Definição do Estilo

- **Nome:** Memphis Design
- **Tipo:** Postmodern, Colorful, Geometric, Playful
- **Keywords:** 80s, geometric, playful, postmodern, shapes, patterns, squiggles, triangles, neon, abstract, bold
- **Era:** 1980s Postmodern
- **Light/Dark:** ✓ Full / ✓ Full

## 2. Paleta de Cores

- **Primárias:** #FF71CE (Hot Pink), #FFCE5C (Yellow), #86CCCA (Teal), #6A7BB4 (Blue Purple)
- **Secundárias:** Complementary geometric colors, pattern fills, contrasting accent shapes

## 3. Efeitos Visuais

transform: rotate(), clip-path: polygon(), mix-blend-mode, repeating patterns, bold shapes

## 4. AI Prompt Keywords

Design a Memphis style interface. Use: bold geometric shapes (triangles, squiggles, circles), bright clashing colors, 80s postmodern aesthetic, playful patterns, dotted textures, asymmetric layouts, decorative elements.

## 5. CSS Technical

```css
clip-path: polygon() for shapes, background: repeating patterns, transform: rotate() for tilted elements, mix-blend-mode for overlays, border: dashed/dotted patterns, bold sans-serif
```

## 6. Design System Variables

```css
--memphis-pink: #FF71CE, --memphis-yellow: #FFCE5C, --memphis-teal: #86CCCA, --memphis-purple: #6A7BB4, --pattern-size: 20px, --shape-rotation: 15deg
```

## 7. Checklist de Implementação

- ☐ Geometric shapes visible
- ☐ Colors bold/clashing
- ☐ Patterns present
- ☐ Layout asymmetric
- ☐ Playful decorations
- ☐ 80s vibe achieved

## 8. Visual Theme & Atmosphere

Memphis Design — Design general com 80s, geometric, playful. Template e prompt pronto para IA. Estilo Memphis Design representa uma tendência moderna em design UI/UX web com foco em general.

- Density: 5/10 — Balanced
- Variance: 7/10 — Dynamic
- Motion: 4/10 — Subtle

## 9. Color Palette & Roles

- **#FF71CE** (#FF71CE) — Primary surface or dominant color
- **#FFCE5C** (#FFCE5C) — Secondary surface or text color
- **#86CCCA** (#86CCCA) — Supporting palette color
- **#6A7BB4** (#6A7BB4) — Supporting palette color

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
- No pure white (#FFFFFF) backgrounds — use off-white or dark surfaces
- No oversaturated accent colors (saturation cap: 80%)
- No 3-column equal-width feature layouts — use zig-zag or asymmetric grid
- No `h-screen` — use `min-h-[100dvh]`
- No AI copywriting clichés: "Elevate", "Seamless", "Unleash", "Next-Gen"
- No broken external image links — use picsum.photos or inline SVG
- No generic lorem ipsum in demos

## Contexto Histórico

Estilo Memphis Design representa uma tendência moderna em design UI/UX web com foco em general.

## Caso de Uso

Landing pages, SaaS
