# Design System: Conversion-Optimized

## 1. Definição do Estilo

- **Nome:** Conversion-Optimized
- **Tipo:** Landing Page
- **Keywords:** Form-focused, minimalist design, single CTA focus, high contrast, urgency elements, trust signals, social proof, clear value
- **Era:** 2020s Modern
- **Light/Dark:** ✓ Full / ✓ Full

## 2. Paleta de Cores

- **Primárias:** Primary brand color, high-contrast white/light backgrounds, warning/urgency colors for time-limited offers
- **Secundárias:** Secondary CTA color (muted), trust element colors (testimonial highlights), accent for key benefits

## 3. Efeitos Visuais

Hover states on CTA (color shift, slight scale), form field focus animations, loading spinner, success feedback

## 4. AI Prompt Keywords

Design a conversion-optimized landing page. Use: single primary CTA, minimal distractions, trust badges, urgency elements (limited time), social proof (testimonials), clear value proposition, form above fold, progress indicators.

## 5. CSS Technical

```css
form with focus states, input:focus ring, button: primary color high contrast, position: sticky for CTA, max-width: 600px for form, loading spinner, success/error states
```

## 6. Design System Variables

```css
--cta-color: high contrast primary, --form-max-width: 600px, --input-height: 48px, --focus-ring: 3px solid accent, --success-color: #22C55E, --error-color: #EF4444
```

## 7. Checklist de Implementação

- ☐ Single primary CTA visible
- ☐ Form fields minimal (3-5)
- ☐ Trust badges present
- ☐ Social proof above fold
- ☐ Mobile form optimized
- ☐ Loading states implemented
- ☐ A/B test ready

## 8. Visual Theme & Atmosphere

Conversion-Optimized — Design landing page com form-focused, minimalist design, single cta focus. Template e prompt pronto para IA. Estilo Conversion-Optimized representa uma tendência moderna em design UI/UX web com foco em landing page.

- Density: 3/10 — Airy
- Variance: 3/10 — Restrained
- Motion: 6/10 — Expressive

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
- **Entry animations:** Fade + translate-Y (16px → 0) over 480ms ease-out. Staggered cascades for lists: 100ms between items.
- **Hover states:** Scale(1.03) + shadow lift over 200ms.
- **Page transitions:** Fade + slide (300ms).
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

Estilo Conversion-Optimized representa uma tendência moderna em design UI/UX web com foco em landing page.

## Caso de Uso

Marketing, Conversão, Lead gen
