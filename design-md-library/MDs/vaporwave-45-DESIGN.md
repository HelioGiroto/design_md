# Design System: Vaporwave

## 1. Definição do Estilo

- **Nome:** Vaporwave
- **Tipo:** Nostalgic, Pastel, Surreal, Digital
- **Keywords:** Synthwave, retro-futuristic, 80s-90s, neon, glitch, nostalgic, sunset gradient, dreamy, aesthetic
- **Era:** 1980s-90s Retro
- **Light/Dark:** ✓ Full / ✓ Dark focused

## 2. Paleta de Cores

- **Primárias:** #FF71CE (Pink), #01CDFE (Cyan), #05FFA1 (Mint), #B967FF (Purple)
- **Secundárias:** Sunset gradients, glitch overlays, VHS effects, neon accents, pastel variations

## 3. Efeitos Visuais

text-shadow glow, linear-gradient, filter: hue-rotate(), glitch animations, retro scan lines

## 4. AI Prompt Keywords

Design a vaporwave aesthetic interface. Use: sunset gradients (pink/cyan/purple), 80s-90s nostalgia, glitch effects, Greek statue imagery, palm trees, grid patterns, neon glow, retro-futuristic feel, dreamy atmosphere.

## 5. CSS Technical

```css
background: linear-gradient(180deg, #FF71CE, #01CDFE, #B967FF), filter: hue-rotate(), text-shadow: neon glow, retro grid (perspective + linear-gradient), VHS scanlines
```

## 6. Design System Variables

```css
--vapor-pink: #FF71CE, --vapor-cyan: #01CDFE, --vapor-mint: #05FFA1, --vapor-purple: #B967FF, --grid-color: rgba(255,255,255,0.1), --glow-intensity: 15px
```

## 7. Checklist de Implementação

- ☐ Sunset gradient present
- ☐ Neon glow applied
- ☐ Retro grid visible
- ☐ Glitch effects subtle
- ☐ Dreamy atmosphere
- ☐ 80s-90s aesthetic

## 8. Visual Theme & Atmosphere

Vaporwave — Design general com synthwave, retro-futuristic, 80s-90s. Template e prompt pronto para IA. Estilo Vaporwave representa uma tendência moderna em design UI/UX web com foco em general.

- Density: 5/10 — Balanced
- Variance: 8/10 — Expressive
- Motion: 6/10 — Expressive

## 9. Color Palette & Roles

- **#FF71CE** (#FF71CE) — Primary surface or dominant color
- **#01CDFE** (#01CDFE) — Secondary surface or text color
- **#05FFA1** (#05FFA1) — Supporting palette color
- **#B967FF** (#B967FF) — Supporting palette color

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

Estilo Vaporwave representa uma tendência moderna em design UI/UX web com foco em general.

## Caso de Uso

Landing pages, SaaS
