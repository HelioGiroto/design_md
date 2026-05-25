---
version: alpha
name: Amazon
description: The classic e-commerce giant design system. Highly dense, utility-driven layout with signature orange accents on dark navy headers. Action-oriented, utilizing pill-shaped gold and orange buttons to drive immediate conversions.

colors:
  primary: "#FF9900"
  primary-dark: "#FA8900"
  secondary: "#007185"
  secondary-hover: "#C7511F"
  button-cart: "#FFD814"
  button-cart-hover: "#F7CA00"
  button-buy: "#FFA41C"
  button-buy-hover: "#FA8900"
  header-bg: "#131921"
  subheader-bg: "#232F3E"
  search-btn: "#FEB869"
  search-btn-hover: "#F3A847"
  canvas: "#FFFFFF"
  canvas-subdued: "#EAEDED"
  ink: "#0F1111"
  ink-mute: "#565959"
  hairline: "#D5D9D9"

typography:
  display-lg:
    fontFamily: '"Amazon Ember", Arial, sans-serif'
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  heading-md:
    fontFamily: '"Amazon Ember", Arial, sans-serif'
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  heading-sm:
    fontFamily: '"Amazon Ember", Arial, sans-serif'
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: '"Amazon Ember", Arial, sans-serif'
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  body-sm:
    fontFamily: '"Amazon Ember", Arial, sans-serif'
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button:
    fontFamily: '"Amazon Ember", Arial, sans-serif'
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0

rounded:
  sm: 4px
  md: 8px
  pill: 20px

spacing:
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  xxl: 32px

components:
  button-cart:
    backgroundColor: "{colors.button-cart}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 10px 16px
  button-buy:
    backgroundColor: "{colors.button-buy}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 10px 16px
  card-grid:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 16px
  nav-bar:
    backgroundColor: "{colors.header-bg}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-md}"
    rounded: "0px"
    padding: 12px 24px
---

## Overview

Amazon's design language is utilitarian, dense, and hyper-optimized for e-commerce. It uses a prominent dark navy (`#131921`) header to anchor the navigation and search, while the page body remains an off-white gray (`#EAEDED`) to make the stark white (`#FFFFFF`) product cards pop.

The brand's primary color is its signature Orange (`#FF9900`), but it is mostly used for accents, ratings, and logos. The actual transactional hierarchy is driven by two specific shades for buttons: Gold (`#FFD814`) for "Add to Cart" and deeper Orange (`#FFA41C`) for "Buy Now". These buttons use a full pill radius (`20px`).

Typography is driven by the proprietary **Amazon Ember** font, falling back securely to Arial. The text colors rely on a deep charcoal `#0F1111` for high legibility and a muted `#565959` for secondary data like review counts. Link tags are typically a teal `#007185` that transitions to a burnt orange `#C7511F` on hover.

## Do's and Don'ts

### Do
- Use the dark navy (`#131921`) for the top navigation bar.
- Use the distinctive gold pill button for primary "Add to Cart" actions.
- Use the teal color (`#007185`) for text links.
- Rely on dense grid structures to display multiple products.

### Don't
- Don't use the brand orange (`#FF9900`) for large background areas; it's an accent color.
- Don't use sharp square buttons for primary actions; they must be pills (`20px`).
- Don't over-use box shadows; cards should rely mostly on background color contrast or 1px hairline borders.
