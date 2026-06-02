# Design System: E-Ink / Paper

## 1. Definição do Estilo

- **Nome:** E-Ink / Paper
- **Tipo:** Paper-Like, Minimal, Calm, Readable
- **Keywords:** Paper-like, matte, high contrast, texture, reading, calm, slow tech, monochrome
- **Era:** 2020s Digital Well-being
- **Light/Dark:** ✓ Full / ✗ Low (inverted only)

## 2. Paleta de Cores

- **Primárias:** Off-White #FDFBF7, Paper White #F5F5F5, Ink Black #1A1A1A
- **Secundárias:** Pencil Grey #4A4A4A, Highlighter Yellow #FFFF00 (accent)

## 3. Efeitos Visuais

No motion blur, distinct page turns, grain/noise texture, sharp transitions (no fade)

## 4. AI Prompt Keywords

Design an e-ink/paper style interface. Use: high contrast black on off-white, paper texture, no animations (instant transitions), reading-focused, minimal UI chrome, distraction-free, calm aesthetic, monochrome.

## 5. CSS Technical

```css
background: #FDFBF7 (paper white), color: #1A1A1A, transition: none, font-family: serif for reading, no gradients, border: 1px solid #E0E0E0, texture overlay (noise)
```

## 6. Design System Variables

```css
--paper-bg: #FDFBF7, --ink-color: #1A1A1A, --pencil-grey: #4A4A4A, --border-color: #E0E0E0, --font-reading: Georgia, --transition: none
```

## 7. Checklist de Implementação

- ☐ Paper background color
- ☐ High contrast text
- ☐ No animations
- ☐ Reading optimized
- ☐ Distraction-free
- ☐ Print-friendly

## 8. Visual Theme & Atmosphere

E-Ink / Paper — Design general com paper-like, matte, high contrast. Template e prompt pronto para IA. Estilo E-Ink / Paper representa uma tendência moderna em design UI/UX web com foco em general.

- Density: 3/10 — Airy
- Variance: 2/10 — Structured
- Motion: 6/10 — Expressive

## 9. Color Palette & Roles

- **Off-White** (#FDFBF7) — Light surface, card backgrounds
- **Paper White** (#F5F5F5) — Light surface, card backgrounds
- **Ink Black** (#1A1A1A) — Dark surface, primary background
- **Pencil Grey** (#4A4A4A) — Secondary text, borders, muted elements
- **Highlighter Yellow** (#FFFF00) — Warning states, attention indicators

## 10. Typography Rules

- **Display / Hero:** serif for reading — Weight 700, tight tracking, used for headline impact
- **Body:** serif for reading — Weight 400, 16px/1.6 line-height, max 72ch per line
- **UI Labels / Captions:** serif for reading — 0.875rem, weight 500, slight letter-spacing
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

Estilo E-Ink / Paper representa uma tendência moderna em design UI/UX web com foco em general.

## Caso de Uso

Landing pages, SaaS
