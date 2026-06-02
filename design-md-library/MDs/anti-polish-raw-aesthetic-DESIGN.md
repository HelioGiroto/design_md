# Design System: Anti-Polish / Raw Aesthetic

## 1. Definição do Estilo

- **Nome:** Anti-Polish / Raw Aesthetic
- **Tipo:** Raw, Imperfect, Authentic, Anti-Polish
- **Keywords:** Hand-drawn, collage, scanned textures, unfinished, imperfect, authentic, human, sketch, raw marks, creative process
- **Era:** 2025+ Anti-Digital
- **Light/Dark:** ✓ Full / ✓ Full

## 2. Paleta de Cores

- **Primárias:** Paper White #FAFAF8, Pencil Grey #4A4A4A, Marker Black #1A1A1A, Kraft Brown #C4A77D
- **Secundárias:** Watercolor washes, pencil shading, ink splatters, tape textures, aged paper tones

## 3. Efeitos Visuais

No smooth transitions, hand-drawn animations, paper texture overlays, jitter effects, sketch reveal

## 4. AI Prompt Keywords

Design with anti-polish raw aesthetic. Use: hand-drawn elements, scanned textures, unfinished look, paper/pencil textures, collage style, authentic imperfection, sketch marks, tape/sticker overlays, human touch.

## 5. CSS Technical

```css
background: url(paper-texture.png), filter: grayscale() contrast(), border: hand-drawn SVG, transform: rotate(small random), no smooth transitions, sketch-style fonts, opacity variations
```

## 6. Design System Variables

```css
--paper-bg: #FAFAF8, --pencil-color: #4A4A4A, --marker-black: #1A1A1A, --kraft-brown: #C4A77D, --sketch-rotation: random(-3deg, 3deg), --texture-opacity: 0.3
```

## 7. Checklist de Implementação

- ☐ Textures loaded
- ☐ Hand-drawn elements present
- ☐ Imperfections intentional
- ☐ Authentic feel achieved
- ☐ Performance ok with textures
- ☐ Accessibility maintained

## 8. Visual Theme & Atmosphere

Anti-Polish / Raw Aesthetic — Design general com hand-drawn, collage, scanned textures. Template e prompt pronto para IA. Estilo Anti-Polish / Raw Aesthetic representa uma tendência moderna em design UI/UX web com foco em general.

- Density: 5/10 — Balanced
- Variance: 8/10 — Expressive
- Motion: 6/10 — Expressive

## 9. Color Palette & Roles

- **Paper White** (#FAFAF8) — Light surface, card backgrounds
- **Pencil Grey** (#4A4A4A) — Secondary text, borders, muted elements
- **Marker Black** (#1A1A1A) — Dark surface, primary background
- **Kraft Brown** (#C4A77D) — Supporting palette color

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

- **Primary Button:** Moderately rounded (0.75rem) shape. Accent color fill. Hover: 8% darken + subtle lift shadow. Active: -1px translate tactile press. Font weight 600. No outer glows.
- **Secondary / Ghost Button:** Outline variant. 1.5px border in muted color. Text in primary color. Hover: subtle background fill.
- **Cards:** Moderately rounded (0.75rem) corners. Surface background. Subtle shadow (0 2px 12px rgba(0,0,0,0.06)). 1px border stroke.
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

Estilo Anti-Polish / Raw Aesthetic representa uma tendência moderna em design UI/UX web com foco em general.

## Caso de Uso

Landing pages, SaaS
