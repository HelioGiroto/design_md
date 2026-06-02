# Design System: Organic Biophilic

## 1. Definição do Estilo

- **Nome:** Organic Biophilic
- **Tipo:** Natural, Organic, Sustainable, Calming
- **Keywords:** Nature, organic shapes, green, sustainable, rounded, flowing, wellness, earthy, natural textures
- **Era:** 2020s Sustainable
- **Light/Dark:** ✓ Full / ✓ Full

## 2. Paleta de Cores

- **Primárias:** #228B22 (Forest Green), #8B4513 (Earth Brown), #87CEEB (Sky Blue), #F5F5DC (Beige)
- **Secundárias:** Natural gradients, earth tones, sky blues, organic textures, wood/stone colors

## 3. Efeitos Visuais

Rounded corners (16-24px), organic curves (border-radius variations), natural shadows, flowing SVG shapes

## 4. AI Prompt Keywords

Design a biophilic organic interface. Use: nature-inspired colors (greens, browns), organic curved shapes, rounded corners (16-24px), natural textures (wood, stone), flowing SVG elements, wellness aesthetic, earthy palette.

## 5. CSS Technical

```css
border-radius: 16-24px (varied), background: earth tones, SVG organic shapes (blob), box-shadow: natural soft, color: #228B22 #8B4513 #87CEEB, texture overlays (subtle)
```

## 6. Design System Variables

```css
--forest-green: #228B22, --earth-brown: #8B4513, --sky-blue: #87CEEB, --cream-bg: #F5F5DC, --organic-radius: 24px, --shadow-soft: 0 8px 32px rgba(0,0,0,0.08)
```

## 7. Checklist de Implementação

- ☐ Earth tones dominant
- ☐ Organic curves present
- ☐ Natural textures subtle
- ☐ Green accents
- ☐ Rounded everywhere
- ☐ Calming feel

## 8. Visual Theme & Atmosphere

Organic Biophilic — Design general com nature, organic shapes, green. Template e prompt pronto para IA. Estilo Organic Biophilic representa uma tendência moderna em design UI/UX web com foco em general.

- Density: 5/10 — Balanced
- Variance: 8/10 — Expressive
- Motion: 4/10 — Subtle

## 9. Color Palette & Roles

- **#228B22** (#228B22) — Primary surface or dominant color
- **#8B4513** (#8B4513) — Secondary surface or text color
- **#87CEEB** (#87CEEB) — Supporting palette color
- **#F5F5DC** (#F5F5DC) — Supporting palette color

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
- **Hero layout:** Asymmetric composition.
- **Feature sections:** Asymmetric grid with varied card sizes. No 3-equal-columns.
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

Estilo Organic Biophilic representa uma tendência moderna em design UI/UX web com foco em general.

## Caso de Uso

Landing pages, SaaS
