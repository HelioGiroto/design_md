# Design System: Sales Intelligence Dashboard

## 1. Definição do Estilo

- **Nome:** Sales Intelligence Dashboard
- **Tipo:** BI/Analytics
- **Keywords:** Deal pipeline, sales metrics, territory performance, sales rep leaderboard, win-loss analysis, quota tracking, forecast accuracy
- **Era:** 2020s Modern
- **Light/Dark:** ✓ Full / ✓ Full

## 2. Paleta de Cores

- **Primárias:** Sales colors: won (green), lost (red), in-progress (blue), blocked (orange), quota met (gold), quota missed (grey)
- **Secundárias:** Pipeline stage colors, rep performance colors, quota achievement colors, forecast accuracy colors

## 3. Efeitos Visuais

Deal movement animations, metric updates, leaderboard ranking changes, gauge needle movements, status change highlights

## 4. AI Prompt Keywords

Design a sales intelligence dashboard. Use: pipeline funnel, deal cards (kanban), quota gauges, leaderboard table, territory map, win/loss ratios, forecast accuracy, activity timeline.

## 5. CSS Technical

```css
kanban columns (flex), gauge chart (SVG arc), leaderboard ranking styles, map integration (Mapbox/Google), timeline vertical, deal card with status border
```

## 6. Design System Variables

```css
--pipeline-colors: stage gradient, --gauge-track: #E5E7EB, --gauge-fill: primary, --rank-1-color: #FFD700, --rank-2-color: #C0C0C0, --rank-3-color: #CD7F32
```

## 7. Checklist de Implementação

- ☐ Pipeline stages shown
- ☐ Deals draggable
- ☐ Quotas visualized
- ☐ Rankings updated
- ☐ Territory clickable
- ☐ CRM integration

## 8. Visual Theme & Atmosphere

Sales Intelligence Dashboard — Design bi/analytics com deal pipeline, sales metrics, territory performance. Template e prompt pronto para IA. Estilo Sales Intelligence Dashboard representa uma tendência moderna em design UI/UX web com foco em bi/analytics.

- Density: 8/10 — Dense
- Variance: 4/10 — Moderate
- Motion: 6/10 — Expressive

## 9. Color Palette & Roles

- Palette derived from style keywords and era context

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

Estilo Sales Intelligence Dashboard representa uma tendência moderna em design UI/UX web com foco em bi/analytics.

## Caso de Uso

Landing pages, Websites modernas
