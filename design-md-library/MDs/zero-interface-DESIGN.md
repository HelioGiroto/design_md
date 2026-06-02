# Design System: Zero Interface

## 1. Definição do Estilo

- **Nome:** Zero Interface
- **Tipo:** Invisible, Ambient, Voice-Driven, Minimal
- **Keywords:** Minimal visible UI, voice-first, gesture-based, AI-driven, invisible controls, predictive, context-aware, ambient
- **Era:** 2020s AI-Era
- **Light/Dark:** ✓ Full / ✓ Full

## 2. Paleta de Cores

- **Primárias:** Neutral backgrounds: Soft white #FAFAFA, light grey #F0F0F0, warm off-white #F5F1E8
- **Secundárias:** Subtle feedback: light green, light red, minimal UI elements, soft accents

## 3. Efeitos Visuais

Voice recognition UI, gesture detection, AI predictions (smooth reveal), progressive disclosure, smart suggestions

## 4. AI Prompt Keywords

Create a voice-first, gesture-based, AI-driven interface with minimal visible UI, progressive disclosure, voice recognition UI, gesture detection, AI predictions, smart suggestions, context-aware actions. Hide controls until needed.

## 5. CSS Technical

```css
voice-commands: Web Speech API, gesture-detection: touch events, AI-predictions: hidden by default (reveal on hover), progressive-disclosure: show on demand, minimal UI visible
```

## 6. Design System Variables

```css
--voice-ui: enabled, --gesture-detection: active, --ai-predictions: smart, --progressive-disclosure: true, --visible-ui: minimal, --context-aware: true
```

## 7. Checklist de Implementação

- ☐ Voice commands responsive
- ☐ Gesture detection active
- ☐ AI predictions hidden/revealed
- ☐ Progressive disclosure working
- ☐ Minimal visible UI
- ☐ Smart suggestions contextual

## 8. Visual Theme & Atmosphere

Zero Interface — Design general com minimal visible ui, voice-first, gesture-based. Template e prompt pronto para IA. Estilo Zero Interface representa uma tendência moderna em design UI/UX web com foco em general.

- Density: 3/10 — Airy
- Variance: 2/10 — Structured
- Motion: 4/10 — Subtle

## 9. Color Palette & Roles

- **Soft white** (#FAFAFA) — Light surface, card backgrounds
- **light grey** (#F0F0F0) — Secondary text, borders, muted elements
- **warm off-white** (#F5F1E8) — Light surface, card backgrounds

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

- **Physics:** Ease-out curves, 200-300ms duration. Smooth and predictable.
- **Entry animations:** Fade + translate-Y (16px → 0) over 420ms ease-out. Staggered cascades for lists: 80ms between items.
- **Hover states:** Subtle color shift + shadow adjustment over 200ms.
- **Page transitions:** Fade only (200ms).
- **Performance:** Only transform and opacity animated. No layout-triggering properties.

## 14. Anti-Patterns (Banned)

- No emojis in UI — use icon system only (Lucide, Heroicons)
- No decorative gradients — flat color only
- No shadows heavier than 0 2px 8px rgba(0,0,0,0.08)
- No pure black (#000000) — use off-black or charcoal variants
- No oversaturated accent colors (saturation cap: 80%)
- No 3-column equal-width feature layouts — use zig-zag or asymmetric grid
- No `h-screen` — use `min-h-[100dvh]`
- No AI copywriting clichés: "Elevate", "Seamless", "Unleash", "Next-Gen"
- No broken external image links — use picsum.photos or inline SVG
- No generic lorem ipsum in demos

## Contexto Histórico

Estilo Zero Interface representa uma tendência moderna em design UI/UX web com foco em general.

## Caso de Uso

Landing pages, SaaS
