# Design System: Skeuomorphism

## 1. Definição do Estilo

- **Nome:** Skeuomorphism
- **Tipo:** Realistic, Tactile, Textured, Detailed
- **Keywords:** Realistic, texture, depth, 3D appearance, real-world metaphors, shadows, gradients, tactile, detailed, material
- **Era:** 2007-2012 iOS
- **Light/Dark:** ◐ Partial / ◐ Partial

## 2. Paleta de Cores

- **Primárias:** Rich realistic: wood, leather, metal colors, detailed gradients (8-12 stops), metallic effects
- **Secundárias:** Realistic lighting gradients, shadow variations (30-50% darker), texture overlays, material colors

## 3. Efeitos Visuais

Realistic shadows (layers), depth (perspective), texture details (noise, grain), realistic animations (300-500ms)

## 4. AI Prompt Keywords

Design a realistic, textured interface with 3D depth, real-world metaphors (leather, wood, metal), complex gradients (8-12 stops), realistic shadows, grain/texture overlays, tactile press animations. Perfect for premium/luxury products.

## 5. CSS Technical

```css
background: complex gradient (8-12 stops), box-shadow: realistic multi-layer, background-image: texture overlay (noise, grain), filter: drop-shadow, transform: scale on press (300-500ms)
```

## 6. Design System Variables

```css
--gradient-stops: 8-12, --texture-overlay: noise+grain, --shadow-layers: 3+, --animation-duration: 300-500ms, --depth-effect: pronounced, --tactile: true
```

## 7. Checklist de Implementação

- ☐ Realistic textures applied
- ☐ Complex gradients 8-12 stops
- ☐ Multi-layer shadows
- ☐ Texture overlays present
- ☐ Tactile animations smooth
- ☐ Depth effect pronounced

## 8. Visual Theme & Atmosphere

Skeuomorphism — Design general com realistic, texture, depth. Template e prompt pronto para IA. Estilo Skeuomorphism representa uma tendência moderna em design UI/UX web com foco em general.

- Density: 5/10 — Balanced
- Variance: 4/10 — Moderate
- Motion: 8/10 — Cinematic

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
- **Entry animations:** Fade + translate-Y (16px → 0) over 540ms ease-out. Staggered cascades for lists: 120ms between items.
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

Estilo Skeuomorphism representa uma tendência moderna em design UI/UX web com foco em general.

## Caso de Uso

Landing pages, SaaS
