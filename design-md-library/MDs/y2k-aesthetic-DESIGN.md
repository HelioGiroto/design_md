# Design System: Y2K Aesthetic

## 1. Definição do Estilo

- **Nome:** Y2K Aesthetic
- **Tipo:** Nostalgic, Shiny, Futuristic, Playful
- **Keywords:** Neon pink, chrome, metallic, bubblegum, iridescent, glossy, retro-futurism, 2000s, futuristic nostalgia
- **Era:** Y2K 2000s
- **Light/Dark:** ✓ Full / ◐ Partial

## 2. Paleta de Cores

- **Primárias:** #FF69B4 (Hot Pink), #00FFFF (Cyan), #C0C0C0 (Silver), #9400D3 (Purple)
- **Secundárias:** Metallic gradients, glossy overlays, iridescent effects, chrome textures

## 3. Efeitos Visuais

linear-gradient metallic, glossy buttons, 3D chrome effects, glow animations, bubble shapes

## 4. AI Prompt Keywords

Design a Y2K aesthetic interface. Use: neon pink/cyan colors, chrome/metallic textures, bubblegum gradients, glossy buttons, iridescent effects, 2000s futurism, star/sparkle decorations, bubble shapes, tech-optimistic vibe.

## 5. CSS Technical

```css
background: linear-gradient(135deg, #FF69B4, #00FFFF), filter: drop-shadow for glow, border-radius: 50% for bubbles, metallic gradients (silver/chrome), text-shadow: neon glow, ::before for sparkles
```

## 6. Design System Variables

```css
--neon-pink: #FF69B4, --neon-cyan: #00FFFF, --chrome-silver: #C0C0C0, --glossy-gradient: linear-gradient(180deg, white 0%, transparent 50%), --glow-blur: 10px
```

## 7. Checklist de Implementação

- ☐ Neon colors balanced
- ☐ Chrome effects visible
- ☐ Glossy buttons styled
- ☐ Bubble shapes decorative
- ☐ Sparkle animations
- ☐ Retro fonts loaded

## 8. Visual Theme & Atmosphere

Y2K Aesthetic — Design general com neon pink, chrome, metallic. Template e prompt pronto para IA. Estilo Y2K Aesthetic representa uma tendência moderna em design UI/UX web com foco em general.

- Density: 5/10 — Balanced
- Variance: 7/10 — Dynamic
- Motion: 8/10 — Cinematic

## 9. Color Palette & Roles

- **#FF69B4** (#FF69B4) — Primary surface or dominant color
- **#00FFFF** (#00FFFF) — Secondary surface or text color
- **#C0C0C0** (#C0C0C0) — Supporting palette color
- **#9400D3** (#9400D3) — Supporting palette color

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

- **Primary Button:** Rounded (50% for bubbles) shape. Accent color fill. Hover: 8% darken + subtle lift shadow. Active: -1px translate tactile press. Font weight 600. No outer glows.
- **Secondary / Ghost Button:** Outline variant. 1.5px border in muted color. Text in primary color. Hover: subtle background fill.
- **Cards:** Rounded (50% for bubbles) corners. Surface background. Subtle shadow (0 2px 12px rgba(0,0,0,0.06)). 1px border stroke.
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
- **Entry animations:** Fade + translate-Y (16px → 0) over 540ms ease-out. Staggered cascades for lists: 120ms between items.
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

Estilo Y2K Aesthetic representa uma tendência moderna em design UI/UX web com foco em general.

## Caso de Uso

Landing pages, SaaS
