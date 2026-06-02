# design_md — AGENTS.md

## What this is

A curated collection of **DESIGN.md** files — design system definitions in [Google Stitch](https://designmd.app/what-is-design-md) format (YAML front matter + Markdown prose). AI coding agents consume these from a project root to generate visually consistent UI.

## Layout

- `design-md-awesome/` — 73 hand-curated DESIGN.md files (Airbnb, Apple, Stripe, etc.), each in `brand/DESIGN.md` + `brand/README.md`
- `design-md-library/454/` — 454 DESIGN.md files bulk-downloaded from [designmd.app/library](https://designmd.app/library), organized by slug
- `design-md-library/elementos_designmd.md` — Master table of all 454 library entries
- `skills/extract_design_skill.md` — AI skill for reverse-engineering a site's design system into DESIGN.md
- `llms-full.txt` — Complete catalog dump of all design systems from designmd.app

## DESIGN.md format

YAML front matter with sections: `colors`, `typography`, `rounded`, `spacing`, `components`. Followed by Markdown body with sections: Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts. Component tokens use `{path.to.token}` cross-references. See any file in `design-md-awesome/` for reference.

## No build / test / lint tooling

This is a static content repo. No package.json, no CI, no formatter, no typechecker. There is nothing to install or run.

## Creating new DESIGN.md files

Use the workflow in `skills/extract_design_skill.md`:
1. Read an existing reference (e.g. `design-md-awesome/stripe/DESIGN.md`)
2. Inspect the target URL's DOM and computed styles via browser
3. Extract exact HEX colors, font stacks, border-radius, shadows, spacing
4. Write a new `DESIGN.md` under `design-md-library/454/<slug>/`

## Reference sources

- `llms-full.txt` — The canonical offline reference (~500 entries)
- [designmd.app/library](https://designmd.app/library) — Library browser with 454+ design systems
- `npx @google/design.md lint` — Official CLI for validating DESIGN.md files (broken-refs, contrast-ratio, section-order)

## Language note

Many files, scripts, and design system names are in Brazilian Portuguese. The canonical author is ft.ia.br. `dicas.md` and `comandos.js` are scratch notes — ignore their content unless specifically needed.

## Browser automation helpers

- `automacao_bookmarklet.py` — PyAutoGUI script to bulk-download DESIGN.md files from the library (requires `pip install pyautogui opencv-python`)
- `download_and_move.py` — Downloads preview thumbnails for the 454 library entries
- `comandos.js` — DevTools snippet for scraping the library page via `document.querySelectorAll('.group.block')`
