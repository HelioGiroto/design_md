# design_md

Coleção de arquivos **DESIGN.md** — definições de design system no formato [Google Stitch](https://designmd.app/what-is-design-md) (YAML front matter + Markdown). Agentes de IA (Claude Code, Cursor, Windsurf, Kiro, Google Stitch) consomem esses arquivos para gerar UI visualmente consistente.

## Estrutura

- **`design-md-awesome/`** — 73 DESIGN.md curados manualmente (Airbnb, Apple, Stripe, Spotify, Tesla…). Cada marca em `brand/DESIGN.md` + `brand/README.md`.
- **`design-md-library/`**
  - `elementos_designmd.md` — Tabela mestre com os 454 sistemas catalogados em [designmd.app/library](https://designmd.app/library)
  - `454/` — 454 diretórios (slug) com thumbnails `.png`
  - `MDs/` — 454 arquivos `<slug>-DESIGN.md` baixados
- **`skills/extract_design_skill.md`** — Skill para fazer engenharia reversa do design system de qualquer site e gerar um DESIGN.md
- **`llms-full.txt`** — Catálogo completo offline (~500 entradas) do designmd.app

## Formato DESIGN.md

```
---
colors:    { primary: "#ff385c", ink: "#222222", … }
typography: { display-xl: { fontFamily: …, fontSize: …, … }, … }
rounded:   { sm: 8px, md: 14px, lg: 20px, … }
spacing:   { xs: 4px, sm: 8px, base: 16px, … }
components: { button-primary: { backgroundColor: "{colors.primary}", … }, … }
---

## Overview
…
```

## Uso

Adicione o caminho do `DESIGN.md` desejado na configuração do seu agente:
- **Claude Code:** inclua `@DESIGN.md` no `CLAUDE.md`
- **Cursor:** crie `.cursor/rules/` referenciando o arquivo
- **Google Stitch:** import direto na UI nativa

## CLI oficial

```bash
npx @google/design.md lint    # valida DESIGN.md (broken-refs, contrast-ratio, section-order)
```

## Links

- [designmd.app/library](https://designmd.app/library) — Biblioteca com 454+ design systems
- [designmd.app/what-is-design-md](https://designmd.app/what-is-design-md) — Especificação completa do formato
- [github.com/google-labs-code/design.md](https://github.com/google-labs-code/design.md) — Repositório oficial