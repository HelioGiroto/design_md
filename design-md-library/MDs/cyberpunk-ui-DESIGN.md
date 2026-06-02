# Design System: Cyberpunk UI

## 1. Definição do Estilo

- **Nome:** Cyberpunk UI
- **Tipo:** Neon, Dark, Dystopian, High-Tech
- **Keywords:** Neon, dark mode, terminal, HUD, sci-fi, glitch, dystopian, futuristic, matrix, tech noir
- **Era:** 2020s Cyberpunk
- **Light/Dark:** ✗ No / ✓ Only

## 2. Paleta de Cores

- **Primárias:** #00FF00 (Matrix Green), #FF00FF (Magenta), #00FFFF (Cyan), #0D0D0D (Dark)
- **Secundárias:** Neon gradients, scanline overlays, glitch colors, terminal green accents

## 3. Efeitos Visuais

Neon glow (text-shadow), glitch animations (skew/offset), scanlines (::before overlay), terminal fonts

## 4. AI Prompt Keywords

Design a cyberpunk interface. Use: neon colors on dark (#0D0D0D), terminal/HUD aesthetic, glitch effects, scanlines overlay, matrix green accents, monospace fonts, angular shapes, dystopian tech feel.

## 5. CSS Technical

```css
background: #0D0D0D, color: #00FF00 or #FF00FF, font-family: monospace, text-shadow: 0 0 10px neon, animation: glitch (transform skew), ::before scanlines (repeating-linear-gradient)
```

## 6. Design System Variables

```css
--bg-dark: #0D0D0D, --neon-green: #00FF00, --neon-magenta: #FF00FF, --neon-cyan: #00FFFF, --scanline-opacity: 0.1, --glitch-duration: 0.3s
```

## 7. Checklist de Implementação

- ☐ Dark background only
- ☐ Neon accents visible
- ☐ Glitch effect subtle
- ☐ Scanlines optional
- ☐ Monospace font
- ☐ Terminal aesthetic

## 8. Visual Theme & Atmosphere

Cyberpunk UI — Design general com neon, dark mode, terminal. Template e prompt pronto para IA. Estilo Cyberpunk UI representa uma tendência moderna em design UI/UX web com foco em general.

- Density: 8/10 — Dense
- Variance: 8/10 — Expressive
- Motion: 6/10 — Expressive

## 9. Color Palette & Roles

- **#00FF00** (#00FF00) — Primary surface or dominant color
- **#FF00FF** (#FF00FF) — Secondary surface or text color
- **#00FFFF** (#00FFFF) — Supporting palette color
- **#0D0D0D** (#0D0D0D) — Supporting palette color

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
- No pure white (#FFFFFF) backgrounds — use off-white or dark surfaces
- No oversaturated accent colors (saturation cap: 80%)
- No 3-column equal-width feature layouts — use zig-zag or asymmetric grid
- No `h-screen` — use `min-h-[100dvh]`
- No AI copywriting clichés: "Elevate", "Seamless", "Unleash", "Next-Gen"
- No broken external image links — use picsum.photos or inline SVG
- No generic lorem ipsum in demos

## Contexto Histórico

Estilo Cyberpunk UI representa uma tendência moderna em design UI/UX web com foco em general.

## Caso de Uso

Landing pages, SaaS
