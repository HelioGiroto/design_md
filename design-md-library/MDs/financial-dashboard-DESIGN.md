# Design System: Financial Dashboard

## 1. Definição do Estilo

- **Nome:** Financial Dashboard
- **Tipo:** BI/Analytics
- **Keywords:** Revenue metrics, profit/loss visualization, budget tracking, financial ratios, portfolio performance, cash flow, audit trail
- **Era:** 2020s Modern
- **Light/Dark:** ✓ Full / ✓ Full

## 2. Paleta de Cores

- **Primárias:** Financial colors: profit (green #22C55E), loss (red #EF4444), neutral (grey), trust (dark blue #003366)
- **Secundárias:** Revenue highlight (green), expenses (red), budget variance (orange/red), balance (grey), accuracy (blue)

## 3. Efeitos Visuais

Number animations (count-up), trend direction indicators, percentage change animations, profit/loss color transitions

## 4. AI Prompt Keywords

Design a financial dashboard. Use: revenue/expense charts, profit margins, budget vs actual, cash flow waterfall, financial ratios, audit trail table, currency formatting, period comparisons.

## 5. CSS Technical

```css
number formatting (Intl.NumberFormat), waterfall chart (positive/negative bars), variance coloring, table with totals row, sparkline for trends, sticky column headers
```

## 6. Design System Variables

```css
--currency-symbol: $, --decimal-places: 2, --profit-color: #22C55E, --loss-color: #EF4444, --variance-threshold: 10%, --table-header-bg: #F3F4F6
```

## 7. Checklist de Implementação

- ☐ Currency formatted
- ☐ Decimals consistent
- ☐ P&L clear
- ☐ Budget variance shown
- ☐ Audit trail complete
- ☐ Export to Excel

## 8. Visual Theme & Atmosphere

Financial Dashboard — Design bi/analytics com revenue metrics, profit/loss visualization, budget tracking. Template e prompt pronto para IA. Estilo Financial Dashboard representa uma tendência moderna em design UI/UX web com foco em bi/analytics.

- Density: 8/10 — Dense
- Variance: 4/10 — Moderate
- Motion: 6/10 — Expressive

## 9. Color Palette & Roles

- **green** (#22C55E) — Primary surface or dominant color
- **red** (#EF4444) — Error states, destructive actions
- **dark blue** (#003366) — Dark surface, primary background

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

Estilo Financial Dashboard representa uma tendência moderna em design UI/UX web com foco em bi/analytics.

## Caso de Uso

Landing pages, Websites modernas
