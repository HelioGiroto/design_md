# Design System: Vibrant & Block-based

## 1. Definição do Estilo

- **Nome:** Vibrant & Block-based
- **Tipo:** Bold, Energetic, Playful, Geometric
- **Keywords:** Bold, energetic, playful, block layout, geometric shapes, high color contrast, duotone, modern, energetic
- **Era:** 2020s Modern
- **Light/Dark:** ✓ Full / ✓ Full

## 2. Paleta de Cores

- **Primárias:** Neon Green #39FF14, Electric Purple #BF00FF, Vivid Pink #FF1493, Bright Cyan #00FFFF, Sunburst #FFAA00
- **Secundárias:** Complementary: Orange #FF7F00, Shocking Pink #FF006E, Lime #CCFF00, triadic schemes

## 3. Efeitos Visuais

Large sections (48px+ gaps), animated patterns, bold hover (color shift), scroll-snap, large type (32px+), 200-300ms

## 4. AI Prompt Keywords

Design an energetic, vibrant interface with bold block layouts, geometric shapes, high color contrast, large typography (32px+), animated background patterns, duotone effects. Perfect for startups and youth-focused apps. Use 4-6 contrasting colors from complementary/triadic schemes.

## 5. CSS Technical

```css
display: flex/grid with large gaps (48px+), font-size: 32px+, background: animated patterns (CSS), color: neon/vibrant colors, animation: continuous pattern movement
```

## 6. Design System Variables

```css
--block-gap: 48px, --typography-size: 32px+, --color-palette: 4-6 vibrant colors, --animation: continuous pattern, --contrast-ratio: 7:1+
```

## 7. Checklist de Implementação

- ☐ Block layout with 48px+ gaps
- ☐ Large typography 32px+
- ☐ 4-6 vibrant colors max
- ☐ Animated patterns active
- ☐ Scroll-snap enabled
- ☐ High contrast verified (7:1+)

## 8. Visual Theme & Atmosphere

Layout blocos gigantes, cores vibrantes, tipografia 32px+. Para startups, apps de energia e ecommerce conversível. Prompt pronto para customizar. Y2K revivals (2020s) + Memphis Design (1980s). Cores altas, gaps gigantes, tipografia gigante dominam startups modernas.

- Density: 5/10 — Balanced
- Variance: 4/10 — Moderate
- Motion: 6/10 — Expressive

## 9. Color Palette & Roles

- **Neon Green** (#39FF14) — Primary surface or dominant color
- **Electric Purple** (#BF00FF) — Accent color, emphasis elements
- **Vivid Pink** (#FF1493) — Primary text color
- **Bright Cyan** (#00FFFF) — Accent highlight, links and focus states
- **Sunburst** (#FFAA00) — Supporting palette color
- **Orange** (#FF7F00) — Warm accent, call-to-action secondary
- **Shocking Pink** (#FF006E) — Primary text color
- **Lime** (#CCFF00) — Extended palette, decorative use

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
- No pure black (#000000) — use off-black or charcoal variants
- No oversaturated accent colors (saturation cap: 80%)
- No 3-column equal-width feature layouts — use zig-zag or asymmetric grid
- No `h-screen` — use `min-h-[100dvh]`
- No AI copywriting clichés: "Elevate", "Seamless", "Unleash", "Next-Gen"
- No broken external image links — use picsum.photos or inline SVG
- No generic lorem ipsum in demos

## Contexto Histórico

Y2K revivals (2020s) + Memphis Design (1980s). Cores altas, gaps gigantes, tipografia gigante dominam startups modernas.

## Caso de Uso

Startups, Ecommerce fashion, Apps gaming, Marketing conversível
