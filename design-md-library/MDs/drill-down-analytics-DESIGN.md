# Design System: Drill-Down Analytics

## 1. Definição do Estilo

- **Nome:** Drill-Down Analytics
- **Tipo:** BI/Analytics
- **Keywords:** Hierarchical data exploration, expandable sections, interactive drill-down paths, summary-to-detail flow, context preservation
- **Era:** 2020s Modern
- **Light/Dark:** ✓ Full / ✓ Full

## 2. Paleta de Cores

- **Primárias:** Primary brand, breadcrumb colors, drill-level indicator colors, hierarchy depth colors
- **Secundárias:** Drill-down path indicator colors, level-specific colors, highlight colors for selected level, transition colors

## 3. Efeitos Visuais

Drill-down expand animations, breadcrumb click transitions, smooth detail reveal, level change smooth, data reload animation

## 4. AI Prompt Keywords

Design a drill-down analytics dashboard. Use: breadcrumb navigation, expandable sections, summary-to-detail flow, back button prominent, level indicators, context preservation, hierarchical data display.

## 5. CSS Technical

```css
breadcrumb nav with separators, details/summary for expand, transition for drill animation, position: sticky breadcrumb, nested grid layouts, smooth scroll to detail
```

## 6. Design System Variables

```css
--breadcrumb-separator: /, --expand-duration: 300ms, --level-indent: 24px, --back-button-size: 40px, --context-bar-height: 48px, --drill-transition: 300ms ease
```

## 7. Checklist de Implementação

- ☐ Breadcrumbs clear
- ☐ Back navigation easy
- ☐ Expand animation smooth
- ☐ Context preserved
- ☐ Mobile drill works
- ☐ Deep links supported

## 8. Visual Theme & Atmosphere

Drill-Down Analytics — Design bi/analytics com hierarchical data exploration, expandable sections, interactive drill-down paths. Template e prompt pronto par... Estilo Drill-Down Analytics representa uma tendência moderna em design UI/UX web com foco em bi/analytics.

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

Estilo Drill-Down Analytics representa uma tendência moderna em design UI/UX web com foco em bi/analytics.

## Caso de Uso

Landing pages, Websites modernas
