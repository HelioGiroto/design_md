# Design System: Knolling Pastel Flat Lay

## 1. Definição do Estilo

- **Nome:** Knolling Pastel Flat Lay
- **Tipo:** Organized, Instructional, Calm
- **Keywords:** knolling, flat lay, organized, pastel, clean, photography, symmetrical, grid
- **Era:** Modern Photography
- **Light/Dark:** ✓ Full / ✗ No

## 2. Paleta de Cores

- **Primárias:** Background #F6D0D6, Text #2D2D2D, Accent #CBE4F0
- **Secundárias:** Soft Mint #D0F0C0, Lavender #E6E6FA, Shadow Grey #00000020

## 3. Efeitos Visuais

Photorealistic stationery items, 50/50 vertical background split, tech and analog mixture, soft natural shadows, matte paper stock.

## 4. AI Prompt Keywords

knolling landing page, flat lay style, organized objects, pastel background, clean 90 degree alignment, overhead photography look

## 5. CSS Technical

```css
background-color: #F6D0D6; color: #2D2D2D; font-family: 'Lato', sans-serif; display: grid; grid-template-columns: repeat(auto-fill, minmax(100px, 1fr)); gap: 20px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
```

## 6. Design System Variables

```css
--bg-pink: #F6D0D6, --bg-blue: #CBE4F0, --text-dark: #2D2D2D, --font-clean: 'Lato', sans-serif, --shadow-soft: 0 4px 6px rgba(0,0,0,0.1)
```

## 7. Checklist de Implementação

- ☐ Grid alignment (Knolling)
- ☐ Soft pastel background split
- ☐ Realistic drop shadows (depth)
- ☐ Mixed media (tech + analog objects)
- ☐ Clean sans-serif type

## 8. Visual Theme & Atmosphere

Knolling Pastel Flat Lay — Design organization com knolling, flat lay, organized. Template e prompt pronto para IA. Estilo Knolling Pastel Flat Lay representa uma tendência moderna em design UI/UX web com foco em organization.

- Density: 3/10 — Airy
- Variance: 2/10 — Structured
- Motion: 4/10 — Subtle

## 9. Color Palette & Roles

- **Background** (#F6D0D6) — Primary background surface
- **Text** (#2D2D2D) — Primary text color
- **Accent** (#CBE4F0) — Primary accent, CTAs and interactive elements
- **Soft Mint** (#D0F0C0) — Extended palette, decorative use
- **Lavender** (#E6E6FA) — Extended palette, decorative use
- **Shadow Grey** (#00000020) — Secondary text, borders, muted elements

## 10. Typography Rules

- **Display / Hero:** Lato — Weight 700, tight tracking, used for headline impact
- **Body:** Lato — Weight 400, 16px/1.6 line-height, max 72ch per line
- **UI Labels / Captions:** Lato — 0.875rem, weight 500, slight letter-spacing
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
- **Hero layout:** Split-screen (text left, visual right).
- **Feature sections:** Zig-zag alternating text+image rows. No 3-equal-columns.
- **Mobile collapse:** All multi-column layouts collapse below 768px. No horizontal overflow.
- **z-index contract:** base (0) / sticky-nav (100) / overlay (200) / modal (300) / toast (500).

## 13. Motion & Interaction

- **Physics:** Ease-out curves, 200-300ms duration. Smooth and predictable.
- **Entry animations:** Fade + translate-Y (16px → 0) over 420ms ease-out. Staggered cascades for lists: 80ms between items.
- **Hover states:** Subtle color shift + shadow adjustment over 200ms.
- **Page transitions:** Fade only (200ms).
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

Estilo Knolling Pastel Flat Lay representa uma tendência moderna em design UI/UX web com foco em organization.

## Caso de Uso

Landing pages, Websites modernas
