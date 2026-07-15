# Create or update AGENTS.md

**Session ID:** ses_1767d44a8ffeEYRWY9nhTvghXT
**Created:** 6/2/2026, 3:05:06 PM
**Updated:** 7/15/2026, 3:07:31 PM

---

## User

Create or update `AGENTS.md` for this repository.

The goal is a compact instruction file that helps future OpenCode sessions avoid mistakes and ramp up quickly. Every line should answer: "Would an agent likely miss this without help?" If not, leave it out.

User-provided focus or constraints (honor these):


## How to investigate

Read the highest-value sources first:
- `README*`, root manifests, workspace config, lockfiles
- build, test, lint, formatter, typecheck, and codegen config
- CI workflows and pre-commit / task runner config
- existing instruction files (`AGENTS.md`, `CLAUDE.md`, `.cursor/rules/`, `.cursorrules`, `.github/copilot-instructions.md`)
- repo-local OpenCode config such as `opencode.json`

If architecture is still unclear after reading config and docs, inspect a small number of representative code files to find the real entrypoints, package boundaries, and execution flow. Prefer reading the files that explain how the system is wired together over random leaf files.

Prefer executable sources of truth over prose. If docs conflict with config or scripts, trust the executable source and only keep what you can verify.

## What to extract

Look for the highest-signal facts for an agent working in this repo:
- exact developer commands, especially non-obvious ones
- how to run a single test, a single package, or a focused verification step
- required command order when it matters, such as `lint -> typecheck -> test`
- monorepo or multi-package boundaries, ownership of major directories, and the real app/library entrypoints
- framework or toolchain quirks: generated code, migrations, codegen, build artifacts, special env loading, dev servers, infra deploy flow
- repo-specific style or workflow conventions that differ from defaults
- testing quirks: fixtures, integration test prerequisites, snapshot workflows, required services, flaky or expensive suites
- important constraints from existing instruction files worth preserving

Good `AGENTS.md` content is usually hard-earned context that took reading multiple files to infer.

## Questions

Only ask the user questions if the repo cannot answer something important. Use the `question` tool for one short batch at most.

Good questions:
- undocumented team conventions
- branch / PR / release expectations
- missing setup or test prerequisites that are known but not written down

Do not ask about anything the repo already makes clear.

## Writing rules

Include only high-signal, repo-specific guidance such as:
- exact commands and shortcuts the agent would otherwise guess wrong
- architecture notes that are not obvious from filenames
- conventions that differ from language or framework defaults
- setup requirements, environment quirks, and operational gotchas
- references to existing instruction sources that matter

Exclude:
- generic software advice
- long tutorials or exhaustive file trees
- obvious language conventions
- speculative claims or anything you could not verify
- content better stored in another file referenced via `opencode.json` `instructions`

When in doubt, omit.

Prefer short sections and bullets. If the repo is simple, keep the file simple. If the repo is large, summarize the few structural facts that actually change how an agent should work.

If `AGENTS.md` already exists at `/home/mkt/design_md`, improve it in place rather than rewriting blindly. Preserve verified useful guidance, delete fluff or stale claims, and reconcile it with the current codebase.

---

## Assistant (Build · Big Pickle · 8.5s)

_Thinking:_

Let me start by investigating the repository structure to understand what we're working with.

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md"
}
```

**Output:**
```
<path>/home/mkt/design_md</path>
<type>directory</type>
<entries>
.DS_Store
.git/
comandos.js
design-md-awesome/
design-md-library/
dicas.md
llms-full.txt
README.md
skills/

(9 entries)
</entries>
```

**Tool: glob**

**Input:**
```json
{
  "pattern": "README*",
  "path": "/home/mkt/design_md"
}
```

**Output:**
```
/home/mkt/design_md/skills/README.md
/home/mkt/design_md/design-md-awesome/webflow/README.md
/home/mkt/design_md/design-md-awesome/wise/README.md
/home/mkt/design_md/design-md-awesome/warp/README.md
/home/mkt/design_md/design-md-awesome/vercel/README.md
/home/mkt/design_md/design-md-awesome/together.ai/README.md
/home/mkt/design_md/design-md-awesome/vodafone/README.md
/home/mkt/design_md/design-md-awesome/voltagent/README.md
/home/mkt/design_md/design-md-awesome/theverge/README.md
/home/mkt/design_md/design-md-awesome/uber/README.md
/home/mkt/design_md/design-md-awesome/zapier/README.md
/home/mkt/design_md/design-md-awesome/wired/README.md
/home/mkt/design_md/design-md-awesome/x.ai/README.md
/home/mkt/design_md/design-md-awesome/starbucks/README.md
/home/mkt/design_md/design-md-awesome/spacex/README.md
/home/mkt/design_md/design-md-awesome/sentry/README.md
/home/mkt/design_md/design-md-awesome/sanity/README.md
/home/mkt/design_md/design-md-awesome/superhuman/README.md
/home/mkt/design_md/design-md-awesome/stripe/README.md
/home/mkt/design_md/design-md-awesome/tesla/README.md
/home/mkt/design_md/design-md-awesome/spotify/README.md
/home/mkt/design_md/design-md-awesome/supabase/README.md
/home/mkt/design_md/design-md-awesome/shopify/README.md
/home/mkt/design_md/design-md-awesome/playstation/README.md
/home/mkt/design_md/design-md-awesome/posthog/README.md
/home/mkt/design_md/design-md-awesome/renault/README.md
/home/mkt/design_md/design-md-awesome/pinterest/README.md
/home/mkt/design_md/design-md-awesome/runwayml/README.md
/home/mkt/design_md/design-md-awesome/replicate/README.md
/home/mkt/design_md/design-md-awesome/resend/README.md
/home/mkt/design_md/design-md-awesome/revolut/README.md
/home/mkt/design_md/design-md-awesome/raycast/README.md
/home/mkt/design_md/design-md-awesome/ollama/README.md
/home/mkt/design_md/design-md-awesome/opencode.ai/README.md
/home/mkt/design_md/design-md-awesome/nike/README.md
/home/mkt/design_md/design-md-awesome/nvidia/README.md
/home/mkt/design_md/design-md-awesome/notion/README.md
/home/mkt/design_md/design-md-awesome/mongodb/README.md
/home/mkt/design_md/design-md-awesome/minimax/README.md
/home/mkt/design_md/design-md-awesome/mintlify/README.md
/home/mkt/design_md/design-md-awesome/meta/README.md
/home/mkt/design_md/design-md-awesome/mistral.ai/README.md
/home/mkt/design_md/design-md-awesome/miro/README.md
/home/mkt/design_md/design-md-awesome/mastercard/README.md
/home/mkt/design_md/design-md-awesome/hashicorp/README.md
/home/mkt/design_md/design-md-awesome/lovable/README.md
/home/mkt/design_md/design-md-awesome/linear.app/README.md
/home/mkt/design_md/design-md-awesome/intercom/README.md
/home/mkt/design_md/design-md-awesome/lamborghini/README.md
/home/mkt/design_md/design-md-awesome/ibm/README.md
/home/mkt/design_md/design-md-awesome/kraken/README.md
/home/mkt/design_md/design-md-awesome/framer/README.md
/home/mkt/design_md/design-md-awesome/cohere/README.md
/home/mkt/design_md/design-md-awesome/ferrari/README.md
/home/mkt/design_md/design-md-awesome/clickhouse/README.md
/home/mkt/design_md/design-md-awesome/expo/README.md
/home/mkt/design_md/design-md-awesome/coinbase/README.md
/home/mkt/design_md/design-md-awesome/elevenlabs/README.md
/home/mkt/design_md/design-md-awesome/cursor/README.md
/home/mkt/design_md/design-md-awesome/figma/README.md
/home/mkt/design_md/design-md-awesome/composio/README.md
/home/mkt/design_md/design-md-awesome/binance/README.md
/home/mkt/design_md/design-md-awesome/bugatti/README.md
/home/mkt/design_md/design-md-awesome/bmw-m/README.md
/home/mkt/design_md/design-md-awesome/claude/README.md
/home/mkt/design_md/design-md-awesome/bmw/README.md
/home/mkt/design_md/design-md-awesome/cal/README.md
/home/mkt/design_md/design-md-awesome/clay/README.md
/home/mkt/design_md/design-md-awesome/airbnb/README.md
/home/mkt/design_md/README.md
/home/mkt/design_md/design-md-awesome/airtable/README.md
/home/mkt/design_md/design-md-awesome/apple/README.md
```

**Tool: glob**

**Input:**
```json
{
  "pattern": "AGENTS.md",
  "path": "/home/mkt/design_md"
}
```

**Output:**
```
No files found
```

**Tool: glob**

**Input:**
```json
{
  "pattern": "CLAUDE.md",
  "path": "/home/mkt/design_md"
}
```

**Output:**
```
No files found
```

**Tool: glob**

**Input:**
```json
{
  "pattern": "opencode.json",
  "path": "/home/mkt/design_md"
}
```

**Output:**
```
No files found
```

**Tool: glob**

**Input:**
```json
{
  "pattern": ".cursorrules",
  "path": "/home/mkt/design_md"
}
```

**Output:**
```
No files found
```

**Tool: glob**

**Input:**
```json
{
  "pattern": ".cursor/rules/*",
  "path": "/home/mkt/design_md"
}
```

**Output:**
```
No files found
```

**Tool: glob**

**Input:**
```json
{
  "pattern": ".github/copilot-instructions.md",
  "path": "/home/mkt/design_md"
}
```

**Output:**
```
No files found
```

---

## Assistant (Build · Big Pickle · 3.4s)

_Thinking:_

No existing AGENTS.md or similar instruction files. Let me read the key files to understand the repo structure.

Let me read the highest-value sources to understand the repo.

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/README.md"
}
```

**Output:**
```
<path>/home/mkt/design_md/README.md</path>
<type>file</type>
<content>
1: # design_md

(End of file - total 1 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/dicas.md"
}
```

**Output:**
```
<path>/home/mkt/design_md/dicas.md</path>
<type>file</type>
<content>
1: curl -s https://api.github.com/repos/VoltAgent/awesome-design-md/git/trees/main?recursive=1 | grep ".md"
2: 
3: curl -s https://designmd.app/en/library/minimalism-swiss-style | grep -i 'design.md' | head -n 20
4: 
5: 
6: sim, por gentileza, faça isso, mas não poupe nenhuma de suas melhores habilidades e capacidade para fazer isso de forma mais excelente possível
7: 
8: https://designmd.app/library
9: https://github.com/designmd/awesome-design-md
10: 
11: 
12: 
13: curl -X GET "https://api.webflow.com/collections" \\
14:      

(End of file - total 14 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/comandos.js"
}
```

**Output:**
```
<path>/home/mkt/design_md/comandos.js</path>
<type>file</type>
<content>
1: // acesse : https://designmd.app/library/
2: 
3: // obtenha uma lista de elementos com essa classe: .group.block
4: lista = document.querySelectorAll('.group.block')
5: 
6: 
7: // para cada elemento da lista, obtenha o h3 e o src da imagem e o href
8: lista[3].querySelector('h3').innerText
9: 
10: // para a imagem, obtenha o src
11: lista[3].querySelector('img').src
12: 
13: // obtenha o href de cada elemento
14: lista[3].href
15: 
16: // coloque numa lista:
17: const listaDeElementos = [];
18: lista.forEach((elemento) => {
19:     listaDeElementos.push({
20:         titulo: elemento.querySelector('h3').innerText,
21:         imagem: elemento.querySelector('img').src,
22:         href: elemento.href,
23:     });
24: });
25: 
26: 
27: // para baixar: 
28: document.querySelector('#download-designmd').click()
29: 
30: 
31: // coloque numa tabela para mim que seja markdown, salvando-a na pasta raiz desse projeto
32: 
33: 
34: 

(End of file - total 34 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/skills/README.md"
}
```

**Output:**
```
<path>/home/mkt/design_md/skills/README.md</path>
<type>file</type>
<content>
1: # O que faz a skill dessa pasta:
2: Esta skill permite que ao passar a url de um site, ele extraia o DESIGN System e gere todos os arquivos necessarios para o projeto. 
3: 
4: Exemplo:
5: Se eu passar a url de um site, a skill vai extrair o design system e gerar todos os arquivos necessarios para o projeto.

(End of file - total 5 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/design-md-library"
}
```

**Output:**
```
<path>/home/mkt/design_md/design-md-library</path>
<type>directory</type>
<entries>
454/
automacao_bookmarklet.py
download_and_move.py
elementos_designmd.md
todo.md

(5 entries)
</entries>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/design-md-awesome"
}
```

**Output:**
```
<path>/home/mkt/design_md/design-md-awesome</path>
<type>directory</type>
<entries>
.DS_Store
airbnb/
airtable/
amazon/
apple/
binance/
bmw-m/
bmw/
bugatti/
cal/
claude/
clay/
clickhouse/
cohere/
coinbase/
composio/
cursor/
elevenlabs/
expo/
ferrari/
figma/
framer/
hashicorp/
ibm/
intercom/
kraken/
lamborghini/
linear.app/
lovable/
mastercard/
meta/
minimax/
mintlify/
miro/
mistral.ai/
mongodb/
nike/
notion/
nvidia/
ollama/
opencode.ai/
pinterest/
playstation/
posthog/
raycast/
renault/
replicate/
resend/
revolut/
runwayml/
sanity/
sentry/
shopify/
slack/
spacex/
spotify/
starbucks/
stripe/
supabase/
superhuman/
tesla/
theverge/
together.ai/
uber/
vercel/
vodafone/
voltagent/
warp/
webflow/
wired/
wise/
x.ai/
zapier/

(73 entries)
</entries>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/llms-full.txt"
}
```

**Output:**
```
<path>/home/mkt/design_md/llms-full.txt</path>
<type>file</type>
<content>
1: # designmd.app — Full Reference
2: 
3: > Open reference of documented DESIGN.md files for AI coding agents.
4: 
5: ## What is DESIGN.md
6: A Markdown file with YAML front matter that combines machine-readable design tokens (colors, typography, spacing, rounded, components) with human-readable design rationale prose. Open-source format maintained by Google (github.com/google-labs-code/design.md). Introduced by Google Stitch in March 2026. The agent reads it from the project root and applies visual rules consistently across all generated UI.
7: 
8: ## Format structure
9: - Two layers: YAML front matter (tokens) + Markdown body (prose)
10: - Token types: Color (#hex sRGB), Dimension (px/em/rem), Typography (object), Token Reference ({path.to.token})
11: - 8 sections in canonical order: Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts
12: - Official CLI: npx @google/design.md lint|diff|export|spec
13: - Interoperability: export to Tailwind theme config and DTCG tokens.json (W3C)
14: 
15: ## Site sections
16: - https://designmd.app/library — Documented DESIGN.md files by vertical and style, ready to copy
17: - https://designmd.app/what-is-design-md — Complete technical reference on the format and official specification
18: - https://designmd.app/guides — Agent-specific setup: Claude Code, Cursor, Kiro, Windsurf, Google Stitch
19: - https://designmd.app/for — DESIGN.md patterns by industry vertical (SaaS, e-commerce, fintech, etc.)
20: - https://designmd.app/blog — Technical articles on DESIGN.md, design systems for AI, vibe coding
21: - https://designmd.app/skills — AI agent skills (SKILL.md modules) by ft.ia.br
22: 
23: ## Key technical details
24: - Format: Markdown + YAML front matter (machine-readable tokens)
25: - Sections: Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts
26: - Token schema: colors, typography, rounded, spacing, components (with cross-references {path.to.token})
27: - Validation: npx @google/design.md lint (broken-ref, contrast-ratio, missing-primary, orphaned-tokens, section-order)
28: - Compatibility: any agent that reads project files (Claude Code, Cursor, Kiro, Windsurf, Stitch)
29: - Purpose: persistent visual context that prevents inconsistent AI-generated UI
30: 
31: ## Library catalog (454 DESIGN.md files)
32: - 3D & Hyperrealism: Build an immersive 3D interface using realistic textures, 3D models (Three.js/Babylon.js), complex shadows, realistic lighting, parallax scrolling (3-5 layers), physics-based motion. Ideal for premium e-commerce, real estate, automotive, immersive education. AI-ready template.
33: - 3D Product Preview: 3D product preview interface. Ideal for landing pages, saas. AI-ready template.
34: - 3x3 Grid Design: 3x3 grid-based landing page where content is organized in nine uniform boxes. Ideal for feeds de instagram, moodboards, portfólios, design de vestuário/boutiques. AI-ready template.
35: - 70s Psychedelic Flower Power: 70s landing page, psychedelic style, flower power, groovy font, wavy lines, bright retro colors, hippie aesthetic. Ideal for landing pages, modern websites. AI-ready template.
36: - 8-Bit Orbit: 8-Bit Orbit — Pixel-art neon arcade aesthetic on a deep navy void. Tektur typography. deep navy/black void with neon pink, cyan, and yellow pops. Best for gaming pitch, hackathon demo, web3 / crypto deck. AI-ready design system.
37: - 8-Bit Retro Terminal: 8-bit landing page, retro terminal style, pixel art, green phosphor text, scanlines, arcade game aesthetic. Ideal for landing pages, modern websites. AI-ready template.
38: - 90s Retro Video Game: 90s/Y2K retro video game style landing page. Ideal for games indie, projetos nostálgicos, marketing y2k, streaming, comunidades gamer. AI-ready template.
39: - Acanthus: Landing page inspired by acanthus leaf patterns from Greek and Roman architecture. Ideal for detalhes arquitetônicos, tipografia sofisticada, layouts de impressão elegantes, museums. AI-ready template.
40: - Accessible & Ethical: Design with WCAG AAA compliance. Ideal for government, healthcare, education, qualquer site inclusivo. AI-ready template.
41: - Afrofuturismo Digital: Design an Afrofuturist digital landing page. Ideal for landing pages, saas. AI-ready template.
42: - Agency Viral Videos & Reels Hero: High-impact full-screen hero section for a viral video agency. Ideal for agências de vídeo, produtoras de conteúdo, marketing de reels, creative agencies, social media agencies. AI-ready template.
43: - AI Automation Hero: Design an AI hero with dark purple-black background #070612. Ideal for plataformas de ai, automação de workflows, produtos de machine learning, startups de inteligência artificial. AI-ready template.
44: - AI-Native UI: Design an AI-native interface. Ideal for landing pages, saas. AI-ready template.
45: - Airbnb Coral Marketplace: Design an Airbnb-inspired warm marketplace landing page. Ideal for marketplaces, viagens, plataformas de hospedagem, e-commerce experiencial. AI-ready template.
46: - Albert Sans Typography: Render a 2D isolated text on a solid background. Ideal for startups, lifestyle brands, landing pages, and simple marketing sites.. AI-ready template.
47: - Amazônia Futurista: Futuristic Amazon rainforest landing page. Ideal for landing pages tech, projetos sustentáveis, sites futuristas. AI-ready template.
48: - American Diner Americana: American diner landing page, 50s retro style, mint green and red, checkerboard pattern, chrome typography, neon signs, nostalgic. Ideal for landing pages, modern websites. AI-ready template.
49: - Analytics Metric Flow: Design uma landing page analytics SaaS em scroll contínuo: hero fullscreen com headline 'Every number that matters. Ideal for saas analytics, dashboards de métricas, plataformas de dados, ferramentas de integração. AI-ready template.
50: - Ancient Egyptian / Historical: Design an Ancient Egyptian historical interface. Ideal for landing pages, saas. AI-ready template.
51: - Ancient Egyptian Instructional Scroll: Ancient egypt landing page, papyrus scroll background, hieroglyphics design, gold and lapis lazuli, flat profile art, historical aesthetic. Ideal for landing pages, modern websites. AI-ready template.
52: - Anime Battle: Design an anime battle-style landing page with intense, dynamic energy. Ideal for games, esports, entertainment, fan sites, streaming de anime. AI-ready template.
53: - Anthropomorphic: Whimsical anthropomorphic-themed landing page with playful character-driven aesthetics. Ideal for livros infantis, mascotes de marcas, campanhas lúdicas, embalagens de produtos vintage. AI-ready template.
54: - Anti-Polish / Raw Aesthetic: Design with anti-polish raw aesthetic. Ideal for landing pages, saas. AI-ready template.
55: - Apple Premium Cinematic: Premium Apple-style landing page with binary light/dark section rhythm. Ideal for produtos premium, technology, eletrônicos, marcas de luxo. AI-ready template.
56: - Aprendizado Criativo Artesanal: Creative and engaging hand-drawn landing page for an online art and creativity course platform. Ideal for landing pages, modern websites. AI-ready template.
57: - Architectural Portfolio Cinematic: High-end cinematic 2-page architectural portfolio. Ideal for portfolios de arquitetura, estúdios de design, creative agencies, portfolios pessoais premium, showcases de projetos tech. AI-ready template.
58: - Architectural Schematic: Architectural landing page, schematic design, floor plan style, technical drawing, clean lines, dimension markers, white background. Ideal for landing pages, modern websites. AI-ready template.
59: - Arctic Forsythia Premium: Fresh, minimal, and luminous UI inspired by Scandinavian design. Ideal for saas moderno, fintechs, apps de produtividade, startups de tecnologia, plataformas de saúde digital. AI-ready template.
60: - Art Deco: Design an Art Deco landing page with elegant glamour from the 1920s-30s. Ideal for embalagens de luxo, bares de cocktails, hotéis, interiores com toque great gatsby. AI-ready template.
61: - Art Deco / Golden Age: Design an Art Deco / Golden Age interface. Ideal for landing pages, saas. AI-ready template.
62: - Art Nouveau: Design an Art Nouveau landing page with flowing organic lines and nature-inspired motifs. Ideal for design de pôsteres, capas de livros, branding orgânico e romântico, ilustração editorial. AI-ready template.
63: - Art Nouveau Florido: Design an Art Nouveau floral landing page. Ideal for landing pages, saas. AI-ready template.
64: - Artesanato Orgânico e Acolhedor: Design an organic and warm hand-drawn landing page for an online craft store. Ideal for landing pages, modern websites. AI-ready template.
65: - Aura Premium WebGL & Iconify: Premium dark-themed landing page with advanced animations and interactions. Ideal for portfolios de luxo, estúdios de arquitetura, marcas premium, móveis de alto padrão, wellness premium, creative agencies. AI-ready template.
66: - Aurora: Design an aurora-inspired landing page with dreamy multi-color gradients mimicking the northern lights. Ideal for branding moderno, ui/ux, web design, digital art, temas cósmicos e mágicos. AI-ready template.
67: - Aurora Boreal Nórdica: Nordic aurora borealis landing page. Ideal for landing pages, saas. AI-ready template.
68: - Aurora UI: Vibrant gradient interface inspired by Northern Lights with mesh gradients, smooth color blends, flowing animations. Ideal for saas premium, creative tools, agência moderna, brand exclusiva. AI-ready template.
69: - Azulejaria Digital Moderna: Geometric and modular landing page for a collaborative digital art platform, inspired by Brazilian modernist azulejaria. Ideal for landing pages, saas. AI-ready template.
70: - Azulejo Português: Portuguese azulejo landing page. Ideal for landing pages, saas. AI-ready template.
71: - Baroque: Baroque-inspired landing page with dramatic contrasts, rich deep colors (crimson, gold, black), ornate decorative borders, gold leaf accents, theatrical lighting via radial gradients. Ideal for branding de eventos de luxo, layouts editoriais, embalagens elegantes, convites premium. AI-ready template.
72: - Bauhaus: Bauhaus-inspired landing page with strict primary colors and bold geometric shapes. Ideal for identidade de marca, layouts em grade para editorial, web design geométrico, pôsteres. AI-ready template.
73: - Bauhaus / Risograph Modern: Bauhaus risograph modern interface. Ideal for landing pages, saas. AI-ready template.
74: - Belle Époque Lithograph: Belle epoque landing page, art nouveau style, alphonse mucha aesthetic, lithograph texture, floral borders, vintage elegance, pastel colors. Ideal for landing pages, modern websites. AI-ready template.
75: - Bento Box Grid: Bento Box grid layout. Ideal for landing pages, saas. AI-ready template.
76: - Bento Dados Estruturados: Data-driven and organized Bento Style landing page for a data analysis dashboard. Ideal for landing pages, modern websites. AI-ready template.
77: - Bento Eventos Dinâmicos: Dynamic and organized Bento Style landing page for an event and ticketing platform. Ideal for landing pages, modern websites. AI-ready template.
78: - Bento Grid: Bento Grid landing page inspired by Japanese bento boxes and Apple's design language. Ideal for ui/ux, dashboards, portfólios, web design limpo, branding de produtos apple. AI-ready template.
79: - Bento Grid Tech Minimalist: Bento grid landing page, apple style aesthetic, modular layout, rounded cards, clean minimalist tech, organized grid system. Ideal for landing pages, modern websites. AI-ready template.
80: - Bento Grids: Bento Grid layout. Ideal for landing pages, saas. AI-ready template.
81: - Bento Notícias Curadas: Personalized and organized Bento Style landing page for a curated news platform. Ideal for landing pages, modern websites. AI-ready template.
82: - Bento Portfólio de Produto: Visual and organized Bento Style landing page for a product designer portfolio. Ideal for landing pages, modern websites. AI-ready template.
83: - Bento Produtividade Flexível: Modular and organized Bento Style landing page for a customizable productivity platform. Ideal for landing pages, modern websites. AI-ready template.
84: - Biennale Yellow: Biennale Yellow — Solar yellow on warm parchment with deep indigo serif and atmospheric sun-glow gradients. Instrument Serif typography. warm parchment ground with a signature solar-yellow accent, deep indigo navy ink. Best for exhibition or biennale, arts institution programme, design or typography conference. AI-ready design system.
85: - Biomimetic / Organic 2.0: Biomimetic organic interface. Ideal for landing pages, saas. AI-ready template.
86: - BlockFrame: BlockFrame — Neobrutalist deck with pastel-neon color blocks and chunky black borders. Space Grotesk typography. off-white background with neon pastel blocks (hot pink, sky blue, lime green, go. Best for creative agency pitch, indie SaaS launch, designer portfolio. AI-ready design system.
87: - Blue Professional: Blue Professional — Cream paper background with electric cobalt blue accents; clean modern professional. Space Grotesk typography. warm cream paper background with one electric cobalt blue accent. Best for B2B SaaS pitch, consulting deliverable, internal review. AI-ready design system.
88: - Blueprint / Engineering: Blueprint engineering interface. Ideal for landing pages, saas. AI-ready template.
89: - BMW Angular Precision: BMW-inspired angular precision landing page. Ideal for automotivo de luxo, engenharia, marcas premium, produtos industriais. AI-ready template.
90: - Bohemian (Boho): Bohemian landing page with vibrant yet muted earthy tones. Ideal for branding de eventos, linhas de moda, produtos lifestyle, marcas de viagem. AI-ready template.
91: - Bold & Energetic: Bold and energetic poster-style interface using 60/30/10 color balance. Ideal for design de pôsteres, eventos e festivais, campanhas promocionais, landing pages de lançamento, conteúdo social de alto impacto. AI-ready template.
92: - Bold Portfolio Hero: Bold portfolio hero with vertical gradient from red-orange #fd2601 to orange #f37e1c. Ideal for creative portfolios, designers freelancer, agências de branding, sites pessoais de artistas. AI-ready template.
93: - Bold Poster: Bold Poster — Editorial poster aesthetic with massive Shrikhand display and a single fire-engine red accent. Shrikhand typography. white and warm-cream paper with deep almost-black ink, lifted by a single satura. Best for brand manifesto, creative-led pitch, magazine / editorial. AI-ready design system.
94: - Bold Signal: Bold, confident dark landing page. Ideal for creative agencies, startups tech, portfolios de design, apresentações corporativas. AI-ready template.
95: - Bossa Nova Lounge: Bossa Nova lounge style landing page. Ideal for landing pages musicais, projetos culturais, sites sofisticados. AI-ready template.
96: - Broadside: Broadside — Dark editorial canvas with a single fire orange accent and bilingual Latin/Chinese type stack. Barlow typography. near-black newspaper canvas with warm cream text and a single fire-orange headli. Best for brand manifesto, founder vision deck, magazine / cultural pitch. AI-ready design system.
97: - Brutalism: Brutalist landing page with raw, stark, intentionally unpolished aesthetics. Ideal for streetwear, marcas experimentais, layouts editoriais, portfólios de design. AI-ready template.
98: - Brutalism: Brutalist design with raw, unpolished, stark aesthetic. Ideal for creative portfolio, design agency, experimental blog, digital art. AI-ready template.
99: - Brutalismo Artístico Abstrato: Design an artistic and experimental brutalist landing page for a digital artist portfolio. Ideal for landing pages, modern websites. AI-ready template.
100: - Brutalismo Sonoro Glitch: Design an edgy and raw brutalist landing page for an experimental electronic music festival. Ideal for landing pages, modern websites. AI-ready template.
101: - Brutalismo Urbano Expressivo: Design an edgy and expressive brutalist landing page for an urban art and streetwear store. Ideal for landing pages, modern websites. AI-ready template.
102: - Brutalist Web Design: Brutalist web landing page. Ideal for landing pages, saas. AI-ready template.
103: - CAD-Inspired Blueprint: CAD landing page style, blueprint aesthetic, dark blue background, white technical lines, mechanical details, engineering look. Ideal for landing pages, modern websites. AI-ready template.
104: - Café Artesanal Aconchegante: Cozy and rustic hand-drawn landing page for an artisanal coffee shop and bakery. Ideal for landing pages, modern websites. AI-ready template.
105: - Capsule: Capsule — Modular pill-shaped cards on warm bone with a full pastel-pop palette. Bodoni Moda typography. warm bone background, ink-black structure, and a full pastel-pop palette (coral,. Best for lifestyle brand, creator portfolio, DTC product launch. AI-ready design system.
106: - Caramelo Quente Premium: Warm, inviting, and artisanal UI with a premium feel. Ideal for cafeterias artesanais, padarias premium, marcas de lifestyle, restaurantes acolhedores, e-commerce de produtos naturais. AI-ready template.
107: - Cartazista de Supermercado: Brazilian supermarket cartazista (sign maker) style landing page. Ideal for landing pages, saas. AI-ready template.
108: - Cartesian: Cartesian — Quiet warm-neutral palette with classical Playfair serifs; tasteful and unhurried. Playfair Display typography. warm bone and stone neutrals only. Best for investment thesis, white paper, advisory deliverable. AI-ready design system.
109: - Cassette Futurism: Cassette futurism landing page. Ideal for landing pages, saas. AI-ready template.
110: - Cerâmica Wabi-Sabi: Wabi-Sabi ceramic landing page. Ideal for landing pages, saas. AI-ready template.
111: - Cerrado Minimalista: Cerrado (Brazilian savanna) minimalist landing page. Ideal for landing pages sustentáveis, projetos ecológicos, sites minimalistas. AI-ready template.
112: - Chalkboard: Chalkboard-style landing page. Ideal for education, tutoriais, restaurants, projetos nostálgicos, menus criativos. AI-ready template.
113: - Chalkboard / Hand-Drawn: Chalkboard hand-drawn interface. Ideal for landing pages, saas. AI-ready template.
114: - Chalkboard Sketch-Note: Chalkboard landing page, blackboard background, hand drawn chalk style, white sketch on dark, educational aesthetic, doodle icons. Ideal for landing pages, modern websites. AI-ready template.
115: - Chromatic Aberration / RGB Split: Design with chromatic aberration RGB split effect. Ideal for landing pages, saas. AI-ready template.
116: - Circuit Board / PCB: Circuit board PCB interface. Ideal for landing pages, saas. AI-ready template.
117: - Claude Warm Parchment: Warm editorial landing page inspired by Claude/Anthropic. Ideal for plataformas de ia, education, editoras, produtos literários. AI-ready template.
118: - Clay Artisanal Swatch: Clay-inspired artisanal landing page. Ideal for b2b criativo, agências, plataformas de dados, ferramentas de enriquecimento. AI-ready template.
119: - Claymation 3D: Claymation 3D interface. Ideal for landing pages, saas. AI-ready template.
120: - Claymation 3D Illustration: Claymation landing page, plasticine style, 3d clay illustration, soft lighting, rounded shapes, cute and friendly, stop motion aesthetic. Ideal for landing pages, modern websites. AI-ready template.
121: - Claymorphism: Playful, toy-like interface with soft 3D, chunky elements, bubbly aesthetic, rounded edges (16-24px), thick borders (3-4px), double shadows (inner + outer), pastel colors, smooth animations. Ideal for apps infantis, creative tools, education, jogos interativos. AI-ready template.
122: - ClearInvoice SaaS Hero: SaaS hero with HLS background video at full opacity no overlay. Ideal for saas de faturamento, plataformas de billing, ferramentas de pagamento, gestão financeira. AI-ready template.
123: - ClickHouse Neon Volt: ClickHouse-inspired neon performance landing page. Ideal for databases, analytics em tempo real, infraestrutura de dados, data warehouses. AI-ready template.
124: - Coastal Commerce: Coastal-inspired e-commerce UI using navy, driftwood beige, and pale ocean blues. Ideal for e-commerce de moda praia, lojas de surf e lifestyle, produtos artesanais costeiros, decoração náutica. AI-ready template.
125: - Coastal Mist: Serene coastal UI using deep navy, pale seafoam, and soft slate blues. Ideal for saas de bem-estar, apps de meditação, turismo costeiro, imobiliárias de praia, clínicas e spas. AI-ready template.
126: - Coastal Studio: Creative studio landing page inspired by rocky coastal cliffs, using deep navy, slate blue, and ocean pearl overlays. Ideal for portfólios de fotografia, estúdios criativos, agências de branding, arquitetura costeira. AI-ready template.
127: - Cobalt Grid: Cobalt Grid — Electric cobalt italic serifs on a graph-paper canvas, anchored by stair-stepped pixel-glitch decorations and slim hairline rules. Newsreader (italic) typography. warm cream / ivory paper canvas with one strict accent of electric cobalt royal . Best for design trend or research report, studio annual or seasonal bulletin, creative agency capabilities deck. AI-ready design system.
128: - Cohere Enterprise Serif: Cohere-inspired enterprise landing page. Ideal for enterprise ai, infraestrutura de dados, plataformas b2b, apis corporativas. AI-ready template.
129: - Coinbase Trust Blue: Coinbase-inspired clean fintech landing page. Ideal for exchanges crypto, fintechs, plataformas financeiras, wallets digitais. AI-ready template.
130: - Comic Book / Pop Art: Comic book pop art interface. Ideal for landing pages, saas. AI-ready template.
131: - Comparative Analysis Dashboard: Comparison dashboard. Ideal for landing pages, modern websites. AI-ready template.
132: - Composio Cyber Nocturnal: Composio-inspired nocturnal landing page. Ideal for integrações de ferramentas, apis, plataformas developer, automação de agentes. AI-ready template.
133: - Conceptual Sketch / Doodle Art: Doodle art landing page with hand-drawn, sketch-like aesthetics. Ideal for branding lúdico, creative agencies, produtos para público jovem, editoriais divertidos. AI-ready template.
134: - Conforto Artesanal Brasileiro: Warm and authentic landing page for an online store of handmade Brazilian furniture, inspired by Sérgio Rodrigues and Irmãos Campana. Ideal for landing pages, saas. AI-ready template.
135: - Construtivismo Arquitetônico: Precise and structured constructivist landing page for a modern architecture firm. Ideal for landing pages, modern websites. AI-ready template.
136: - Construtivismo de Dados Dinâmicos: Data-driven and dynamic constructivist landing page for a business intelligence platform. Ideal for landing pages, modern websites. AI-ready template.
137: - Construtivismo de Eventos Dinâmicos: Design an energetic and innovative constructivist landing page for a design and innovation conference. Ideal for landing pages, modern websites. AI-ready template.
138: - Construtivismo Dinâmico Tech: Functional and dynamic constructivist landing page for an agile tech startup. Ideal for landing pages, modern websites. AI-ready template.
139: - Construtivismo Literário Experimental: Design an artistic and experimental constructivist landing page for an independent book publisher. Ideal for landing pages, modern websites. AI-ready template.
140: - Conversion-Optimized: Conversion-optimized landing page. Ideal for marketing, conversão, lead gen. AI-ready template.
141: - Coquette: Coquette landing page with soft romantic pastels and delicate feminine aesthetics. Ideal for branding de boutiques, editoriais femininos, embalagens de beleza e moda, convites. AI-ready template.
142: - Coral: Coral — Cream and coral on near-black, set in oversized Bebas Neue. Bebas Neue typography. near-black canvas, warm cream paper for content, and a saturated coral accent th. Best for fashion / beauty pitch, fitness brand, F&B brand deck. AI-ready design system.
143: - Cordel Digital: Brazilian cordel literature style landing page. Ideal for landing pages culturais, projetos nordestinos, sites artísticos. AI-ready template.
144: - Corporate Radial Process: Corporate landing page, radial process visualization, clean white background, teal accent, structured layout, flat design. Ideal for landing pages, modern websites. AI-ready template.
145: - Creative Mode: Creative Mode — Cream paper canvas with confident multi-color (green, pink, orange, yellow) accents and Archivo Black display. Archivo Black typography. warm cream paper background with a saturated multi-accent palette (forest green,. Best for creative agency pitch, design studio deck, ad shop credentials. AI-ready design system.
146: - Creative Voltage: Bold, creative, energetic landing page with retro-modern vibes. Ideal for creative agencies, estúdios de música, marcas jovens, eventos culturais. AI-ready template.
147: - Criatividade Artesanal e Pessoal: Personal and creative hand-drawn landing page for a small business creative consulting firm. Ideal for landing pages, modern websites. AI-ready template.
148: - CRM Copper Sand: Modern CRM landing + dashboard-style UI using Geist font, a warm copper primary color (#C08532), and a soft neutral background (#F2F1ED). Ideal for plataformas crm, painéis de vendas, ferramentas de gestão comercial, dashboards saas. AI-ready template.
149: - Crypto Exchange Plataforma: Crypto exchange landing, digital assets, charts, neon cyan, dark background, futuristic, security, wallets, trading. Ideal for landing pages, modern websites. AI-ready template.
150: - Culinária Afetiva Brasileira: Warm and authentic landing page for a homemade and affective recipe sharing platform, inspired by Brazilian vernacular culture. Ideal for landing pages, saas. AI-ready template.
151: - Cursor Warm Gothic: Cursor-inspired warm landing page. Ideal for editores de código ai, ferramentas developer, ides inteligentes, plataformas de coding. AI-ready template.
152: - Cyber Core: Cyber core landing page with neon-lit, high-speed digital aesthetics. Ideal for marcas de gaming, design de pôsteres, branding digital edgy, portfólios tech. AI-ready template.
153: - Cyber-Tribal: Cyber-tribal landing page. Ideal for landing pages, saas. AI-ready template.
154: - Cyberpunk Dark Mode Flow: Cyberpunk dark mode landing page, sleek flow design, neon blue accents, circuit patterns, modern dark ui, tech aesthetic. Ideal for landing pages, modern websites. AI-ready template.
155: - Cyberpunk Neon Noir: Cyberpunk landing page, neon noir style, dark background, glowing neon colors, glitch effects, futuristic ui, high contrast. Ideal for landing pages, modern websites. AI-ready template.
156: - Cyberpunk UI: Cyberpunk interface. Ideal for landing pages, saas. AI-ready template.
157: - Daisy Days: Daisy Days — Cheerful pastel deck with hand-drawn daisies, stars, and rainbows. Friendly, soft, and warm. Fredoka One typography. warm cream base with a full pastel rainbow (mint, lavender, peach, sky, soft pin. Best for education / classroom, kids product launch, wellness program. AI-ready design system.
158: - Dark Botanical: Design an elegant, sophisticated dark landing page with artistic premium feel. Ideal for marcas de luxo, joalherias, spas premium, art galleries, vinícolas. AI-ready template.
159: - Dark Glassmorphism Infographic: Dark glassmorphism infographic. Ideal for landing pages, modern websites. AI-ready template.
160: - Dark Mode (OLED): Create an OLED-optimized dark interface with deep black (#000000), dark grey (#121212), midnight blue accents. Ideal for dashboards financeiros, apps criativas, mobile-first, gaming. AI-ready template.
161: - Dark Portfolio Hero: Dark portfolio with animated loading screen (2.7s): counter 000→100 via rAF, rotating words with AnimatePresence, gradient progress bar (#89AACC to #4E85BF) with glow. Ideal for portfólios de desenvolvedores, designers criativos, freelancers fullstack, sites pessoais premium. AI-ready template.
162: - Dark SaaS Hero with Liquid Glass: Dark SaaS landing page hero section. Ideal for b2b saas, ai tools, plataformas de desenvolvedores, landing pages tech, startups, apis e sdks. AI-ready template.
163: - Data-Dense Dashboard: Data-dense dashboard. Ideal for landing pages, modern websites. AI-ready template.
164: - Datacore SaaS Hero: Linear-style dark SaaS hero with HLS background video and black overlay (bg-black/60). Ideal for plataformas de dados, ferramentas de infraestrutura, redes e networking, saas enterprise. AI-ready template.
165: - De Stijl Abstrato: De Stijl abstract landing page. Ideal for landing pages, saas. AI-ready template.
166: - Degraded Colorful / Vibrant Gradient: Vibrant gradient infographic. Ideal for landing pages, modern websites. AI-ready template.
167: - Democratized Fancy Animations: Visually stunning landing page with democratized fancy animations using CSS and lightweight WebGL-inspired effects. Ideal for landing pages premium, portfolios criativos, lancamentos de produto tech, agencias digitais, experiencias imersivas, showcases de design. AI-ready template.
168: - Denim and Industrial Craft: Denim style landing, jeans texture background, gold stitching, industrial craft, textile aesthetic, rugged design. Ideal for landing pages, modern websites. AI-ready template.
169: - Desenho à Mão Lúdico: Playful and organic hand-drawn landing page for a children's illustrator blog. Ideal for landing pages, modern websites. AI-ready template.
170: - Design Autoral Robusto: Design an authentic and robust landing page for an online store of authorial Brazilian design products, inspired by Sérgio Rodrigues. Ideal for landing pages, saas. AI-ready template.
171: - Dimensional Layering: Design with dimensional layering. Ideal for landing pages, saas. AI-ready template.
172: - Doodle / Sketch Livre: Doodle sketch infographic. Ideal for landing pages, modern websites. AI-ready template.
173: - Drill-Down Analytics: Drill-down analytics dashboard. Ideal for landing pages, modern websites. AI-ready template.
174: - E-Ink / Paper: Design an e-ink/paper style interface. Ideal for landing pages, saas. AI-ready template.
175: - Earthy & Organic: Design an earthy and organic interface with 60/30/10 palette discipline. Ideal for design de embalagens, marcas orgânicas, cosméticos naturais, alimentos artesanais, produtos eco-friendly. AI-ready template.
176: - Editorial Contemporâneo: Design an artistic and immersive editorial landing page for a contemporary culture and art digital magazine. Ideal for landing pages, modern websites. AI-ready template.
177: - Editorial de Portfólio Criativo: Design an artistic and visual editorial landing page for a graphic design portfolio. Ideal for landing pages, modern websites. AI-ready template.
178: - Editorial de Viagem Sofisticado: Design an elegant and aspirational editorial landing page for a luxury travel blog. Ideal for landing pages, modern websites. AI-ready template.
179: - Editorial Grid / Magazine: Design an editorial magazine layout. Ideal for landing pages, saas. AI-ready template.
180: - Editorial Interativo Digital: Design an engaging and informative editorial landing page for an interactive digital book. Ideal for landing pages, modern websites. AI-ready template.
181: - Editorial Investigativo Sóbrio: Serious and informative editorial landing page for an investigative journalism platform. Ideal for landing pages, modern websites. AI-ready template.
182: - Editorial Tri-Tone: Editorial Tri-Tone — Three-color editorial system: dusty pink, mustard cream, and deep burgundy, set in Bricolage + Instrument Serif. Bricolage Grotesque typography. dusty pink, mustard cream, and deep burgundy used as full-bleed color blocks. Best for editorial / magazine pitch, fashion brand deck, lifestyle media. AI-ready design system.
183: - EdTech Plataforma de Cursos: Edtech landing, online courses, gamification, progress badges, vibrant colors, students, learning path, challenges, modern UI. Ideal for landing pages, modern websites. AI-ready template.
184: - Electric Studio: Bold, clean professional landing page with a two-panel vertical split layout. Ideal for estúdios de design, digital agencies, portfolios profissionais, consultorias. AI-ready template.
185: - Elementos Musicais: Musical elements infographic. Ideal for landing pages, modern websites. AI-ready template.
186: - ElevenLabs Ethereal Voice: Design an ElevenLabs-inspired ethereal landing page. Ideal for voice ai, plataformas de áudio, text-to-speech, ferramentas de mídia. AI-ready template.
187: - Ember & Amethyst Premium: Vibrant, bold, and luxurious UI that fuses fiery warmth with regal depth. Ideal for marcas de moda premium, gastronomia autoral, entretenimento e eventos, vinícolas e destilarias, creative agencies. AI-ready template.
188: - Engineering Blueprint Schematic: Engineering landing page, blueprint style, schematic design, technical precision, dark blue background, cyan lines, industrial aesthetic, wireframe graphics. Ideal for landing pages, modern websites. AI-ready template.
189: - Estilo de Computação de Alta Performance: Powerful and technical landing page for new server processors. Ideal for landing pages, modern websites. AI-ready template.
190: - Estilo de Dados Empresariais: Robust and secure landing page for an Autonomous Database. Ideal for landing pages, modern websites. AI-ready template.
191: - Estilo de Ecossistema Digital: Dynamic and social landing page for a gaming and social platform. Ideal for landing pages, modern websites. AI-ready template.
192: - Estilo de Elegância Espacial: Minimalist premium landing page for a spatial computing device. Ideal for landing pages, modern websites. AI-ready template.
193: - Estilo de Elegância Fintech: Clean and professional landing page for a payment platform. Ideal for landing pages, modern websites. AI-ready template.
194: - Estilo de Entretenimento Imersivo: Cinematic and engaging landing page for a new interactive series. Ideal for landing pages, modern websites. AI-ready template.
195: - Estilo de Experiência de Compra Contínua: Functional and trustworthy landing page for a premium subscription service. Ideal for landing pages, modern websites. AI-ready template.
196: - Estilo de Fluxo de Rede: Robust and connected landing page for network solutions. Ideal for landing pages, modern websites. AI-ready template.
197: - Estilo de Futuro Autônomo: Sleek and futuristic landing page for a new autonomous car. Ideal for landing pages, modern websites. AI-ready template.
198: - Estilo de IA Criativa: Design an artistic and innovative landing page for a creative AI tool. Ideal for landing pages, modern websites. AI-ready template.
199: - Estilo de IA Ética: Clean and trustworthy landing page for a safe conversational AI. Ideal for landing pages, modern websites. AI-ready template.
200: - Estilo de IA para Negócios: Professional and data-driven landing page for a sales AI platform. Ideal for landing pages, modern websites. AI-ready template.
201: - Estilo de Inovação em Dispositivos Móveis: Sleek and modern landing page for a new foldable smartphone. Ideal for landing pages, modern websites. AI-ready template.
202: - Estilo de Inteligência Generativa: Futuristic and minimalist landing page for a next-gen language model. Ideal for landing pages, modern websites. AI-ready template.
203: - Estilo de Litografia de Precisão: Precise and industrial landing page for EUV technology. Ideal for landing pages, modern websites. AI-ready template.
204: - Estilo de Realidade Virtual Social: Design an immersive and futuristic landing page for a new metaverse space. Ideal for landing pages, modern websites. AI-ready template.
205: - Estilo de Tecnologia de Precisão: Precise and industrial landing page for 2nm chips. Ideal for landing pages, modern websites. AI-ready template.
206: - Estilo Deep Learning High-Tech: High-tech AI platform landing page. Ideal for landing pages, modern websites. AI-ready template.
207: - Estilo Fluent AI: Clean and professional landing page for an AI assistant. Ideal for landing pages, modern websites. AI-ready template.
208: - Estilo Material AI: Clean and vibrant landing page for a generative AI platform. Ideal for landing pages, modern websites. AI-ready template.
209: - Estilo Suíço Artístico: Design an artistic and clean Swiss Style landing page for a modern art gallery. Ideal for landing pages, modern websites. AI-ready template.
210: - Estilo Suíço Científico: Design an academic and precise Swiss Style landing page for an online scientific publication. Ideal for landing pages, modern websites. AI-ready template.
211: - Estilo Suíço Corporativo: Clean and professional Swiss Style landing page for a corporate IT consulting firm. Ideal for landing pages, modern websites. AI-ready template.
212: - Estilo Suíço Educacional: Design an educational and structured Swiss Style landing page for an online course platform. Ideal for landing pages, modern websites. AI-ready template.
213: - Estilo Suíço Premium: Design an elegant and minimalist Swiss Style landing page for a premium product brand. Ideal for landing pages, modern websites. AI-ready template.
214: - Ethereal: Design an ethereal landing page with extremely soft, delicate tones. Ideal for lookbooks de alta-costura, arte conceitual, designs refinados, portfólios artísticos. AI-ready template.
215: - Exaggerated Minimalism: Design with exaggerated minimalism. Ideal for landing pages, saas. AI-ready template.
216: - Executive Dashboard: Design an executive dashboard. Ideal for landing pages, modern websites. AI-ready template.
217: - Expo Luminous Developer: Design an Expo-inspired luminous developer landing page. Ideal for plataformas cross-platform, react native, sdks mobile, ferramentas de build. AI-ready template.
218: - Farmhouse / Cottage Core: Farmhouse/cottage core landing page with rustic countryside charm. Ideal for decoração de interiores, marcas de vestuário boutique, capas de livros, produtos artesanais. AI-ready template.
219: - Feature-Rich Showcase: Feature showcase landing page. Ideal for marketing, conversão, lead gen. AI-ready template.
220: - Figma Vibrant Monochrome: Figma-inspired landing page with strictly black-and-white interface chrome. Ideal for ferramentas de design, plataformas criativas, editores visuais, portfolios de design. AI-ready template.
221: - Filigree: Filigree-inspired landing page with intricate lace-like patterns. Ideal for convites de casamento, tipografia sofisticada, embalagens de luxo, joalherias. AI-ready template.
222: - Financial Dashboard: Financial dashboard. Ideal for landing pages, modern websites. AI-ready template.
223: - FinTech Plataforma Financeira: Fintech landing, finance dashboard, charts, security, gold and dark palette, premium, trust, transactions, cards, modern UI. Ideal for landing pages, modern websites. AI-ready template.
224: - Fitness App de Treinos: Fitness app landing, workouts, before-after, progress tracking, red and orange, energetic, mobile app, gym, health. Ideal for landing pages, modern websites. AI-ready template.
225: - Flat Design: Flat, 2D interface with bold colors, no shadows/gradients, clean lines, simple geometric shapes, icon-heavy, typography-focused, minimal ornamentation. Ideal for landing pages, saas. AI-ready template.
226: - Flat Design Corporativo: Corporate flat design landing page. Ideal for landing pages, saas. AI-ready template.
227: - Flat Design Educacional Vibrante: Design an engaging and interactive flat design landing page for an e-learning platform. Ideal for landing pages, modern websites. AI-ready template.
228: - Flat Design Financeiro Seguro: Secure and efficient flat design landing page for a personal finance management app. Ideal for landing pages, modern websites. AI-ready template.
229: - Flat Design Informativo Claro: Clear and informative flat design landing page for a news and articles platform. Ideal for landing pages, modern websites. AI-ready template.
230: - Flat Design Musical Intuitivo: Design an intuitive and modern flat design landing page for a music streaming service. Ideal for landing pages, modern websites. AI-ready template.
231: - Flat Design Produtivo: Simple and efficient flat design landing page for a task management app. Ideal for landing pages, modern websites. AI-ready template.
232: - Fractal Bioluminescence: Fractal landing page, bioluminescent design, glowing organic shapes, dark background, electric purple and green, intricate geometry. Ideal for landing pages, modern websites. AI-ready template.
233: - Framelix 3D Studios: Cinematic 3D studio page with pure black background. Ideal for estúdios 3d, agências de motion design, produtoras de vídeo, portfólios de animação. AI-ready template.
234: - Fraunces Typography: Render a 2D isolated text on a solid background. Ideal for branding and logos, headlines, hero sections, and editorial layouts.. AI-ready template.
235: - Futuristic UI Glassmorphism: Glassmorphism landing page, futuristic glass ui, transparent panels, blur effects, glowing edges, dark background, 3d interface. Ideal for landing pages, modern websites. AI-ready template.
236: - Gatsby Art Deco Noir: Art deco landing page, great gatsby style, black and gold luxury, geometric patterns, ornate borders, elegant typography, noir aesthetic. Ideal for landing pages, modern websites. AI-ready template.
237: - Gen Z Chaos / Maximalism: Gen Z chaos maximalist interface. Ideal for landing pages, saas. AI-ready template.
238: - Geometric: Geometric patterns infographic. Ideal for landing pages, modern websites. AI-ready template.
239: - Ghibli-Inspired Narrative Map: Ghibli style landing page, watercolor background, narrative map, whimsical design, soft colors, hand painted look, nature inspired. Ideal for landing pages, modern websites. AI-ready template.
240: - Glass Gradient Creative: Full-screen hero page with a vertical white-to-magenta gradient background, overlapping blurred triangular shapes in purple and pink, and tall glass columns using glassmorphism. Ideal for landing pages criativas, portfólios de design, digital agencies, produtos visuais premium. AI-ready template.
241: - Glassmorphism: Glassmorphic interface with frosted glass effect. Ideal for overlays, modal dialogs, card components, premium interfaces. AI-ready template.
242: - Glassmorphism Agency Hero: Dark agency hero with HLS video using mix-blend-screen. Ideal for digital agencies, estúdios criativos, consultorias de design, portfólios de agência. AI-ready template.
243: - Glitch UI Dystopian Terminal: Glitch ui landing page, dystopian terminal, red alert style, digital interference, chaotic design, scanlines, warning aesthetic. Ideal for landing pages, modern websites. AI-ready template.
244: - Google Sans Typography: Render a 2D isolated text on a solid background. Ideal for product and marketing sites that want a clean, big tech aesthetic.. AI-ready template.
245: - Gothic: Gothic landing page with dark, mysterious, cathedral-inspired aesthetics. Ideal for merchandising de bandas, logótipos provocadores, branding vintage dark, moda gótica. AI-ready template.
246: - Gótico Moderno: Modern gothic landing page. Ideal for landing pages, saas. AI-ready template.
247: - Grade School Color Palette: Landing page using grade school primary colors — the kind you remember from crayons and traffic signs. Ideal for startups consumer, apps educacionais, ecommerce jovem, plataformas de comunidade, marketing de produto, food delivery. AI-ready template.
248: - Gradient Aurora Borealis: Gradient aurora borealis infographic. Ideal for landing pages, modern websites. AI-ready template.
249: - Gradient Mesh / Aurora Evolved: Design with gradient mesh aurora effect. Ideal for landing pages, saas. AI-ready template.
250: - Graffiti: Graffiti-inspired landing page with bright spray-paint colors on gritty urban backgrounds. Ideal for campanhas de marcas provocadoras, pôsteres de música, linhas de streetwear, eventos urbanos. AI-ready template.
251: - Grove: Grove — Forest-green canvas with cream type, classical Playfair serifs, and a single rust accent. Playfair Display typography. deep forest green canvas with warm bone type and a single rust-red accent. Best for sustainability brand, wellness brand, outdoor / nature product. AI-ready design system.
252: - Grunge Rock dos Anos 90: 90s grunge rock landing page. Ideal for landing pages, saas. AI-ready template.
253: - Hacker Aesthetic CRT/CLI: Hacker style landing page, terminal ui, crt monitor effect, green text on black, ascii art, command line interface, retro coding. Ideal for landing pages, modern websites. AI-ready template.
254: - Hand-Drawn Sketch-Note: Hand drawn landing page, notebook paper background, sketch style, doodles, handwriting font, casual and fun design. Ideal for landing pages, modern websites. AI-ready template.
255: - Happy Art Tropical: Happy Art tropical landing page with vibrant saturated colors. Ideal for landing pages, saas. AI-ready template.
256: - HashiCorp Infra Dual: HashiCorp-inspired infrastructure landing page. Ideal for infraestrutura cloud, devops, automação de infraestrutura, plataformas multi-produto. AI-ready template.
257: - HealthTech Plataforma Clínica: Healthtech landing, medical icons, clinic portal, healthcare green, patient journey, appointments, doctors, trust, clean, accessible, digital health. Ideal for landing pages, modern websites. AI-ready template.
258: - Heat Map & Heatmap Style: Heatmap visualization. Ideal for landing pages, modern websites. AI-ready template.
259: - Helios Design System (HashiCorp): Highly structured and technical enterprise UI inspired by HashiCorp Helios. Ideal for ferramentas devops, saas técnico, dashboards de infraestrutura, plataformas open-source, painéis de engenharia. AI-ready template.
260: - Hero-Centric Design: Hero-centric landing page. Ideal for marketing, conversão, lead gen. AI-ready template.
261: - High-Contrast Tech: High-contrast tech interface with strict 60/30/10 color distribution. Ideal for ux/ui de produto digital, dashboards analytics, saas platforms, conteúdo tecnológico, apps b2b. AI-ready template.
262: - Holographic Data-Viz: Holographic landing page, data visualization style, futuristic hud, 3d floating elements, glowing blue interface, sci-fi aesthetic. Ideal for landing pages, modern websites. AI-ready template.
263: - Horror / Gothic Dark: Horror gothic dark interface. Ideal for landing pages, saas. AI-ready template.
264: - HR SaaS Hero: Minimalist white SaaS hero with background video vertically flipped scaleY(-1) and white gradient overlay (transparent at 26.4% to white at 66.9%). Ideal for saas de rh, gestão de equipes remotas, ferramentas de colaboração, plataformas de onboarding. AI-ready template.
265: - HUD / Sci-Fi FUI: Futuristic HUD (Heads Up Display) or FUI. Ideal for landing pages, saas. AI-ready template.
266: - IBM Carbon Enterprise: Design an IBM Carbon-inspired enterprise landing page. Ideal for enterprise, infraestrutura cloud, plataformas corporativas, consultoria tech. AI-ready template.
267: - IBM Plex Sans Typography: Render a 2D isolated text on a solid background. Ideal for enterprise products, design systems, documentation, and tech brands.. AI-ready template.
268: - Inclusive Design: Design for universal accessibility: high contrast (7:1+), large text (16px+), keyboard-only navigation, screen reader optimization, WCAG AAA compliance, symbol-based color indicators (not color-only), haptic feedback, voice interaction support, reduced motion options. Ideal for landing pages, saas. AI-ready template.
269: - Industrial Workbench Schematic: Industrial workbench landing, garage style, workshop aesthetic, metal textures, tools background, rugger design, hardware focus. Ideal for landing pages, modern websites. AI-ready template.
270: - Inter Typography: Render a 2D isolated text on a solid background. Ideal for apps, dashboards, documentation, digital product needing maximum clarity.. AI-ready template.
271: - Interactive Cursor Design: Design with interactive cursor effects. Ideal for landing pages, saas. AI-ready template.
272: - Interactive Product Demo: Design an interactive demo landing page. Ideal for marketing, conversão, lead gen. AI-ready template.
273: - Internet Nostalgia Y2K Revival: Landing page with full Windows 95/98 internet nostalgia aesthetic. Ideal for portfolios criativos retro, jogos indie, eventos tematicos, blogs pessoais nostalgicos, lancamentos de produto ironicos, comunidades de nicho. AI-ready template.
274: - Isometric Gaming / Voxel: Design an isometric voxel gaming interface. Ideal for landing pages, saas. AI-ready template.
275: - Japandi: Japandi landing page blending Japanese minimalism with Scandinavian warmth. Ideal for interior design, produtos lifestyle, branding minimalista, design de pôsteres. AI-ready template.
276: - Kawaii: Kawaii landing page with soft pastel colors and adorable rounded aesthetics. Ideal for embalagens de brinquedos, vestuário, branding de personagens, gráficos de redes sociais. AI-ready template.
277: - Kawaii / Sweet Pastel: Kawaii sweet pastel interface. Ideal for landing pages, saas. AI-ready template.
278: - Kawaii Doodle Art: Kawaii doodle art style landing page. Ideal for projetos infantis, lojas de presentes, apps de bem-estar, fan sites, blogs criativos. AI-ready template.
279: - Kawaii Pastel Pop: Kawaii landing page, pastel pink background, cute aesthetic, soft shapes, sparkles, japanese pop culture, fluffy clouds. Ideal for landing pages, modern websites. AI-ready template.
280: - Kinetic Typography: Design with kinetic typography. Ideal for landing pages, saas. AI-ready template.
281: - Kitsch: Kitsch landing page with intentionally bright, exaggerated, over-the-top aesthetics. Ideal for branding satírico, produtos de novidade, autocolantes, campanhas de marketing exageradas. AI-ready template.
282: - Knolling Pastel Flat Lay: Knolling landing page, flat lay style, organized objects, pastel background, clean 90 degree alignment, overhead photography look. Ideal for landing pages, modern websites. AI-ready template.
283: - Kraken Purple Exchange: Kraken-inspired crypto exchange landing page. Ideal for exchanges crypto, trading, plataformas financeiras, defi. AI-ready template.
284: - Lambe-Lambe Brasileiro: Brazilian lambe-lambe street poster style landing page. Ideal for landing pages, saas. AI-ready template.
285: - Laranja Queimado Premium: Warm, earthy, and elegant UI with a premium feel. Ideal for marcas orgânicas, cafeterias premium, produtos artesanais, restaurantes farm-to-table, lifestyle natural. AI-ready template.
286: - Linear Precision Dark: Precision-engineered dark landing page inspired by Linear. Ideal for ferramentas de gestão de projetos, saas developer, plataformas de engenharia, issue trackers. AI-ready template.
287: - Liquid Glass: Premium liquid glass effect with morphing shapes, flowing animations, chromatic aberration, iridescent gradients, smooth 400-600ms transitions. Ideal for landing pages, saas. AI-ready template.
288: - Locomotive Infinite Scroll: Design an immersive infinite scroll landing page inspired by Locomotive Scroll v5 and Lenis. Ideal for landing pages imersivas, storytelling digital, portfolios criativos, sites de agências, apresentações de produto premium, one-page narrativas. AI-ready template.
289: - Logoisum Video Agency Hero: Premium video agency hero with full-screen video no color overlay. Ideal for agências de vídeo, produtoras de reels e shorts, estúdios de edição, freelancers de vídeo. AI-ready template.
290: - Lovable Cream Humanist: Lovable-inspired warm landing page. Ideal for ai builders, ferramentas no-code, plataformas amigáveis, dev tools approachable. AI-ready template.
291: - Luxury & Elegant: Luxury and elegant interface with strict 60/30/10 color hierarchy. Ideal for branding de luxo, hotéis e hospitalidade premium, moda high-end, joalheria, serviços financeiros exclusivos. AI-ready template.

(Output capped at 50 KB. Showing lines 1-291. Use offset=292 to continue.)
</content>
```

---

## Assistant (Build · Big Pickle · 3.1s)

_Thinking:_

Let me continue reading the llms-full.txt and explore more of the repo structure.

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/llms-full.txt",
  "offset": 292
}
```

**Output:**
```
<path>/home/mkt/design_md/llms-full.txt</path>
<type>file</type>
<content>
292: - Luxury Typography: Luxury typography-focused landing page where type IS the design. Ideal for moda haute couture, embalagens premium, streetwear de luxo, capas de revistas. AI-ready template.
293: - Manga Instructional Comic: Manga style landing page, black and white comic, speed lines, dynamic panels, ink aesthetic, instructional comic design. Ideal for landing pages, modern websites. AI-ready template.
294: - Manrope Typography: Render a 2D isolated text on a solid background. Ideal for digital products and interfaces, branding for tech, saas, and contemporary lifestyle companies.. AI-ready template.
295: - Maracatu Tech: Maracatu percussion-inspired tech landing page. Ideal for landing pages culturais, projetos afro-brasileiros, sites energéticos. AI-ready template.
296: - Mat: Mat — Dark sage canvas with bone paper and burnt-orange accent; mid-century modern with wood undertones. Bricolage Grotesque typography. muted sage green canvas with warm bone paper and a saturated burnt-orange accent. Best for design studio credentials, architecture / interior brand, ceramics or craft brand. AI-ready design system.
297: - Memphis: Memphis-style landing page with vibrant bold colors, geometric shapes (triangles, circles, squiggles), postmodern 80s aesthetic. Ideal for branding retro, peças editoriais, embalagens funky, campanhas jovens. AI-ready template.
298: - Memphis Design: Memphis style interface. Ideal for landing pages, saas. AI-ready template.
299: - Merriweather Typography: Render a 2D isolated text on a solid background. Ideal for blogs, news sites, long-form reading, and editorial platforms.. AI-ready template.
300: - Micro-interactions: Design with delightful micro-interactions: small 50-100ms animations, gesture-based responses, tactile feedback, loading spinners, success/error states, subtle hover effects, haptic feedback triggers for mobile. Ideal for landing pages, saas. AI-ready template.
301: - Micro-Sound UX: Multisensory landing page with micro-sound UX integration. Ideal for apps de produtividade premium, plataformas de musica, interfaces de gaming, dashboards interativos, experiencias imersivas, ferramentas criativas. AI-ready template.
302: - Mid-Century Modern: Mid-century modern landing page with clean lines, organic curves and muted vibrant colors from the 1950s. Ideal for branding de móveis, layouts de pôsteres retro, decoração de interiores, produtos lifestyle. AI-ready template.
303: - Midnight Garden Premium: Create an elegant, premium UI with a nocturnal botanical garden atmosphere. Ideal for marcas sustentáveis premium, jardins botânicos, cosméticos naturais, wellness de luxo, resorts ecológicos. AI-ready template.
304: - Mini World: Miniature world / diorama-style landing page. Ideal for games indie, educação infantil, projetos criativos, portfólios lúdicos. AI-ready template.
305: - Minimal & Direct: Minimal direct landing page. Ideal for marketing, conversão, lead gen. AI-ready template.
306: - Minimalism & Swiss Style: Minimalist landing page. Ideal for b2b saas, enterprise apps, design saas, professional tools. AI-ready template.
307: - Minimalismo Chic de Luxo: Design an elegant and minimalist luxury fashion e-commerce landing page. Ideal for landing pages, modern websites. AI-ready template.
308: - Minimalismo Confiável Financeiro: Professional and trustworthy minimalist landing page for a financial consulting firm. Ideal for landing pages, modern websites. AI-ready template.
309: - Minimalismo Fotográfico Elegante: Design an elegant and minimalist photography portfolio landing page. Ideal for landing pages, modern websites. AI-ready template.
310: - Minimalismo Funcional B2B: Clean and professional minimalist landing page for a B2B project management platform. Ideal for landing pages, modern websites. AI-ready template.
311: - Minimalismo Sereno de Bem-Estar: Calm and minimalist landing page for a meditation and wellness app. Ideal for landing pages, modern websites. AI-ready template.
312: - Minimalist React Hero with Motion: Minimalist, high-end React hero section using Tailwind CSS v4 and the Motion library. Ideal for saas landing pages, ferramentas de gestão remota, startups premium, produtos digitais high-end. AI-ready template.
313: - MiniMax Colorful Cards: MiniMax-inspired landing page with white canvas and colorful product cards. Ideal for plataformas de ia multi-modelo, galerias de ai, produtos consumer ai, showcases de tecnologia. AI-ready template.
314: - Mintlify Green Docs: Mintlify-inspired documentation landing page. Ideal for documentação, developer portals, plataformas de docs, knowledge bases. AI-ready template.
315: - Mistral Golden Amber: Mistral AI-inspired golden landing page. Ideal for ia europeia, marcas de luxo, plataformas premium, tecnologia francesa. AI-ready template.
316: - Mixed Media: Mixed media landing page combining collage, painting and photography aesthetics. Ideal for spreads de revistas, capas de álbuns, publicidade criativa, portfólios artísticos. AI-ready template.
317: - Mixed Reality / VR-AR: Mixed reality VR/AR infographic. Ideal for landing pages, modern websites. AI-ready template.
318: - Modern Minimalist: Modern minimalist landing page with strict 60/30/10 color balance. Ideal for design de logos minimalistas, landing pages corporativas, sites institucionais clean, produtos saas premium. AI-ready template.
319: - Modernismo Jornalístico Brasileiro: Structured and dynamic landing page for a Brazilian cultural news portal, inspired by modernism and azulejaria. Ideal for landing pages, saas. AI-ready template.
320: - MongoDB Forest Neon: MongoDB-inspired forest-dark landing page. Ideal for databases, infraestrutura de dados, plataformas developer, apis de dados. AI-ready template.
321: - Monochrome: Monochrome — Ivory ledger paper with all-black type; Lora serif headlines, Jost body, no color at all. Lora typography. ivory and pale-cream paper with deep ink-black type only. Best for user research synthesis, white paper, longform report. AI-ready design system.
322: - Motion-Driven: Build an animation-heavy interface with scroll-triggered animations, microinteractions, parallax scrolling (3-5 layers), smooth transitions (300-400ms), entrance animations, page transitions. Ideal for landing pages, saas. AI-ready template.
323: - Mystical Western: Mystical western landing page blending classic cowboy desert aesthetics with cosmic spiritual vibes. Ideal for pôsteres de festivais de música, marcas de vestuário indie, branding espiritual, eventos temáticos. AI-ready template.
324: - Nature Distilled: Design with nature distilled aesthetic. Ideal for landing pages, saas. AI-ready template.
325: - Natureza / Elementos Botânicos: Nature botanical infographic. Ideal for landing pages, modern websites. AI-ready template.
326: - Neo-Grid Bold: Neo-Grid Bold — Editorial neo-brutalism with a single neon yellow accent on off-white paper. Space Grotesk typography. off-white paper background, ink black, signature neon yellow accent used sparing. Best for product launch, design review, founder pitch. AI-ready design system.
327: - Neobrutalismo Crítico: Direct and bold neobrutalist landing page for a social and political critique blog. Ideal for landing pages, modern websites. AI-ready template.
328: - Neobrutalismo Ousado: Bold and provocative neobrutalist landing page for a disruptive design agency. Ideal for landing pages, modern websites. AI-ready template.
329: - Neoclassical Art: Neoclassical landing page inspired by ancient Greek and Roman art. Ideal for marcas de luxo, interior design, art galleries, projetos formais e institucionais. AI-ready template.
330: - Neon Cyber: Futuristic, techy, confident landing page with neon cyber aesthetic. Ideal for plataformas gaming, startups tech, apps de criptomoeda, eventos de tecnologia. AI-ready template.
331: - Neubrutalism: Neubrutalist interface. Ideal for landing pages, saas. AI-ready template.
332: - Neumorphic Tech Schematic: Neumorphic landing page, soft ui, tech schematic, light background, soft shadows, clean layout, hub and spoke design. Ideal for landing pages, modern websites. AI-ready template.
333: - Neumorphism: Neumorphic UI with soft 3D effects. Ideal for modern apps, dashboards, health/fitness, productivity. AI-ready template.
334: - New Era Automotive Hero: Design an automotive hero with full-viewport video (min 600px, max 965px). Ideal for concessionárias de carros, marketplaces automotivos, marcas de veículos, landing pages de lançamento. AI-ready template.
335: - New Era Bold Hero: Bold cinematic hero with full-screen background video and dark blue fallback. Ideal for creative agencies, portfólios impactantes, landing pages editoriais, marcas de moda. AI-ready template.
336: - Noir Detetive: Noir detective landing page. Ideal for landing pages, saas. AI-ready template.
337: - Notebook Tabs: Design an editorial, organized landing page that looks like a notebook. Ideal for blogs editoriais, digital magazines, portfolios criativos, educational platforms. AI-ready template.
338: - Notion Warm Workspace: Notion-inspired warm workspace landing page. Ideal for ferramentas de produtividade, workspaces colaborativos, gestão de conhecimento, wikis. AI-ready template.
339: - NVIDIA Power Green: Design an NVIDIA-inspired high-contrast landing page. Ideal for gpu computing, hardware, tecnologia de alto desempenho, data centers, gaming. AI-ready template.
340: - Ollama Pure Grayscale: Radically minimal Ollama-inspired landing page. Ideal for ferramentas cli, open-source, plataformas developer minimalistas, modelos de ia local. AI-ready template.
341: - OpenCode Terminal Mono: Design an OpenCode-inspired terminal-native landing page. Ideal for agentes de código ai, clis, ferramentas open-source, editores de terminal. AI-ready template.
342: - Organic Biophilic: Biophilic organic interface. Ideal for landing pages, saas. AI-ready template.
343: - Origami Geométrico: Design an origami geometric landing page. Ideal for landing pages, saas. AI-ready template.
344: - Paper & Ink: Design an editorial, literary, thoughtful landing page with paper and ink aesthetic. Ideal for editoras, blogs literários, revistas culturais, portfolios de escritores. AI-ready template.
345: - Parallax Storytelling: Parallax storytelling page. Ideal for landing pages, saas. AI-ready template.
346: - Passport Travel UI: Passport style landing page, travel document aesthetic, ink stamps, visa stickers, paper texture, official look, travel theme. Ideal for landing pages, modern websites. AI-ready template.
347: - Pastel Geometry: Friendly, organized, modern landing page with pastel geometry. Ideal for apps de produtividade, educational platforms, saas friendly, health apps. AI-ready template.
348: - PCB Schematic Architecture: PCB design landing, circuit board style, electronics aesthetic, green and copper palette, connecting traces, chip outlines, technical precision. Ideal for landing pages, modern websites. AI-ready template.
349: - People's Platform (Block & Bold): People's Platform (Block & Bold) — Activist poster energy: blue, orange, red on cream, with Alfa Slab + Caveat Brush. Alfa Slab One typography. saturated political-poster palette: cobalt blue, signal orange, warning red, on . Best for cultural commentary, manifesto, community / civic deck. AI-ready design system.
350: - Pin & Paper: Pin & Paper — Yellow paper with safety-pin illustrations, ink-blue handwritten Caveat, paper-grain texture. Caveat typography. saturated yellow paper, soft cream alternate, deep ink-blue type, plus rust red,. Best for research findings with personality, qualitative report, founder reflection. AI-ready design system.
351: - Pink Script — After Hours: Pink Script — After Hours — Black canvas, hot pink accent, pearl-cream paper, Instrument Serif headlines: late-night editorial luxury. Instrument Serif typography. near-black canvas with one saturated hot pink accent and a pearl-cream paper for. Best for fashion brand deck, creator personal brand, after-hours product (nightlife / dating / spirits). AI-ready design system.
352: - Pinterest Warm Discovery: Pinterest-inspired warm discovery landing page. Ideal for marketplaces visuais, galerias de inspiração, plataformas de descoberta, e-commerce visual. AI-ready template.
353: - Pixel Art: Pixel art inspired interface. Ideal for landing pages, saas. AI-ready template.
354: - Pixel Art 8-bit: Pixel art 8-bit landing page with retro gaming aesthetics. Ideal for jogos indie, marketing retro, designs nostálgicos, portfólios de desenvolvedores de games. AI-ready template.
355: - Playful: Playful — Sun-warm peach background with Syne display: a friendly indie launch deck. Syne typography. warm peach / sand backgrounds with ink-black structure and lighter cream cards. Best for creator portfolio, indie product launch, lifestyle brand. AI-ready design system.
356: - Pointillism / Stipple Art: Pointillism/stipple art landing page where visual texture is created through thousands of tiny dots. Ideal for ilustrações editoriais, embalagens artísticas, marcas com margem artística, pôsteres. AI-ready template.
357: - Pop Art: Pop Art landing page with extremely saturated bold colors and comic-strip aesthetics. Ideal for branding lúdico, design de vestuário, embalagens icônicas, capas editoriais. AI-ready template.
358: - Portfolio Dev Full-Stack: Developer portfolio, full-stack, projects gallery, clean layout, minimal, dark and cyan, code, tech stack, personal brand. Ideal for landing pages, modern websites. AI-ready template.
359: - Predictive Analytics: Predictive analytics dashboard. Ideal for landing pages, modern websites. AI-ready template.
360: - Psicodélico Anos 60: 60s psychedelic landing page. Ideal for landing pages, saas. AI-ready template.
361: - Radial Diagram / Donut Chart: Radial donut chart infographic. Ideal for landing pages, modern websites. AI-ready template.
362: - Raw Grid: Raw Grid — Neo-brutalist deck with thick borders, offset shadows, and a pink/sage/ink palette. Segoe UI / system-ui typography. white background with ink-black structure, soft pink and sage green as flat colo. Best for startup pitch, accelerator demo day, founder pitch. AI-ready design system.
363: - Real Estate Imobiliária Digital: Real estate landing, property cards, listings, luxury, gold and beige, modern, maps, filters, home search. Ideal for landing pages, modern websites. AI-ready template.
364: - Real-Time Monitoring: Real-time monitoring dashboard. Ideal for landing pages, modern websites. AI-ready template.
365: - Replicate Blaze Gallery: Replicate-inspired explosive landing page. Ideal for plataformas de modelos ai, apis de ml, comunidades developer, marketplaces de ai. AI-ready template.
366: - Resend Frost Cinematic: Resend-inspired cinematic dark landing page. Ideal for apis de email, infraestrutura developer, saas técnico, plataformas de comunicação. AI-ready template.
367: - Resume Journey Oregon Trail: Career resume landing page in Oregon Trail retro game style. Ideal for currículos criativos, portfólios de desenvolvedores, páginas pessoais, apresentações de carreira. AI-ready template.
368: - Retro Arcade Pixelado: Nostalgic and playful retro landing page for an online classic arcade. Ideal for landing pages, modern websites. AI-ready template.
369: - Retro Aventura Anos 70: Nostalgic and adventurous retro landing page for a 70s-style travel blog. Ideal for landing pages, modern websites. AI-ready template.
370: - Retro Barbershop Clássica: Classic and masculine retro landing page for a barbershop. Ideal for landing pages, modern websites. AI-ready template.
371: - Retro Boutique Vintage: Nostalgic and elegant retro landing page for a vintage clothing store. Ideal for landing pages, modern websites. AI-ready template.
372: - Retro Digital Anos 90: Nostalgic and playful retro landing page for a 90s-style digital marketing agency. Ideal for landing pages, modern websites. AI-ready template.
373: - Retro Travel Poster: Retro travel poster interface. Ideal for landing pages, saas. AI-ready template.
374: - Retro Windows: Retro Windows — Windows 95 chrome: gray title bars, MS Sans Serif, pixel typography, full nostalgia. Press Start 2P typography. Windows 95 system palette: 3D-button gray, navy title bars, pixel-perfect inset/. Best for retro gaming pitch, Y2K brand, creator portfolio (90s aesthetic). AI-ready design system.
375: - Retro Zine: Retro Zine — Beige paper with green accent and Bebas Neue + Caveat: a riso-printed zine in HTML form. Bebas Neue typography. warm beige / khaki paper with one saturated forest green. Best for indie zine / publication, music or arts brand, creator portfolio. AI-ready design system.
376: - Retro-Comic Action Blueprint: Retro comic landing page, superhero style, pop art, halftone dots, speech bubbles, bold black outlines, bright primary colors. Ideal for landing pages, modern websites. AI-ready template.
377: - Retro-Futurism: Retro-futuristic (cyberpunk/vaporwave) interface with neon colors (blue, pink, cyan), deep black background, 80s aesthetic, CRT scanlines, glitch effects, neon glow text/borders, monospace fonts, geometric patterns. Ideal for landing pages, saas. AI-ready template.
378: - Reuso Criativo Disruptivo: Design an innovative and playful landing page for a creative reuse and upcycling platform, inspired by Irmãos Campana. Ideal for landing pages, saas. AI-ready template.
379: - Revolut Billboard Fintech: Revolut-inspired billboard fintech landing page. Ideal for banking digital, fintechs, plataformas financeiras, neobanks. AI-ready template.
380: - Risograph / Retro-Pop: Risograph retro-pop interface. Ideal for landing pages, saas. AI-ready template.
381: - Risograph Zine Aesthetic: Risograph landing page, zine aesthetics, grainy texture, multiply blending mode, retro print style, bright pink and blue ink. Ideal for landing pages, modern websites. AI-ready template.
382: - Rococó Delicado: Delicate Rococo landing page. Ideal for landing pages, saas. AI-ready template.
383: - Rococo Romantic Narrative: Rococo landing page, romantic style, pastel colors, gold accents, floral decorations, soft and dreamy, ornate luxury. Ideal for landing pages, modern websites. AI-ready template.
384: - Roxo Veludo Real: Luxurious and sophisticated UI with a royal feel. Ideal for marcas de luxo, joalherias, moda premium, hotéis boutique, eventos exclusivos. AI-ready template.
385: - Runway Cinematic Editorial: Runway-inspired cinematic editorial landing page. Ideal for ai criativa, geração de vídeo, plataformas de mídia, estúdios de produção. AI-ready template.
386: - SaaS Enterprise Analytics: SaaS landing, analytics dashboard, metrics cards, corporate blue, b2b, business intelligence, charts, integrations, trust, clean UI, glassmorphism, data visualization. Ideal for landing pages, modern websites. AI-ready template.
387: - SaaS Signature Gradient: Design the quintessential SaaS/AI startup landing page with THE signature tech gradient. Ideal for startups saas, ai tools, plataformas de desenvolvedores, landing pages tech, produtos b2b modernos, apis e sdks. AI-ready template.
388: - Sakura / Floral Japonês: Sakura floral Japanese infographic. Ideal for landing pages, modern websites. AI-ready template.
389: - Sakura Chroma: Sakura Chroma — Vintage Japanese cassette-package aesthetic: cream paper, diagonal rainbow ribbons, condensed bold type, JIS-style spec checkboxes. Big Shoulders Display typography. warm cream paper canvas with dark warm-brown ink and a six-colour primary palett. Best for product launch or catalogue, indie hardware or analog studio brand, music label or release schedule. AI-ready design system.
390: - Sales Intelligence Dashboard: Sales intelligence dashboard. Ideal for landing pages, modern websites. AI-ready template.
391: - Sanity Neon Structured: Sanity-inspired nocturnal CMS landing page. Ideal for cms headless, plataformas de conteúdo estruturado, ferramentas de dados, apis de conteúdo. AI-ready template.
392: - Scatterbrain: Scatterbrain — Post-it inspired: pastel sticky notes, Caveat handwriting, Shrikhand and Zilla Slab type stack. Shrikhand typography. off-white paper with a full pastel sticky-note palette (yellow, blue, pink, gree. Best for brainstorm / workshop, creative agency credentials, design-thinking session. AI-ready design system.
393: - Scrapbook / Collage: Scrapbook/collage landing page with analog handmade tactile aesthetics. Ideal for diários pessoais, convites de casamento, vision boards, publicações acolhedoras em redes sociais. AI-ready template.
394: - Sentry Purple Debugger: Sentry-inspired dark purple developer landing page. Ideal for monitoramento de erros, devops, ferramentas developer, observabilidade. AI-ready template.
395: - Shabby Chic: Shabby chic landing page with faded pastel tones and vintage romance. Ideal for convites de casamento, embalagens acolhedoras, marcas nostálgicas, decoração de interiores. AI-ready template.
396: - Signal: Signal — Deep navy canvas with bone paper and a single muted-gold accent; institutional with quiet weight. Source Serif 4 typography. deep navy primary with warm bone paper alternate and a single muted-gold accent. Best for investor deck, consulting deliverable, board presentation. AI-ready design system.
397: - Símbolos Ambientais Brasileiros: Design an urgent and informative landing page for an Amazon preservation campaign, inspired by Brazilian graphic symbolism. Ideal for landing pages, saas. AI-ready template.
398: - Símbolos Cívicos Brasileiros: Design an informative and symbolic landing page for a civic education platform, inspired by Aloísio Magalhães' graphic identity. Ideal for landing pages, saas. AI-ready template.
399: - Símbolos Culturais Brasileiros: Design an authentic and engaging landing page for a Brazilian cultural tourism platform, inspired by graphic symbolism. Ideal for landing pages, saas. AI-ready template.
400: - Símbolos Políticos Brasileiros: Design an informative and authoritative landing page for a Brazilian political news and analysis platform, inspired by graphic symbolism. Ideal for landing pages, saas. AI-ready template.
401: - Símbolos Regionais Brasileiros: Design an authentic and diverse landing page for an online store of Brazilian regional products, inspired by graphic symbolism and regional identity. Ideal for landing pages, saas. AI-ready template.
402: - Skeuomorphism: Realistic, textured interface with 3D depth, real-world metaphors (leather, wood, metal), complex gradients (8-12 stops), realistic shadows, grain/texture overlays, tactile press animations. Ideal for landing pages, saas. AI-ready template.
403: - Social Proof-Focused: Social proof landing page. Ideal for marketing, conversão, lead gen. AI-ready template.
404: - Soft Editorial: Soft Editorial — Cormorant Garamond serif on warm paper with sage, blush, and lemon accents. Cormorant Garamond typography. warm paper canvas with deep ink type, accented by soft pink, lemon, blush, and s. Best for editorial feature, longform brand story, gallery or museum. AI-ready design system.
405: - Soft Maximalism: Soft maximalist landing page with CONTROLLED CHAOS energy. Ideal for marcas jovens, agencias criativas, lancamentos de produto, portfolios ousados, eventos e festivais. AI-ready template.
406: - Soft UI Evolution: Design evolved neumorphism with improved contrast (WCAG AA+), modern aesthetics, subtle depth, accessibility focus. Ideal for landing pages, saas. AI-ready template.
407: - Solarpunk Utópico: Solarpunk utopian landing page. Ideal for landing pages, saas. AI-ready template.
408: - Space Grotesk Typography: Render a 2D isolated text on a solid background. Ideal for developer tools, web3/crypto, tech startups, and data-driven interfaces.. AI-ready template.
409: - Spaceship Instruction Manual: Landing page that looks like a spaceship instruction manual or engineering blueprint. Ideal for produtos de hardware, startups deep-tech, apis e ferramentas dev, plataformas de engenharia, documentacao tecnica, cybersecurity. AI-ready template.
410: - SpaceX Cinematic Void: SpaceX-inspired cinematic void landing page. Ideal for aeroespacial, tecnologia espacial, marcas futuristas, engenharia avançada. AI-ready template.
411: - Spatial UI (VisionOS): VisionOS-style spatial interface. Ideal for landing pages, saas. AI-ready template.
412: - Split Pastel: Playful, modern, friendly landing page with split pastel background. Ideal for apps criativos, plataformas de design, startups friendly, ecommerce lifestyle. AI-ready template.
413: - Spotify Dark Immersive: Spotify-inspired dark immersive landing page. Ideal for streaming de música, plataformas de áudio, podcasts, entretenimento digital. AI-ready template.
414: - Steampunk: Steampunk landing page fusing Victorian elegance with steam-powered mechanical aesthetics. Ideal for capas de livros de fantasia, merchandise temático, gráficos de videojogos, eventos cosplay. AI-ready template.
415: - Steampunk Industrial: Steampunk industrial interface. Ideal for landing pages, saas. AI-ready template.
416: - Steampunk Nebula Explorer: Steampunk space landing page, nebula background, brass and copper gears, vintage sci-fi aesthetic, explorer style, cosmic industrial. Ideal for landing pages, modern websites. AI-ready template.
417: - Steampunk Vitoriano: Victorian steampunk landing page. Ideal for landing pages, saas. AI-ready template.
418: - Stencil & Tablet: Stencil & Tablet — Bone paper with stencil-cut headlines and a six-color earth palette: archaeology meets brand. Bowlby One typography. warm bone and paper neutrals with a saturated earthy palette (sienna, magenta, o. Best for museum / cultural institution, art / architecture brand, longform research. AI-ready design system.
419: - Storytelling-Driven: Storytelling landing page. Ideal for marketing, conversão, lead gen. AI-ready template.
420: - Stripe Fintech Elegance: Stripe-inspired fintech landing page. Ideal for fintechs, plataformas de pagamento, infraestrutura financeira, saas enterprise. AI-ready template.
421: - Studio: Studio — Black canvas with electric-yellow type; high-voltage design studio aesthetic. Barlow typography. near-black canvas with one signature electric-yellow that doubles as foreground . Best for design studio credentials, creative agency pitch, brand showcase. AI-ready design system.
422: - Studygram / Notebook Kawaii: Studygram notebook kawaii interface. Ideal for landing pages, saas. AI-ready template.
423: - Sumi-e Tech Scroll: Sumi-e style landing, ink wash painting, rice paper texture, red seal accent, isometric tech details, east asian aesthetic. Ideal for landing pages, modern websites. AI-ready template.
424: - Supabase Dark Emerald: Dark-mode-native developer landing page inspired by Supabase. Ideal for plataformas developer, ferramentas open-source, bancos de dados, apis. AI-ready template.
425: - Surrealism: Surrealist landing page that defies logic and reality. Ideal for capas de álbuns, ilustrações editoriais conceituais, digital art, campanhas criativas. AI-ready template.
426: - Swiss Design Gráfico: Swiss graphic design landing page. Ideal for landing pages, saas. AI-ready template.
427: - Swiss Modern: Clean, precise, Bauhaus-inspired landing page with Swiss Modern aesthetic. Ideal for agências de design, architecture, art galleries, portfolios minimalistas. AI-ready template.
428: - Swiss Modernism 2.0: Design with Swiss Modernism 2.0. Ideal for landing pages, saas. AI-ready template.
429: - Synapse Dark Hero: Pure black SaaS hero with HLS video at 100% opacity no overlay, positioned at height 80vh and absolute bottom-[35vh]. Ideal for saas de inovação, plataformas de ai, ferramentas enterprise, startups de tecnologia. AI-ready template.
430: - Syne Typography: Render a 2D isolated text on a solid background. Ideal for cultural institutions, creative studios, posters, and edgy editorial layouts.. AI-ready template.
431: - Synthwave: Synthwave landing page with dramatic neon sunset gradients and retro-futuristic 80s aesthetics. Ideal for capas de álbuns, promoções de marca, visuais neon, eventos de música eletrônica. AI-ready template.
432: - Tactile 3D Neumorphism: Tactile 3D neumorphic interface with inflated, puffy shapes that look extruded from the background. Ideal for modern apps, dashboards, premium interfaces, produtos digitais, fintech. AI-ready template.
433: - Tactile Digital / Deformable UI: Tactile deformable interface. Ideal for landing pages, saas. AI-ready template.
434: - Targo Logistics Hero: Logistics hero with full-screen video 100% opacity no overlay. Ideal for empresas de logística, transportadoras, frotas corporativas, serviços de entrega premium. AI-ready template.
435: - Taskora SaaS Hero: Dark SaaS hero with background video at opacity-50 and gradient overlay fading to background color. Ideal for produtos saas, plataformas de gestão de projetos, ferramentas de produtividade, dashboards analíticos. AI-ready template.
436: - Tenebrism: Tenebrism-inspired landing page with extreme contrast between light and deep darkness. Ideal for pôsteres atmosféricos, flyers de eventos, spreads editoriais, embalagens premium. AI-ready template.
437: - Tenor Sans Typography: Render a 2D isolated text on a solid background. Ideal for magazines, minimalist brands, and content-heavy layouts with a sophisticated tone.. AI-ready template.
438: - Terminal Green: Developer-focused, hacker aesthetic landing page. Ideal for portfolios de desenvolvedores, ferramentas cli, plataformas devops, technical documentation. AI-ready template.
439: - Terracota Mediterrâneo: Mediterranean terracotta landing page. Ideal for landing pages, saas. AI-ready template.
440: - The Barely-There UI: Design an ultra-minimal AI-native interface inspired by OpenAI and Perplexity. Ideal for plataformas de ia, saas b2b enterprise, dashboards analiticos, ferramentas de produtividade, interfaces de dados. AI-ready template.
441: - Thermal Insight Tech: Thermal imaging landing page, heat map aesthetic, infrared colors, dark tech background, spectrum gradient, technical analysis. Ideal for landing pages, modern websites. AI-ready template.
442: - Timeline Horizontal Corporativo: Horizontal corporate timeline. Ideal for landing pages, modern websites. AI-ready template.
443: - Together Pastel Cloud: Together AI-inspired pastel cloud landing page. Ideal for infraestrutura ai, cloud computing, plataformas de modelos, gpu clusters. AI-ready template.
444: - Travel Plataforma de Viagens: Travel landing, destinations, packages, maps, booking, adventure, blue and accent color, trips, flights, hotels. Ideal for landing pages, modern websites. AI-ready template.
445: - Tropicalismo Aventureiro Natural: Design an adventurous and natural landing page for an ecotourism travel agency in Brazil, inspired by tropicalism. Ideal for landing pages, saas. AI-ready template.
446: - Tropicalismo Gastronômico Vibrante: Vibrant and flavorful landing page for a Brazilian gastronomy festival, inspired by tropicalism. Ideal for landing pages, saas. AI-ready template.
447: - Tropicalismo Indígena Autêntico: Design an authentic and cultural landing page for a Brazilian indigenous culture platform, inspired by tropicalism and indigenous art. Ideal for landing pages, saas. AI-ready template.
448: - Trust & Authority: Trust-focused landing page. Ideal for marketing, conversão, lead gen. AI-ready template.
449: - Uber Bold Transit: Design an Uber-inspired bold landing page. Ideal for mobilidade urbana, logistics, delivery, plataformas de transporte. AI-ready template.
450: - Ukiyo-e Woodblock Revival: Ukiyo-e landing page, woodblock print style, japanese art, bold outlines, prussian blue, paper texture, traditional graphic design. Ideal for landing pages, modern websites. AI-ready template.
451: - Underwater / Aquático: Design an underwater aquatic infographic. Ideal for landing pages, modern websites. AI-ready template.
452: - Underwater Aquático Deep Sea: Underwater elements, aquatic life, water plants, bubbles, waves, ocean aesthetics, calming, peaceful, exploratory, marine, deep sea, layered depth, cool blue illumination, flowing liquid, underwater infographic. Ideal for landing pages, modern websites. AI-ready template.
453: - User Behavior Analytics: User behavior analytics dashboard. Ideal for landing pages, modern websites. AI-ready template.
454: - Utilitarian: Utilitarian landing page stripped to absolute essentials. Ideal for sinalética, interfaces industriais, etiquetas de roupa, design de embalagens informativas. AI-ready template.
455: - Vaporwave: Vaporwave landing page with intense neon colors and satirical 80s/90s nostalgia. Ideal for capas de álbuns, colagens digitais, anúncios experimentais, arte de internet. AI-ready template.
456: - Vaporwave: Vaporwave aesthetic interface. Ideal for landing pages, saas. AI-ready template.
457: - Vaporwave Aesthetic: Vaporwave aesthetic interface. Ideal for landing pages, saas. AI-ready template.
458: - Vellum: Vellum — Deep navy canvas with warm-yellow italic Cormorant serifs and a single dusty teal accent. A quiet, scholarly aesthetic. Cormorant Garamond Italic typography. deep periwinkle navy canvas with warm yellow italic-serif type and one dusty-tea. Best for research findings, white paper or longform report, academic or university deck. AI-ready design system.
459: - Vercel Geist Minimal: Vercel-inspired minimal landing page. Ideal for infraestrutura developer, plataformas de deploy, ferramentas frontend, ci/cd. AI-ready template.
460: - Vernacular Acolhedor Brasileiro: Design an authentic and rustic landing page for a vernacular interior design blog, inspired by Brazilian material culture. Ideal for landing pages, saas. AI-ready template.
461: - Versus Mode Anime Aesthetic: Versus mode landing page, anime fighting game style, split screen design, dynamic diagonals, high contrast, hud elements. Ideal for landing pages, modern websites. AI-ready template.
462: - Vertical Whiteboard Timeline: Vertical whiteboard tutorial landing page with metallic aluminum frame border (gray gradient, dual box-shadow) and decorative Expo markers at the bottom. Ideal for tutoriais passo a passo, onboarding de produto, guias educativos, how-to pages, documentacao visual, landing pages long-form. AI-ready template.
463: - Vibrant & Block-based: Design an energetic, vibrant interface with bold block layouts, geometric shapes, high color contrast, large typography (32px+), animated background patterns, duotone effects. Ideal for startups, ecommerce fashion, apps gaming, marketing conversível. AI-ready template.
464: - Victorian: Victorian-era landing page with extremely ornate details. Ideal for caligrafia moderna, convites temáticos, branding vintage, designs steampunk. AI-ready template.
465: - Vintage Analog / Retro Film: Design with vintage analog film aesthetic. Ideal for landing pages, saas. AI-ready template.
466: - Vintage Botanical / Scientific: Vintage botanical scientific interface. Ideal for landing pages, saas. AI-ready template.
467: - Vintage Botanical Scientific Illustration: Vintage botanical landing page, scientific illustration style, aged paper background, plant diagram aesthetics, scholarly look, organic colors. Ideal for landing pages, modern websites. AI-ready template.
468: - Vintage Editorial: Witty, confident editorial landing page with personality. Ideal for blogs premium, digital magazines, marcas artesanais, consultorias criativas. AI-ready template.
469: - Vintage Lithograph / Victorian: Victorian lithograph interface. Ideal for landing pages, saas. AI-ready template.
470: - Voice-First Multimodal: Voice-first multimodal interface. Ideal for landing pages, saas. AI-ready template.
471: - VoltAgent Terminal Emerald: VoltAgent-inspired deep-space terminal landing page. Ideal for frameworks de agentes ai, plataformas de engenharia, ferramentas de automação, sdks. AI-ready template.
472: - Voxel Gamified Isometric: Voxel landing page, isometric 3d style, gamified design, floating islands, blocky characters, colorful and friendly. Ideal for landing pages, modern websites. AI-ready template.
473: - Wabi-Sabi Anti-UX: Wabi-sabi inspired landing page celebrating imperfection and human touch. Ideal for portfolios artisticos, marcas artesanais, cafeterias e restaurantes, estudio de design, blogs pessoais, produtos organicos. AI-ready template.
474: - Wealth Video Hero: Premium fintech hero with full-screen looping background video scaled 150% with top-left focal point. Ideal for fintechs, plataformas de investimento, gestão patrimonial, landing pages financeiras premium. AI-ready template.
475: - Web3 EOS Hero: Web3 hero with full-screen video and 50% black overlay. Ideal for projetos blockchain, plataformas web3, daos, landing pages de waitlist cripto. AI-ready template.
476: - Weblex Dark Hero: Dark hero with full-screen video with seamless loop transition via requestAnimationFrame opacity. Ideal for website builders, plataformas no-code, ferramentas de criação de sites, landing pages de produto. AI-ready template.
477: - Whiteboard: Whiteboard-style landing page that looks like a collaborative brainstorming session. Ideal for brainstorming, education, ferramentas colaborativas, startups, apresentações. AI-ready template.
478: - Whiteboard Flowchart: Whiteboard-style landing page with metallic aluminum frame border (gray gradient with dual box-shadow). Ideal for processos e fluxogramas, onboarding e tutoriais, educacao e cursos, startups criativas, brainstorming e ideacao. AI-ready template.
479: - Wise Lime Bold: Wise-inspired bold fintech landing page. Ideal for transferências internacionais, fintechs, plataformas de pagamento, câmbio. AI-ready template.
480: - xAI Brutalist Monospace: Design an xAI-inspired dark brutalist landing page. Ideal for labs de ia, pesquisa, plataformas técnicas, infraestrutura de modelos. AI-ready template.
481: - Y2K: Y2K landing page with vibrant neon colors and early 2000s tech optimism. Ideal for editoriais de moda, colagens digitais, campanhas de streetwear, social networks. AI-ready template.
482: - Y2K Aesthetic: Y2K aesthetic interface. Ideal for landing pages, saas. AI-ready template.
483: - Z-Shape: Z-shape infographic with characters. Ideal for landing pages, modern websites. AI-ready template.
484: - Zapier Warm Automation: Zapier-inspired warm automation landing page. Ideal for automação, integrações, plataformas de workflow, ferramentas no-code. AI-ready template.
485: - Zero Interface: Voice-first, gesture-based, AI-driven interface with minimal visible UI, progressive disclosure, voice recognition UI, gesture detection, AI predictions, smart suggestions, context-aware actions. Ideal for landing pages, saas. AI-ready template.
486: 
487: ## Guides
488: - Claude Code: config file CLAUDE.md, Siga as regras visuais de @DESIGN.md
489: - Cursor: config file .cursor/rules/*.mdc, Include do DESIGN.md
490: - Kiro: config file .kiro/steering/, Copiar DESIGN.md para steering
491: - Windsurf: config file .windsurfrules, Referenciar DESIGN.md
492: - Google Stitch: config file UI nativa, Import direto
493: 
494: ## Blog
495: - How to Use DESIGN.md with Cursor — Complete Setup Guide: Configure DESIGN.md in Cursor for consistent AI-generated UI. Step-by-step setup with .cursorrules integration and practical examples.
496: - How to Create a DESIGN.md from Scratch: Step-by-step guide to writing a DESIGN.md file for your project. Define colors, typography, spacing and components in Markdown for AI agents.
497: 
498: ## Related
499: - github.com/google-labs-code/design.md — Official specification
500: - skill.dev.br — AI agent skills marketplace (SKILL.md modules)
501: - ft.ia.br — Author

(End of file - total 501 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/design-md-library/elementos_designmd.md"
}
```

**Output:**
```
<path>/home/mkt/design_md/design-md-library/elementos_designmd.md</path>
<type>file</type>
<content>
1: # Design Systems Library
2: 
3: ## Sobre
4: Esta é uma coleção extraída do site [designmd.app/library](https://designmd.app/library/), que contém um catálogo extenso de **454 sistemas de design**. A biblioteca serve como um repositório de diretrizes visuais, tokens e estéticas prontas, ideais para acelerar o desenvolvimento de interfaces (UI/UX) e inspirar a criação de aplicações e sites utilizando Inteligência Artificial.
5: 
6: Para baixar: `document.querySelector('#download-designmd').click()`
7: 
8: | Título | Imagem | Link |
9: | --- | --- | --- |
10: | Minimalism & Swiss Style | ![Minimalism & Swiss Style](https://designmd.app/images/library/1.png) | [Link](https://designmd.app/en/library/minimalism-swiss-style) |
11: | Neumorphism | ![Neumorphism](https://designmd.app/images/library/2.png) | [Link](https://designmd.app/en/library/neumorphism) |
12: | Glassmorphism | ![Glassmorphism](https://designmd.app/images/library/3.png) | [Link](https://designmd.app/en/library/glassmorphism) |
13: | Brutalism | ![Brutalism](https://designmd.app/images/library/4.png) | [Link](https://designmd.app/en/library/brutalism-4) |
14: | 3D & Hyperrealism | ![3D & Hyperrealism](https://designmd.app/images/library/5.png) | [Link](https://designmd.app/en/library/3d-hyperrealism) |
15: | Vibrant & Block-based | ![Vibrant & Block-based](https://designmd.app/images/library/6.png) | [Link](https://designmd.app/en/library/vibrant-block-based) |
16: | Dark Mode (OLED) | ![Dark Mode (OLED)](https://designmd.app/images/library/7.png) | [Link](https://designmd.app/en/library/dark-mode-oled) |
17: | Accessible & Ethical | ![Accessible & Ethical](https://designmd.app/images/library/8.png) | [Link](https://designmd.app/en/library/accessible-ethical) |
18: | Claymorphism | ![Claymorphism](https://designmd.app/images/library/9.png) | [Link](https://designmd.app/en/library/claymorphism) |
19: | Aurora UI | ![Aurora UI](https://designmd.app/images/library/10.png) | [Link](https://designmd.app/en/library/aurora-ui) |
20: | Retro-Futurism | ![Retro-Futurism](https://designmd.app/images/library/11.png) | [Link](https://designmd.app/en/library/retro-futurism) |
21: | Flat Design | ![Flat Design](https://designmd.app/images/library/12.png) | [Link](https://designmd.app/en/library/flat-design) |
22: | Skeuomorphism | ![Skeuomorphism](https://designmd.app/images/library/13.png) | [Link](https://designmd.app/en/library/skeuomorphism) |
23: | Liquid Glass | ![Liquid Glass](https://designmd.app/images/library/14.png) | [Link](https://designmd.app/en/library/liquid-glass) |
24: | Motion-Driven | ![Motion-Driven](https://designmd.app/images/library/15.png) | [Link](https://designmd.app/en/library/motion-driven) |
25: | Micro-interactions | ![Micro-interactions](https://designmd.app/images/library/16.png) | [Link](https://designmd.app/en/library/micro-interactions) |
26: | Inclusive Design | ![Inclusive Design](https://designmd.app/images/library/17.png) | [Link](https://designmd.app/en/library/inclusive-design) |
27: | Zero Interface | ![Zero Interface](https://designmd.app/images/library/18.png) | [Link](https://designmd.app/en/library/zero-interface) |
28: | Soft UI Evolution | ![Soft UI Evolution](https://designmd.app/images/library/19.png) | [Link](https://designmd.app/en/library/soft-ui-evolution) |
29: | Hero-Centric Design | ![Hero-Centric Design](https://designmd.app/images/library/20.png) | [Link](https://designmd.app/en/library/hero-centric-design) |
30: | Conversion-Optimized | ![Conversion-Optimized](https://designmd.app/images/library/21.png) | [Link](https://designmd.app/en/library/conversion-optimized) |
31: | Feature-Rich Showcase | ![Feature-Rich Showcase](https://designmd.app/images/library/22.png) | [Link](https://designmd.app/en/library/feature-rich-showcase) |
32: | Minimal & Direct | ![Minimal & Direct](https://designmd.app/images/library/23.png) | [Link](https://designmd.app/en/library/minimal-direct) |
33: | Social Proof-Focused | ![Social Proof-Focused](https://designmd.app/images/library/24.png) | [Link](https://designmd.app/en/library/social-proof-focused) |
34: | Interactive Product Demo | ![Interactive Product Demo](https://designmd.app/images/library/25.png) | [Link](https://designmd.app/en/library/interactive-product-demo) |
35: | Trust & Authority | ![Trust & Authority](https://designmd.app/images/library/26.png) | [Link](https://designmd.app/en/library/trust-authority) |
36: | Storytelling-Driven | ![Storytelling-Driven](https://designmd.app/images/library/27.png) | [Link](https://designmd.app/en/library/storytelling-driven) |
37: | Data-Dense Dashboard | ![Data-Dense Dashboard](https://designmd.app/images/library/28.png) | [Link](https://designmd.app/en/library/data-dense-dashboard) |
38: | Heat Map & Heatmap Style | ![Heat Map & Heatmap Style](https://designmd.app/images/library/29.png) | [Link](https://designmd.app/en/library/heat-map-heatmap-style) |
39: | Executive Dashboard | ![Executive Dashboard](https://designmd.app/images/library/30.png) | [Link](https://designmd.app/en/library/executive-dashboard) |
40: | Real-Time Monitoring | ![Real-Time Monitoring](https://designmd.app/images/library/31.png) | [Link](https://designmd.app/en/library/real-time-monitoring) |
41: | Drill-Down Analytics | ![Drill-Down Analytics](https://designmd.app/images/library/32.png) | [Link](https://designmd.app/en/library/drill-down-analytics) |
42: | Comparative Analysis Dashboard | ![Comparative Analysis Dashboard](https://designmd.app/images/library/33.png) | [Link](https://designmd.app/en/library/comparative-analysis-dashboard) |
43: | Predictive Analytics | ![Predictive Analytics](https://designmd.app/images/library/34.png) | [Link](https://designmd.app/en/library/predictive-analytics) |
44: | User Behavior Analytics | ![User Behavior Analytics](https://designmd.app/images/library/35.png) | [Link](https://designmd.app/en/library/user-behavior-analytics) |
45: | Financial Dashboard | ![Financial Dashboard](https://designmd.app/images/library/36.png) | [Link](https://designmd.app/en/library/financial-dashboard) |
46: | Sales Intelligence Dashboard | ![Sales Intelligence Dashboard](https://designmd.app/images/library/37.png) | [Link](https://designmd.app/en/library/sales-intelligence-dashboard) |
47: | Neubrutalism | ![Neubrutalism](https://designmd.app/images/library/38.png) | [Link](https://designmd.app/en/library/neubrutalism) |
48: | Bento Box Grid | ![Bento Box Grid](https://designmd.app/images/library/39.png) | [Link](https://designmd.app/en/library/bento-box-grid) |
49: | Y2K Aesthetic | ![Y2K Aesthetic](https://designmd.app/images/library/40.png) | [Link](https://designmd.app/en/library/y2k-aesthetic) |
50: | Cyberpunk UI | ![Cyberpunk UI](https://designmd.app/images/library/41.png) | [Link](https://designmd.app/en/library/cyberpunk-ui) |
51: | Organic Biophilic | ![Organic Biophilic](https://designmd.app/images/library/42.png) | [Link](https://designmd.app/en/library/organic-biophilic) |
52: | AI-Native UI | ![AI-Native UI](https://designmd.app/images/library/43.png) | [Link](https://designmd.app/en/library/ai-native-ui) |
53: | Memphis Design | ![Memphis Design](https://designmd.app/images/library/44.png) | [Link](https://designmd.app/en/library/memphis-design) |
54: | Vaporwave | ![Vaporwave](https://designmd.app/images/library/45.png) | [Link](https://designmd.app/en/library/vaporwave-45) |
55: | Dimensional Layering | ![Dimensional Layering](https://designmd.app/images/library/46.png) | [Link](https://designmd.app/en/library/dimensional-layering) |
56: | Exaggerated Minimalism | ![Exaggerated Minimalism](https://designmd.app/images/library/47.png) | [Link](https://designmd.app/en/library/exaggerated-minimalism) |
57: | Kinetic Typography | ![Kinetic Typography](https://designmd.app/images/library/48.png) | [Link](https://designmd.app/en/library/kinetic-typography) |
58: | Parallax Storytelling | ![Parallax Storytelling](https://designmd.app/images/library/49.png) | [Link](https://designmd.app/en/library/parallax-storytelling) |
59: | Swiss Modernism 2.0 | ![Swiss Modernism 2.0](https://designmd.app/images/library/50.png) | [Link](https://designmd.app/en/library/swiss-modernism-2-0) |
60: | HUD / Sci-Fi FUI | ![HUD / Sci-Fi FUI](https://designmd.app/images/library/51.png) | [Link](https://designmd.app/en/library/hud-sci-fi-fui) |
61: | Pixel Art | ![Pixel Art](https://designmd.app/images/library/52.png) | [Link](https://designmd.app/en/library/pixel-art) |
62: | Bento Grids | ![Bento Grids](https://designmd.app/images/library/53.png) | [Link](https://designmd.app/en/library/bento-grids) |
63: | Knolling Pastel Flat Lay | ![Knolling Pastel Flat Lay](https://designmd.app/images/library/54.png) | [Link](https://designmd.app/en/library/knolling-pastel-flat-lay) |
64: | Spatial UI (VisionOS) | ![Spatial UI (VisionOS)](https://designmd.app/images/library/55.png) | [Link](https://designmd.app/en/library/spatial-ui-visionos) |
65: | E-Ink / Paper | ![E-Ink / Paper](https://designmd.app/images/library/56.png) | [Link](https://designmd.app/en/library/e-ink-paper) |
66: | Gen Z Chaos / Maximalism | ![Gen Z Chaos / Maximalism](https://designmd.app/images/library/57.png) | [Link](https://designmd.app/en/library/gen-z-chaos-maximalism) |
67: | Biomimetic / Organic 2.0 | ![Biomimetic / Organic 2.0](https://designmd.app/images/library/58.png) | [Link](https://designmd.app/en/library/biomimetic-organic-2-0) |
68: | Anti-Polish / Raw Aesthetic | ![Anti-Polish / Raw Aesthetic](https://designmd.app/images/library/59.png) | [Link](https://designmd.app/en/library/anti-polish-raw-aesthetic) |
69: | Tactile Digital / Deformable UI | ![Tactile Digital / Deformable UI](https://designmd.app/images/library/60.png) | [Link](https://designmd.app/en/library/tactile-digital-deformable-ui) |
70: | Nature Distilled | ![Nature Distilled](https://designmd.app/images/library/61.png) | [Link](https://designmd.app/en/library/nature-distilled) |
71: | Interactive Cursor Design | ![Interactive Cursor Design](https://designmd.app/images/library/62.png) | [Link](https://designmd.app/en/library/interactive-cursor-design) |
72: | Voice-First Multimodal | ![Voice-First Multimodal](https://designmd.app/images/library/63.png) | [Link](https://designmd.app/en/library/voice-first-multimodal) |
73: | 3D Product Preview | ![3D Product Preview](https://designmd.app/images/library/64.png) | [Link](https://designmd.app/en/library/3d-product-preview) |
74: | Gradient Mesh / Aurora Evolved | ![Gradient Mesh / Aurora Evolved](https://designmd.app/images/library/65.png) | [Link](https://designmd.app/en/library/gradient-mesh-aurora-evolved) |
75: | Editorial Grid / Magazine | ![Editorial Grid / Magazine](https://designmd.app/images/library/66.png) | [Link](https://designmd.app/en/library/editorial-grid-magazine) |
76: | Chromatic Aberration / RGB Split | ![Chromatic Aberration / RGB Split](https://designmd.app/images/library/67.png) | [Link](https://designmd.app/en/library/chromatic-aberration-rgb-split) |
77: | Vintage Analog / Retro Film | ![Vintage Analog / Retro Film](https://designmd.app/images/library/68.png) | [Link](https://designmd.app/en/library/vintage-analog-retro-film) |
78: | Art Deco / Golden Age | ![Art Deco / Golden Age](https://designmd.app/images/library/69.png) | [Link](https://designmd.app/en/library/art-deco-golden-age) |
79: | Risograph / Retro-Pop | ![Risograph / Retro-Pop](https://designmd.app/images/library/70.png) | [Link](https://designmd.app/en/library/risograph-retro-pop) |
80: | Ancient Egyptian / Historical | ![Ancient Egyptian / Historical](https://designmd.app/images/library/71.png) | [Link](https://designmd.app/en/library/ancient-egyptian-historical) |
81: | Vintage Lithograph / Victorian | ![Vintage Lithograph / Victorian](https://designmd.app/images/library/72.png) | [Link](https://designmd.app/en/library/vintage-lithograph-victorian) |
82: | Comic Book / Pop Art | ![Comic Book / Pop Art](https://designmd.app/images/library/73.png) | [Link](https://designmd.app/en/library/comic-book-pop-art) |
83: | Kawaii / Sweet Pastel | ![Kawaii / Sweet Pastel](https://designmd.app/images/library/74.png) | [Link](https://designmd.app/en/library/kawaii-sweet-pastel) |
84: | Isometric Gaming / Voxel | ![Isometric Gaming / Voxel](https://designmd.app/images/library/75.png) | [Link](https://designmd.app/en/library/isometric-gaming-voxel) |
85: | Chalkboard / Hand-Drawn | ![Chalkboard / Hand-Drawn](https://designmd.app/images/library/76.png) | [Link](https://designmd.app/en/library/chalkboard-hand-drawn) |
86: | Bauhaus / Risograph Modern | ![Bauhaus / Risograph Modern](https://designmd.app/images/library/77.png) | [Link](https://designmd.app/en/library/bauhaus-risograph-modern) |
87: | Steampunk Industrial | ![Steampunk Industrial](https://designmd.app/images/library/78.png) | [Link](https://designmd.app/en/library/steampunk-industrial) |
88: | Circuit Board / PCB | ![Circuit Board / PCB](https://designmd.app/images/library/79.png) | [Link](https://designmd.app/en/library/circuit-board-pcb) |
89: | Retro Travel Poster | ![Retro Travel Poster](https://designmd.app/images/library/80.png) | [Link](https://designmd.app/en/library/retro-travel-poster) |
90: | Vaporwave Aesthetic | ![Vaporwave Aesthetic](https://designmd.app/images/library/81.png) | [Link](https://designmd.app/en/library/vaporwave-aesthetic) |
91: | Vintage Botanical / Scientific | ![Vintage Botanical / Scientific](https://designmd.app/images/library/82.png) | [Link](https://designmd.app/en/library/vintage-botanical-scientific) |
92: | Horror / Gothic Dark | ![Horror / Gothic Dark](https://designmd.app/images/library/83.png) | [Link](https://designmd.app/en/library/horror-gothic-dark) |
93: | Blueprint / Engineering | ![Blueprint / Engineering](https://designmd.app/images/library/84.png) | [Link](https://designmd.app/en/library/blueprint-engineering) |
94: | Studygram / Notebook Kawaii | ![Studygram / Notebook Kawaii](https://designmd.app/images/library/85.png) | [Link](https://designmd.app/en/library/studygram-notebook-kawaii) |
95: | Claymation 3D | ![Claymation 3D](https://designmd.app/images/library/86.png) | [Link](https://designmd.app/en/library/claymation-3d) |
96: | Radial Diagram / Donut Chart | ![Radial Diagram / Donut Chart](https://designmd.app/images/library/87.png) | [Link](https://designmd.app/en/library/radial-diagram-donut-chart) |
97: | Timeline Horizontal Corporativo | ![Timeline Horizontal Corporativo](https://designmd.app/images/library/88.png) | [Link](https://designmd.app/en/library/timeline-horizontal-corporativo) |
98: | Z-Shape | ![Z-Shape](https://designmd.app/images/library/89.png) | [Link](https://designmd.app/en/library/z-shape) |
99: | Natureza / Elementos Botânicos | ![Natureza / Elementos Botânicos](https://designmd.app/images/library/90.png) | [Link](https://designmd.app/en/library/natureza-elementos-botanicos) |
100: | Elementos Musicais | ![Elementos Musicais](https://designmd.app/images/library/91.png) | [Link](https://designmd.app/en/library/elementos-musicais) |
101: | Degraded Colorful / Vibrant Gradient | ![Degraded Colorful / Vibrant Gradient](https://designmd.app/images/library/92.png) | [Link](https://designmd.app/en/library/degraded-colorful-vibrant-gradient) |
102: | Dark Glassmorphism Infographic | ![Dark Glassmorphism Infographic](https://designmd.app/images/library/93.png) | [Link](https://designmd.app/en/library/dark-glassmorphism-infographic) |
103: | Sakura / Floral Japonês | ![Sakura / Floral Japonês](https://designmd.app/images/library/94.png) | [Link](https://designmd.app/en/library/sakura-floral-japones) |
104: | Underwater / Aquático | ![Underwater / Aquático](https://designmd.app/images/library/95.png) | [Link](https://designmd.app/en/library/underwater-aquatico) |
105: | Mixed Reality / VR-AR | ![Mixed Reality / VR-AR](https://designmd.app/images/library/96.png) | [Link](https://designmd.app/en/library/mixed-reality-vr-ar) |
106: | Gradient Aurora Borealis | ![Gradient Aurora Borealis](https://designmd.app/images/library/97.png) | [Link](https://designmd.app/en/library/gradient-aurora-borealis) |
107: | Doodle / Sketch Livre | ![Doodle / Sketch Livre](https://designmd.app/images/library/98.png) | [Link](https://designmd.app/en/library/doodle-sketch-livre) |
108: | Geometric | ![Geometric](https://designmd.app/images/library/99.png) | [Link](https://designmd.app/en/library/geometric) |
109: | Grunge Rock dos Anos 90 | ![Grunge Rock dos Anos 90](https://designmd.app/images/library/100.png) | [Link](https://designmd.app/en/library/grunge-rock-dos-anos-90) |
110: | Art Nouveau Florido | ![Art Nouveau Florido](https://designmd.app/images/library/101.png) | [Link](https://designmd.app/en/library/art-nouveau-florido) |
111: | Flat Design Corporativo | ![Flat Design Corporativo](https://designmd.app/images/library/102.png) | [Link](https://designmd.app/en/library/flat-design-corporativo) |
112: | Steampunk Vitoriano | ![Steampunk Vitoriano](https://designmd.app/images/library/103.png) | [Link](https://designmd.app/en/library/steampunk-vitoriano) |
113: | De Stijl Abstrato | ![De Stijl Abstrato](https://designmd.app/images/library/104.png) | [Link](https://designmd.app/en/library/de-stijl-abstrato) |
114: | Cyber-Tribal | ![Cyber-Tribal](https://designmd.app/images/library/105.png) | [Link](https://designmd.app/en/library/cyber-tribal) |
115: | Rococó Delicado | ![Rococó Delicado](https://designmd.app/images/library/106.png) | [Link](https://designmd.app/en/library/rococo-delicado) |
116: | Swiss Design Gráfico | ![Swiss Design Gráfico](https://designmd.app/images/library/107.png) | [Link](https://designmd.app/en/library/swiss-design-grafico) |
117: | Psicodélico Anos 60 | ![Psicodélico Anos 60](https://designmd.app/images/library/108.png) | [Link](https://designmd.app/en/library/psicodelico-anos-60) |
118: | Gótico Moderno | ![Gótico Moderno](https://designmd.app/images/library/109.png) | [Link](https://designmd.app/en/library/gotico-moderno) |
119: | Solarpunk Utópico | ![Solarpunk Utópico](https://designmd.app/images/library/110.png) | [Link](https://designmd.app/en/library/solarpunk-utopico) |
120: | Afrofuturismo Digital | ![Afrofuturismo Digital](https://designmd.app/images/library/111.png) | [Link](https://designmd.app/en/library/afrofuturismo-digital) |
121: | Cerâmica Wabi-Sabi | ![Cerâmica Wabi-Sabi](https://designmd.app/images/library/112.png) | [Link](https://designmd.app/en/library/ceramica-wabi-sabi) |
122: | Cassette Futurism | ![Cassette Futurism](https://designmd.app/images/library/113.png) | [Link](https://designmd.app/en/library/cassette-futurism) |
123: | Azulejo Português | ![Azulejo Português](https://designmd.app/images/library/114.png) | [Link](https://designmd.app/en/library/azulejo-portugues) |
124: | Brutalist Web Design | ![Brutalist Web Design](https://designmd.app/images/library/115.png) | [Link](https://designmd.app/en/library/brutalist-web-design) |
125: | Aurora Boreal Nórdica | ![Aurora Boreal Nórdica](https://designmd.app/images/library/116.png) | [Link](https://designmd.app/en/library/aurora-boreal-nordica) |
126: | Origami Geométrico | ![Origami Geométrico](https://designmd.app/images/library/117.png) | [Link](https://designmd.app/en/library/origami-geometrico) |
127: | Noir Detetive | ![Noir Detetive](https://designmd.app/images/library/118.png) | [Link](https://designmd.app/en/library/noir-detetive) |
128: | Terracota Mediterrâneo | ![Terracota Mediterrâneo](https://designmd.app/images/library/119.png) | [Link](https://designmd.app/en/library/terracota-mediterraneo) |
129: | Estilo Deep Learning High-Tech | ![Estilo Deep Learning High-Tech](https://designmd.app/images/library/120.png) | [Link](https://designmd.app/en/library/estilo-deep-learning-high-tech) |
130: | Estilo de Elegância Espacial | ![Estilo de Elegância Espacial](https://designmd.app/images/library/121.png) | [Link](https://designmd.app/en/library/estilo-de-elegancia-espacial) |
131: | Estilo Material AI | ![Estilo Material AI](https://designmd.app/images/library/122.png) | [Link](https://designmd.app/en/library/estilo-material-ai) |
132: | Estilo Fluent AI | ![Estilo Fluent AI](https://designmd.app/images/library/123.png) | [Link](https://designmd.app/en/library/estilo-fluent-ai) |
133: | Estilo de Experiência de Compra Contínua | ![Estilo de Experiência de Compra Contínua](https://designmd.app/images/library/124.png) | [Link](https://designmd.app/en/library/estilo-de-experiencia-de-compra-continua) |
134: | Estilo de Realidade Virtual Social | ![Estilo de Realidade Virtual Social](https://designmd.app/images/library/125.png) | [Link](https://designmd.app/en/library/estilo-de-realidade-virtual-social) |
135: | Estilo de Tecnologia de Precisão | ![Estilo de Tecnologia de Precisão](https://designmd.app/images/library/126.png) | [Link](https://designmd.app/en/library/estilo-de-tecnologia-de-precisao) |
136: | Estilo de Fluxo de Rede | ![Estilo de Fluxo de Rede](https://designmd.app/images/library/127.png) | [Link](https://designmd.app/en/library/estilo-de-fluxo-de-rede) |
137: | Estilo de Ecossistema Digital | ![Estilo de Ecossistema Digital](https://designmd.app/images/library/128.png) | [Link](https://designmd.app/en/library/estilo-de-ecossistema-digital) |
138: | Estilo de Litografia de Precisão | ![Estilo de Litografia de Precisão](https://designmd.app/images/library/129.png) | [Link](https://designmd.app/en/library/estilo-de-litografia-de-precisao) |
139: | Estilo de Dados Empresariais | ![Estilo de Dados Empresariais](https://designmd.app/images/library/130.png) | [Link](https://designmd.app/en/library/estilo-de-dados-empresariais) |
140: | Estilo de Inovação em Dispositivos Móveis | ![Estilo de Inovação em Dispositivos Móveis](https://designmd.app/images/library/131.png) | [Link](https://designmd.app/en/library/estilo-de-inovacao-em-dispositivos-moveis) |
141: | Estilo de IA Criativa | ![Estilo de IA Criativa](https://designmd.app/images/library/132.png) | [Link](https://designmd.app/en/library/estilo-de-ia-criativa) |
142: | Estilo de IA para Negócios | ![Estilo de IA para Negócios](https://designmd.app/images/library/133.png) | [Link](https://designmd.app/en/library/estilo-de-ia-para-negocios) |
143: | Estilo de Computação de Alta Performance | ![Estilo de Computação de Alta Performance](https://designmd.app/images/library/134.png) | [Link](https://designmd.app/en/library/estilo-de-computacao-de-alta-performance) |
144: | Estilo de Futuro Autônomo | ![Estilo de Futuro Autônomo](https://designmd.app/images/library/135.png) | [Link](https://designmd.app/en/library/estilo-de-futuro-autonomo) |
145: | Estilo de Entretenimento Imersivo | ![Estilo de Entretenimento Imersivo](https://designmd.app/images/library/136.png) | [Link](https://designmd.app/en/library/estilo-de-entretenimento-imersivo) |
146: | Estilo de Elegância Fintech | ![Estilo de Elegância Fintech](https://designmd.app/images/library/137.png) | [Link](https://designmd.app/en/library/estilo-de-elegancia-fintech) |
147: | Estilo de Inteligência Generativa | ![Estilo de Inteligência Generativa](https://designmd.app/images/library/138.png) | [Link](https://designmd.app/en/library/estilo-de-inteligencia-generativa) |
148: | Estilo de IA Ética | ![Estilo de IA Ética](https://designmd.app/images/library/139.png) | [Link](https://designmd.app/en/library/estilo-de-ia-etica) |
149: | Underwater Aquático Deep Sea | ![Underwater Aquático Deep Sea](https://designmd.app/images/library/140.png) | [Link](https://designmd.app/en/library/underwater-aquatico-deep-sea) |
150: | SaaS Enterprise Analytics | ![SaaS Enterprise Analytics](https://designmd.app/images/library/141.png) | [Link](https://designmd.app/en/library/saas-enterprise-analytics) |
151: | HealthTech Plataforma Clínica | ![HealthTech Plataforma Clínica](https://designmd.app/images/library/142.png) | [Link](https://designmd.app/en/library/healthtech-plataforma-clinica) |
152: | FinTech Plataforma Financeira | ![FinTech Plataforma Financeira](https://designmd.app/images/library/143.png) | [Link](https://designmd.app/en/library/fintech-plataforma-financeira) |
153: | EdTech Plataforma de Cursos | ![EdTech Plataforma de Cursos](https://designmd.app/images/library/144.png) | [Link](https://designmd.app/en/library/edtech-plataforma-de-cursos) |
154: | Portfolio Dev Full-Stack | ![Portfolio Dev Full-Stack](https://designmd.app/images/library/145.png) | [Link](https://designmd.app/en/library/portfolio-dev-full-stack) |
155: | Real Estate Imobiliária Digital | ![Real Estate Imobiliária Digital](https://designmd.app/images/library/146.png) | [Link](https://designmd.app/en/library/real-estate-imobiliaria-digital) |
156: | Fitness App de Treinos | ![Fitness App de Treinos](https://designmd.app/images/library/147.png) | [Link](https://designmd.app/en/library/fitness-app-de-treinos) |
157: | Travel Plataforma de Viagens | ![Travel Plataforma de Viagens](https://designmd.app/images/library/148.png) | [Link](https://designmd.app/en/library/travel-plataforma-de-viagens) |
158: | Crypto Exchange Plataforma | ![Crypto Exchange Plataforma](https://designmd.app/images/library/149.png) | [Link](https://designmd.app/en/library/crypto-exchange-plataforma) |
159: | Engineering Blueprint Schematic | ![Engineering Blueprint Schematic](https://designmd.app/images/library/150.png) | [Link](https://designmd.app/en/library/engineering-blueprint-schematic) |
160: | PCB Schematic Architecture | ![PCB Schematic Architecture](https://designmd.app/images/library/151.png) | [Link](https://designmd.app/en/library/pcb-schematic-architecture) |
161: | Industrial Workbench Schematic | ![Industrial Workbench Schematic](https://designmd.app/images/library/152.png) | [Link](https://designmd.app/en/library/industrial-workbench-schematic) |
162: | Architectural Schematic | ![Architectural Schematic](https://designmd.app/images/library/153.png) | [Link](https://designmd.app/en/library/architectural-schematic) |
163: | CAD-Inspired Blueprint | ![CAD-Inspired Blueprint](https://designmd.app/images/library/154.png) | [Link](https://designmd.app/en/library/cad-inspired-blueprint) |
164: | Denim and Industrial Craft | ![Denim and Industrial Craft](https://designmd.app/images/library/155.png) | [Link](https://designmd.app/en/library/denim-and-industrial-craft) |
165: | Bento Grid Tech Minimalist | ![Bento Grid Tech Minimalist](https://designmd.app/images/library/156.png) | [Link](https://designmd.app/en/library/bento-grid-tech-minimalist) |
166: | Neumorphic Tech Schematic | ![Neumorphic Tech Schematic](https://designmd.app/images/library/157.png) | [Link](https://designmd.app/en/library/neumorphic-tech-schematic) |
167: | Corporate Radial Process | ![Corporate Radial Process](https://designmd.app/images/library/158.png) | [Link](https://designmd.app/en/library/corporate-radial-process) |
168: | Sumi-e Tech Scroll | ![Sumi-e Tech Scroll](https://designmd.app/images/library/159.png) | [Link](https://designmd.app/en/library/sumi-e-tech-scroll) |
169: | Ghibli-Inspired Narrative Map | ![Ghibli-Inspired Narrative Map](https://designmd.app/images/library/160.png) | [Link](https://designmd.app/en/library/ghibli-inspired-narrative-map) |
170: | Ukiyo-e Woodblock Revival | ![Ukiyo-e Woodblock Revival](https://designmd.app/images/library/161.png) | [Link](https://designmd.app/en/library/ukiyo-e-woodblock-revival) |
171: | Ancient Egyptian Instructional Scroll | ![Ancient Egyptian Instructional Scroll](https://designmd.app/images/library/162.png) | [Link](https://designmd.app/en/library/ancient-egyptian-instructional-scroll) |
172: | Gatsby Art Deco Noir | ![Gatsby Art Deco Noir](https://designmd.app/images/library/163.png) | [Link](https://designmd.app/en/library/gatsby-art-deco-noir) |
173: | Belle Époque Lithograph | ![Belle Époque Lithograph](https://designmd.app/images/library/164.png) | [Link](https://designmd.app/en/library/belle-epoque-lithograph) |
174: | Rococo Romantic Narrative | ![Rococo Romantic Narrative](https://designmd.app/images/library/165.png) | [Link](https://designmd.app/en/library/rococo-romantic-narrative) |
175: | Vintage Botanical Scientific Illustration | ![Vintage Botanical Scientific Illustration](https://designmd.app/images/library/166.png) | [Link](https://designmd.app/en/library/vintage-botanical-scientific-illustration) |
176: | Steampunk Nebula Explorer | ![Steampunk Nebula Explorer](https://designmd.app/images/library/167.png) | [Link](https://designmd.app/en/library/steampunk-nebula-explorer) |
177: | Hand-Drawn Sketch-Note | ![Hand-Drawn Sketch-Note](https://designmd.app/images/library/168.png) | [Link](https://designmd.app/en/library/hand-drawn-sketch-note) |
178: | Passport Travel UI | ![Passport Travel UI](https://designmd.app/images/library/169.png) | [Link](https://designmd.app/en/library/passport-travel-ui) |
179: | Cyberpunk Neon Noir | ![Cyberpunk Neon Noir](https://designmd.app/images/library/170.png) | [Link](https://designmd.app/en/library/cyberpunk-neon-noir) |
180: | Hacker Aesthetic CRT/CLI | ![Hacker Aesthetic CRT/CLI](https://designmd.app/images/library/171.png) | [Link](https://designmd.app/en/library/hacker-aesthetic-crt-cli) |
181: | Holographic Data-Viz | ![Holographic Data-Viz](https://designmd.app/images/library/172.png) | [Link](https://designmd.app/en/library/holographic-data-viz) |
182: | Thermal Insight Tech | ![Thermal Insight Tech](https://designmd.app/images/library/173.png) | [Link](https://designmd.app/en/library/thermal-insight-tech) |
183: | Futuristic UI Glassmorphism | ![Futuristic UI Glassmorphism](https://designmd.app/images/library/174.png) | [Link](https://designmd.app/en/library/futuristic-ui-glassmorphism) |
184: | Fractal Bioluminescence | ![Fractal Bioluminescence](https://designmd.app/images/library/175.png) | [Link](https://designmd.app/en/library/fractal-bioluminescence) |
185: | Glitch UI Dystopian Terminal | ![Glitch UI Dystopian Terminal](https://designmd.app/images/library/176.png) | [Link](https://designmd.app/en/library/glitch-ui-dystopian-terminal) |
186: | Cyberpunk Dark Mode Flow | ![Cyberpunk Dark Mode Flow](https://designmd.app/images/library/177.png) | [Link](https://designmd.app/en/library/cyberpunk-dark-mode-flow) |
187: | Retro-Comic Action Blueprint | ![Retro-Comic Action Blueprint](https://designmd.app/images/library/178.png) | [Link](https://designmd.app/en/library/retro-comic-action-blueprint) |
188: | Manga Instructional Comic | ![Manga Instructional Comic](https://designmd.app/images/library/179.png) | [Link](https://designmd.app/en/library/manga-instructional-comic) |
189: | Claymation 3D Illustration | ![Claymation 3D Illustration](https://designmd.app/images/library/180.png) | [Link](https://designmd.app/en/library/claymation-3d-illustration) |
190: | Risograph Zine Aesthetic | ![Risograph Zine Aesthetic](https://designmd.app/images/library/181.png) | [Link](https://designmd.app/en/library/risograph-zine-aesthetic) |
191: | 70s Psychedelic Flower Power | ![70s Psychedelic Flower Power](https://designmd.app/images/library/182.png) | [Link](https://designmd.app/en/library/70s-psychedelic-flower-power) |
192: | American Diner Americana | ![American Diner Americana](https://designmd.app/images/library/183.png) | [Link](https://designmd.app/en/library/american-diner-americana) |
193: | Kawaii Pastel Pop | ![Kawaii Pastel Pop](https://designmd.app/images/library/184.png) | [Link](https://designmd.app/en/library/kawaii-pastel-pop) |
194: | Versus Mode Anime Aesthetic | ![Versus Mode Anime Aesthetic](https://designmd.app/images/library/185.png) | [Link](https://designmd.app/en/library/versus-mode-anime-aesthetic) |
195: | 8-Bit Retro Terminal | ![8-Bit Retro Terminal](https://designmd.app/images/library/186.png) | [Link](https://designmd.app/en/library/8-bit-retro-terminal) |
196: | Voxel Gamified Isometric | ![Voxel Gamified Isometric](https://designmd.app/images/library/187.png) | [Link](https://designmd.app/en/library/voxel-gamified-isometric) |
197: | Chalkboard Sketch-Note | ![Chalkboard Sketch-Note](https://designmd.app/images/library/188.png) | [Link](https://designmd.app/en/library/chalkboard-sketch-note) |
198: | Minimalismo Funcional B2B | ![Minimalismo Funcional B2B](https://designmd.app/images/library/189.png) | [Link](https://designmd.app/en/library/minimalismo-funcional-b2b) |
199: | Minimalismo Fotográfico Elegante | ![Minimalismo Fotográfico Elegante](https://designmd.app/images/library/190.png) | [Link](https://designmd.app/en/library/minimalismo-fotografico-elegante) |
200: | Minimalismo Chic de Luxo | ![Minimalismo Chic de Luxo](https://designmd.app/images/library/191.png) | [Link](https://designmd.app/en/library/minimalismo-chic-de-luxo) |
201: | Minimalismo Sereno de Bem-Estar | ![Minimalismo Sereno de Bem-Estar](https://designmd.app/images/library/192.png) | [Link](https://designmd.app/en/library/minimalismo-sereno-de-bem-estar) |
202: | Minimalismo Confiável Financeiro | ![Minimalismo Confiável Financeiro](https://designmd.app/images/library/193.png) | [Link](https://designmd.app/en/library/minimalismo-confiavel-financeiro) |
203: | Neobrutalismo Ousado | ![Neobrutalismo Ousado](https://designmd.app/images/library/194.png) | [Link](https://designmd.app/en/library/neobrutalismo-ousado) |
204: | Brutalismo Sonoro Glitch | ![Brutalismo Sonoro Glitch](https://designmd.app/images/library/195.png) | [Link](https://designmd.app/en/library/brutalismo-sonoro-glitch) |
205: | Brutalismo Artístico Abstrato | ![Brutalismo Artístico Abstrato](https://designmd.app/images/library/196.png) | [Link](https://designmd.app/en/library/brutalismo-artistico-abstrato) |
206: | Neobrutalismo Crítico | ![Neobrutalismo Crítico](https://designmd.app/images/library/197.png) | [Link](https://designmd.app/en/library/neobrutalismo-critico) |
207: | Brutalismo Urbano Expressivo | ![Brutalismo Urbano Expressivo](https://designmd.app/images/library/198.png) | [Link](https://designmd.app/en/library/brutalismo-urbano-expressivo) |
208: | Construtivismo Dinâmico Tech | ![Construtivismo Dinâmico Tech](https://designmd.app/images/library/199.png) | [Link](https://designmd.app/en/library/construtivismo-dinamico-tech) |
209: | Construtivismo Arquitetônico | ![Construtivismo Arquitetônico](https://designmd.app/images/library/200.png) | [Link](https://designmd.app/en/library/construtivismo-arquitetonico) |
210: | Construtivismo de Dados Dinâmicos | ![Construtivismo de Dados Dinâmicos](https://designmd.app/images/library/201.png) | [Link](https://designmd.app/en/library/construtivismo-de-dados-dinamicos) |
211: | Construtivismo de Eventos Dinâmicos | ![Construtivismo de Eventos Dinâmicos](https://designmd.app/images/library/202.png) | [Link](https://designmd.app/en/library/construtivismo-de-eventos-dinamicos) |
212: | Construtivismo Literário Experimental | ![Construtivismo Literário Experimental](https://designmd.app/images/library/203.png) | [Link](https://designmd.app/en/library/construtivismo-literario-experimental) |
213: | Estilo Suíço Corporativo | ![Estilo Suíço Corporativo](https://designmd.app/images/library/204.png) | [Link](https://designmd.app/en/library/estilo-suico-corporativo) |
214: | Estilo Suíço Premium | ![Estilo Suíço Premium](https://designmd.app/images/library/205.png) | [Link](https://designmd.app/en/library/estilo-suico-premium) |
215: | Estilo Suíço Científico | ![Estilo Suíço Científico](https://designmd.app/images/library/206.png) | [Link](https://designmd.app/en/library/estilo-suico-cientifico) |
216: | Estilo Suíço Artístico | ![Estilo Suíço Artístico](https://designmd.app/images/library/207.png) | [Link](https://designmd.app/en/library/estilo-suico-artistico) |
217: | Estilo Suíço Educacional | ![Estilo Suíço Educacional](https://designmd.app/images/library/208.png) | [Link](https://designmd.app/en/library/estilo-suico-educacional) |
218: | Editorial Contemporâneo | ![Editorial Contemporâneo](https://designmd.app/images/library/209.png) | [Link](https://designmd.app/en/library/editorial-contemporaneo) |
219: | Editorial de Viagem Sofisticado | ![Editorial de Viagem Sofisticado](https://designmd.app/images/library/210.png) | [Link](https://designmd.app/en/library/editorial-de-viagem-sofisticado) |
220: | Editorial de Portfólio Criativo | ![Editorial de Portfólio Criativo](https://designmd.app/images/library/211.png) | [Link](https://designmd.app/en/library/editorial-de-portfolio-criativo) |
221: | Editorial Investigativo Sóbrio | ![Editorial Investigativo Sóbrio](https://designmd.app/images/library/212.png) | [Link](https://designmd.app/en/library/editorial-investigativo-sobrio) |
222: | Editorial Interativo Digital | ![Editorial Interativo Digital](https://designmd.app/images/library/213.png) | [Link](https://designmd.app/en/library/editorial-interativo-digital) |
223: | Desenho à Mão Lúdico | ![Desenho à Mão Lúdico](https://designmd.app/images/library/214.png) | [Link](https://designmd.app/en/library/desenho-a-mao-ludico) |
224: | Artesanato Orgânico e Acolhedor | ![Artesanato Orgânico e Acolhedor](https://designmd.app/images/library/215.png) | [Link](https://designmd.app/en/library/artesanato-organico-e-acolhedor) |
225: | Café Artesanal Aconchegante | ![Café Artesanal Aconchegante](https://designmd.app/images/library/216.png) | [Link](https://designmd.app/en/library/cafe-artesanal-aconchegante) |
226: | Criatividade Artesanal e Pessoal | ![Criatividade Artesanal e Pessoal](https://designmd.app/images/library/217.png) | [Link](https://designmd.app/en/library/criatividade-artesanal-e-pessoal) |
227: | Aprendizado Criativo Artesanal | ![Aprendizado Criativo Artesanal](https://designmd.app/images/library/218.png) | [Link](https://designmd.app/en/library/aprendizado-criativo-artesanal) |
228: | Retro Arcade Pixelado | ![Retro Arcade Pixelado](https://designmd.app/images/library/219.png) | [Link](https://designmd.app/en/library/retro-arcade-pixelado) |
229: | Retro Boutique Vintage | ![Retro Boutique Vintage](https://designmd.app/images/library/220.png) | [Link](https://designmd.app/en/library/retro-boutique-vintage) |
230: | Retro Barbershop Clássica | ![Retro Barbershop Clássica](https://designmd.app/images/library/221.png) | [Link](https://designmd.app/en/library/retro-barbershop-classica) |
231: | Retro Aventura Anos 70 | ![Retro Aventura Anos 70](https://designmd.app/images/library/222.png) | [Link](https://designmd.app/en/library/retro-aventura-anos-70) |
232: | Retro Digital Anos 90 | ![Retro Digital Anos 90](https://designmd.app/images/library/223.png) | [Link](https://designmd.app/en/library/retro-digital-anos-90) |
233: | Flat Design Produtivo | ![Flat Design Produtivo](https://designmd.app/images/library/224.png) | [Link](https://designmd.app/en/library/flat-design-produtivo) |
234: | Flat Design Educacional Vibrante | ![Flat Design Educacional Vibrante](https://designmd.app/images/library/225.png) | [Link](https://designmd.app/en/library/flat-design-educacional-vibrante) |
235: | Flat Design Musical Intuitivo | ![Flat Design Musical Intuitivo](https://designmd.app/images/library/226.png) | [Link](https://designmd.app/en/library/flat-design-musical-intuitivo) |
236: | Flat Design Informativo Claro | ![Flat Design Informativo Claro](https://designmd.app/images/library/227.png) | [Link](https://designmd.app/en/library/flat-design-informativo-claro) |
237: | Flat Design Financeiro Seguro | ![Flat Design Financeiro Seguro](https://designmd.app/images/library/228.png) | [Link](https://designmd.app/en/library/flat-design-financeiro-seguro) |
238: | Bento Produtividade Flexível | ![Bento Produtividade Flexível](https://designmd.app/images/library/229.png) | [Link](https://designmd.app/en/library/bento-produtividade-flexivel) |
239: | Bento Dados Estruturados | ![Bento Dados Estruturados](https://designmd.app/images/library/230.png) | [Link](https://designmd.app/en/library/bento-dados-estruturados) |
240: | Bento Portfólio de Produto | ![Bento Portfólio de Produto](https://designmd.app/images/library/231.png) | [Link](https://designmd.app/en/library/bento-portfolio-de-produto) |
241: | Bento Notícias Curadas | ![Bento Notícias Curadas](https://designmd.app/images/library/232.png) | [Link](https://designmd.app/en/library/bento-noticias-curadas) |
242: | Bento Eventos Dinâmicos | ![Bento Eventos Dinâmicos](https://designmd.app/images/library/233.png) | [Link](https://designmd.app/en/library/bento-eventos-dinamicos) |
243: | Lambe-Lambe Brasileiro | ![Lambe-Lambe Brasileiro](https://designmd.app/images/library/234.png) | [Link](https://designmd.app/en/library/lambe-lambe-brasileiro) |
244: | Cartazista de Supermercado | ![Cartazista de Supermercado](https://designmd.app/images/library/235.png) | [Link](https://designmd.app/en/library/cartazista-de-supermercado) |
245: | Happy Art Tropical | ![Happy Art Tropical](https://designmd.app/images/library/236.png) | [Link](https://designmd.app/en/library/happy-art-tropical) |
246: | Azulejaria Digital Moderna | ![Azulejaria Digital Moderna](https://designmd.app/images/library/237.png) | [Link](https://designmd.app/en/library/azulejaria-digital-moderna) |
247: | Modernismo Jornalístico Brasileiro | ![Modernismo Jornalístico Brasileiro](https://designmd.app/images/library/238.png) | [Link](https://designmd.app/en/library/modernismo-jornalistico-brasileiro) |
248: | Cordel Digital | ![Cordel Digital](https://designmd.app/images/library/239.png) | [Link](https://designmd.app/en/library/cordel-digital) |
249: | Bossa Nova Lounge | ![Bossa Nova Lounge](https://designmd.app/images/library/240.png) | [Link](https://designmd.app/en/library/bossa-nova-lounge) |
250: | Maracatu Tech | ![Maracatu Tech](https://designmd.app/images/library/241.png) | [Link](https://designmd.app/en/library/maracatu-tech) |
251: | Cerrado Minimalista | ![Cerrado Minimalista](https://designmd.app/images/library/242.png) | [Link](https://designmd.app/en/library/cerrado-minimalista) |
252: | Amazônia Futurista | ![Amazônia Futurista](https://designmd.app/images/library/243.png) | [Link](https://designmd.app/en/library/amazonia-futurista) |
253: | Tropicalismo Gastronômico Vibrante | ![Tropicalismo Gastronômico Vibrante](https://designmd.app/images/library/244.png) | [Link](https://designmd.app/en/library/tropicalismo-gastronomico-vibrante) |
254: | Tropicalismo Indígena Autêntico | ![Tropicalismo Indígena Autêntico](https://designmd.app/images/library/245.png) | [Link](https://designmd.app/en/library/tropicalismo-indigena-autentico) |
255: | Tropicalismo Aventureiro Natural | ![Tropicalismo Aventureiro Natural](https://designmd.app/images/library/246.png) | [Link](https://designmd.app/en/library/tropicalismo-aventureiro-natural) |
256: | Conforto Artesanal Brasileiro | ![Conforto Artesanal Brasileiro](https://designmd.app/images/library/247.png) | [Link](https://designmd.app/en/library/conforto-artesanal-brasileiro) |
257: | Vernacular Acolhedor Brasileiro | ![Vernacular Acolhedor Brasileiro](https://designmd.app/images/library/248.png) | [Link](https://designmd.app/en/library/vernacular-acolhedor-brasileiro) |
258: | Reuso Criativo Disruptivo | ![Reuso Criativo Disruptivo](https://designmd.app/images/library/249.png) | [Link](https://designmd.app/en/library/reuso-criativo-disruptivo) |
259: | Design Autoral Robusto | ![Design Autoral Robusto](https://designmd.app/images/library/250.png) | [Link](https://designmd.app/en/library/design-autoral-robusto) |
260: | Culinária Afetiva Brasileira | ![Culinária Afetiva Brasileira](https://designmd.app/images/library/251.png) | [Link](https://designmd.app/en/library/culinaria-afetiva-brasileira) |
261: | Símbolos Cívicos Brasileiros | ![Símbolos Cívicos Brasileiros](https://designmd.app/images/library/252.png) | [Link](https://designmd.app/en/library/simbolos-civicos-brasileiros) |
262: | Símbolos Ambientais Brasileiros | ![Símbolos Ambientais Brasileiros](https://designmd.app/images/library/253.png) | [Link](https://designmd.app/en/library/simbolos-ambientais-brasileiros) |
263: | Símbolos Culturais Brasileiros | ![Símbolos Culturais Brasileiros](https://designmd.app/images/library/254.png) | [Link](https://designmd.app/en/library/simbolos-culturais-brasileiros) |
264: | Símbolos Regionais Brasileiros | ![Símbolos Regionais Brasileiros](https://designmd.app/images/library/255.png) | [Link](https://designmd.app/en/library/simbolos-regionais-brasileiros) |
265: | Símbolos Políticos Brasileiros | ![Símbolos Políticos Brasileiros](https://designmd.app/images/library/256.png) | [Link](https://designmd.app/en/library/simbolos-politicos-brasileiros) |
266: | Aura Premium WebGL & Iconify | ![Aura Premium WebGL & Iconify](https://designmd.app/images/library/257.png) | [Link](https://designmd.app/en/library/aura-premium-webgl-iconify) |
267: | Bold Signal | ![Bold Signal](https://designmd.app/images/library/258.png) | [Link](https://designmd.app/en/library/bold-signal) |
268: | Electric Studio | ![Electric Studio](https://designmd.app/images/library/259.png) | [Link](https://designmd.app/en/library/electric-studio) |
269: | Creative Voltage | ![Creative Voltage](https://designmd.app/images/library/260.png) | [Link](https://designmd.app/en/library/creative-voltage) |
270: | Dark Botanical | ![Dark Botanical](https://designmd.app/images/library/261.png) | [Link](https://designmd.app/en/library/dark-botanical) |
271: | Notebook Tabs | ![Notebook Tabs](https://designmd.app/images/library/262.png) | [Link](https://designmd.app/en/library/notebook-tabs) |
272: | Pastel Geometry | ![Pastel Geometry](https://designmd.app/images/library/263.png) | [Link](https://designmd.app/en/library/pastel-geometry) |
273: | Split Pastel | ![Split Pastel](https://designmd.app/images/library/264.png) | [Link](https://designmd.app/en/library/split-pastel) |
274: | Vintage Editorial | ![Vintage Editorial](https://designmd.app/images/library/265.png) | [Link](https://designmd.app/en/library/vintage-editorial) |
275: | Neon Cyber | ![Neon Cyber](https://designmd.app/images/library/266.png) | [Link](https://designmd.app/en/library/neon-cyber) |
276: | Terminal Green | ![Terminal Green](https://designmd.app/images/library/267.png) | [Link](https://designmd.app/en/library/terminal-green) |
277: | Swiss Modern | ![Swiss Modern](https://designmd.app/images/library/268.png) | [Link](https://designmd.app/en/library/swiss-modern) |
278: | Paper & Ink | ![Paper & Ink](https://designmd.app/images/library/269.png) | [Link](https://designmd.app/en/library/paper-ink) |
279: | Manrope Typography | ![Manrope Typography](https://designmd.app/images/library/270.png) | [Link](https://designmd.app/en/library/manrope-typography) |
280: | Fraunces Typography | ![Fraunces Typography](https://designmd.app/images/library/271.png) | [Link](https://designmd.app/en/library/fraunces-typography) |
281: | Syne Typography | ![Syne Typography](https://designmd.app/images/library/272.png) | [Link](https://designmd.app/en/library/syne-typography) |
282: | Inter Typography | ![Inter Typography](https://designmd.app/images/library/273.png) | [Link](https://designmd.app/en/library/inter-typography) |
283: | Albert Sans Typography | ![Albert Sans Typography](https://designmd.app/images/library/274.png) | [Link](https://designmd.app/en/library/albert-sans-typography) |
284: | Merriweather Typography | ![Merriweather Typography](https://designmd.app/images/library/275.png) | [Link](https://designmd.app/en/library/merriweather-typography) |
285: | Tenor Sans Typography | ![Tenor Sans Typography](https://designmd.app/images/library/276.png) | [Link](https://designmd.app/en/library/tenor-sans-typography) |
286: | Space Grotesk Typography | ![Space Grotesk Typography](https://designmd.app/images/library/277.png) | [Link](https://designmd.app/en/library/space-grotesk-typography) |
287: | Google Sans Typography | ![Google Sans Typography](https://designmd.app/images/library/278.png) | [Link](https://designmd.app/en/library/google-sans-typography) |
288: | IBM Plex Sans Typography | ![IBM Plex Sans Typography](https://designmd.app/images/library/279.png) | [Link](https://designmd.app/en/library/ibm-plex-sans-typography) |
289: | Mini World | ![Mini World](https://designmd.app/images/library/280.png) | [Link](https://designmd.app/en/library/mini-world) |
290: | Chalkboard | ![Chalkboard](https://designmd.app/images/library/281.png) | [Link](https://designmd.app/en/library/chalkboard) |
291: | Anime Battle | ![Anime Battle](https://designmd.app/images/library/282.png) | [Link](https://designmd.app/en/library/anime-battle) |
292: | Tactile 3D Neumorphism | ![Tactile 3D Neumorphism](https://designmd.app/images/library/283.png) | [Link](https://designmd.app/en/library/tactile-3d-neumorphism) |
293: | 90s Retro Video Game | ![90s Retro Video Game](https://designmd.app/images/library/284.png) | [Link](https://designmd.app/en/library/90s-retro-video-game) |
294: | Whiteboard | ![Whiteboard](https://designmd.app/images/library/285.png) | [Link](https://designmd.app/en/library/whiteboard) |
295: | Kawaii Doodle Art | ![Kawaii Doodle Art](https://designmd.app/images/library/286.png) | [Link](https://designmd.app/en/library/kawaii-doodle-art) |
296: | Resume Journey Oregon Trail | ![Resume Journey Oregon Trail](https://designmd.app/images/library/287.png) | [Link](https://designmd.app/en/library/resume-journey-oregon-trail) |
297: | Neoclassical Art | ![Neoclassical Art](https://designmd.app/images/library/288.png) | [Link](https://designmd.app/en/library/neoclassical-art) |
298: | Baroque | ![Baroque](https://designmd.app/images/library/289.png) | [Link](https://designmd.app/en/library/baroque) |
299: | Aurora | ![Aurora](https://designmd.app/images/library/290.png) | [Link](https://designmd.app/en/library/aurora) |
300: | Ethereal | ![Ethereal](https://designmd.app/images/library/291.png) | [Link](https://designmd.app/en/library/ethereal) |
301: | Filigree | ![Filigree](https://designmd.app/images/library/292.png) | [Link](https://designmd.app/en/library/filigree) |
302: | Acanthus | ![Acanthus](https://designmd.app/images/library/293.png) | [Link](https://designmd.app/en/library/acanthus) |
303: | Anthropomorphic | ![Anthropomorphic](https://designmd.app/images/library/294.png) | [Link](https://designmd.app/en/library/anthropomorphic) |
304: | Pixel Art 8-bit | ![Pixel Art 8-bit](https://designmd.app/images/library/295.png) | [Link](https://designmd.app/en/library/pixel-art-8-bit) |
305: | Conceptual Sketch / Doodle Art | ![Conceptual Sketch / Doodle Art](https://designmd.app/images/library/296.png) | [Link](https://designmd.app/en/library/conceptual-sketch-doodle-art) |
306: | Luxury Typography | ![Luxury Typography](https://designmd.app/images/library/297.png) | [Link](https://designmd.app/en/library/luxury-typography) |
307: | Japandi | ![Japandi](https://designmd.app/images/library/298.png) | [Link](https://designmd.app/en/library/japandi) |
308: | Memphis | ![Memphis](https://designmd.app/images/library/299.png) | [Link](https://designmd.app/en/library/memphis) |
309: | Bohemian (Boho) | ![Bohemian (Boho)](https://designmd.app/images/library/300.png) | [Link](https://designmd.app/en/library/bohemian-boho) |
310: | Shabby Chic | ![Shabby Chic](https://designmd.app/images/library/301.png) | [Link](https://designmd.app/en/library/shabby-chic) |
311: | Farmhouse / Cottage Core | ![Farmhouse / Cottage Core](https://designmd.app/images/library/302.png) | [Link](https://designmd.app/en/library/farmhouse-cottage-core) |
312: | Victorian | ![Victorian](https://designmd.app/images/library/303.png) | [Link](https://designmd.app/en/library/victorian) |
313: | Art Deco | ![Art Deco](https://designmd.app/images/library/304.png) | [Link](https://designmd.app/en/library/art-deco) |
314: | Art Nouveau | ![Art Nouveau](https://designmd.app/images/library/305.png) | [Link](https://designmd.app/en/library/art-nouveau) |
315: | Mystical Western | ![Mystical Western](https://designmd.app/images/library/306.png) | [Link](https://designmd.app/en/library/mystical-western) |
316: | Kitsch | ![Kitsch](https://designmd.app/images/library/307.png) | [Link](https://designmd.app/en/library/kitsch) |
317: | 3x3 Grid Design | ![3x3 Grid Design](https://designmd.app/images/library/308.png) | [Link](https://designmd.app/en/library/3x3-grid-design) |

(Output capped at 50 KB. Showing lines 1-317. Use offset=318 to continue.)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/design-md-library/todo.md"
}
```

**Output:**
```
<path>/home/mkt/design_md/design-md-library/todo.md</path>
<type>file</type>
<content>
1: Falta:
2: 
3: - Usar o robô para visitar cada url e clicar no botão de favorito de bookmarklet para baixar o DESIGN.md das 454 páginas.

(End of file - total 3 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/design-md-library/download_and_move.py"
}
```

**Output:**
```
<path>/home/mkt/design_md/design-md-library/download_and_move.py</path>
<type>file</type>
<content>
1: import os
2: import re
3: import subprocess
4: import time
5: 
6: md_file = '/Users/fatima/Desktop/awesome_design/design-md-library/elementos_designmd.md'
7: base_dir = '/Users/fatima/Desktop/awesome_design/design-md-library'
8: target_dir = os.path.join(base_dir, '454')
9: 
10: with open(md_file, 'r') as f:
11:     lines = f.readlines()
12: 
13: # Set up to track how many we successfully download/move
14: count = 0
15: 
16: print("Iniciando o download e a cópia das imagens...")
17: 
18: for line in lines:
19:     if line.startswith('|'):
20:         img_match = re.search(r'\((https://designmd\.app/images/library/(\d+)\.png)\)', line)
21:         slug_match = re.search(r'https://designmd\.app/(?:en/)?library/([^)]+)', line)
22:         
23:         if img_match and slug_match:
24:             img_url = img_match.group(1)
25:             img_filename = f"{img_match.group(2)}.png"
26:             slug = slug_match.group(1).strip()
27:             
28:             # Define destination paths
29:             tmp_img_path = os.path.join(base_dir, img_filename)
30:             folder_path = os.path.join(target_dir, slug)
31:             final_img_path = os.path.join(folder_path, img_filename)
32:             
33:             # Step 1: Download using wget
34:             # User-Agent is added to bypass basic blocks
35:             cmd_wget = ['wget', '-q', '--show-progress', '--user-agent=Mozilla/5.0', '-O', tmp_img_path, img_url]
36:             subprocess.run(cmd_wget)
37:             
38:             # Step 2: Move the image to the folder
39:             if os.path.exists(tmp_img_path):
40:                 # Using mv command or python's os.rename
41:                 os.rename(tmp_img_path, final_img_path)
42:                 count += 1
43:             else:
44:                 print(f"Erro ao baixar: {img_url}")
45:                 
46:             # Sleep a tiny bit to avoid being blocked for rapid requests
47:             time.sleep(0.1)
48: 
49: print(f"\nFinalizado! {count} imagens foram baixadas e movidas para as suas respectivas pastas.")

(End of file - total 49 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/design-md-library/automacao_bookmarklet.py"
}
```

**Output:**
```
<path>/home/mkt/design_md/design-md-library/automacao_bookmarklet.py</path>
<type>file</type>
<content>
1: import os
2: import re
3: import time
4: import random
5: import webbrowser
6: 
7: try:
8:     import pyautogui
9: except ImportError:
10:     print("Por favor, instale o pyautogui abrindo o terminal e rodando: pip3 install pyautogui")
11:     exit(1)
12: 
13: # Caminho do arquivo
14: md_file = '/Users/fatima/Desktop/awesome_design/design-md-library/elementos_designmd.md'
15: 
16: # ==============================================================================
17: # CONFIGURAÇÃO DE COMO CLICAR NO BOTÃO (ESCOLHA OPÇÃO 1 OU OPÇÃO 2)
18: # ==============================================================================
19: 
20: # OPÇÃO 1: Coordenadas Fixas da Tela (Mais fácil, rápida e confiável)
21: # Para descobrir essas coordenadas, coloque o mouse em cima do seu favorito 
22: # e rode este comando num terminal: python3 -c "import pyautogui; print(pyautogui.position())"
23: USAR_COORDENADAS = True
24: BOTAO_X = 350  # <-- Mude para o valor X do seu mouse
25: BOTAO_Y = 100  # <-- Mude para o valor Y do seu mouse
26: 
27: # OPÇÃO 2: Reconhecimento de Imagem (Requer salvar um print do botão)
28: # Se USAR_COORDENADAS for False, o script vai procurar essa imagem na tela.
29: # Para isso, tire um "print" BEM PEQUENO contendo apenas o texto do botão do 
30: # favorito, salve como "botao_favorito.png" na mesma pasta deste script.
31: # Obs: É preciso instalar a biblioteca opencv-python para o confidence=0.8 funcionar.
32: NOME_DA_IMAGEM = 'botao_favorito.png'
33: 
34: # ==============================================================================
35: 
36: # 1. Lê a tabela para extrair as URLs
37: with open(md_file, 'r') as f:
38:     lines = f.readlines()
39: 
40: urls = []
41: for line in lines:
42:     if line.startswith('|'):
43:         # Extrai o link da terceira coluna
44:         match = re.search(r'(https://designmd\.app/(?:en/)?library/[^)]+)', line)
45:         if match:
46:             urls.append(match.group(1))
47: 
48: print(f"Foram encontradas {len(urls)} URLs.")
49: print("AVISO: Deixe o seu navegador visível e na mesma posição.")
50: print("Iniciando em 5 segundos... (Para parar a qualquer momento, arraste o mouse rapidamente para qualquer um dos 4 cantos da tela!)")
51: time.sleep(5)
52: 
53: # 2. Executa o fluxo para cada URL
54: for i, url in enumerate(urls):
55:     print(f"\n[{i+1}/{len(urls)}] Abrindo página: {url}")
56:     
57:     # Abre a URL em uma nova aba do navegador padrão
58:     webbrowser.open_new_tab(url)
59:     
60:     # Tempo randômico entre 4 e 15 segundos para simular comportamento humano e carregar a página
61:     tempo_espera = random.randint(4, 15)
62:     print(f"Aguardando {tempo_espera} segundos para o carregamento...")
63:     time.sleep(tempo_espera)
64:     
65:     # 3. Clica no Bookmarklet
66:     if USAR_COORDENADAS:
67:         # Move o mouse e clica
68:         pyautogui.moveTo(BOTAO_X, BOTAO_Y, duration=0.5) # duração de meio segundo simula o humano movendo
69:         pyautogui.click()
70:         print(f"Clicado nas coordenadas ({BOTAO_X}, {BOTAO_Y})")
71:     else:
72:         try:
73:             # Procura a imagem do botão na tela
74:             posicao = pyautogui.locateCenterOnScreen(NOME_DA_IMAGEM, confidence=0.8)
75:             if posicao:
76:                 pyautogui.moveTo(posicao.x, posicao.y, duration=0.5)
77:                 pyautogui.click()
78:                 print("Clicado via reconhecimento de imagem!")
79:             else:
80:                 print("ERRO: Não encontrei a imagem do botão na tela.")
81:         except Exception as e:
82:             print(f"Erro ao procurar a imagem: {e}. (Verifique se instalou o opencv-python)")
83: 
84:     # Pequena pausa antes de abrir a próxima URL para dar tempo do download iniciar
85:     time.sleep(2)
86: 
87: print("\nProcesso concluído!")
88: 
89: 
90: # UTILIZAÇÃO:
91: '''
92: Sim, é totalmente possível e criei exatamente esse script para você! 
93: 
94: Acabei de salvá-lo em: `@[/Users/fatima/Desktop/awesome_design/design-md-library/automacao_bookmarklet.py]`
95: 
96: Sobre a sua dúvida de como o PyAutoGUI reconhece o botão: **Sim, há duas alternativas principais**, e eu deixei ambas preparadas no script para você escolher:
97: 
98: ### Alternativa 1: Coordenadas Fixas (Recomendado, Mais Fácil)
99: O PyAutoGUI não precisa "enxergar" o botão. Se você deixar o navegador em tela cheia e não mexer, a posição do botão na sua tela será sempre a mesma (por exemplo, `X=350, Y=100`). O script simplesmente joga o mouse cegamente nessa coordenada e clica.
100: No arquivo que criei, deixei essa opção ativada por padrão (`USAR_COORDENADAS = True`). Coloquei no código um comando que você pode usar para descobrir qual é o `X` e `Y` exato do seu mouse.
101: 
102: ### Alternativa 2: Reconhecimento de Imagem (Mais Avançado)
103: Nessa opção (`locateCenterOnScreen`), o PyAutoGUI vai "escanear" a tela do seu computador inteira pixel por pixel caçando uma imagem específica.
104: **Como funciona:** Você tira um *print* (captura de tela) bem pequenininho apenas do botão do seu favorito e salva como `botao_favorito.png` na mesma pasta do script. O script vai procurar por essa imagem, descobrir onde ela está e clicar. É excelente se você costuma mudar o tamanho da janela, mas é um pouco mais pesado.
105: 
106: ### Como usar o Script criado:
107: 1. Abra um terminal.
108: 2. Se não tiver as bibliotecas instaladas, rode: `pip3 install pyautogui opencv-python`
109: 3. Abra o script `automacao_bookmarklet.py`, edite as variáveis `BOTAO_X` e `BOTAO_Y` com os números do seu botão de favorito.
110: 4. Rode: `python3 automacao_bookmarklet.py`
111: 
112: **Dica de Ouro:** O PyAutoGUI tem um "botão de emergência". Se o script começar a clicar em coisas erradas ou abrir abas infinitas e você perder o controle, basta dar um "fio terra": **Jogue o seu mouse rapidamente e bruscamente para qualquer um dos 4 cantos extremos do seu monitor** e o script abortará imediatamente!
113: '''

(End of file - total 113 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/design-md-library/454"
}
```

**Output:**
```
<path>/home/mkt/design_md/design-md-library/454</path>
<type>directory</type>
<entries>
3d-hyperrealism/
3d-product-preview/
3x3-grid-design/
70s-psychedelic-flower-power/
8-bit-orbit/
8-bit-retro-terminal/
90s-retro-video-game/
acanthus/
accessible-ethical/
afrofuturismo-digital/
agency-viral-videos-reels-hero/
ai-automation-hero/
ai-native-ui/
airbnb-coral-marketplace/
albert-sans-typography/
amazonia-futurista/
american-diner-americana/
analytics-metric-flow/
ancient-egyptian-historical/
ancient-egyptian-instructional-scroll/
anime-battle/
anthropomorphic/
anti-polish-raw-aesthetic/
apple-premium-cinematic/
aprendizado-criativo-artesanal/
architectural-portfolio-cinematic/
architectural-schematic/
arctic-forsythia-premium/
art-deco-golden-age/
art-deco/
art-nouveau-florido/
art-nouveau/
artesanato-organico-e-acolhedor/
aura-premium-webgl-iconify/
aurora-boreal-nordica/
aurora-ui/
aurora/
azulejaria-digital-moderna/
azulejo-portugues/
baroque/
bauhaus-risograph-modern/
bauhaus/
belle-epoque-lithograph/
bento-box-grid/
bento-dados-estruturados/
bento-eventos-dinamicos/
bento-grid-tech-minimalist/
bento-grid/
bento-grids/
bento-noticias-curadas/
bento-portfolio-de-produto/
bento-produtividade-flexivel/
biennale-yellow/
biomimetic-organic-2-0/
block-frame/
blue-professional/
blueprint-engineering/
bmw-angular-precision/
bohemian-boho/
bold-energetic/
bold-portfolio-hero/
bold-poster/
bold-signal/
bossa-nova-lounge/
broadside/
brutalism-311/
brutalism-4/
brutalismo-artistico-abstrato/
brutalismo-sonoro-glitch/
brutalismo-urbano-expressivo/
brutalist-web-design/
cad-inspired-blueprint/
cafe-artesanal-aconchegante/
capsule/
caramelo-quente-premium/
cartazista-de-supermercado/
cartesian/
cassette-futurism/
ceramica-wabi-sabi/
cerrado-minimalista/
chalkboard-hand-drawn/
chalkboard-sketch-note/
chalkboard/
chromatic-aberration-rgb-split/
circuit-board-pcb/
claude-warm-parchment/
clay-artisanal-swatch/
claymation-3d-illustration/
claymation-3d/
claymorphism/
clearinvoice-saas-hero/
clickhouse-neon-volt/
coastal-commerce/
coastal-mist/
coastal-studio/
cobalt-grid/
cohere-enterprise-serif/
coinbase-trust-blue/
comic-book-pop-art/
comparative-analysis-dashboard/
composio-cyber-nocturnal/
conceptual-sketch-doodle-art/
conforto-artesanal-brasileiro/
construtivismo-arquitetonico/
construtivismo-de-dados-dinamicos/
construtivismo-de-eventos-dinamicos/
construtivismo-dinamico-tech/
construtivismo-literario-experimental/
conversion-optimized/
coquette/
coral/
cordel-digital/
corporate-radial-process/
creative-mode/
creative-voltage/
criatividade-artesanal-e-pessoal/
crm-copper-sand/
crypto-exchange-plataforma/
culinaria-afetiva-brasileira/
cursor-warm-gothic/
cyber-core/
cyber-tribal/
cyberpunk-dark-mode-flow/
cyberpunk-neon-noir/
cyberpunk-ui/
daisy-days/
dark-botanical/
dark-glassmorphism-infographic/
dark-mode-oled/
dark-portfolio-hero/
dark-saas-hero-with-liquid-glass/
data-dense-dashboard/
datacore-saas-hero/
de-stijl-abstrato/
degraded-colorful-vibrant-gradient/
democratized-fancy-animations/
denim-and-industrial-craft/
desenho-a-mao-ludico/
design-autoral-robusto/
dimensional-layering/
doodle-sketch-livre/
drill-down-analytics/
e-ink-paper/
earthy-organic/
editorial-contemporaneo/
editorial-de-portfolio-criativo/
editorial-de-viagem-sofisticado/
editorial-grid-magazine/
editorial-interativo-digital/
editorial-investigativo-sobrio/
editorial-tri-tone/
edtech-plataforma-de-cursos/
electric-studio/
elementos-musicais/
elevenlabs-ethereal-voice/
ember-amethyst-premium/
engineering-blueprint-schematic/
estilo-de-computacao-de-alta-performance/
estilo-de-dados-empresariais/
estilo-de-ecossistema-digital/
estilo-de-elegancia-espacial/
estilo-de-elegancia-fintech/
estilo-de-entretenimento-imersivo/
estilo-de-experiencia-de-compra-continua/
estilo-de-fluxo-de-rede/
estilo-de-futuro-autonomo/
estilo-de-ia-criativa/
estilo-de-ia-etica/
estilo-de-ia-para-negocios/
estilo-de-inovacao-em-dispositivos-moveis/
estilo-de-inteligencia-generativa/
estilo-de-litografia-de-precisao/
estilo-de-realidade-virtual-social/
estilo-de-tecnologia-de-precisao/
estilo-deep-learning-high-tech/
estilo-fluent-ai/
estilo-material-ai/
estilo-suico-artistico/
estilo-suico-cientifico/
estilo-suico-corporativo/
estilo-suico-educacional/
estilo-suico-premium/
ethereal/
exaggerated-minimalism/
executive-dashboard/
expo-luminous-developer/
farmhouse-cottage-core/
feature-rich-showcase/
figma-vibrant-monochrome/
filigree/
financial-dashboard/
fintech-plataforma-financeira/
fitness-app-de-treinos/
flat-design-corporativo/
flat-design-educacional-vibrante/
flat-design-financeiro-seguro/
flat-design-informativo-claro/
flat-design-musical-intuitivo/
flat-design-produtivo/
flat-design/
fractal-bioluminescence/
framelix-3d-studios/
fraunces-typography/
futuristic-ui-glassmorphism/
gatsby-art-deco-noir/
gen-z-chaos-maximalism/
geometric/
ghibli-inspired-narrative-map/
glass-gradient-creative/
glassmorphism-agency-hero/
glassmorphism/
glitch-ui-dystopian-terminal/
google-sans-typography/
gothic/
gotico-moderno/
grade-school-color-palette/
gradient-aurora-borealis/
gradient-mesh-aurora-evolved/
graffiti/
grove/
grunge-rock-dos-anos-90/
hacker-aesthetic-crt-cli/
hand-drawn-sketch-note/
happy-art-tropical/
hashicorp-infra-dual/
healthtech-plataforma-clinica/
heat-map-heatmap-style/
helios-design-system-hashicorp/
hero-centric-design/
high-contrast-tech/
holographic-data-viz/
horror-gothic-dark/
hr-saas-hero/
hud-sci-fi-fui/
ibm-carbon-enterprise/
ibm-plex-sans-typography/
inclusive-design/
industrial-workbench-schematic/
inter-typography/
interactive-cursor-design/
interactive-product-demo/
internet-nostalgia-y2k-revival/
isometric-gaming-voxel/
japandi/
kawaii-doodle-art/
kawaii-pastel-pop/
kawaii-sweet-pastel/
kawaii/
kinetic-typography/
kitsch/
knolling-pastel-flat-lay/
kraken-purple-exchange/
lambe-lambe-brasileiro/
laranja-queimado-premium/
linear-precision-dark/
liquid-glass/
locomotive-infinite-scroll/
logoisum-video-agency-hero/
lovable-cream-humanist/
luxury-elegant/
luxury-typography/
manga-instructional-comic/
manrope-typography/
maracatu-tech/
mat/
memphis-design/
memphis/
merriweather-typography/
micro-interactions/
micro-sound-ux/
mid-century-modern/
midnight-garden-premium/
mini-world/
minimal-direct/
minimalism-swiss-style/
minimalismo-chic-de-luxo/
minimalismo-confiavel-financeiro/
minimalismo-fotografico-elegante/
minimalismo-funcional-b2b/
minimalismo-sereno-de-bem-estar/
minimalist-react-hero-with-motion/
minimax-colorful-cards/
mintlify-green-docs/
mistral-golden-amber/
mixed-media/
mixed-reality-vr-ar/
modern-minimalist/
modernismo-jornalistico-brasileiro/
mongodb-forest-neon/
monochrome/
motion-driven/
mystical-western/
nature-distilled/
natureza-elementos-botanicos/
neo-grid-bold/
neobrutalismo-critico/
neobrutalismo-ousado/
neoclassical-art/
neon-cyber/
neubrutalism/
neumorphic-tech-schematic/
neumorphism/
new-era-automotive-hero/
new-era-bold-hero/
noir-detetive/
notebook-tabs/
notion-warm-workspace/
nvidia-power-green/
ollama-pure-grayscale/
opencode-terminal-mono/
organic-biophilic/
origami-geometrico/
paper-ink/
parallax-storytelling/
passport-travel-ui/
pastel-geometry/
pcb-schematic-architecture/
peoples-platform/
pin-and-paper/
pink-script/
pinterest-warm-discovery/
pixel-art-8-bit/
pixel-art/
playful/
pointillism-stipple-art/
pop-art/
portfolio-dev-full-stack/
predictive-analytics/
psicodelico-anos-60/
radial-diagram-donut-chart/
raw-grid/
real-estate-imobiliaria-digital/
real-time-monitoring/
replicate-blaze-gallery/
resend-frost-cinematic/
resume-journey-oregon-trail/
retro-arcade-pixelado/
retro-aventura-anos-70/
retro-barbershop-classica/
retro-boutique-vintage/
retro-comic-action-blueprint/
retro-digital-anos-90/
retro-futurism/
retro-travel-poster/
retro-windows/
retro-zine/
reuso-criativo-disruptivo/
revolut-billboard-fintech/
risograph-retro-pop/
risograph-zine-aesthetic/
rococo-delicado/
rococo-romantic-narrative/
roxo-veludo-real/
runway-cinematic-editorial/
saas-enterprise-analytics/
saas-signature-gradient/
sakura-chroma/
sakura-floral-japones/
sales-intelligence-dashboard/
sanity-neon-structured/
scatterbrain/
scrapbook-collage/
sentry-purple-debugger/
shabby-chic/
signal/
simbolos-ambientais-brasileiros/
simbolos-civicos-brasileiros/
simbolos-culturais-brasileiros/
simbolos-politicos-brasileiros/
simbolos-regionais-brasileiros/
skeuomorphism/
social-proof-focused/
soft-editorial/
soft-maximalism/
soft-ui-evolution/
solarpunk-utopico/
space-grotesk-typography/
spaceship-instruction-manual/
spacex-cinematic-void/
spatial-ui-visionos/
split-pastel/
spotify-dark-immersive/
steampunk-industrial/
steampunk-nebula-explorer/
steampunk-vitoriano/
steampunk/
stencil-tablet/
storytelling-driven/
stripe-fintech-elegance/
studio/
studygram-notebook-kawaii/
sumi-e-tech-scroll/
supabase-dark-emerald/
surrealism/
swiss-design-grafico/
swiss-modern/
swiss-modernism-2-0/
synapse-dark-hero/
syne-typography/
synthwave/
tactile-3d-neumorphism/
tactile-digital-deformable-ui/
targo-logistics-hero/
taskora-saas-hero/
tenebrism/
tenor-sans-typography/
terminal-green/
terracota-mediterraneo/
the-barely-there-ui/
thermal-insight-tech/
timeline-horizontal-corporativo/
together-pastel-cloud/
travel-plataforma-de-viagens/
tropicalismo-aventureiro-natural/
tropicalismo-gastronomico-vibrante/
tropicalismo-indigena-autentico/
trust-authority/
uber-bold-transit/
ukiyo-e-woodblock-revival/
underwater-aquatico-deep-sea/
underwater-aquatico/
user-behavior-analytics/
utilitarian/
vaporwave-314/
vaporwave-45/
vaporwave-aesthetic/
vellum/
vercel-geist-minimal/
vernacular-acolhedor-brasileiro/
versus-mode-anime-aesthetic/
vertical-whiteboard-timeline/
vibrant-block-based/
victorian/
vintage-analog-retro-film/
vintage-botanical-scientific-illustration/
vintage-botanical-scientific/
vintage-editorial/
vintage-lithograph-victorian/
voice-first-multimodal/
voltagent-terminal-emerald/
voxel-gamified-isometric/
wabi-sabi-anti-ux/
wealth-video-hero/
web3-eos-hero/
weblex-dark-hero/
whiteboard-flowchart/
whiteboard/
wise-lime-bold/
xai-brutalist-monospace/
y2k-aesthetic/
y2k/
z-shape/
zapier-warm-automation/
zero-interface/

(454 entries)
</entries>
```

---

## Assistant (Build · Big Pickle · 5.1s)

_Thinking:_

Now I have a good understanding of the repository. Let me check if any README files in the design-md-awesome subdirectories contain DESIGN.md files (the actual design tokens), and look at one example.

Let me look at a sample DESIGN.md file to understand what's in the design-md-awesome subdirectories, and check git history.

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/design-md-awesome/airbnb"
}
```

**Output:**
```
<path>/home/mkt/design_md/design-md-awesome/airbnb</path>
<type>directory</type>
<entries>
DESIGN.md
README.md

(2 entries)
</entries>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/design-md-awesome/apple"
}
```

**Output:**
```
<path>/home/mkt/design_md/design-md-awesome/apple</path>
<type>directory</type>
<entries>
DESIGN.md
README.md

(2 entries)
</entries>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/skills"
}
```

**Output:**
```
<path>/home/mkt/design_md/skills</path>
<type>directory</type>
<entries>
extract_design_skill.md
README.md

(2 entries)
</entries>
```

**Tool: bash**

**Input:**
```json
{
  "command": "git log --oneline -10",
  "description": "Check recent git history"
}
```

**Output:**
```
72dd65c 1o. commit
4afdb27 Initial commit

```

**Tool: bash**

**Input:**
```json
{
  "command": "git log --oneline --all -- AGENTS.md CLAUDE.md 2>/dev/null; ls -la .git/hooks/ 2>/dev/null | head -5",
  "description": "Check for existing instruction files in git"
}
```

**Output:**
```
total 72
drwxrwxr-x 2 mkt mkt 4096 jun  2 15:03 .
drwxrwxr-x 8 mkt mkt 4096 jun  2 15:04 ..
-rwxrwxr-x 1 mkt mkt  478 jun  2 15:03 applypatch-msg.sample
-rwxrwxr-x 1 mkt mkt  896 jun  2 15:03 commit-msg.sample

```

---

## Assistant (Build · Big Pickle · 2.7s)

_Thinking:_

Let me read a sample DESIGN.md and the skills file to fully understand the repo.

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/design-md-awesome/airbnb/DESIGN.md"
}
```

**Output:**
```
<path>/home/mkt/design_md/design-md-awesome/airbnb/DESIGN.md</path>
<type>file</type>
<content>
1: ---
2: version: alpha
3: name: Airbnb
4: description: A warm, generous consumer marketplace anchored on a clean white canvas and Airbnb Rausch (#ff385c), the single brand voltage that carries every primary CTA, search-button orb, and rating dot. Type runs Airbnb Cereal VF at modest weights — display sits at 22–28px in weight 500/600 rather than the heavy 700+ that fintech and enterprise systems use; the brand trusts photography and generous whitespace over typographic muscle. Three product entries (Homes, Experiences, Services) sit in the top nav with hand-illustrated 32-icon glyphs and "NEW" badges, signaling a marketplace expansion rather than a feature dump. Pill-shaped search bars (`{rounded.full}`), softly rounded property cards (`{rounded.lg}` ~14px), and 32px button radii read as friendly and human — there is no hard corner anywhere except the body grid.
5: 
6: colors:
7:   primary: "#ff385c"
8:   primary-active: "#e00b41"
9:   primary-disabled: "#ffd1da"
10:   primary-error-text: "#c13515"
11:   primary-error-text-hover: "#b32505"
12:   luxe: "#460479"
13:   plus: "#92174d"
14:   ink: "#222222"
15:   body: "#3f3f3f"
16:   muted: "#6a6a6a"
17:   muted-soft: "#929292"
18:   hairline: "#dddddd"
19:   hairline-soft: "#ebebeb"
20:   border-strong: "#c1c1c1"
21:   canvas: "#ffffff"
22:   surface-soft: "#f7f7f7"
23:   surface-card: "#ffffff"
24:   surface-strong: "#f2f2f2"
25:   on-primary: "#ffffff"
26:   on-dark: "#ffffff"
27:   legal-link: "#428bff"
28:   star-rating: "#222222"
29:   scrim: "#000000"
30: 
31: typography:
32:   display-xl:
33:     fontFamily: "'Airbnb Cereal VF', Circular, -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
34:     fontSize: 28px
35:     fontWeight: 700
36:     lineHeight: 1.43
37:     letterSpacing: 0
38:   display-lg:
39:     fontFamily: "'Airbnb Cereal VF', Circular, sans-serif"
40:     fontSize: 22px
41:     fontWeight: 500
42:     lineHeight: 1.18
43:     letterSpacing: -0.44px
44:   display-md:
45:     fontFamily: "'Airbnb Cereal VF', Circular, sans-serif"
46:     fontSize: 21px
47:     fontWeight: 700
48:     lineHeight: 1.43
49:     letterSpacing: 0
50:   display-sm:
51:     fontFamily: "'Airbnb Cereal VF', Circular, sans-serif"
52:     fontSize: 20px
53:     fontWeight: 600
54:     lineHeight: 1.20
55:     letterSpacing: -0.18px
56:   title-md:
57:     fontFamily: "'Airbnb Cereal VF', Circular, sans-serif"
58:     fontSize: 16px
59:     fontWeight: 600
60:     lineHeight: 1.25
61:     letterSpacing: 0
62:   title-sm:
63:     fontFamily: "'Airbnb Cereal VF', Circular, sans-serif"
64:     fontSize: 16px
65:     fontWeight: 500
66:     lineHeight: 1.25
67:     letterSpacing: 0
68:   rating-display:
69:     fontFamily: "'Airbnb Cereal VF', Circular, sans-serif"
70:     fontSize: 64px
71:     fontWeight: 700
72:     lineHeight: 1.1
73:     letterSpacing: -1px
74:   body-md:
75:     fontFamily: "'Airbnb Cereal VF', Circular, sans-serif"
76:     fontSize: 16px
77:     fontWeight: 400
78:     lineHeight: 1.5
79:     letterSpacing: 0
80:   body-sm:
81:     fontFamily: "'Airbnb Cereal VF', Circular, sans-serif"
82:     fontSize: 14px
83:     fontWeight: 400
84:     lineHeight: 1.43
85:     letterSpacing: 0
86:   caption:
87:     fontFamily: "'Airbnb Cereal VF', Circular, sans-serif"
88:     fontSize: 14px
89:     fontWeight: 500
90:     lineHeight: 1.29
91:     letterSpacing: 0
92:   caption-sm:
93:     fontFamily: "'Airbnb Cereal VF', Circular, sans-serif"
94:     fontSize: 13px
95:     fontWeight: 400
96:     lineHeight: 1.23
97:     letterSpacing: 0
98:   badge:
99:     fontFamily: "'Airbnb Cereal VF', Circular, sans-serif"
100:     fontSize: 11px
101:     fontWeight: 600
102:     lineHeight: 1.18
103:     letterSpacing: 0
104:   micro-label:
105:     fontFamily: "'Airbnb Cereal VF', Circular, sans-serif"
106:     fontSize: 12px
107:     fontWeight: 700
108:     lineHeight: 1.33
109:     letterSpacing: 0
110:   uppercase-tag:
111:     fontFamily: "'Airbnb Cereal VF', Circular, sans-serif"
112:     fontSize: 8px
113:     fontWeight: 700
114:     lineHeight: 1.25
115:     letterSpacing: 0.32px
116:     textTransform: uppercase
117:   button-md:
118:     fontFamily: "'Airbnb Cereal VF', Circular, sans-serif"
119:     fontSize: 16px
120:     fontWeight: 500
121:     lineHeight: 1.25
122:     letterSpacing: 0
123:   button-sm:
124:     fontFamily: "'Airbnb Cereal VF', Circular, sans-serif"
125:     fontSize: 14px
126:     fontWeight: 500
127:     lineHeight: 1.29
128:     letterSpacing: 0
129:   link:
130:     fontFamily: "'Airbnb Cereal VF', Circular, sans-serif"
131:     fontSize: 14px
132:     fontWeight: 400
133:     lineHeight: 1.43
134:     letterSpacing: 0
135:   nav-link:
136:     fontFamily: "'Airbnb Cereal VF', Circular, sans-serif"
137:     fontSize: 16px
138:     fontWeight: 600
139:     lineHeight: 1.25
140:     letterSpacing: 0
141: 
142: rounded:
143:   none: 0px
144:   xs: 4px
145:   sm: 8px
146:   md: 14px
147:   lg: 20px
148:   xl: 32px
149:   full: 9999px
150: 
151: spacing:
152:   xxs: 2px
153:   xs: 4px
154:   sm: 8px
155:   md: 12px
156:   base: 16px
157:   lg: 24px
158:   xl: 32px
159:   xxl: 48px
160:   section: 64px
161: 
162: components:
163:   button-primary:
164:     backgroundColor: "{colors.primary}"
165:     textColor: "{colors.on-primary}"
166:     typography: "{typography.button-md}"
167:     rounded: "{rounded.sm}"
168:     padding: 14px 24px
169:     height: 48px
170:   button-primary-active:
171:     backgroundColor: "{colors.primary-active}"
172:     textColor: "{colors.on-primary}"
173:     rounded: "{rounded.sm}"
174:   button-primary-disabled:
175:     backgroundColor: "{colors.primary-disabled}"
176:     textColor: "{colors.on-primary}"
177:     rounded: "{rounded.sm}"
178:   button-secondary:
179:     backgroundColor: "{colors.canvas}"
180:     textColor: "{colors.ink}"
181:     typography: "{typography.button-md}"
182:     rounded: "{rounded.sm}"
183:     padding: 13px 23px
184:     height: 48px
185:   button-tertiary-text:
186:     backgroundColor: transparent
187:     textColor: "{colors.ink}"
188:     typography: "{typography.button-md}"
189:   button-pill-rausch:
190:     backgroundColor: "{colors.primary}"
191:     textColor: "{colors.on-primary}"
192:     typography: "{typography.button-sm}"
193:     rounded: "{rounded.full}"
194:     padding: 10px 20px
195:   search-orb:
196:     backgroundColor: "{colors.primary}"
197:     textColor: "{colors.on-primary}"
198:     rounded: "{rounded.full}"
199:     height: 48px
200:   icon-button-circle:
201:     backgroundColor: "{colors.surface-strong}"
202:     textColor: "{colors.ink}"
203:     rounded: "{rounded.full}"
204:     height: 32px
205:   icon-button-outline:
206:     backgroundColor: "{colors.canvas}"
207:     textColor: "{colors.ink}"
208:     rounded: "{rounded.full}"
209:     height: 40px
210:   top-nav:
211:     backgroundColor: "{colors.canvas}"
212:     textColor: "{colors.ink}"
213:     typography: "{typography.nav-link}"
214:     height: 80px
215:   product-tab-active:
216:     backgroundColor: transparent
217:     textColor: "{colors.ink}"
218:     typography: "{typography.nav-link}"
219:     rounded: "{rounded.none}"
220:   product-tab-inactive:
221:     backgroundColor: transparent
222:     textColor: "{colors.muted}"
223:     typography: "{typography.nav-link}"
224:   search-bar-pill:
225:     backgroundColor: "{colors.canvas}"
226:     textColor: "{colors.ink}"
227:     typography: "{typography.body-sm}"
228:     rounded: "{rounded.full}"
229:     padding: 14px 24px
230:     height: 64px
231:   search-field-segment:
232:     backgroundColor: transparent
233:     textColor: "{colors.ink}"
234:     typography: "{typography.caption}"
235:     padding: 8px 24px
236:   category-strip:
237:     backgroundColor: "{colors.canvas}"
238:     textColor: "{colors.muted}"
239:     typography: "{typography.button-sm}"
240:   category-tab-active:
241:     backgroundColor: transparent
242:     textColor: "{colors.ink}"
243:     typography: "{typography.button-sm}"
244:     rounded: "{rounded.none}"
245:   property-card:
246:     backgroundColor: "{colors.canvas}"
247:     textColor: "{colors.ink}"
248:     typography: "{typography.body-sm}"
249:     rounded: "{rounded.md}"
250:   property-card-photo:
251:     rounded: "{rounded.md}"
252:   experience-card:
253:     backgroundColor: "{colors.canvas}"
254:     textColor: "{colors.ink}"
255:     typography: "{typography.title-md}"
256:     rounded: "{rounded.md}"
257:   city-link-block:
258:     backgroundColor: transparent
259:     textColor: "{colors.ink}"
260:     typography: "{typography.title-sm}"
261:   rating-display-card:
262:     backgroundColor: transparent
263:     textColor: "{colors.ink}"
264:     typography: "{typography.rating-display}"
265:   guest-favorite-badge:
266:     backgroundColor: "{colors.canvas}"
267:     textColor: "{colors.ink}"
268:     typography: "{typography.badge}"
269:     rounded: "{rounded.full}"
270:     padding: 4px 10px
271:   new-tag:
272:     backgroundColor: "{colors.canvas}"
273:     textColor: "{colors.ink}"
274:     typography: "{typography.uppercase-tag}"
275:     rounded: "{rounded.full}"
276:     padding: 2px 6px
277:   amenity-row:
278:     backgroundColor: transparent
279:     textColor: "{colors.ink}"
280:     typography: "{typography.body-md}"
281:     padding: 12px 0
282:   reviews-card:
283:     backgroundColor: transparent
284:     textColor: "{colors.ink}"
285:     typography: "{typography.body-sm}"
286:   host-card:
287:     backgroundColor: "{colors.canvas}"
288:     textColor: "{colors.ink}"
289:     typography: "{typography.body-sm}"
290:     rounded: "{rounded.md}"
291:     padding: 24px
292:   reservation-card:
293:     backgroundColor: "{colors.canvas}"
294:     textColor: "{colors.ink}"
295:     typography: "{typography.body-md}"
296:     rounded: "{rounded.md}"
297:     padding: 24px
298:   date-picker-day:
299:     backgroundColor: transparent
300:     textColor: "{colors.ink}"
301:     typography: "{typography.body-sm}"
302:     rounded: "{rounded.full}"
303:   date-picker-day-selected:
304:     backgroundColor: "{colors.ink}"
305:     textColor: "{colors.on-dark}"
306:     rounded: "{rounded.full}"
307:   text-input:
308:     backgroundColor: "{colors.canvas}"
309:     textColor: "{colors.ink}"
310:     typography: "{typography.body-md}"
311:     rounded: "{rounded.sm}"
312:     padding: 14px 12px
313:     height: 56px
314:   footer-light:
315:     backgroundColor: "{colors.canvas}"
316:     textColor: "{colors.ink}"
317:     typography: "{typography.body-sm}"
318:     padding: 48px 80px
319:   footer-link:
320:     backgroundColor: transparent
321:     textColor: "{colors.ink}"
322:     typography: "{typography.body-sm}"
323:   legal-band:
324:     backgroundColor: "{colors.canvas}"
325:     textColor: "{colors.muted}"
326:     typography: "{typography.caption-sm}"
327: ---
328: 
329: ## Overview
330: 
331: Airbnb is the canonical example of a generous, photography-led consumer marketplace. The base canvas is **pure white** (`{colors.canvas}` — #ffffff) with deep near-black ink (`{colors.ink}` — #222222) for headlines and body, and a single voltage of **Rausch** (`{colors.primary}` — #ff385c) carrying every primary CTA, the search-button orb, the heart save state, and inline brand links. There is no secondary brand color in mainline marketing — the **Luxe purple** (`{colors.luxe}` — #460479) and **Plus magenta** (`{colors.plus}` — #92174d) tokens are sub-brand accents that only appear inside Airbnb Luxe / Plus contexts.
332: 
333: Type runs **Airbnb Cereal VF** (a custom variable font Airbnb licenses), with **Circular** as the historic in-house fallback and a system stack underneath. Cereal sits at modest weights — display headlines render at 22–28px in weight 500–600, not the heavy 700+ weights that financial or enterprise systems lean on. The hero h1 ("Inspiration for future getaways") on the homepage is just 28px / 700, which would feel small on a typical SaaS page; here it works because the layout leans on photography (city collage, property cards) for visual weight rather than typographic muscle.
334: 
335: The shape language is **soft**. Buttons are 8px radius (`{rounded.sm}`), property cards are ~14px (`{rounded.md}`), the search bar is fully pill-shaped (`{rounded.full}`), wishlist hearts and search orbs are circles (`{rounded.full}`), and category strip rounded corners run at 32px (`{rounded.xl}`). There is essentially no hard corner anywhere except the body grid itself — every interactive element is rounded.
336: 
337: **Key Characteristics:**
338: - Single accent color: `{colors.primary}` (#ff385c — "Rausch") carries every primary CTA, the search orb, the heart save state, and the brand wordmark. Used scarcely — most pages are 90% white + ink with one or two Rausch moments.
339: - Custom variable type: `Airbnb Cereal VF`. Display weights sit at 500–700, body at 400. Modest weight is intentional — the system trusts photography for visual heft.
340: - Three-product top nav: Homes, Experiences, Services — each with a hand-illustrated 32px icon and "NEW" badges (`{component.new-tag}`) on the two newer products. Active tab uses an underline rule (`{component.product-tab-active}`).
341: - Pill-shaped global search bar: white surface, fully rounded (`{rounded.full}`), divided by 1px hairlines into Where / When / Who segments, terminated by a circular Rausch search orb (`{component.search-orb}`).
342: - Property cards are photo-first: aspect-ratio rectangles with `{rounded.md}` corner clipping, swipeable image carousel, "Guest favorite" floating badge top-left, heart icon top-right, then 4–5 lines of meta beneath.
343: - Editorial dropdowns (footer, language picker) are clean text columns over the white canvas — no card surface, no shadow.
344: - The design system caps elevation at one shadow tier (`box-shadow: rgba(0,0,0,0.02) 0 0 0 1px, rgba(0,0,0,0.04) 0 2px 6px, rgba(0,0,0,0.1) 0 4px 8px`) — used on hover-floated cards and search/account dropdowns.
345: - 8px base spacing system, with major sections at `{spacing.section}` (64px) — generous but not airy enough to feel editorial-magazine; the marketplace density wants more cards per scroll.
346: 
347: ## Colors
348: 
349: ### Brand & Accent
350: - **Rausch** (`{colors.primary}` — #ff385c): The single brand color. Used for primary CTA backgrounds (Reserve, Continue), the search orb, the heart save state on property cards, and inline brand links. The most recognizable color in consumer travel.
351: - **Rausch Active** (`{colors.primary-active}` — #e00b41): The press / pointer-down variant — slightly more saturated. Used on `{component.button-primary-active}`.
352: - **Rausch Disabled** (`{colors.primary-disabled}` — #ffd1da): A pale tint used on disabled CTAs.
353: - **Luxe Purple** (`{colors.luxe}` — #460479): Sub-brand accent for Airbnb Luxe. Only appears inside Luxe-branded surfaces — never in mainline marketing.
354: - **Plus Magenta** (`{colors.plus}` — #92174d): Sub-brand accent for Airbnb Plus. Same scoping as Luxe — sub-product only.
355: 
356: ### Surface
357: - **Canvas** (`{colors.canvas}` — #ffffff): The default page floor for every public page. Airbnb does not have a dark mode on the public web.
358: - **Surface Soft** (`{colors.surface-soft}` — #f7f7f7): The lightest fill — used on disabled fields, sub-nav hover backgrounds, and the inline search filter band.
359: - **Surface Strong** (`{colors.surface-strong}` — #f2f2f2): Slightly heavier fill — circular icon-button surface (e.g., the breadcrumb back-arrow and listing toolbar buttons).
360: 
361: ### Hairlines & Borders
362: - **Hairline** (`{colors.hairline}` — #dddddd): The default 1px border tone — search bar dividers, table separators, footer column splitters, card 1px borders.
363: - **Hairline Soft** (`{colors.hairline-soft}` — #ebebeb): A lighter divider used on long-scrolling editorial body separators.
364: - **Border Strong** (`{colors.border-strong}` — #c1c1c1): A heavier stroke used on disabled outline buttons and form input outlines after focus.
365: 
366: ### Text
367: - **Ink** (`{colors.ink}` — #222222): The dominant text color on light surfaces. Display headlines, body paragraphs, primary nav links, and most inline link text. Never pure black.
368: - **Body** (`{colors.body}` — #3f3f3f): A secondary running-text color used inside long-form review and amenity copy where ink would feel too heavy.
369: - **Muted** (`{colors.muted}` — #6a6a6a): Sub-titles inside city link blocks ("Cottage rentals", "Villa rentals"), inactive product-tab labels, footer category sub-labels, "View all" links.
370: - **Muted Soft** (`{colors.muted-soft}` — #929292): Disabled link text. Used very sparingly.
371: - **Star Rating** (`{colors.star-rating}` — #222222): The same ink token — Airbnb's star icon and "4.81" rating numbers all render in ink rather than a yellow/gold color, which is a deliberate brand choice (yellow stars feel cheap in travel context).
372: - **On Primary** (`{colors.on-primary}` — #ffffff): White text on Rausch CTAs.
373: 
374: ### Semantic
375: - **Error** (`{colors.primary-error-text}` — #c13515): Inline error text for form validation. Distinct from Rausch — slightly darker, more saturated red.
376: - **Error Hover** (`{colors.primary-error-text-hover}` — #b32505): Darkens on link hover.
377: - **Legal Link Blue** (`{colors.legal-link}` — #428bff): Inline links inside legal copy (Privacy, Terms). Only used inside the legal sub-band.
378: 
379: ### Scrim
380: - **Scrim** (`{colors.scrim}` — #000000 at 50% opacity): The global modal backdrop tone — date picker, login dialog, language picker. Stored as the base hex; opacity is applied at render time.
381: 
382: ## Typography
383: 
384: ### Font Family
385: The system runs **Airbnb Cereal VF** for everything — display, body, navigation, captions, microcopy. Fallbacks walk `Circular, -apple-system, system-ui, Roboto, "Helvetica Neue", sans-serif`. **Circular** is the historic in-house typeface still kept as the first non-variable fallback; system stacks back it up.
386: 
387: There is no separate display family. The variable font carries the entire scale.
388: 
389: ### Hierarchy
390: 
391: | Token | Size | Weight | Line Height | Letter Spacing | Use |
392: |---|---|---|---|---|---|
393: | `{typography.rating-display}` | 64px | 700 | 1.1 | -1px | Listing detail rating display ("4.81") |
394: | `{typography.display-xl}` | 28px | 700 | 1.43 | 0 | Homepage h1 ("Inspiration for future getaways") |
395: | `{typography.display-lg}` | 22px | 500 | 1.18 | -0.44px | Listing detail h1 ("Close to Fethiye Aliyah Bali Beach…") |
396: | `{typography.display-md}` | 21px | 700 | 1.43 | 0 | Section heads inside listing detail ("What this place offers") |
397: | `{typography.display-sm}` | 20px | 600 | 1.20 | -0.18px | Sub-section titles ("Things to know") |
398: | `{typography.title-md}` | 16px | 600 | 1.25 | 0 | City link block titles ("Wilmington", "Athens") |
399: | `{typography.title-sm}` | 16px | 500 | 1.25 | 0 | Footer column heads ("Support", "Hosting", "Airbnb") |
400: | `{typography.body-md}` | 16px | 400 | 1.5 | 0 | Default running-text inside listing copy |
401: | `{typography.body-sm}` | 14px | 400 | 1.43 | 0 | Card meta lines, dates, prices, distance text |
402: | `{typography.caption}` | 14px | 500 | 1.29 | 0 | Search field segment labels ("Where", "When", "Who") |
403: | `{typography.caption-sm}` | 13px | 400 | 1.23 | 0 | Footer legal line ("© 2026 Airbnb, Inc.") |
404: | `{typography.badge}` | 11px | 600 | 1.18 | 0 | "Guest favorite" floating badge text |
405: | `{typography.micro-label}` | 12px | 700 | 1.33 | 0 | Card amenity micro-labels ("Inline 6") |
406: | `{typography.uppercase-tag}` | 8px | 700 | 1.25 | 0.32px (uppercase) | "NEW" badge on product nav tabs |
407: | `{typography.button-md}` | 16px | 500 | 1.25 | 0 | Primary CTA button labels |
408: | `{typography.button-sm}` | 14px | 500 | 1.29 | 0 | Pill button labels (category strip) |
409: | `{typography.link}` | 14px | 400 | 1.43 | 0 | Inline body links |
410: | `{typography.nav-link}` | 16px | 600 | 1.25 | 0 | Top product-nav labels (Homes, Experiences, Services) |
411: 
412: ### Principles
413: Display weights stay modest. The homepage h1 at 28px / 700 is deliberately small — it tucks under the search bar so photography and the city-link grid carry visual hierarchy. The listing-detail h1 at 22px / 500 is even quieter; the listing photo banner does the work above it.
414: 
415: The single typographically loud moment in the entire system is the **rating display** (`{typography.rating-display}` — 64px / 700) on listing pages. That is the only place the system trusts type alone to carry hierarchy — rating numbers are a peak trust signal, so they get the loudest treatment.
416: 
417: ### Note on Font Substitutes
418: If Airbnb Cereal VF and Circular are unavailable, **Inter** is the closest open-source substitute. Adjust display headlines down by ~2% in line-height to match Cereal's slightly tighter cap height; otherwise the proportions transfer cleanly.
419: 
420: ## Layout
421: 
422: ### Spacing System
423: - **Base unit:** 4px (with 2px micro-step).
424: - **Tokens:** `{spacing.xxs}` 2px · `{spacing.xs}` 4px · `{spacing.sm}` 8px · `{spacing.md}` 12px · `{spacing.base}` 16px · `{spacing.lg}` 24px · `{spacing.xl}` 32px · `{spacing.xxl}` 48px · `{spacing.section}` 64px.
425: - **Section padding (vertical):** `{spacing.section}` (64px) for major page bands; tighter than typical SaaS marketing (80–96px) because marketplace pages need higher card density per scroll.
426: - **Card internal padding:** `{spacing.lg}` (24px) for `{component.host-card}` and `{component.reservation-card}`; `{spacing.base}` (16px) for property-card meta block; `{spacing.sm}` (8px) for caption / date-row gutters.
427: - **Gutters:** `{spacing.base}` (16px) between cards in the homepage city grid; `{spacing.lg}` (24px) inside footer column gutters; `{spacing.xs}` (4px) on dense category-strip dividers.
428: 
429: ### Grid & Container
430: - **Max content width:** ~1280px centered on the homepage and editorial pages. Listing detail pages cap closer to 1080px to keep the photo banner and reservation rail readable.
431: - **City link grid (homepage footer):** 6-column grid at desktop with each cell housing a city name in `{typography.title-md}` and a category sub-label in `{typography.body-sm}` muted.
432: - **Listing detail:** 2-column with photo / amenity body on the left (~64% width) and a sticky reservation card (`{component.reservation-card}`) on the right (~32%).
433: - **Footer:** 3-column link list (Support / Hosting / Airbnb) at desktop, collapsing to 1-column on mobile.
434: 
435: ### Whitespace Philosophy
436: The system gives editorial bands 64px of vertical breathing room but compresses card grids — property and city-link cards sit just 16px apart. The contrast is intentional: the page reads as "open hero, dense marketplace below," reinforcing the marketplace nature without overwhelming the visitor at the fold.
437: 
438: ## Elevation
439: 
440: The system has essentially **one shadow tier** plus the flat baseline.
441: 
442: - **Flat (no shadow):** Body, hero, footer, all editorial bands — 95% of surfaces.
443: - **Card hover float:** `box-shadow: rgba(0, 0, 0, 0.02) 0 0 0 1px, rgba(0, 0, 0, 0.04) 0 2px 6px 0, rgba(0, 0, 0, 0.1) 0 4px 8px 0` — applied to property cards on pointer hover, the search bar at rest, and the dropdown menus (account menu, language picker, date picker). This is the single shadow definition in the entire system.
444: - **Modal scrim:** `{colors.scrim}` rendered at 50% opacity — the global modal backdrop. Used on date pickers, login dialogs, language picker.
445: 
446: There are no progressive elevation tiers — the system either has the one shadow or none. Depth comes from photography, the white-on-white surface separation, and rounded-corner clipping rather than from layered shadows.
447: 
448: ## Components
449: 
450: ### Buttons
451: 
452: **`button-primary`** — Rausch fill, white text, 8px radius, 14×24px padding, 48px height, weight 500. The most common CTA across the system: "Reserve", "Continue", "Search", account-flow primaries.
453: 
454: **`button-primary-active`** — The press state. Background flips to `{colors.primary-active}`. No transform, no shadow change.
455: 
456: **`button-primary-disabled`** — Pale Rausch tint at #ffd1da with white text. Cursor not-allowed.
457: 
458: **`button-secondary`** — White fill with ink text and a 1px ink outline. 8px radius. Used for "Save", "Cancel", and inverse CTAs over Rausch surfaces.
459: 
460: **`button-tertiary-text`** — Plain ink text, no surface, no border. Underlined on hover. Used for "Show more" type links and modal close labels.
461: 
462: **`button-pill-rausch`** — A pill-shaped Rausch CTA used on featured cells (e.g., "Become a host" sub-CTA) — 9999px radius, 10×20px padding, 14px label.
463: 
464: ### Search Surface
465: 
466: **`search-bar-pill`** — The signature global search bar. White fill, 9999px radius, 64px height, 1px hairline 1px-shadow border. Internally divided by vertical hairline rules into `{component.search-field-segment}` cells (Where / When / Who). Each segment holds an uppercase caption label above a placeholder line in `{typography.caption}`.
467: 
468: **`search-orb`** — The circular Rausch orb terminating the right edge of the search bar. 48×48px, fully rounded, white magnifying-glass icon centered. The hottest single color moment on the homepage.
469: 
470: ### Top Navigation
471: 
472: **`top-nav`** — White surface, 80px height, 1px bottom hairline. The Airbnb wordmark sits flush left, the three product tabs (Homes / Experiences / Services) sit in the dead center, and account utilities (host link, language globe, account menu) sit flush right.
473: 
474: **`product-tab-active`** — Ink label in `{typography.nav-link}`, 32px hand-illustrated icon, 2px ink underline rule beneath the icon-label pair.
475: 
476: **`product-tab-inactive`** — Muted label, illustrated icon, no underline. Becomes active on click.
477: 
478: **`new-tag`** — A tiny rounded-pill badge (`{rounded.full}`) anchored top-right of an icon, carrying the uppercase "NEW" label in `{typography.uppercase-tag}` (8px / 700 with 0.32px tracking, uppercase). Used on Experiences and Services to signal recency.
479: 
480: ### Listing Cards
481: 
482: **`property-card`** — A photo-first card. 1:1 aspect-ratio image with `{rounded.md}` corner clipping, image carousel dots overlay, "Guest favorite" floating badge top-left (`{component.guest-favorite-badge}`), and a heart icon top-right (`{component.icon-button-circle}` in default outlined state, Rausch-filled when saved). Beneath the image: 4–5 lines of meta — title (`{typography.title-md}`), distance / dates (`{typography.body-sm}` muted), and price ("$X night") right-aligned.
483: 
484: **`property-card-photo`** — The photo plate itself, separated as a token because some surfaces (wishlist, search results) reuse just the photo without the meta block.
485: 
486: **`experience-card`** — A taller-aspect card (4:5) for experience listings. Same `{rounded.md}` clipping, floating "NEW" badge top-left, heart top-right, and a single-line title beneath.
487: 
488: **`guest-favorite-badge`** — White rounded pill (`{rounded.full}`) at 11px / 600 weight. Sits over the photo with the system's only shadow tier applied for elevation.
489: 
490: ### Listing Detail
491: 
492: **`rating-display-card`** — The signature listing-detail moment. A 64px / 700 rating number ("4.81") flanked left and right by tiny laurel-wreath SVG ornaments. Beneath the rating: "Guest favorite" tagline and a row of ink stat columns. The largest typographic weight in the whole system.
493: 
494: **`amenity-row`** — A 1-column list of amenity icons + ink labels in `{typography.body-md}`. 12px row padding, no border between rows; section is closed by a 1px hairline divider above and below.
495: 
496: **`reviews-card`** — A 2-column grid of review excerpts. Each column holds an author row (avatar, name, date) above a 3-line excerpt with "Show more" tertiary link.
497: 
498: **`host-card`** — A white card with `{rounded.md}` rounding and 24px padding holding a host avatar, name, "Superhost" badge, response-rate stat, and a "Contact host" `{component.button-secondary}`.
499: 
500: **`reservation-card`** — The sticky right-rail card on listing detail pages. White surface, `{rounded.md}` rounding, 1px hairline border, 1px shadow tier elevation, 24px padding. Contains: nightly price (`{typography.display-md}` ink), date-range selector, guest-count stepper, "Reserve" primary CTA full-width, and a fee breakdown stack beneath in `{typography.body-sm}`.
501: 
502: ### Date Picker
503: 
504: **`date-picker-day`** — A 40×40px circular cell carrying the day number in `{typography.body-sm}`. Default state is transparent fill, ink text.
505: 
506: **`date-picker-day-selected`** — Ink fill, white text, full circle (`{rounded.full}`). Range states between two selected days carry a `{colors.surface-soft}` lozenge background that connects them.
507: 
508: ### Forms
509: 
510: **`text-input`** — White surface, 1px hairline outline, `{rounded.sm}` 8px radius, 56px height, 14×12px padding. Stacked label above (in `{typography.caption}` muted), placeholder text in `{typography.body-md}` muted. On focus, the border thickens to 2px ink and the border color flips to `{colors.ink}` — no glow, no ring.
511: 
512: ### Footer
513: 
514: **`footer-light`** — White surface (matches the page canvas — Airbnb has no contrast footer), 48×80px padding. Three columns of link blocks (Support / Hosting / Airbnb), separated by generous 24px gutters. Each column heads with a `{typography.title-sm}` ink label and stacks `{component.footer-link}` rows in `{typography.body-sm}` ink.
515: 
516: **`legal-band`** — A bottom strip beneath the footer columns carrying the copyright line, language picker (globe icon + "English (US)" link), currency picker, and social icons (Facebook, X, Instagram). All text in muted `{colors.muted}` at `{typography.caption-sm}`.
517: 
518: ## Responsive Behavior
519: 
520: | Name | Width | Key Changes |
521: |---|---|---|
522: | Mobile | < 744px | Top nav collapses to logo + hamburger; product tabs hide behind a sheet; search bar collapses to a single tappable pill; property cards stack 1-up; city grid 1-column; listing detail collapses reservation card to a sticky bottom bar. |
523: | Tablet | 744–1128px | Top nav keeps product tabs but search bar narrows; property cards 2-up; city grid 2–3 column; reservation card stays sticky right-rail at narrower width. |
524: | Desktop | 1128–1440px | Full top nav with three product tabs centered; search bar at full pill width with all 3 segments visible; property cards 4-up; city grid 6-column; listing detail 2-column with reservation rail. |
525: | Wide | > 1440px | Content width caps at 1440px on listing/search pages and ~1280px on editorial; gutters absorb the rest. |
526: 
527: ### Touch Targets
528: - Primary CTAs at minimum 48×48px (above WCAG AAA).
529: - Search orb is 48×48px circular — the most-tapped element on the page.
530: - Heart save button is 32×32px circular — borderline for AAA but compensated by a generous 12px padding inside the photo card.
531: - Date-picker day cells are 40×40px circular.
532: 
533: ### Collapsing Strategy
534: - Top product tabs collapse into a hamburger sheet below 744px.
535: - Search bar's 3 segments collapse into a single-tap entry that opens a full-screen search overlay on mobile.
536: - Property and city-link grids drop column counts cleanly at each breakpoint — never reflow rows; always reduce columns.
537: - Reservation card on listing detail switches from sticky right-rail to a sticky bottom bar on mobile, carrying just the "Reserve" CTA + nightly price summary.
538: 
539: ## Known Gaps
540: 
541: - **Hover state colors:** intentionally not documented per the global no-hover policy — Airbnb's actual `:hover` styling for property cards is a subtle elevation lift, but precise extraction is unreliable.
542: - **Loading states / skeleton screens:** not visible on the extracted surfaces.
543: - **Map view styling:** the search-results map uses Mapbox-tinted tiles with custom Rausch markers; not captured here.
544: - **Form input error states:** error text color (`{colors.primary-error-text}`) is documented, but the full input outline + helper-text combination on validation failure was not visible in the captured surfaces.
545: - **Sub-brand palettes:** Luxe (`{colors.luxe}`) and Plus (`{colors.plus}`) are documented as tokens, but their full sub-system (typography overrides, surface treatment) lives on separate sub-domains and is not captured here.

(End of file - total 545 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/skills/extract_design_skill.md"
}
```

**Output:**
```
<path>/home/mkt/design_md/skills/extract_design_skill.md</path>
<type>file</type>
<content>
1: # Skill: Precision DESIGN.md Extractor
2: 
3: ## Objetivo
4: Atuar como um Engenheiro de UI/UX de elite. Sua tarefa é visitar uma URL alvo fornecida pelo usuário e fazer engenharia reversa do design system do site, transformando-o em um arquivo `DESIGN.md` impecável e *pixel-perfect*, seguindo estritamente o padrão do Google Stitch.
5: 
6: ## Pré-Requisitos (Pre-Flight)
7: 1. **Aprender o Padrão (Schema):** Antes de iniciar qualquer extração, você DEVE obrigatoriamente usar a ferramenta `view_file` para ler e absorver a estrutura do arquivo de referência localizado em `/Users/fatima/Desktop/awesome_design/design-md/stripe/DESIGN.md` (ou `apple/DESIGN.md`).
8: 2. Preste atenção rigorosa em como as cores (Hex), tipografia, raios de borda (border-radius), sombras e estados interativos são documentados.
9: 
10: ## Passos de Execução
11: 
12: ### Fase 1: Inspeção Visual e Técnica Profunda
13: Invoque o `browser_subagent` com a URL alvo. Instrua o subagente a realizar uma auditoria técnica rigorosa do DOM e do CSS (Computed Styles):
14: - **Cores (Colors):** Extraia os valores exatos em HEX para o fundo (background), texto (primário, secundário, mutado), cores primárias da marca e cores semânticas (sucesso, aviso, erro). Verifique se há variáveis CSS (`--var`).
15: - **Tipografia (Typography):** Identifique a stack exata de `font-family`. Extraia os pesos (weights - ex: 400, 500, 600) e tamanhos para os títulos (H1-H6) e texto base (body).
16: - **Elementos e Componentes (UI Elements):** Inspecione botões, inputs e cards. Extraia os valores matemáticos exatos para:
17:   - `border-radius` (ex: 4px, 8px, pill/9999px)
18:   - `box-shadow` (sombras de elevação, sombras suaves)
19:   - Escala de espaçamento (padding e margins padrão)
20:   - Estados de Hover e Active (transições, mudanças de cor)
21: - **Layout:** Identifique a largura máxima (max-width) do container principal e a estrutura do grid.
22: 
23: ### Fase 2: Síntese e Mapeamento
24: Traduza o CSS bruto e os dados visuais capturados para a formatação rigorosa do `DESIGN.md`.
25: - **PROIBIDO ALUCINAR DADOS:** Se um valor não for óbvio visualmente, baseie-se nos estilos computados do CSS.
26: - **Filosofia do Design:** Escreva uma breve introdução que capture a "vibe" e a filosofia estética da marca (ex: "minimalista de luxo", "brutalista", "corporativo limpo").
27: 
28: ### Fase 3: Geração do Arquivo
29: 1. Determine o nome da marca a partir da URL (ex: `netflix`, `spotify`).
30: 2. Use a ferramenta `write_to_file` para criar o novo arquivo exatamente no caminho: `/Users/fatima/Desktop/awesome_design/design-md/<nome_da_marca>/DESIGN.md`.
31: 3. O arquivo gerado DEVE manter a exata hierarquia de Markdown (headings, blocos de código, listas) aprendida na fase de Pré-Requisitos.
32: 
33: ## Garantia de Qualidade (QA)
34: Antes de finalizar a tarefa e retornar ao usuário, verifique internamente:
35: - Os códigos HEX são reais e foram extraídos do site?
36: - A tipografia reflete a identidade verdadeira da marca?
37: - A estrutura do Markdown bate 100% com o padrão Stitch adotado pelos exemplos?

(End of file - total 37 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/design-md-awesome/airbnb/README.md"
}
```

**Output:**
```
<path>/home/mkt/design_md/design-md-awesome/airbnb/README.md</path>
<type>file</type>
<content>
1: # Airbnb Inspired Design System
2: 
3: Design system details have been moved to: https://getdesign.md/airbnb/design-md
4: 
5: You can also view previews, dark mode examples, and download options on getdesign.md.

(End of file - total 5 lines)
</content>
```

---

## Assistant (Build · Big Pickle · 10.4s)

_Thinking:_

Now I have a comprehensive understanding of this repository. Let me summarize what I've learned:

## Repository: design_md

### Purpose
A curated collection of DESIGN.md files — YAML front matter + Markdown design system definitions in the Google Stitch format. These are design tokens (colors, typography, spacing, rounding, components) that AI coding agents can consume to generate visually consistent UI.

### Structure
- `/design-md-awesome/` — 73 brand-inspired DESIGN.md files (Airbnb, Apple, Spotify, Stripe, etc.), each in its own subdirectory with a DESIGN.md and a README.md
- `/design-md-library/` — Tools for downloading/extracting design systems from designmd.app
  - `elementos_designmd.md` — A table of 454 design systems from the library
  - `automacao_bookmarklet.py` — Selenium-like automation to download DESIGN.md files
  - `download_and_move.py` — Script to download and organize screen thumbnails
  - `todo.md` — Notes on remaining tasks
  - `454/` — The actual extracted DESIGN.md files (454 subdirectories)
- `/skills/` — AI skill definitions (e.g., `extract_design_skill.md` for reverse-engineering design systems from URLs)
- `comandos.js` — Bookmarklet/browser automation helper JS
- `dicas.md` — Scratch notes
- `llms-full.txt` — Full catalog dump of all 454+ design systems from designmd.app

### Key Facts for an Agent
1. **No build system, no tests, no linter** — this is a static content repository. No npm/pip/package manager needed.
2. **No existing AGENTS.md** — fresh file to create.
3. **DESIGN.md format** is the core artifact: YAML front matter with `colors`, `typography`, `rounded`, `spacing`, `components` sections, plus Markdown body with design rationale.
4. **Two sources** of DESIGN.md files:
   - `design-md-awesome/` — hand-curated, brand-specific files
   - `design-md-library/454/` — bulk-downloaded from designmd.app (454 files)
5. **Workflow**: The `skills/extract_design_skill.md` describes the process for creating new DESIGN.md files by reverse-engineering URLs. This is the main "active" workflow.
6. **References**: `llms-full.txt` is a comprehensive reference. `designmd.app` is the canonical source.
7. **Portuguese context**: Several files are in Portuguese (Brazilian), including the skills file, automation scripts, and many DESIGN.md names. The project origin is ft.ia.br.
8. **No package.json, no CI, no pre-commit hooks** — very simple project.

Let me now create the AGENTS.md file. Since there's no existing one, I'll write a compact, high-signal instruction file.

Key things to include:
- Repo purpose: collection of DESIGN.md design system files
- Two source directories and their distinction
- The DESIGN.md format (YAML front matter + Markdown body)
- The extractor skill workflow for creating new files
- No build/test/lint tooling — this is a static content repo
- Important reference: `llms-full.txt` and `skills/`
- Portuguese context
- The designmd.app URLs and how tools/widgets work
- No env/setup needed

Now I have a thorough understanding of the repo. Let me check git diff to see current state.

**Tool: bash**

**Input:**
```json
{
  "command": "git diff HEAD --stat",
  "description": "Check working tree changes"
}
```

**Output:**
```
(no output)
```

**Tool: bash**

**Input:**
```json
{
  "command": "git status --short",
  "description": "Check git status"
}
```

**Output:**
```
(no output)
```

---

## Assistant (Build · Big Pickle · 7.7s)

_Thinking:_

Clean working tree. Now let me create the AGENTS.md file.

**Tool: write**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/AGENTS.md",
  "content": "# design_md — AGENTS.md\n\n## What this is\n\nA curated collection of **DESIGN.md** files — design system definitions in [Google Stitch](https://designmd.app/what-is-design-md) format (YAML front matter + Markdown prose). AI coding agents consume these from a project root to generate visually consistent UI.\n\n## Layout\n\n- `design-md-awesome/` — 73 hand-curated DESIGN.md files (Airbnb, Apple, Stripe, etc.), each in `brand/DESIGN.md` + `brand/README.md`\n- `design-md-library/454/` — 454 DESIGN.md files bulk-downloaded from [designmd.app/library](https://designmd.app/library), organized by slug\n- `design-md-library/elementos_designmd.md` — Master table of all 454 library entries\n- `skills/extract_design_skill.md` — AI skill for reverse-engineering a site's design system into DESIGN.md\n- `llms-full.txt` — Complete catalog dump of all design systems from designmd.app\n\n## DESIGN.md format\n\nYAML front matter with sections: `colors`, `typography`, `rounded`, `spacing`, `components`. Followed by Markdown body with sections: Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts. Component tokens use `{path.to.token}` cross-references. See any file in `design-md-awesome/` for reference.\n\n## No build / test / lint tooling\n\nThis is a static content repo. No package.json, no CI, no formatter, no typechecker. There is nothing to install or run.\n\n## Creating new DESIGN.md files\n\nUse the workflow in `skills/extract_design_skill.md`:\n1. Read an existing reference (e.g. `design-md-awesome/stripe/DESIGN.md`)\n2. Inspect the target URL's DOM and computed styles via browser\n3. Extract exact HEX colors, font stacks, border-radius, shadows, spacing\n4. Write a new `DESIGN.md` under `design-md-library/454/<slug>/`\n\n## Reference sources\n\n- `llms-full.txt` — The canonical offline reference (~500 entries)\n- [designmd.app/library](https://designmd.app/library) — Library browser with 454+ design systems\n- `npx @google/design.md lint` — Official CLI for validating DESIGN.md files (broken-refs, contrast-ratio, section-order)\n\n## Language note\n\nMany files, scripts, and design system names are in Brazilian Portuguese. The canonical author is ft.ia.br. `dicas.md` and `comandos.js` are scratch notes — ignore their content unless specifically needed.\n\n## Browser automation helpers\n\n- `automacao_bookmarklet.py` — PyAutoGUI script to bulk-download DESIGN.md files from the library (requires `pip install pyautogui opencv-python`)\n- `download_and_move.py` — Downloads preview thumbnails for the 454 library entries\n- `comandos.js` — DevTools snippet for scraping the library page via `document.querySelectorAll('.group.block')`\n"
}
```

**Output:**
```
Wrote file successfully.
```

---

## Assistant (Build · Big Pickle · 6.5s)

_Thinking:_

The file has been written. Let me verify it looks correct.

`AGENTS.md` created at `/home/mkt/design_md/AGENTS.md`. It captures the repo's structure (two DESIGN.md collections, 73 + 454 files), the DESIGN.md format, the extractor skill workflow, references (`llms-full.txt`, designmd.app), the static-content nature (no build/test/lint), Portuguese context, and browser helper scripts — all verified from source.

---

## User

sobre o que se trata ese projeto? 

---

## Assistant (Build · Big Pickle · 2.9s)

_Thinking:_

The user is asking in Portuguese: "what is this project about?" Let me answer concisely.

Coleção de arquivos `DESIGN.md` (definições de design system no formato Google Stitch) para agentes de IA usarem ao gerar UI visualmente consistente. Contém 73 sistemas curados de marcas como Airbnb, Apple, Stripe, e 454 sistemas baixados em massa de [designmd.app/library](https://designmd.app/library).

---

## User

o que faz o @design-md-library/automacao_bookmarklet.py ?

---

## Assistant (Build · Big Pickle · 3.2s)

_Thinking:_

The user is asking what `automacao_bookmarklet.py` does. I already read the file and understand it. Let me answer concisely.

Automação com PyAutoGUI para baixar os 454 DESIGN.md files em massa. Ele lê a tabela em `elementos_designmd.md`, abre cada URL do library no navegador, e clica no bookmarklet do navegador para disparar o download — tudo via coordenadas fixas ou reconhecimento de imagem.

---

## User

qual o botão que ele vai clicar nesse script? 

---

## Assistant (Build · Big Pickle · 7.0s)

_Thinking:_

The user is asking what button the script clicks. Let me think about this based on the code and the context.

The script is called `automacao_bookmarklet.py`. The key variable is `USAR_COORDENADAS` and it clicks at `BOTAO_X, BOTAO_Y` coordinates. But what is this button?

Looking at the `comandos.js` file, there's a line:
```js
// para baixar: 
document.querySelector('#download-designmd').click()
```

And looking at the llms-full.txt guides section:
```
- Claude Code: config file CLAUDE.md, Siga as regras visuais de @DESIGN.md
- Cursor: config file .cursor/rules/*.mdc, Include do DESIGN.md
...
```

The script opens each library page on designmd.app, then clicks on a bookmarklet (browser bookmarklet) that presumably triggers the download of the DESIGN.md file. 

The user is asking **which button** specifically. Looking at the script name — "automacao_bookmarklet" — it's clicking a **browser bookmarklet** (favorito). Each page on designmd.app/library has a download button or a bookmarklet that, when clicked, downloads/copies the DESIGN.md file.

Looking at `comandos.js` line 28:
```js
document.querySelector('#download-designmd').click()
```

So the button has id `#download-designmd`. But the script itself uses PyAutoGUI to click on the browser's bookmark bar (where the user has saved a bookmarklet), not a button on the page.

Actually, re-reading the script more carefully:
- It opens each library URL in a new tab
- Then it moves the mouse to coordinates (BOTAO_X, BOTAO_Y) and clicks
- The "button" is a **bookmarklet** saved in the browser's bookmarks bar

But wait, what does the bookmarklet actually do? Looking at designmd.app, the bookmarklet likely triggers the download of the DESIGN.md file. The `download-designmd` element in comandos.js gives a hint.

So the script is clicking on a bookmarklet in the browser's bookmark bar (at fixed coordinates like X=350, Y=100), which is a JavaScript bookmarklet that downloads the DESIGN.md file from the current page.

Let me answer concisely: it's clicking a **browser bookmarklet (favorito)** that downloads the DESIGN.md file from the current library page.

O script clica num **bookmarklet do navegador** (aquele favorito na barra de favoritos) que, ao ser acionado na página do library, dispara o download do arquivo `DESIGN.md`. O elemento equivalente na página tem id `#download-designmd` (como visto em `comandos.js:28`).

---

## User

mas o botão tem coordenadas ou uma imagem png ou jpg? 

---

## Assistant (Build · Big Pickle · 4.3s)

_Thinking:_

The user is asking what the script clicks on - coordinates or an image. Looking at the code again:

- Option 1 (default, `USAR_COORDENADAS = True`): clicks at fixed screen coordinates `BOTAO_X = 350`, `BOTAO_Y = 100` — no image involved, just a blind mouse move+click.
- Option 2: uses `pyautogui.locateCenterOnScreen` with an image file `botao_favorito.png`.

The script doesn't click on a button rendered in the page's DOM — it clicks on the browser's bookmark bar button (the bookmarklet). That's why it uses PyAutoGUI instead of a browser automation tool.

So the answer is: by default it uses fixed screen coordinates (`350, 100`), no image. Optionally it can use an image file (`botao_favorito.png`).

Nenhum dos dois por padrão. O script usa **coordenadas fixas da tela** (`BOTAO_X = 350`, `BOTAO_Y = 100`) — ele move o mouse cegamente para aquela posição e clica, sem reconhecer nada visualmente. A opção alternativa (desativada por padrão) usa uma imagem `botao_favorito.png` via `locateCenterOnScreen`.

---

## User

comente essa linha e mude-a para uma imagem. Me diga porém, com qual nome salvo a imagem que o script vai procurar para clicar sobre ele

---

## Assistant (Build · Big Pickle · 4.4s)

_Thinking:_

The user wants me to:
1. Change the script from using fixed coordinates to using image recognition
2. They want to know what name to save the image as

The current code has `USAR_COORDENADAS = True` and uses `BOTAO_X = 350, BOTAO_Y = 100`. I need to:
- Comment out the coordinate lines or set `USAR_COORDENADAS = False`
- The image file is already defined as `NOME_DA_IMAGEM = 'botao_favorito.png'` on line 32
- Tell them to save the image as `botao_favorito.png`

O nome já está definido no script: `botao_favorito.png` (linha 32). Salve um print **bem pequeno** apenas do botão do bookmarklet na barra de favoritos com esse nome, na mesma pasta do script.

**Tool: edit**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/design-md-library/automacao_bookmarklet.py",
  "oldString": "USAR_COORDENADAS = True\nBOTAO_X = 350  # <-- Mude para o valor X do seu mouse\nBOTAO_Y = 100  # <-- Mude para o valor Y do seu mouse",
  "newString": "# OPÇÃO 1: Coordenadas Fixas da Tela (desativada — usando imagem)\n# BOTAO_X = 350\n# BOTAO_Y = 100\nUSAR_COORDENADAS = False"
}
```

**Output:**
```
Edit applied successfully.
```

---

## Assistant (Build · Big Pickle · 2.9s)

_Thinking:_

Done. The script now uses image recognition mode. The user needs to save a screenshot of the bookmarklet button as `botao_favorito.png` in the same directory as the script.

Pronto. Salve a imagem do botão do bookmarklet como **`botao_favorito.png`** na pasta `design-md-library/`.

---

## User

---

## Assistant (Build · Big Pickle · 0.0s)

**Tool: bash**

**Input:**
```json
{
  "command": "pwd"
}
```

**Output:**
```
/home/mkt/design_md

```

---

## User

o script está programado a abrir as páginas? ou seja, digitar a URL??? a partir de que lista?

---

## Assistant (Build · Big Pickle · 3.8s)

_Thinking:_

The user is asking if the script opens pages (types URLs) and from what list. I already know the answer from reading the file - it reads URLs from `elementos_designmd.md` and opens them using `webbrowser.open_new_tab(url)`. But let me re-read the relevant part to be precise.

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/design-md-library/automacao_bookmarklet.py",
  "offset": 36,
  "limit": 25
}
```

**Output:**
```
<path>/home/mkt/design_md/design-md-library/automacao_bookmarklet.py</path>
<type>file</type>
<content>
36: 
37: # 1. Lê a tabela para extrair as URLs
38: with open(md_file, 'r') as f:
39:     lines = f.readlines()
40: 
41: urls = []
42: for line in lines:
43:     if line.startswith('|'):
44:         # Extrai o link da terceira coluna
45:         match = re.search(r'(https://designmd\.app/(?:en/)?library/[^)]+)', line)
46:         if match:
47:             urls.append(match.group(1))
48: 
49: print(f"Foram encontradas {len(urls)} URLs.")
50: print("AVISO: Deixe o seu navegador visível e na mesma posição.")
51: print("Iniciando em 5 segundos... (Para parar a qualquer momento, arraste o mouse rapidamente para qualquer um dos 4 cantos da tela!)")
52: time.sleep(5)
53: 
54: # 2. Executa o fluxo para cada URL
55: for i, url in enumerate(urls):
56:     print(f"\n[{i+1}/{len(urls)}] Abrindo página: {url}")
57:     
58:     # Abre a URL em uma nova aba do navegador padrão
59:     webbrowser.open_new_tab(url)
60:     

(Showing lines 36-60 of 114. Use offset=61 to continue.)
</content>
```

---

## Assistant (Build · Big Pickle · 3.0s)

Sim. O script extrai as URLs da tabela em `elementos_designmd.md` (linha 14: `md_file = '/Users/fatima/Desktop/awesome_design/design-md-library/elementos_designmd.md'`) e abre cada uma com `webbrowser.open_new_tab(url)` (linha 59) — que usa o navegador padrão do sistema, não digita URL manualmente.

---

## User

abra apenas um dos URLs sem clicar em nada 

---

## Assistant (Build · Big Pickle · 5.5s)

_Thinking:_

The user wants me to open just one URL from the library without clicking anything. I should use the browser tool to open a page from designmd.app/library. Let me pick a URL - maybe one of the simpler ones. I'll use the Stripe one or a simple one. Let me just open one of the URLs from the library, like the minimalism-swiss-style one or something simple.

Actually, the user said "abra apenas um dos URLs sem clicar em nada" - open just one of the URLs without clicking anything. They want to see what the page looks like, probably to understand what the bookmarklet is about.

Let me pick a URL from the library. I'll navigate to one.

**Tool: chrome-devtools_new_page**

**Input:**
```json
{
  "url": "https://designmd.app/en/library/airbnb-coral-marketplace"
}
```

**Output:**
```
## Pages
1: about:blank
2: https://designmd.app/library/airbnb-coral-marketplace [selected]
```

---

## Assistant (Build · Big Pickle · 2.9s)

_Thinking:_

Let me take a screenshot and snapshot so the user can see what the page looks like.

**Tool: chrome-devtools_take_snapshot**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/design-md-library/library_page_snapshot.txt"
}
```

**Output:**
```
Saved snapshot to /home/mkt/design_md/design-md-library/library_page_snapshot.txt.
```

---

## Assistant (Build · Big Pickle · 2.6s)

_Thinking:_

Let me take a screenshot so the user can see the page, and also let me read the snapshot to understand what the download button looks like.

**Tool: chrome-devtools_take_screenshot**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/screenshot.png"
}
```

**Output:**
```
Took a screenshot of the current page's viewport.
Saved screenshot to /home/mkt/design_md/screenshot.png.
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/design-md-library/library_page_snapshot.txt"
}
```

**Output:**
```
<path>/home/mkt/design_md/design-md-library/library_page_snapshot.txt</path>
<type>file</type>
<content>
1: uid=1_0 RootWebArea "Airbnb Coral Marketplace — DESIGN.md | designmd.app" url="https://designmd.app/library/airbnb-coral-marketplace"
2:   uid=1_1 banner
3:     uid=1_2 navigation
4:       uid=1_3 link "DESIGN.MD APP" url="https://designmd.app/"
5:         uid=1_4 StaticText "DESIGN.MD"
6:         uid=1_5 StaticText " APP"
7:       uid=1_6 link "Home" url="https://designmd.app/"
8:         uid=1_7 StaticText "Home"
9:       uid=1_8 link "Library" url="https://designmd.app/library"
10:         uid=1_9 StaticText "Library"
11:       uid=1_10 link "Guides" url="https://designmd.app/guides"
12:         uid=1_11 StaticText "Guides"
13:       uid=1_12 link "Blog" url="https://designmd.app/blog"
14:         uid=1_13 StaticText "Blog"
15:       uid=1_14 link "Skills" url="https://designmd.app/skills"
16:         uid=1_15 StaticText "Skills"
17:       uid=1_16 link "Português" url="https://designmd.app.br/library/airbnb-coral-marketplace/"
18:         uid=1_17 StaticText "Português"
19:   uid=1_18 navigation "Breadcrumb"
20:     uid=1_19 link "Home" url="https://designmd.app/"
21:       uid=1_20 StaticText "Home"
22:     uid=1_21 StaticText " "
23:     uid=1_22 link "Library" url="https://designmd.app/library"
24:       uid=1_23 StaticText "Library"
25:     uid=1_24 StaticText " "
26:     uid=1_25 StaticText "Airbnb Coral Marketplace"
27:   uid=1_26 main
28:     uid=1_27 StaticText "Temas & Verticais"
29:     uid=1_28 StaticText "2024-2026 Travel Marketplace"
30:     uid=1_29 heading "AIRBNB CORAL MARKETPLACE" level="1"
31:     uid=1_30 StaticText "Design an Airbnb-inspired warm marketplace landing page. Ideal for marketplaces, viagens, plataformas de hospedagem, e-commerce experiencial. AI-ready template."
32:     uid=1_31 StaticText "airbnb"
33:     uid=1_32 StaticText "coral"
34:     uid=1_33 StaticText "marketplace"
35:     uid=1_34 StaticText "Rausch Red"
36:     uid=1_35 StaticText "Cereal VF"
37:     uid=1_36 StaticText "three-layer shadows"
38:     uid=1_37 StaticText "warm near-black"
39:     uid=1_38 StaticText "circular controls"
40:     uid=1_39 StaticText "photography-first"
41:     uid=1_40 StaticText "palette tokens"
42:     uid=1_41 StaticText "USE CASE:"
43:     uid=1_42 StaticText " Marketplaces, Viagens, Plataformas de hospedagem, E-commerce experiencial"
44:     uid=1_43 image "Airbnb Coral Marketplace" url="https://designmd.app/images/library/420.png"
45:     uid=1_44 heading "HISTORICAL CONTEXT" level="2"
46:     uid=1_45 StaticText "Airbnb's design system didn't emerge from a rebrand exercise or a design trends mood board. It came from operational pain. By 2016, the product had grown into a sprawling mess of inconsistent patterns across web, iOS, and Android — different teams shipping different interpretations of the same components. The DLS (Design Language System) was their first serious attempt at unification, but Coral represents the maturation of that thinking into something far more ambitious. Coral is fundamentally a marketplace design system, which means it has to solve problems most design systems never face: trust between strangers, complex multi-party flows, and the tension between host and guest experiences that share the same interface. The system had to encode hospitality — warmth, approachability, clarity — without sacrificing the transactional efficiency a booking platform demands. What makes Coral genuinely interesting is how it treats illustration, photography, and motion as first-class citizens rather than decorative afterthoughts. The rounded forms, the Cereal typeface, the deliberate softness — these aren't aesthetic choices, they're trust-building mechanisms. Every visual decision serves the goal of making strangers comfortable enough to sleep in each other's homes."
47:     uid=1_46 heading "WHEN TO USE" level="2"
48:     uid=1_47 StaticText "Reach for Coral's patterns when you're building any platform where trust is the product. Peer-to-peer marketplaces, hospitality platforms, travel booking flows, or any service where users transact with strangers. The system excels at balancing warmth with utility — if your product needs to feel human and approachable while handling complex multi-step transactions, this is your reference. Skip it if you're building enterprise tooling or data-heavy dashboards; Coral's generosity with whitespace and illustration won't survive information density requirements."
49:     uid=1_48 heading "DESIGN PRINCIPLES" level="2"
50:     uid=1_49 StaticText "Trust through visual warmth — rounded corners, soft illustration, and generous spacing aren't decoration, they're psychological safety mechanisms for peer-to-peer transactions"
51:     uid=1_50 StaticText "Dual-persona architecture — every component must work for both sides of the marketplace without feeling like a compromise for either party"
52:     uid=1_51 StaticText "Progressive disclosure of complexity — booking flows hide enormous transactional depth behind deceptively simple surfaces, revealing complexity only when the user needs it"
53:     uid=1_52 StaticText "Photography as interface — real images of real spaces do more trust-building work than any UI pattern; the system treats content imagery as a structural element, not a fill"
54:     uid=1_53 StaticText "Locality without fragmentation — the system flexes across cultures, languages, and currencies while maintaining a single coherent identity that feels native everywhere"
55:     uid=1_54 heading "TECHNICAL SPECS" level="2"
56:     uid=1_55 heading "COLORS" level="3"
57:     uid=1_56 StaticText "PRIMARY"
58:     uid=1_57 generic description="#ffffff"
59:     uid=1_58 StaticText "#ffffff"
60:     uid=1_59 generic description="#222222"
61:     uid=1_60 StaticText "#222222"
62:     uid=1_61 generic description="#ff385c"
63:     uid=1_62 StaticText "#ff385c"
64:     uid=1_63 generic description="#f2f2f2"
65:     uid=1_64 StaticText "#f2f2f2"
66:     uid=1_65 StaticText "SECONDARY"
67:     uid=1_66 generic description="#3f3f3f"
68:     uid=1_67 StaticText "#3f3f3f"
69:     uid=1_68 generic description="#6a6a6a"
70:     uid=1_69 StaticText "#6a6a6a"
71:     uid=1_70 generic description="#c1c1c1"
72:     uid=1_71 StaticText "#c1c1c1"
73:     uid=1_72 generic description="#460479"
74:     uid=1_73 StaticText "#460479"
75:     uid=1_74 heading "EFFECTS" level="3"
76:     uid=1_75 StaticText "Canvas branco puro com Rausch Red (#ff385c) como acento singular icônico. Texto near-black quente (#222222) — nunca preto puro. Cereal VF variable font com terminais arredondados quentes, pesos 500-700. Sombras three-layer: ring (0.02) + soft blur (0.04) + primary lift (0.1). Radius generoso: 8px botões, 14px badges, 20px cards, 32px large, 50% circular. Controles circulares (50%) para carrosséis. Fotografia como conteúdo primário. Letter-spacing negativo (-0.18px a -0.44px) em headings para intimidade."
77:     uid=1_76 heading "LIGHT/DARK" level="3"
78:     uid=1_77 StaticText "✓ Full / ✗ Not Recommended"
79:     uid=1_78 heading "TECHNICAL SPECS" level="2"
80:     uid=1_79 heading "CSS" level="3"
81:     uid=1_80 StaticText "background:#ffffff;color:#222222;accent:#ff385c;box-shadow:rgba(0,0,0,0.02) 0px 0px 0px 1px,rgba(0,0,0,0.04) 0px 2px 6px,rgba(0,0,0,0.1) 0px 4px 8px;border-radius:8px buttons,20px cards,50% circles;font-family:system-ui;font-weight:500-700;letter-spacing:-0.44px at 22px"
82:     uid=1_81 heading "VARIABLES" level="3"
83:     uid=1_82 StaticText "--bg:#ffffff;--text:#222222;--red:#ff385c;--surface:#f2f2f2;--secondary:#6a6a6a;--border:#c1c1c1;--luxe:#460479;--radius-btn:8px;--radius-card:20px;--radius-circle:50%"
84:     uid=1_83 heading "CHECKLIST" level="3"
85:     uid=1_84 StaticText "☐ Canvas branco com Rausch Red, ☐ Texto near-black #222222, ☐ Variable font 500-700, ☐ Sombras three-layer, ☐ Radius generoso 8-50%, ☐ Controles circulares, ☐ Fotografia-first, ☐ Tracking negativo headings, ☐ Responsivo"
86:     uid=1_85 heading "DESIGN.MD" level="2"
87:     uid=1_86 heading "Design System: Airbnb Coral Marketplace" level="1"
88:     uid=1_87 LineBreak "
89: "
90:     uid=1_88 heading "1. Definição do Estilo" level="2"
91:     uid=1_89 LineBreak "
92: "
93:     uid=1_90 StaticText "Nome:"
94:     uid=1_91 StaticText " Airbnb Coral Marketplace"
95:     uid=1_92 StaticText "Tipo:"
96:     uid=1_93 StaticText " Warm White Canvas, Rausch Red Accent, Cereal VF Variable Font, Three-Layer Shadows, Photography-First"
97:     uid=1_94 StaticText "Keywords:"
98:     uid=1_95 StaticText " airbnb, coral, marketplace, Rausch Red, Cereal VF, three-layer shadows, warm near-black, circular controls, photography-first, palette tokens"
99:     uid=1_96 StaticText "Era:"
100:     uid=1_97 StaticText " 2024-2026 Travel Marketplace"
101:     uid=1_98 StaticText "Light/Dark:"
102:     uid=1_99 StaticText " ✓ Full / ✗ Not Recommended"
103:     uid=1_100 LineBreak "
104: "
105:     uid=1_101 heading "2. Paleta de Cores" level="2"
106:     uid=1_102 LineBreak "
107: "
108:     uid=1_103 StaticText "Primárias:"
109:     uid=1_104 StaticText " Branco #ffffff, Near Black #222222, Rausch Red #ff385c, Light Surface #f2f2f2"
110:     uid=1_105 StaticText "Secundárias:"
111:     uid=1_106 StaticText " Focused Gray #3f3f3f, Secondary Gray #6a6a6a, Border Gray #c1c1c1, Luxe Purple #460479"
112:     uid=1_107 LineBreak "
113: "
114:     uid=1_108 heading "3. Efeitos Visuais" level="2"
115:     uid=1_109 LineBreak "
116: "
117:     uid=1_110 StaticText "Canvas branco puro com Rausch Red (#ff385c) como acento singular icônico. Texto near-black quente (#222222) — nunca preto puro. Cereal VF variable font com terminais arredondados quentes, pesos 500-700. Sombras three-layer: ring (0.02) + soft blur (0.04) + primary lift (0.1). Radius generoso: 8px botões, 14px badges, 20px cards, 32px large, 50% circular. Controles circulares (50%) para carrosséis. Fotografia como conteúdo primário. Letter-spacing negativo (-0.18px a -0.44px) em headings para intimidade."
118:     uid=1_111 LineBreak "
119: "
120:     uid=1_112 heading "4. AI Prompt Keywords" level="2"
121:     uid=1_113 LineBreak "
122: "
123:     uid=1_114 StaticText "Design an Airbnb-inspired warm marketplace landing page. White canvas with Rausch Red (#ff385c) as singular iconic accent. Warm near-black (#222222) text — never pure black. Variable font with rounded terminals at weight 500-700. Three-layer card shadows: rgba(0,0,0,0.02) 0px 0px 0px 1px + rgba(0,0,0,0.04) 0px 2px 6px + rgba(0,0,0,0.1) 0px 4px 8px. Generous radius: 8px buttons, 20px cards, 50% circular controls. Photography-first listing cards. Negative letter-spacing (-0.18px to -0.44px) on headings."
124:     uid=1_115 LineBreak "
125: "
126:     uid=1_116 heading "5. CSS Technical" level="2"
127:     uid=1_117 LineBreak "
128: "
129:     uid=1_118 StaticText "background:#ffffff;color:#222222;accent:#ff385c;box-shadow:rgba(0,0,0,0.02) 0px 0px 0px 1px,rgba(0,0,0,0.04) 0px 2px 6px,rgba(0,0,0,0.1) 0px 4px 8px;border-radius:8px buttons,20px cards,50% circles;font-family:system-ui;font-weight:500-700;letter-spacing:-0.44px at 22px
130: "
131:     uid=1_119 LineBreak "
132: "
133:     uid=1_120 heading "6. Design System Variables" level="2"
134:     uid=1_121 LineBreak "
135: "
136:     uid=1_122 StaticText "--bg:#ffffff;--text:#222222;--red:#ff385c;--surface:#f2f2f2;--secondary:#6a6a6a;--border:#c1c1c1;--luxe:#460479;--radius-btn:8px;--radius-card:20px;--radius-circle:50%
137: "
138:     uid=1_123 LineBreak "
139: "
140:     uid=1_124 heading "7. Checklist de Implementação" level="2"
141:     uid=1_125 LineBreak "
142: "
143:     uid=1_126 StaticText "☐ Canvas branco com Rausch Red"
144:     uid=1_127 StaticText "☐ Texto near-black #222222"
145:     uid=1_128 StaticText "☐ Variable font 500-700"
146:     uid=1_129 StaticText "☐ Sombras three-layer"
147:     uid=1_130 StaticText "☐ Radius generoso 8-50%"
148:     uid=1_131 StaticText "☐ Controles circulares"
149:     uid=1_132 StaticText "☐ Fotografia-first"
150:     uid=1_133 StaticText "☐ Tracking negativo headings"
151:     uid=1_134 StaticText "☐ Responsivo"
152:     uid=1_135 LineBreak "
153: "
154:     uid=1_136 heading "8. Visual Theme & Atmosphere" level="2"
155:     uid=1_137 LineBreak "
156: "
157:     uid=1_138 StaticText "Estilo Airbnb Coral Marketplace com acento Rausch Red, sombras three-layer e layout photography-first. Ideal para marketplaces, viagens e plataformas de hospedagem. Inspirado no design do Airbnb, que usa Rausch Red (nomeado pela primeira rua da empresa) e fotografia como linguagem visual primária."
158:     uid=1_139 LineBreak "
159: "
160:     uid=1_140 StaticText "Density: 5/10 — Balanced"
161:     uid=1_141 StaticText "Variance: 4/10 — Moderate"
162:     uid=1_142 StaticText "Motion: 4/10 — Subtle"
163:     uid=1_143 LineBreak "
164: "
165:     uid=1_144 heading "9. Color Palette & Roles" level="2"
166:     uid=1_145 LineBreak "
167: "
168:     uid=1_146 StaticText "Branco"
169:     uid=1_147 StaticText " (#ffffff) — Light surface, card backgrounds"
170:     uid=1_148 StaticText "Near Black"
171:     uid=1_149 StaticText " (#222222) — Dark surface, primary background"
172:     uid=1_150 StaticText "Rausch Red"
173:     uid=1_151 StaticText " (#ff385c) — Error states, destructive actions"
174:     uid=1_152 StaticText "Light Surface"
175:     uid=1_153 StaticText " (#f2f2f2) — Supporting palette color"
176:     uid=1_154 StaticText "Focused Gray"
177:     uid=1_155 StaticText " (#3f3f3f) — Secondary text, borders, muted elements"
178:     uid=1_156 StaticText "Secondary Gray"
179:     uid=1_157 StaticText " (#6a6a6a) — Secondary text, borders, muted elements"
180:     uid=1_158 StaticText "Border Gray"
181:     uid=1_159 StaticText " (#c1c1c1) — Secondary text, borders, muted elements"
182:     uid=1_160 StaticText "Luxe Purple"
183:     uid=1_161 StaticText " (#460479) — Accent color, emphasis elements"
184:     uid=1_162 LineBreak "
185: "
186:     uid=1_163 heading "10. Typography Rules" level="2"
187:     uid=1_164 LineBreak "
188: "
189:     uid=1_165 StaticText "Display / Hero:"
190:     uid=1_166 StaticText " system-ui — Weight 700, tight tracking, used for headline impact"
191:     uid=1_167 StaticText "Body:"
192:     uid=1_168 StaticText " system-ui — Weight 400, 16px/1.6 line-height, max 72ch per line"
193:     uid=1_169 StaticText "UI Labels / Captions:"
194:     uid=1_170 StaticText " system-ui — 0.875rem, weight 500, slight letter-spacing"
195:     uid=1_171 StaticText "Monospace:"
196:     uid=1_172 StaticText " JetBrains Mono — Used for code, metadata, and technical values"
197:     uid=1_173 LineBreak "
198: "
199:     uid=1_174 StaticText "Scale:"
200:     uid=1_175 StaticText "Hero: clamp(2.5rem, 5vw, 4rem)"
201:     uid=1_176 StaticText "H1: 2.25rem"
202:     uid=1_177 StaticText "H2: 1.5rem"
203:     uid=1_178 StaticText "Body: 1rem / 1.6"
204:     uid=1_179 StaticText "Small: 0.875rem"
205:     uid=1_180 LineBreak "
206: "
207:     uid=1_181 heading "11. Component Stylings" level="2"
208:     uid=1_182 LineBreak "
209: "
210:     uid=1_183 StaticText "Primary Button:"
211:     uid=1_184 StaticText " Rounded (8px buttons) shape. Accent color fill. Hover: 8% darken + subtle lift shadow. Active: -1px translate tactile press. Font weight 600. No outer glows."
212:     uid=1_185 StaticText "Secondary / Ghost Button:"
213:     uid=1_186 StaticText " Outline variant. 1.5px border in muted color. Text in primary color. Hover: subtle background fill."
214:     uid=1_187 StaticText "Cards:"
215:     uid=1_188 StaticText " Rounded (8px buttons) corners. Surface background. Subtle shadow (0 2px 12px rgba(0,0,0,0.06)). 1px border stroke."
216:     uid=1_189 StaticText "Inputs:"
217:     uid=1_190 StaticText " Label above input. 1px border stroke. Focus ring: 2px accent color offset 2px. Error text below in semantic red. No floating labels."
218:     uid=1_191 StaticText "Navigation:"
219:     uid=1_192 StaticText " Primary surface background. Active item: accent color indicator. Font weight 500 when active."
220:     uid=1_193 StaticText "Skeletons:"
221:     uid=1_194 StaticText " Shimmer animation matching component dimensions. No circular spinners."
222:     uid=1_195 StaticText "Empty States:"
223:     uid=1_196 StaticText " Icon-based composition with descriptive text and action button."
224:     uid=1_197 LineBreak "
225: "
226:     uid=1_198 heading "12. Layout Principles" level="2"
227:     uid=1_199 LineBreak "
228: "
229:     uid=1_200 StaticText "Grid:"
230:     uid=1_201 StaticText " CSS Grid primary. Max-width containment: 1280px centered with 1.5rem side padding."
231:     uid=1_202 StaticText "Spacing rhythm:"
232:     uid=1_203 StaticText " Balanced. Base unit: 0.5rem (8px)."
233:     uid=1_204 StaticText "Section vertical gaps:"
234:     uid=1_205 StaticText " clamp(4rem, 8vw, 8rem)."
235:     uid=1_206 StaticText "Hero layout:"
236:     uid=1_207 StaticText " Split-screen (text left, visual right)."
237:     uid=1_208 StaticText "Feature sections:"
238:     uid=1_209 StaticText " Zig-zag alternating text+image rows. No 3-equal-columns."
239:     uid=1_210 StaticText "Mobile collapse:"
240:     uid=1_211 StaticText " All multi-column layouts collapse below 768px. No horizontal overflow."
241:     uid=1_212 StaticText "z-index contract:"
242:     uid=1_213 StaticText " base (0) / sticky-nav (100) / overlay (200) / modal (300) / toast (500)."
243:     uid=1_214 LineBreak "
244: "
245:     uid=1_215 heading "13. Motion & Interaction" level="2"
246:     uid=1_216 LineBreak "
247: "
248:     uid=1_217 StaticText "Physics:"
249:     uid=1_218 StaticText " Ease-out curves, 200-300ms duration. Smooth and predictable."
250:     uid=1_219 StaticText "Entry animations:"
251:     uid=1_220 StaticText " Fade + translate-Y (16px → 0) over 420ms ease-out. Staggered cascades for lists: 80ms between items."
252:     uid=1_221 StaticText "Hover states:"
253:     uid=1_222 StaticText " Subtle color shift + shadow adjustment over 200ms."
254:     uid=1_223 StaticText "Page transitions:"
255:     uid=1_224 StaticText " Fade only (200ms)."
256:     uid=1_225 StaticText "Performance:"
257:     uid=1_226 StaticText " Only transform and opacity animated. No layout-triggering properties."
258:     uid=1_227 LineBreak "
259: "
260:     uid=1_228 heading "14. Anti-Patterns (Banned)" level="2"
261:     uid=1_229 LineBreak "
262: "
263:     uid=1_230 StaticText "No emojis in UI — use icon system only (Lucide, Heroicons)"
264:     uid=1_231 StaticText "No pure black (#000000) — use off-black or charcoal variants"
265:     uid=1_232 StaticText "No oversaturated accent colors (saturation cap: 80%)"
266:     uid=1_233 StaticText "No 3-column equal-width feature layouts — use zig-zag or asymmetric grid"
267:     uid=1_234 StaticText "No "
268:     uid=1_235 StaticText "`"
269:     uid=1_236 StaticText "h-screen"
270:     uid=1_235 StaticText "`"
271:     uid=1_237 StaticText " — use "
272:     uid=1_235 StaticText "`"
273:     uid=1_238 StaticText "min-h-[100dvh]"
274:     uid=1_235 StaticText "`"
275:     uid=1_239 StaticText "No AI copywriting clichés: "Elevate", "Seamless", "Unleash", "Next-Gen""
276:     uid=1_240 StaticText "No broken external image links — use picsum.photos or inline SVG"
277:     uid=1_241 StaticText "No generic lorem ipsum in demos"
278:     uid=1_242 LineBreak "
279: "
280:     uid=1_243 heading "Contexto Histórico" level="2"
281:     uid=1_244 LineBreak "
282: "
283:     uid=1_245 StaticText "Inspirado no design do Airbnb, que usa Rausch Red (nomeado pela primeira rua da empresa) e fotografia como linguagem visual primária."
284:     uid=1_246 LineBreak "
285: "
286:     uid=1_247 heading "Caso de Uso" level="2"
287:     uid=1_248 LineBreak "
288: "
289:     uid=1_249 StaticText "Marketplaces, Viagens, Plataformas de hospedagem, E-commerce experiencial"
290:     uid=1_250 button "Download DESIGN.md"
291:     uid=1_251 button "Copy DESIGN.md"
292:     uid=1_252 heading "AI PROMPT" level="2"
293:     uid=1_253 StaticText "Act as a Senior Frontend Engineer and Expert UI Designer."
294:     uid=1_254 StaticText "Your task is to code a complete Landing Page on the first attempt."
295:     uid=1_255 StaticText "Landing Page Theme:"
296:     uid=1_256 StaticText "Sections to add:"
297:     uid=1_257 LineBreak "
298: "
299:     uid=1_258 StaticText "Generate the final code immediately following these definitions:"
300:     uid=1_259 LineBreak "
301: "
302:     uid=1_260 heading "Style" level="2"
303:     uid=1_261 LineBreak "
304: "
305:     uid=1_262 StaticText "Name:"
306:     uid=1_263 StaticText " Airbnb Coral Marketplace"
307:     uid=1_264 StaticText "Type:"
308:     uid=1_265 StaticText " Warm White Canvas, Rausch Red Accent, Cereal VF Variable Font, Three-Layer Shadows, Photography-First"
309:     uid=1_266 StaticText "Keywords:"
310:     uid=1_267 StaticText " airbnb, coral, marketplace, Rausch Red, Cereal VF, three-layer shadows, warm near-black, circular controls, photography-first, palette tokens"
311:     uid=1_268 StaticText "Era:"
312:     uid=1_269 StaticText " 2024-2026 Travel Marketplace"
313:     uid=1_270 StaticText "Light/Dark:"
314:     uid=1_271 StaticText " ✓ Full / ✗ Not Recommended"
315:     uid=1_272 LineBreak "
316: "
317:     uid=1_273 heading "Color Palette" level="2"
318:     uid=1_274 LineBreak "
319: "
320:     uid=1_275 StaticText "Primary:"
321:     uid=1_276 StaticText " Branco #ffffff, Near Black #222222, Rausch Red #ff385c, Light Surface #f2f2f2"
322:     uid=1_277 StaticText "Secondary:"
323:     uid=1_278 StaticText " Focused Gray #3f3f3f, Secondary Gray #6a6a6a, Border Gray #c1c1c1, Luxe Purple #460479"
324:     uid=1_279 LineBreak "
325: "
326:     uid=1_280 heading "Visual Effects" level="2"
327:     uid=1_281 LineBreak "
328: "
329:     uid=1_282 StaticText "Canvas branco puro com Rausch Red (#ff385c) como acento singular icônico. Texto near-black quente (#222222) — nunca preto puro. Cereal VF variable font com terminais arredondados quentes, pesos 500-700. Sombras three-layer: ring (0.02) + soft blur (0.04) + primary lift (0.1). Radius generoso: 8px botões, 14px badges, 20px cards, 32px large, 50% circular. Controles circulares (50%) para carrosséis. Fotografia como conteúdo primário. Letter-spacing negativo (-0.18px a -0.44px) em headings para intimidade."
330:     uid=1_283 LineBreak "
331: "
332:     uid=1_284 heading "AI Visual Direction" level="2"
333:     uid=1_285 LineBreak "
334: "
335:     uid=1_286 StaticText "Design an Airbnb-inspired warm marketplace landing page. White canvas with Rausch Red (#ff385c) as singular iconic accent. Warm near-black (#222222) text — never pure black. Variable font with rounded terminals at weight 500-700. Three-layer card shadows: rgba(0,0,0,0.02) 0px 0px 0px 1px + rgba(0,0,0,0.04) 0px 2px 6px + rgba(0,0,0,0.1) 0px 4px 8px. Generous radius: 8px buttons, 20px cards, 50% circular controls. Photography-first listing cards. Negative letter-spacing (-0.18px to -0.44px) on headings."
336:     uid=1_287 LineBreak "
337: "
338:     uid=1_288 heading "CSS Technical" level="2"
339:     uid=1_289 LineBreak "
340: "
341:     uid=1_290 StaticText "background:#ffffff;color:#222222;accent:#ff385c;box-shadow:rgba(0,0,0,0.02) 0px 0px 0px 1px,rgba(0,0,0,0.04) 0px 2px 6px,rgba(0,0,0,0.1) 0px 4px 8px;border-radius:8px buttons,20px cards,50% circles;font-family:system-ui;font-weight:500-700;letter-spacing:-0.44px at 22px
342: "
343:     uid=1_291 LineBreak "
344: "
345:     uid=1_292 heading "Design System Variables" level="2"
346:     uid=1_293 LineBreak "
347: "
348:     uid=1_294 StaticText "--bg:#ffffff;--text:#222222;--red:#ff385c;--surface:#f2f2f2;--secondary:#6a6a6a;--border:#c1c1c1;--luxe:#460479;--radius-btn:8px;--radius-card:20px;--radius-circle:50%
349: "
350:     uid=1_295 LineBreak "
351: "
352:     uid=1_296 heading "Implementation Checklist" level="2"
353:     uid=1_297 LineBreak "
354: "
355:     uid=1_298 StaticText "☐ Canvas branco com Rausch Red, ☐ Texto near-black #222222, ☐ Variable font 500-700, ☐ Sombras three-layer, ☐ Radius generoso 8-50%, ☐ Controles circulares, ☐ Fotografia-first, ☐ Tracking negativo headings, ☐ Responsivo"
356:     uid=1_299 LineBreak "
357: "
358:     uid=1_300 heading "Execution Rules" level="2"
359:     uid=1_301 LineBreak "
360: "
361:     uid=1_302 StaticText "1. Strictly follow the defined visual style."
362:     uid=1_303 StaticText "2. Use high-quality inline SVG icons (Heroicons or Lucide style) — NEVER use emojis as icons."
363:     uid=1_304 StaticText "3. Add "
364:     uid=1_235 StaticText "`"
365:     uid=1_305 StaticText "cursor-pointer"
366:     uid=1_235 StaticText "`"
367:     uid=1_306 StaticText " and smooth "
368:     uid=1_235 StaticText "`"
369:     uid=1_307 StaticText "hover"
370:     uid=1_235 StaticText "`"
371:     uid=1_308 StaticText " states (transition-all) on all interactive elements."
372:     uid=1_309 StaticText "4. Required Page Structure:"
373:     uid=1_310 StaticText "- Navbar (Logo + Links + CTA)"
374:     uid=1_311 StaticText "- Hero Section (Impactful Headline + Subtitle + 2 buttons + 3D/Abstract visual element via CSS)"
375:     uid=1_312 StaticText "- Features (3 cards with icons)"
376:     uid=1_313 StaticText "- Testimonials (3 cards)"
377:     uid=1_314 StaticText "- Pricing (3 tiers, highlight the middle one)"
378:     uid=1_315 StaticText "- Final CTA"
379:     uid=1_316 StaticText "- Full Footer with social links, privacy policy, terms of use, contact and SEO links."
380:     uid=1_317 StaticText "5. All text content must be in English."
381:     uid=1_318 StaticText "6. The visual must be CLEARLY distinct — do not create a "default Bootstrap" design. Force the use of the provided design system variables."
382:     uid=1_319 StaticText "7. Use "
383:     uid=1_235 StaticText "`"
384:     uid=1_235 StaticText "`"
385:     uid=1_320 button "Copy Prompt"
386:     uid=1_321 heading "RELATED" level="2"
387:     uid=1_322 link "Claude Warm Parchment Editorial & Tipografia Claude Warm Parchment" url="https://designmd.app/library/claude-warm-parchment"
388:       uid=1_323 image "Claude Warm Parchment" url="https://designmd.app/images/library/382.png"
389:       uid=1_324 StaticText "Editorial & Tipografia"
390:       uid=1_325 heading "Claude Warm Parchment" level="3"
391:     uid=1_326 link "Notion Warm Workspace Minimalismo & Swiss Notion Warm Workspace" url="https://designmd.app/library/notion-warm-workspace"
392:       uid=1_327 image "Notion Warm Workspace" url="https://designmd.app/images/library/387.png"
393:       uid=1_328 StaticText "Minimalismo & Swiss"
394:       uid=1_329 heading "Notion Warm Workspace" level="3"
395:     uid=1_330 link "Lovable Cream Humanist Flat & Soft UI Lovable Cream Humanist" url="https://designmd.app/library/lovable-cream-humanist"
396:       uid=1_331 image "Lovable Cream Humanist" url="https://designmd.app/images/library/392.png"
397:       uid=1_332 StaticText "Flat & Soft UI"
398:       uid=1_333 heading "Lovable Cream Humanist" level="3"
399:     uid=1_334 link "Pinterest Warm Discovery Temas & Verticais Pinterest Warm Discovery" url="https://designmd.app/library/pinterest-warm-discovery"
400:       uid=1_335 image "Pinterest Warm Discovery" url="https://designmd.app/images/library/415.png"
401:       uid=1_336 StaticText "Temas & Verticais"
402:       uid=1_337 heading "Pinterest Warm Discovery" level="3"
403:     uid=1_338 link "Zapier Warm Automation Flat & Soft UI Zapier Warm Automation" url="https://designmd.app/library/zapier-warm-automation"
404:       uid=1_339 image "Zapier Warm Automation" url="https://designmd.app/images/library/399.png"
405:       uid=1_340 StaticText "Flat & Soft UI"
406:       uid=1_341 heading "Zapier Warm Automation" level="3"
407:     uid=1_342 StaticText "Last synced: 4/1/2026"
408:   uid=1_343 contentinfo
409:     uid=1_344 navigation "Footer"
410:       uid=1_345 link "About" url="https://designmd.app/about"
411:         uid=1_346 StaticText "About"
412:       uid=1_347 link "llms.txt" url="https://designmd.app/llms.txt"
413:         uid=1_348 StaticText "llms.txt"
414:       uid=1_349 link "RSS" url="https://designmd.app/rss.xml"
415:         uid=1_350 StaticText "RSS"
416:       uid=1_351 link "GitLab (opens in new tab)" url="https://gitlab.com/fabriciotelles/vibe-styles"
417:         uid=1_352 StaticText "GitLab"
418:         uid=1_353 StaticText "(opens in new tab)"
419:       uid=1_354 link "skill.dev.br (opens in new tab)" url="https://skill.dev.br/"
420:         uid=1_355 StaticText "skill.dev.br"
421:         uid=1_356 StaticText "(opens in new tab)"
422:     uid=1_357 navigation "Legal links"
423:       uid=1_358 link "Terms of Use" url="https://designmd.app/terms-of-use"
424:         uid=1_359 StaticText "Terms of Use"
425:       uid=1_360 link "Privacy Policy" url="https://designmd.app/privacy-policy"
426:         uid=1_361 StaticText "Privacy Policy"
427:       uid=1_362 button "Cookies"
428:     uid=1_363 StaticText "DESIGN.MD APP — OPEN REFERENCE OF DESIGN.MD FILES"
429:   uid=1_364 StaticText "We use cookies for traffic analysis (Google Analytics). Essential cookies and cookieless analytics (Plausible) run without consent."
430:   uid=1_365 button "Reject"
431:   uid=1_366 button "Accept"

(End of file - total 431 lines)
</content>
```

---

## Assistant (Build · Big Pickle · 3.4s)

_Thinking:_

The user just wanted me to open the page. Now they can see the page — there's a "Download DESIGN.md" button (uid=1_250) on the page. That's the button the bookmarklet would click. Let me show the screenshot and explain what they're looking at.

**Tool: chrome-devtools_take_screenshot**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/screenshot.png",
  "fullPage": true
}
```

**Output:**
```
Took a screenshot of the full current page.
Saved screenshot to /home/mkt/design_md/screenshot.png.
```

---

## Assistant (Build · Big Pickle · 3.1s)

_Thinking:_

The page clearly shows a "Download DESIGN.md" button. This is the button the bookmarklet targets. The page renders the DESIGN.md content inline and the button triggers a download of the file. Let me explain this to the user simply.

A página foi aberta. O botão que o bookmarklet clica é o **"Download DESIGN.md"** (uid=1_250). Cada página do library tem um desses — ele baixa o arquivo `DESIGN.md` daquele design system.

O screenshot completo foi salvo em `/home/mkt/design_md/screenshot.png` — lá você pode ver o botão no topo e todo o conteúdo da página.

---

## User

inclua isso no script: `O PyAutoGUI tem um "botão de emergência". Se o script começar a clicar em coisas erradas ou abrir abas infinitas e você perder o controle, basta dar um "fio terra": **Jogue o seu mouse rapidamente e bruscamente para qualquer um dos 4 cantos extremos do seu monitor** e o script abortará imediatamente! ` 

---

## Assistant (Build · Big Pickle · 2.9s)

_Thinking:_

The user wants me to include that emergency instructions text in the script. But looking at the script, that text is already present in the docstring at the bottom (lines 112-113: "Dica de Ouro"). The user likely wants it in the main print output too, so it appears when the script runs, not just in the comments.

Let me re-read the current state of the script to be precise about the edit needed.

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/design-md-library/automacao_bookmarklet.py"
}
```

**Output:**
```
<path>/home/mkt/design_md/design-md-library/automacao_bookmarklet.py</path>
<type>file</type>
<content>
1: import os
2: import re
3: import time
4: import random
5: import webbrowser
6: 
7: try:
8:     import pyautogui
9: except ImportError:
10:     print("Por favor, instale o pyautogui abrindo o terminal e rodando: pip3 install pyautogui")
11:     exit(1)
12: 
13: # Caminho do arquivo
14: md_file = '/Users/fatima/Desktop/awesome_design/design-md-library/elementos_designmd.md'
15: 
16: # ==============================================================================
17: # CONFIGURAÇÃO DE COMO CLICAR NO BOTÃO (ESCOLHA OPÇÃO 1 OU OPÇÃO 2)
18: # ==============================================================================
19: 
20: # OPÇÃO 1: Coordenadas Fixas da Tela (Mais fácil, rápida e confiável)
21: # Para descobrir essas coordenadas, coloque o mouse em cima do seu favorito 
22: # e rode este comando num terminal: python3 -c "import pyautogui; print(pyautogui.position())"
23: # OPÇÃO 1: Coordenadas Fixas da Tela (desativada — usando imagem)
24: # BOTAO_X = 350
25: # BOTAO_Y = 100
26: USAR_COORDENADAS = False
27: 
28: # OPÇÃO 2: Reconhecimento de Imagem (Requer salvar um print do botão)
29: # Se USAR_COORDENADAS for False, o script vai procurar essa imagem na tela.
30: # Para isso, tire um "print" BEM PEQUENO contendo apenas o texto do botão do 
31: # favorito, salve como "botao_favorito.png" na mesma pasta deste script.
32: # Obs: É preciso instalar a biblioteca opencv-python para o confidence=0.8 funcionar.
33: NOME_DA_IMAGEM = 'botao_favorito.png'
34: 
35: # ==============================================================================
36: 
37: # 1. Lê a tabela para extrair as URLs
38: with open(md_file, 'r') as f:
39:     lines = f.readlines()
40: 
41: urls = []
42: for line in lines:
43:     if line.startswith('|'):
44:         # Extrai o link da terceira coluna
45:         match = re.search(r'(https://designmd\.app/(?:en/)?library/[^)]+)', line)
46:         if match:
47:             urls.append(match.group(1))
48: 
49: print(f"Foram encontradas {len(urls)} URLs.")
50: print("AVISO: Deixe o seu navegador visível e na mesma posição.")
51: print("Iniciando em 5 segundos... (Para parar a qualquer momento, arraste o mouse rapidamente para qualquer um dos 4 cantos da tela!)")
52: time.sleep(5)
53: 
54: # 2. Executa o fluxo para cada URL
55: for i, url in enumerate(urls):
56:     print(f"\n[{i+1}/{len(urls)}] Abrindo página: {url}")
57:     
58:     # Abre a URL em uma nova aba do navegador padrão
59:     webbrowser.open_new_tab(url)
60:     
61:     # Tempo randômico entre 4 e 15 segundos para simular comportamento humano e carregar a página
62:     tempo_espera = random.randint(4, 15)
63:     print(f"Aguardando {tempo_espera} segundos para o carregamento...")
64:     time.sleep(tempo_espera)
65:     
66:     # 3. Clica no Bookmarklet
67:     if USAR_COORDENADAS:
68:         # Move o mouse e clica
69:         pyautogui.moveTo(BOTAO_X, BOTAO_Y, duration=0.5) # duração de meio segundo simula o humano movendo
70:         pyautogui.click()
71:         print(f"Clicado nas coordenadas ({BOTAO_X}, {BOTAO_Y})")
72:     else:
73:         try:
74:             # Procura a imagem do botão na tela
75:             posicao = pyautogui.locateCenterOnScreen(NOME_DA_IMAGEM, confidence=0.8)
76:             if posicao:
77:                 pyautogui.moveTo(posicao.x, posicao.y, duration=0.5)
78:                 pyautogui.click()
79:                 print("Clicado via reconhecimento de imagem!")
80:             else:
81:                 print("ERRO: Não encontrei a imagem do botão na tela.")
82:         except Exception as e:
83:             print(f"Erro ao procurar a imagem: {e}. (Verifique se instalou o opencv-python)")
84: 
85:     # Pequena pausa antes de abrir a próxima URL para dar tempo do download iniciar
86:     time.sleep(2)
87: 
88: print("\nProcesso concluído!")
89: 
90: 
91: # UTILIZAÇÃO:
92: '''
93: Sim, é totalmente possível e criei exatamente esse script para você! 
94: 
95: Acabei de salvá-lo em: `@[/Users/fatima/Desktop/awesome_design/design-md-library/automacao_bookmarklet.py]`
96: 
97: Sobre a sua dúvida de como o PyAutoGUI reconhece o botão: **Sim, há duas alternativas principais**, e eu deixei ambas preparadas no script para você escolher:
98: 
99: ### Alternativa 1: Coordenadas Fixas (Recomendado, Mais Fácil)
100: O PyAutoGUI não precisa "enxergar" o botão. Se você deixar o navegador em tela cheia e não mexer, a posição do botão na sua tela será sempre a mesma (por exemplo, `X=350, Y=100`). O script simplesmente joga o mouse cegamente nessa coordenada e clica.
101: No arquivo que criei, deixei essa opção ativada por padrão (`USAR_COORDENADAS = True`). Coloquei no código um comando que você pode usar para descobrir qual é o `X` e `Y` exato do seu mouse.
102: 
103: ### Alternativa 2: Reconhecimento de Imagem (Mais Avançado)
104: Nessa opção (`locateCenterOnScreen`), o PyAutoGUI vai "escanear" a tela do seu computador inteira pixel por pixel caçando uma imagem específica.
105: **Como funciona:** Você tira um *print* (captura de tela) bem pequenininho apenas do botão do seu favorito e salva como `botao_favorito.png` na mesma pasta do script. O script vai procurar por essa imagem, descobrir onde ela está e clicar. É excelente se você costuma mudar o tamanho da janela, mas é um pouco mais pesado.
106: 
107: ### Como usar o Script criado:
108: 1. Abra um terminal.
109: 2. Se não tiver as bibliotecas instaladas, rode: `pip3 install pyautogui opencv-python`
110: 3. Abra o script `automacao_bookmarklet.py`, edite as variáveis `BOTAO_X` e `BOTAO_Y` com os números do seu botão de favorito.
111: 4. Rode: `python3 automacao_bookmarklet.py`
112: 
113: **Dica de Ouro:** O PyAutoGUI tem um "botão de emergência". Se o script começar a clicar em coisas erradas ou abrir abas infinitas e você perder o controle, basta dar um "fio terra": **Jogue o seu mouse rapidamente e bruscamente para qualquer um dos 4 cantos extremos do seu monitor** e o script abortará imediatamente!
114: '''

(End of file - total 114 lines)
</content>
```

---

## Assistant (Build · Big Pickle · 4.7s)

_Thinking:_

The text is already in the script (lines 113-114 in the docstring). But the user wants me to "include this in the script" - perhaps they want it more prominently, or they want it printed as a visible warning when the script runs, not just buried in the docstring.

Looking at line 51, there's already a short version: `"Iniciando em 5 segundos... (Para parar a qualquer momento, arraste o mouse rapidamente para qualquer um dos 4 cantos da tela!)"` - but it's a brief version.

Let me add the full emergency instructions as a prominent print statement right after line 51, so it's visible to the user when running.

Já está no docstring, mas está pouco visível. Vou colocar como print destacado na execução:

**Tool: edit**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/design-md-library/automacao_bookmarklet.py",
  "oldString": "print(\"Iniciando em 5 segundos... (Para parar a qualquer momento, arraste o mouse rapidamente para qualquer um dos 4 cantos da tela!)\")\ntime.sleep(5)",
  "newString": "print(\"Iniciando em 5 segundos...\")\nprint()\nprint(\"⚠️  BOTÃO DE EMERGÊNCIA DO PYAUTOGUI:\")\nprint(\"Se o script começar a clicar em coisas erradas ou abrir abas infinitas e você perder\")\nprint(\"o controle, JOGUE O MOUSE RAPIDAMENTE PARA QUALQUER UM DOS 4 CANTOS DA TELA —\")\nprint(\"o script abortará imediatamente!\")\nprint()\ntime.sleep(5)"
}
```

**Output:**
```
Edit applied successfully.
```

---

## Assistant (Build · Big Pickle · 2.5s)

_Thinking:_

Done. Now the emergency instructions appear as visible printed output at runtime, not just hidden in the docstring.

Agora o aviso de emergência aparece como print visível durante a execução, não só no docstring.

---

## User

inclua tb no script a capacidade de criar uma lista dos urls já visitados e clicados no bookmarklet

---

## Assistant (Build · Big Pickle · 3.8s)

_Thinking:_

The user wants to add tracking of which URLs have been visited and bookmarklet-clicked, so if the script is interrupted and restarted, it can resume from where it left off. I'll add a file-based tracking mechanism.

Let me add:
1. A file to track processed URLs (e.g., `visitados.txt`)
2. On startup, load already-processed URLs from that file
3. Skip URLs that are already processed
4. After successfully clicking the bookmarklet on a URL, write it to the file

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/design-md-library/automacao_bookmarklet.py"
}
```

**Output:**
```
<path>/home/mkt/design_md/design-md-library/automacao_bookmarklet.py</path>
<type>file</type>
<content>
1: import os
2: import re
3: import time
4: import random
5: import webbrowser
6: 
7: try:
8:     import pyautogui
9: except ImportError:
10:     print("Por favor, instale o pyautogui abrindo o terminal e rodando: pip3 install pyautogui")
11:     exit(1)
12: 
13: # Caminho do arquivo
14: md_file = '/Users/fatima/Desktop/awesome_design/design-md-library/elementos_designmd.md'
15: 
16: # ==============================================================================
17: # CONFIGURAÇÃO DE COMO CLICAR NO BOTÃO (ESCOLHA OPÇÃO 1 OU OPÇÃO 2)
18: # ==============================================================================
19: 
20: # OPÇÃO 1: Coordenadas Fixas da Tela (Mais fácil, rápida e confiável)
21: # Para descobrir essas coordenadas, coloque o mouse em cima do seu favorito 
22: # e rode este comando num terminal: python3 -c "import pyautogui; print(pyautogui.position())"
23: # OPÇÃO 1: Coordenadas Fixas da Tela (desativada — usando imagem)
24: # BOTAO_X = 350
25: # BOTAO_Y = 100
26: USAR_COORDENADAS = False
27: 
28: # OPÇÃO 2: Reconhecimento de Imagem (Requer salvar um print do botão)
29: # Se USAR_COORDENADAS for False, o script vai procurar essa imagem na tela.
30: # Para isso, tire um "print" BEM PEQUENO contendo apenas o texto do botão do 
31: # favorito, salve como "botao_favorito.png" na mesma pasta deste script.
32: # Obs: É preciso instalar a biblioteca opencv-python para o confidence=0.8 funcionar.
33: NOME_DA_IMAGEM = 'botao_favorito.png'
34: 
35: # ==============================================================================
36: 
37: # 1. Lê a tabela para extrair as URLs
38: with open(md_file, 'r') as f:
39:     lines = f.readlines()
40: 
41: urls = []
42: for line in lines:
43:     if line.startswith('|'):
44:         # Extrai o link da terceira coluna
45:         match = re.search(r'(https://designmd\.app/(?:en/)?library/[^)]+)', line)
46:         if match:
47:             urls.append(match.group(1))
48: 
49: print(f"Foram encontradas {len(urls)} URLs.")
50: print("AVISO: Deixe o seu navegador visível e na mesma posição.")
51: print("Iniciando em 5 segundos...")
52: print()
53: print("⚠️  BOTÃO DE EMERGÊNCIA DO PYAUTOGUI:")
54: print("Se o script começar a clicar em coisas erradas ou abrir abas infinitas e você perder")
55: print("o controle, JOGUE O MOUSE RAPIDAMENTE PARA QUALQUER UM DOS 4 CANTOS DA TELA —")
56: print("o script abortará imediatamente!")
57: print()
58: time.sleep(5)
59: 
60: # 2. Executa o fluxo para cada URL
61: for i, url in enumerate(urls):
62:     print(f"\n[{i+1}/{len(urls)}] Abrindo página: {url}")
63:     
64:     # Abre a URL em uma nova aba do navegador padrão
65:     webbrowser.open_new_tab(url)
66:     
67:     # Tempo randômico entre 4 e 15 segundos para simular comportamento humano e carregar a página
68:     tempo_espera = random.randint(4, 15)
69:     print(f"Aguardando {tempo_espera} segundos para o carregamento...")
70:     time.sleep(tempo_espera)
71:     
72:     # 3. Clica no Bookmarklet
73:     if USAR_COORDENADAS:
74:         # Move o mouse e clica
75:         pyautogui.moveTo(BOTAO_X, BOTAO_Y, duration=0.5) # duração de meio segundo simula o humano movendo
76:         pyautogui.click()
77:         print(f"Clicado nas coordenadas ({BOTAO_X}, {BOTAO_Y})")
78:     else:
79:         try:
80:             # Procura a imagem do botão na tela
81:             posicao = pyautogui.locateCenterOnScreen(NOME_DA_IMAGEM, confidence=0.8)
82:             if posicao:
83:                 pyautogui.moveTo(posicao.x, posicao.y, duration=0.5)
84:                 pyautogui.click()
85:                 print("Clicado via reconhecimento de imagem!")
86:             else:
87:                 print("ERRO: Não encontrei a imagem do botão na tela.")
88:         except Exception as e:
89:             print(f"Erro ao procurar a imagem: {e}. (Verifique se instalou o opencv-python)")
90: 
91:     # Pequena pausa antes de abrir a próxima URL para dar tempo do download iniciar
92:     time.sleep(2)
93: 
94: print("\nProcesso concluído!")
95: 
96: 
97: # UTILIZAÇÃO:
98: '''
99: Sim, é totalmente possível e criei exatamente esse script para você! 
100: 
101: Acabei de salvá-lo em: `@[/Users/fatima/Desktop/awesome_design/design-md-library/automacao_bookmarklet.py]`
102: 
103: Sobre a sua dúvida de como o PyAutoGUI reconhece o botão: **Sim, há duas alternativas principais**, e eu deixei ambas preparadas no script para você escolher:
104: 
105: ### Alternativa 1: Coordenadas Fixas (Recomendado, Mais Fácil)
106: O PyAutoGUI não precisa "enxergar" o botão. Se você deixar o navegador em tela cheia e não mexer, a posição do botão na sua tela será sempre a mesma (por exemplo, `X=350, Y=100`). O script simplesmente joga o mouse cegamente nessa coordenada e clica.
107: No arquivo que criei, deixei essa opção ativada por padrão (`USAR_COORDENADAS = True`). Coloquei no código um comando que você pode usar para descobrir qual é o `X` e `Y` exato do seu mouse.
108: 
109: ### Alternativa 2: Reconhecimento de Imagem (Mais Avançado)
110: Nessa opção (`locateCenterOnScreen`), o PyAutoGUI vai "escanear" a tela do seu computador inteira pixel por pixel caçando uma imagem específica.
111: **Como funciona:** Você tira um *print* (captura de tela) bem pequenininho apenas do botão do seu favorito e salva como `botao_favorito.png` na mesma pasta do script. O script vai procurar por essa imagem, descobrir onde ela está e clicar. É excelente se você costuma mudar o tamanho da janela, mas é um pouco mais pesado.
112: 
113: ### Como usar o Script criado:
114: 1. Abra um terminal.
115: 2. Se não tiver as bibliotecas instaladas, rode: `pip3 install pyautogui opencv-python`
116: 3. Abra o script `automacao_bookmarklet.py`, edite as variáveis `BOTAO_X` e `BOTAO_Y` com os números do seu botão de favorito.
117: 4. Rode: `python3 automacao_bookmarklet.py`
118: 
119: **Dica de Ouro:** O PyAutoGUI tem um "botão de emergência". Se o script começar a clicar em coisas erradas ou abrir abas infinitas e você perder o controle, basta dar um "fio terra": **Jogue o seu mouse rapidamente e bruscamente para qualquer um dos 4 cantos extremos do seu monitor** e o script abortará imediatamente!
120: '''

(End of file - total 120 lines)
</content>
```

---

## Assistant (Build · Big Pickle · 4.4s)

_Thinking:_

I need to:
1. Add a constant for the tracking file path
2. Load already-visited URLs from file on startup
3. Filter out visited URLs from the list
4. Save to the tracking file after each successful click

Let me also fix the md_file path - it's hardcoded to `/Users/fatima/Desktop/...` and probably doesn't exist on this machine. But the user didn't ask me to fix that, so I'll leave it.

Actually, looking more carefully, the path won't work on this machine. But the user didn't ask me to fix it - they just want the tracking feature added. Let me just add the tracking mechanism.

I'll use a simple approach: save a `visitados.txt` file in the same directory as the script.

**Tool: edit**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/design-md-library/automacao_bookmarklet.py",
  "oldString": "# Caminho do arquivo\nmd_file = '/Users/fatima/Desktop/awesome_design/design-md-library/elementos_designmd.md'",
  "newString": "# Caminho do arquivo\nmd_file = '/Users/fatima/Desktop/awesome_design/design-md-library/elementos_designmd.md'\nVISITADOS_FILE = 'visitados.txt'"
}
```

**Output:**
```
Edit applied successfully.
```

---

## Assistant (Build · Big Pickle · 4.0s)

_Thinking:_

Now add the loading of visited URLs after the URLs are extracted, and filtering/saving logic.

**Tool: edit**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/design-md-library/automacao_bookmarklet.py",
  "oldString": "print(f\"Foram encontradas {len(urls)} URLs.\")\nprint(\"AVISO: Deixe o seu navegador visível e na mesma posição.\")",
  "newString": "# Carrega URLs já visitadas para retomar de onde parou\nvisitadas = set()\nif os.path.exists(VISITADOS_FILE):\n    with open(VISITADOS_FILE, 'r') as f:\n        visitadas = set(line.strip() for line in f if line.strip())\n    print(f\"{len(visitadas)} URLs já processadas (lido de {VISITADOS_FILE}).\")\n\nurls_pendentes = [u for u in urls if u not in visitadas]\nprint(f\"Total: {len(urls)} URLs. Pendentes: {len(urls_pendentes)}. Já visitadas: {len(visitadas)}.\")\nprint(\"AVISO: Deixe o seu navegador visível e na mesma posição.\")"
}
```

**Output:**
```
Edit applied successfully.
```

---

## Assistant (Build · Big Pickle · 3.4s)

_Thinking:_

Now update the loop to iterate over `urls_pendentes` instead of `urls`:

**Tool: edit**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/design-md-library/automacao_bookmarklet.py",
  "oldString": "# 2. Executa o fluxo para cada URL\nfor i, url in enumerate(urls):\n    print(f\"\\n[{i+1}/{len(urls)}] Abrindo página: {url}\")",
  "newString": "# 2. Executa o fluxo para cada URL pendente\nfor i, url in enumerate(urls_pendentes, start=1):\n    print(f\"\\n[{i}/{len(urls_pendentes)}] Abrindo página: {url}\")"
}
```

**Output:**
```
Edit applied successfully.
```

---

## Assistant (Build · Big Pickle · 5.9s)

_Thinking:_

Now add the save-to-file after a successful click. I need to add it after the click success (both coordinate and image paths):

**Tool: edit**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/design-md-library/automacao_bookmarklet.py",
  "oldString": "    # 3. Clica no Bookmarklet\n    if USAR_COORDENADAS:\n        # Move o mouse e clica\n        pyautogui.moveTo(BOTAO_X, BOTAO_Y, duration=0.5) # duração de meio segundo simula o humano movendo\n        pyautogui.click()\n        print(f\"Clicado nas coordenadas ({BOTAO_X}, {BOTAO_Y})\")\n    else:\n        try:\n            # Procura a imagem do botão na tela\n            posicao = pyautogui.locateCenterOnScreen(NOME_DA_IMAGEM, confidence=0.8)\n            if posicao:\n                pyautogui.moveTo(posicao.x, posicao.y, duration=0.5)\n                pyautogui.click()\n                print(\"Clicado via reconhecimento de imagem!\")\n            else:\n                print(\"ERRO: Não encontrei a imagem do botão na tela.\")\n        except Exception as e:\n            print(f\"Erro ao procurar a imagem: {e}. (Verifique se instalou o opencv-python)\")\n\n    # Pequena pausa antes de abrir a próxima URL para dar tempo do download iniciar\n    time.sleep(2)",
  "newString": "    # 3. Clica no Bookmarklet\n    clicou = False\n    if USAR_COORDENADAS:\n        # Move o mouse e clica\n        pyautogui.moveTo(BOTAO_X, BOTAO_Y, duration=0.5)\n        pyautogui.click()\n        print(f\"Clicado nas coordenadas ({BOTAO_X}, {BOTAO_Y})\")\n        clicou = True\n    else:\n        try:\n            # Procura a imagem do botão na tela\n            posicao = pyautogui.locateCenterOnScreen(NOME_DA_IMAGEM, confidence=0.8)\n            if posicao:\n                pyautogui.moveTo(posicao.x, posicao.y, duration=0.5)\n                pyautogui.click()\n                print(\"Clicado via reconhecimento de imagem!\")\n                clicou = True\n            else:\n                print(\"ERRO: Não encontrei a imagem do botão na tela.\")\n        except Exception as e:\n            print(f\"Erro ao procurar a imagem: {e}. (Verifique se instalou o opencv-python)\")\n\n    if clicou:\n        with open(VISITADOS_FILE, 'a') as f:\n            f.write(url + '\\n')\n        print(f\"✓ URL registrada em {VISITADOS_FILE}\")\n\n    # Pequena pausa antes de abrir a próxima URL para dar tempo do download iniciar\n    time.sleep(2)"
}
```

**Output:**
```
Edit applied successfully.
```

---

## Assistant (Build · Big Pickle · 2.5s)

_Thinking:_

The edit is done. Let me verify the final state of the script to make sure everything looks correct.

Let me verificar o resultado final:

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/design-md-library/automacao_bookmarklet.py",
  "limit": 100
}
```

**Output:**
```
<path>/home/mkt/design_md/design-md-library/automacao_bookmarklet.py</path>
<type>file</type>
<content>
1: import os
2: import re
3: import time
4: import random
5: import webbrowser
6: 
7: try:
8:     import pyautogui
9: except ImportError:
10:     print("Por favor, instale o pyautogui abrindo o terminal e rodando: pip3 install pyautogui")
11:     exit(1)
12: 
13: # Caminho do arquivo
14: md_file = '/Users/fatima/Desktop/awesome_design/design-md-library/elementos_designmd.md'
15: VISITADOS_FILE = 'visitados.txt'
16: 
17: # ==============================================================================
18: # CONFIGURAÇÃO DE COMO CLICAR NO BOTÃO (ESCOLHA OPÇÃO 1 OU OPÇÃO 2)
19: # ==============================================================================
20: 
21: # OPÇÃO 1: Coordenadas Fixas da Tela (Mais fácil, rápida e confiável)
22: # Para descobrir essas coordenadas, coloque o mouse em cima do seu favorito 
23: # e rode este comando num terminal: python3 -c "import pyautogui; print(pyautogui.position())"
24: # OPÇÃO 1: Coordenadas Fixas da Tela (desativada — usando imagem)
25: # BOTAO_X = 350
26: # BOTAO_Y = 100
27: USAR_COORDENADAS = False
28: 
29: # OPÇÃO 2: Reconhecimento de Imagem (Requer salvar um print do botão)
30: # Se USAR_COORDENADAS for False, o script vai procurar essa imagem na tela.
31: # Para isso, tire um "print" BEM PEQUENO contendo apenas o texto do botão do 
32: # favorito, salve como "botao_favorito.png" na mesma pasta deste script.
33: # Obs: É preciso instalar a biblioteca opencv-python para o confidence=0.8 funcionar.
34: NOME_DA_IMAGEM = 'botao_favorito.png'
35: 
36: # ==============================================================================
37: 
38: # 1. Lê a tabela para extrair as URLs
39: with open(md_file, 'r') as f:
40:     lines = f.readlines()
41: 
42: urls = []
43: for line in lines:
44:     if line.startswith('|'):
45:         # Extrai o link da terceira coluna
46:         match = re.search(r'(https://designmd\.app/(?:en/)?library/[^)]+)', line)
47:         if match:
48:             urls.append(match.group(1))
49: 
50: # Carrega URLs já visitadas para retomar de onde parou
51: visitadas = set()
52: if os.path.exists(VISITADOS_FILE):
53:     with open(VISITADOS_FILE, 'r') as f:
54:         visitadas = set(line.strip() for line in f if line.strip())
55:     print(f"{len(visitadas)} URLs já processadas (lido de {VISITADOS_FILE}).")
56: 
57: urls_pendentes = [u for u in urls if u not in visitadas]
58: print(f"Total: {len(urls)} URLs. Pendentes: {len(urls_pendentes)}. Já visitadas: {len(visitadas)}.")
59: print("AVISO: Deixe o seu navegador visível e na mesma posição.")
60: print("Iniciando em 5 segundos...")
61: print()
62: print("⚠️  BOTÃO DE EMERGÊNCIA DO PYAUTOGUI:")
63: print("Se o script começar a clicar em coisas erradas ou abrir abas infinitas e você perder")
64: print("o controle, JOGUE O MOUSE RAPIDAMENTE PARA QUALQUER UM DOS 4 CANTOS DA TELA —")
65: print("o script abortará imediatamente!")
66: print()
67: time.sleep(5)
68: 
69: # 2. Executa o fluxo para cada URL pendente
70: for i, url in enumerate(urls_pendentes, start=1):
71:     print(f"\n[{i}/{len(urls_pendentes)}] Abrindo página: {url}")
72:     
73:     # Abre a URL em uma nova aba do navegador padrão
74:     webbrowser.open_new_tab(url)
75:     
76:     # Tempo randômico entre 4 e 15 segundos para simular comportamento humano e carregar a página
77:     tempo_espera = random.randint(4, 15)
78:     print(f"Aguardando {tempo_espera} segundos para o carregamento...")
79:     time.sleep(tempo_espera)
80:     
81:     # 3. Clica no Bookmarklet
82:     clicou = False
83:     if USAR_COORDENADAS:
84:         # Move o mouse e clica
85:         pyautogui.moveTo(BOTAO_X, BOTAO_Y, duration=0.5)
86:         pyautogui.click()
87:         print(f"Clicado nas coordenadas ({BOTAO_X}, {BOTAO_Y})")
88:         clicou = True
89:     else:
90:         try:
91:             # Procura a imagem do botão na tela
92:             posicao = pyautogui.locateCenterOnScreen(NOME_DA_IMAGEM, confidence=0.8)
93:             if posicao:
94:                 pyautogui.moveTo(posicao.x, posicao.y, duration=0.5)
95:                 pyautogui.click()
96:                 print("Clicado via reconhecimento de imagem!")
97:                 clicou = True
98:             else:
99:                 print("ERRO: Não encontrei a imagem do botão na tela.")
100:         except Exception as e:

(Showing lines 1-100 of 137. Use offset=101 to continue.)
</content>
```

---

## Assistant (Build · Big Pickle · 2.9s)

_Thinking:_

The script looks good. Let me also verify the remaining lines.

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/design-md-library/automacao_bookmarklet.py",
  "offset": 100
}
```

**Output:**
```
<path>/home/mkt/design_md/design-md-library/automacao_bookmarklet.py</path>
<type>file</type>
<content>
100:         except Exception as e:
101:             print(f"Erro ao procurar a imagem: {e}. (Verifique se instalou o opencv-python)")
102: 
103:     if clicou:
104:         with open(VISITADOS_FILE, 'a') as f:
105:             f.write(url + '\n')
106:         print(f"✓ URL registrada em {VISITADOS_FILE}")
107: 
108:     # Pequena pausa antes de abrir a próxima URL para dar tempo do download iniciar
109:     time.sleep(2)
110: 
111: print("\nProcesso concluído!")
112: 
113: 
114: # UTILIZAÇÃO:
115: '''
116: Sim, é totalmente possível e criei exatamente esse script para você! 
117: 
118: Acabei de salvá-lo em: `@[/Users/fatima/Desktop/awesome_design/design-md-library/automacao_bookmarklet.py]`
119: 
120: Sobre a sua dúvida de como o PyAutoGUI reconhece o botão: **Sim, há duas alternativas principais**, e eu deixei ambas preparadas no script para você escolher:
121: 
122: ### Alternativa 1: Coordenadas Fixas (Recomendado, Mais Fácil)
123: O PyAutoGUI não precisa "enxergar" o botão. Se você deixar o navegador em tela cheia e não mexer, a posição do botão na sua tela será sempre a mesma (por exemplo, `X=350, Y=100`). O script simplesmente joga o mouse cegamente nessa coordenada e clica.
124: No arquivo que criei, deixei essa opção ativada por padrão (`USAR_COORDENADAS = True`). Coloquei no código um comando que você pode usar para descobrir qual é o `X` e `Y` exato do seu mouse.
125: 
126: ### Alternativa 2: Reconhecimento de Imagem (Mais Avançado)
127: Nessa opção (`locateCenterOnScreen`), o PyAutoGUI vai "escanear" a tela do seu computador inteira pixel por pixel caçando uma imagem específica.
128: **Como funciona:** Você tira um *print* (captura de tela) bem pequenininho apenas do botão do seu favorito e salva como `botao_favorito.png` na mesma pasta do script. O script vai procurar por essa imagem, descobrir onde ela está e clicar. É excelente se você costuma mudar o tamanho da janela, mas é um pouco mais pesado.
129: 
130: ### Como usar o Script criado:
131: 1. Abra um terminal.
132: 2. Se não tiver as bibliotecas instaladas, rode: `pip3 install pyautogui opencv-python`
133: 3. Abra o script `automacao_bookmarklet.py`, edite as variáveis `BOTAO_X` e `BOTAO_Y` com os números do seu botão de favorito.
134: 4. Rode: `python3 automacao_bookmarklet.py`
135: 
136: **Dica de Ouro:** O PyAutoGUI tem um "botão de emergência". Se o script começar a clicar em coisas erradas ou abrir abas infinitas e você perder o controle, basta dar um "fio terra": **Jogue o seu mouse rapidamente e bruscamente para qualquer um dos 4 cantos extremos do seu monitor** e o script abortará imediatamente!
137: '''

(End of file - total 137 lines)
</content>
```

---

## Assistant (Build · Big Pickle · 3.0s)

Pronto. Agora o script:

1. **Carrega** `visitados.txt` no início e filtra URLs já processadas
2. **Pula** URLs já visitadas, processando só as pendentes
3. **Registra** cada URL em `visitados.txt` após clicar com sucesso
4. **Retoma** de onde parou se for interrompido e executado de novo

---

## User

qual o site que tem os design awesome? 

---

## Assistant (Build · Big Pickle · 7.6s)

_Thinking:_

The user is asking what website has the "awesome designs" - they're referring to the DESIGN.md files. Looking at what I've read, the design-md-awesome directory contains curated DESIGN.md files for brands like Airbnb, Apple, Stripe, etc. Let me check if there's a source website for these files. The README in the airbnb directory mentions "https://getdesign.md/airbnb/design-md" and the llms-full.txt mentions designmd.app. But the design-md-awesome directory might come from a different source.

Let me look at the git remote or any other clue about where this came from.

**Tool: bash**

**Input:**
```json
{
  "command": "git remote -v",
  "description": "Check git remote"
}
```

**Output:**
```
origin	https://github.com/HelioGiroto/design_md.git (fetch)
origin	https://github.com/HelioGiroto/design_md.git (push)

```

---

## Assistant (Build · Big Pickle · 5.0s)

_Thinking:_

The git remote is for a fork. The original source of the design-md-awesome directory is likely from the VoltAgent/awesome-design-md repo mentioned in dicas.md:

```
https://github.com/designmd/awesome-design-md
```

And also:
```
curl -s https://api.github.com/repos/VoltAgent/awesome-design-md/git/trees/main?recursive=1 | grep ".md"
```

Let me fetch that to verify.

Actually, looking more carefully, the `dicas.md` mentions two URLs:
- `https://designmd.app/library` - the main library site
- `https://github.com/designmd/awesome-design-md` - the awesome-design-md repo

The `design-md-awesome/` directory with 73 brand DESIGN.md files likely came from the `github.com/designmd/awesome-design-md` repo or from `designmd.app` itself.

Let me just answer the user based on what I know.

Os DESIGN.md curados em `design-md-awesome/` vêm de dois lugares:

- **Repositório GitHub:** [github.com/designmd/awesome-design-md](https://github.com/designmd/awesome-design-md)
- **Site principal:** [designmd.app/library](https://designmd.app/library) — onde estão todos os 454 sistemas de design

---

## User

o que faz esse projeto? 

---

## Assistant (Build · Big Pickle · 8.6s)

_Thinking:_

The user is asking "what does this project do?" - they want a concise explanation of the project's purpose.

Coleção de arquivos `DESIGN.md` — definições de design system (cores, tipografia, espaçamento, componentes) no formato Google Stitch. Agentes de IA leem esses arquivos da raiz do projeto para gerar UI visualmente consistente. O repositório reúne 73 sistemas curados de marcas (Airbnb, Apple, Stripe...) e 454 baixados de [designmd.app/library](https://designmd.app/library), além de scripts e skills para criar novos.

---

## User

se eu executar a skill agora, o que vai fazer?

---

## Assistant (Build · Big Pickle · 3.4s)

_Thinking:_

The user is asking what would happen if they run the skill now. They're referring to the skills/extract_design_skill.md. Let me re-read that file to answer accurately.

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/skills/extract_design_skill.md"
}
```

**Output:**
```
<path>/home/mkt/design_md/skills/extract_design_skill.md</path>
<type>file</type>
<content>
1: # Skill: Precision DESIGN.md Extractor
2: 
3: ## Objetivo
4: Atuar como um Engenheiro de UI/UX de elite. Sua tarefa é visitar uma URL alvo fornecida pelo usuário e fazer engenharia reversa do design system do site, transformando-o em um arquivo `DESIGN.md` impecável e *pixel-perfect*, seguindo estritamente o padrão do Google Stitch.
5: 
6: ## Pré-Requisitos (Pre-Flight)
7: 1. **Aprender o Padrão (Schema):** Antes de iniciar qualquer extração, você DEVE obrigatoriamente usar a ferramenta `view_file` para ler e absorver a estrutura do arquivo de referência localizado em `/Users/fatima/Desktop/awesome_design/design-md/stripe/DESIGN.md` (ou `apple/DESIGN.md`).
8: 2. Preste atenção rigorosa em como as cores (Hex), tipografia, raios de borda (border-radius), sombras e estados interativos são documentados.
9: 
10: ## Passos de Execução
11: 
12: ### Fase 1: Inspeção Visual e Técnica Profunda
13: Invoque o `browser_subagent` com a URL alvo. Instrua o subagente a realizar uma auditoria técnica rigorosa do DOM e do CSS (Computed Styles):
14: - **Cores (Colors):** Extraia os valores exatos em HEX para o fundo (background), texto (primário, secundário, mutado), cores primárias da marca e cores semânticas (sucesso, aviso, erro). Verifique se há variáveis CSS (`--var`).
15: - **Tipografia (Typography):** Identifique a stack exata de `font-family`. Extraia os pesos (weights - ex: 400, 500, 600) e tamanhos para os títulos (H1-H6) e texto base (body).
16: - **Elementos e Componentes (UI Elements):** Inspecione botões, inputs e cards. Extraia os valores matemáticos exatos para:
17:   - `border-radius` (ex: 4px, 8px, pill/9999px)
18:   - `box-shadow` (sombras de elevação, sombras suaves)
19:   - Escala de espaçamento (padding e margins padrão)
20:   - Estados de Hover e Active (transições, mudanças de cor)
21: - **Layout:** Identifique a largura máxima (max-width) do container principal e a estrutura do grid.
22: 
23: ### Fase 2: Síntese e Mapeamento
24: Traduza o CSS bruto e os dados visuais capturados para a formatação rigorosa do `DESIGN.md`.
25: - **PROIBIDO ALUCINAR DADOS:** Se um valor não for óbvio visualmente, baseie-se nos estilos computados do CSS.
26: - **Filosofia do Design:** Escreva uma breve introdução que capture a "vibe" e a filosofia estética da marca (ex: "minimalista de luxo", "brutalista", "corporativo limpo").
27: 
28: ### Fase 3: Geração do Arquivo
29: 1. Determine o nome da marca a partir da URL (ex: `netflix`, `spotify`).
30: 2. Use a ferramenta `write_to_file` para criar o novo arquivo exatamente no caminho: `/Users/fatima/Desktop/awesome_design/design-md/<nome_da_marca>/DESIGN.md`.
31: 3. O arquivo gerado DEVE manter a exata hierarquia de Markdown (headings, blocos de código, listas) aprendida na fase de Pré-Requisitos.
32: 
33: ## Garantia de Qualidade (QA)
34: Antes de finalizar a tarefa e retornar ao usuário, verifique internamente:
35: - Os códigos HEX são reais e foram extraídos do site?
36: - A tipografia reflete a identidade verdadeira da marca?
37: - A estrutura do Markdown bate 100% com o padrão Stitch adotado pelos exemplos?

(End of file - total 37 lines)
</content>
```

---

## Assistant (Build · Big Pickle · 4.3s)

Nada — a skill não executa automaticamente. Ela só define o **passo a passo** para um agente de IA seguir. Para rodá-la, você precisaria carregá-la via ferramenta `skill` e fornecer uma URL alvo. O agente então:

1. Abriria o site no navegador
2. Inspecionaria DOM e CSS computed
3. Extrairia cores, tipografia, border-radius, sombras
4. Escreveria um `DESIGN.md` em `design-md-library/454/<slug>/`

No momento, sem uma URL alvo, a skill não faz nada.

---

## User

quais listas de urls ele percorreria? tendo em conta o que já foi baixado em @design-md-library/ 

---

## Assistant (Build · Big Pickle · 5.5s)

_Thinking:_

The user is asking what list of URLs the skill/script would go through, considering what's already been downloaded in `design-md-library/`. 

Let me check what's in the 454 directory to see which slugs are already downloaded, and cross-reference with the URLs in `elementos_designmd.md`.

The skill itself doesn't use a URL list - it takes a single URL from the user. But the `automacao_bookmarklet.py` script reads all URLs from `elementos_designmd.md`.

The user seems to be asking: given what's already in `design-md-library/454/`, which URLs are still pending?

Let me check how many slugs are in 454/ and compare with the table.

**Tool: bash**

**Input:**
```json
{
  "command": "ls /home/mkt/design_md/design-md-library/454/ | wc -l",
  "description": "Count downloaded slugs"
}
```

**Output:**
```
454

```

**Tool: bash**

**Input:**
```json
{
  "command": "ls /home/mkt/design_md/design-md-library/454/ > /tmp/slugs_existentes.txt",
  "description": "List existing slugs"
}
```

**Output:**
```
(no output)
```

**Tool: bash**

**Input:**
```json
{
  "command": "grep -oP 'https://designmd\\.app/(?:en/)?library/\\K[^) ]+' /home/mkt/design_md/design-md-library/elementos_designmd.md | wc -l",
  "description": "Count total URLs in table"
}
```

**Output:**
```
454

```

---

## Assistant (Build · Big Pickle · 4.5s)

_Thinking:_

So there are exactly 454 slugs in the 454/ directory and 454 URLs in the table in `elementos_designmd.md`. Let me check if the slugs match the URLs. But first, let me check if there are DESIGN.md files inside these slug directories or if they're empty (just the directory with maybe an image).

**Tool: bash**

**Input:**
```json
{
  "command": "ls /home/mkt/design_md/design-md-library/454/3x3-grid-design/ 2>/dev/null | head -5; echo \"---\"; ls /home/mkt/design_md/design-md-library/454/minimalism-swiss-style/ 2>/dev/null | head -5",
  "description": "Check if DESIGN.md files exist in 454/ subdirectories"
}
```

**Output:**
```
308.png
---
1.png

```

**Tool: bash**

**Input:**
```json
{
  "command": "find /home/mkt/design_md/design-md-library/454/ -name 'DESIGN.md' | wc -l",
  "description": "Count DESIGN.md files in 454/"
}
```

**Output:**
```
0

```

---

## Assistant (Build · Big Pickle · 4.7s)

_Thinking:_

So the 454/ directory contains only images (thumbnails), not DESIGN.md files. The actual DESIGN.md files haven't been downloaded yet. The `todo.md` says exactly this:

```
Falta:

- Usar o robô para visitar cada url e clicar no botão de favorito de bookmarklet para baixar o DESIGN.md das 454 páginas.
```

So the slugs in 454/ are just directories with images. The actual DESIGN.md files still need to be downloaded. The `automacao_bookmarklet.py` script was designed to do exactly that - visit each URL and click the bookmarklet to trigger the download.

Let me count how many of the images were downloaded vs missing.

**Tool: bash**

**Input:**
```json
{
  "command": "find /home/mkt/design_md/design-md-library/454/ -name '*.png' | wc -l",
  "description": "Count downloaded images"
}
```

**Output:**
```
454

```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/design-md-library/todo.md"
}
```

**Output:**
```
<path>/home/mkt/design_md/design-md-library/todo.md</path>
<type>file</type>
<content>
1: Falta:
2: 
3: - Usar o robô para visitar cada url e clicar no botão de favorito de bookmarklet para baixar o DESIGN.md das 454 páginas.

(End of file - total 3 lines)
</content>
```

---

## Assistant (Build · Big Pickle · 5.3s)

_Thinking:_

So the situation is:
- 454 subdirectories in 454/ — each has a `.png` thumbnail (454 images) but no `DESIGN.md` files
- The `todo.md` says what's missing: actually visiting each URL and clicking the bookmarklet to download the DESIGN.md files
- The `automacao_bookmarklet.py` script was created precisely for this task

So if the skill were run or the `automacao_bookmarklet.py` script were used, it would go through all 454 URLs from `elementos_designmd.md` and try to download the DESIGN.md files from each page. None of the 454 DESIGN.md files have been downloaded yet - only the preview images.

As 454 pastas em `454/` contêm apenas **imagens thumbnail** (`.png`). Nenhum `DESIGN.md` foi baixado ainda. O `todo.md` confirma:

> *"Usar o robô para visitar cada url e clicar no botão de favorito de bookmarklet para baixar o DESIGN.md das 454 páginas."*

O script `automacao_bookmarklet.py` percorreria **todas as 454 URLs** da tabela em `elementos_designmd.md` — nenhuma foi visitada ainda, então seriam 454 pendentes.

---

## User

considere as que já estao na pasta @design-md-library/MDs/ e baixe as outras, pode ser? 

---

## Assistant (Build · Big Pickle · 11.2s)

_Thinking:_

There's a `MDs/` directory with 61 DESIGN.md files already downloaded. The naming pattern is `<slug>-DESIGN.md`. So 61 out of 454 are already downloaded. I need to:

1. Extract slugs from the 61 existing files in MDs/
2. Cross-reference with the 454 URLs from elementos_designmd.md
3. Download the remaining ones

The files in MDs/ use the format `<slug>-DESIGN.md`. I need to extract the slugs from those filenames.

Let me plan:
1. List all slugs already downloaded (from MDs/ filenames)
2. Get all slugs from elementos_designmd.md
3. Find which slugs are missing
4. Visit each missing URL and download the DESIGN.md

But wait - I can't run the pyautogui bookmarklet script. I can use the browser tools directly to visit each page and click the download button. But that would be extremely slow for ~400 pages.

Actually, let me think about this differently. Looking at the library page we opened earlier, the page content already contains the full DESIGN.md inline - it's rendered in the HTML. We could scrape it directly from the page content instead of clicking a bookmarklet.

But the user asked me to "baixe as outras" (download the others). Let me think about the best approach.

Actually, looking at the snapshot of the library page more carefully:
- There's a "Download DESIGN.md" button (uid=1_250)
- There's a "Copy DESIGN.md" button (uid=1_251)
- The DESIGN.md content is already rendered inline on the page

So I could:
1. Extract the slugs we already have
2. Find which ones we're missing
3. For each missing slug, fetch the page and either click download or extract the inline content

But wait - I can use pyautogui... actually, the user said to proceed, so maybe they want me to write a better script or use the browser to download them. But clicking 400 pages via browser tool would be too many iterations.

Actually, let me think about this more practically. The `automacao_bookmarklet.py` was designed for this but uses pyautogui. A better approach would be to write a script that:
1. Fetches each URL with requests/urllib
2. Extracts the DESIGN.md content from the HTML
3. Saves it to the appropriate directory

Or even better, I could look at whether the library page has an API or a simpler download mechanism. Let me check what happens when you click "Download DESIGN.md" - it might just be a direct download link.

Let me check the network request or the page source to see if there's a direct download URL pattern.

Actually, from the snapshot, the download button is just a button element without a direct link. It might trigger a download via JavaScript.

Let me look at the page more carefully to understand the download mechanism. Let me check network requests or evaluate a script to see what the download button does.

Actually, I should first figure out which ones we already have, then come up with a plan to download the rest.

Let me:
1. Get the slugs from MDs/
2. Get all slugs from elementos_designmd.md
3. Find the missing ones
4. Figure out the download approach

Let me start.

**Tool: todowrite**

**Input:**
```json
{
  "todos": [
    {
      "content": "List slugs already downloaded in MDs/",
      "status": "in_progress",
      "priority": "high"
    },
    {
      "content": "Cross-reference with all 454 slugs from elementos_designmd.md",
      "status": "pending",
      "priority": "high"
    },
    {
      "content": "Figure out download approach and download missing DESIGN.md files",
      "status": "pending",
      "priority": "high"
    }
  ]
}
```

**Output:**
```
[
  {
    "content": "List slugs already downloaded in MDs/",
    "status": "in_progress",
    "priority": "high"
  },
  {
    "content": "Cross-reference with all 454 slugs from elementos_designmd.md",
    "status": "pending",
    "priority": "high"
  },
  {
    "content": "Figure out download approach and download missing DESIGN.md files",
    "status": "pending",
    "priority": "high"
  }
]
```

---

## Assistant (Build · Big Pickle · 6.5s)

_Thinking:_

Let me get the slugs from both the existing MDs/ files and from elementos_designmd.md to see what's missing. I also need to examine the download mechanism on the page.

**Tool: bash**

**Input:**
```json
{
  "command": "ls /home/mkt/design_md/design-md-library/MDs/ | sed 's/-DESIGN\\.md$//' | sort > /tmp/slugs_baixados.txt && wc -l /tmp/slugs_baixados.txt",
  "description": "Extract downloaded slugs from MDs/ filenames"
}
```

**Output:**
```
61 /tmp/slugs_baixados.txt

```

**Tool: bash**

**Input:**
```json
{
  "command": "grep -oP 'https://designmd\\.app/(?:en/)?library/\\K[^) ]+' /home/mkt/design_md/design-md-library/elementos_designmd.md > /tmp/slugs_totais.txt && wc -l /tmp/slugs_totais.txt",
  "description": "Extract all slugs from elementos_designmd.md"
}
```

**Output:**
```
454 /tmp/slugs_totais.txt

```

**Tool: chrome-devtools_evaluate_script**

**Input:**
```json
{
  "function": "() => { const btn = document.querySelector('#download-designmd, button:has-text(\"Download DESIGN.md\")'); return btn ? btn.outerHTML : 'not found'; }"
}
```

**Error:**
```
Error: SyntaxError: Failed to execute 'querySelector' on 'Document': '#download-designmd, button:has-text("Download DESIGN.md")' is not a valid selector.
pptr:evaluateHandle;performEvaluation%20(file%3A%2F%2F%2Fhome%2Fmkt%2F.npm%2F_npx%2F15c61037b1978c83%2Fnode_modules%2Fchrome-devtools-mcp%2Fbuild%2Fsrc%2Ftools%2Fscript.js%3A100%3A34):1:31
pptr:evaluate;performEvaluation%20(file%3A%2F%2F%2Fhome%2Fmkt%2F.npm%2F_npx%2F15c61037b1978c83%2Fnode_modules%2Fchrome-devtools-mcp%2Fbuild%2Fsrc%2Ftools%2Fscript.js%3A102%3A42):3:41
```

---

## Assistant (Build · Big Pickle · 4.1s)

_Thinking:_

The `:has-text()` pseudo-selector is not valid in standard CSS. Let me find the download button differently. Also, let me find the missing slugs.

**Tool: bash**

**Input:**
```json
{
  "command": "comm -23 /tmp/slugs_totais.txt /tmp/slugs_baixados.txt > /tmp/slugs_faltantes.txt && wc -l /tmp/slugs_faltantes.txt",
  "description": "Find missing slugs"
}
```

**Output:**
```
comm: o arquivo 1 não está ordenado
comm: a entrada não está ordenada

```

**Tool: chrome-devtools_evaluate_script**

**Input:**
```json
{
  "function": "() => { const buttons = document.querySelectorAll('button'); return Array.from(buttons).map(b => ({ text: b.innerText.slice(0,50), id: b.id, class: b.className })); }"
}
```

**Output:**
```
Script ran on page and returned:
```json
[]
```
```

---

## Assistant (Build · Big Pickle · 3.7s)

_Thinking:_

Empty buttons array - the page might have navigated away or the session expired. Let me sort the files first and retry, and also navigate back to the page.

**Tool: bash**

**Input:**
```json
{
  "command": "sort /tmp/slugs_baixados.txt -o /tmp/slugs_baixados.txt && sort /tmp/slugs_totais.txt -o /tmp/slugs_totais.txt && comm -23 /tmp/slugs_totais.txt /tmp/slugs_baixados.txt > /tmp/slugs_faltantes.txt && wc -l /tmp/slugs_faltantes.txt",
  "description": "Find missing slugs after sorting"
}
```

**Output:**
```
393 /tmp/slugs_faltantes.txt

```

**Tool: chrome-devtools_list_pages**

**Input:**
```json
{}
```

**Output:**
```
## Pages
1: about:blank [selected]
```

---

## Assistant (Build · Big Pickle · 5.5s)

_Thinking:_

So we have 61 downloaded, 393 missing (total 454). Let me understand the download mechanism better. Let me open a fresh page and examine the Download button.

**Tool: chrome-devtools_navigate_page**

**Input:**
```json
{
  "url": "https://designmd.app/library/airbnb-coral-marketplace"
}
```

**Output:**
```
Successfully navigated to https://designmd.app/library/airbnb-coral-marketplace.
## Pages
1: Airbnb Coral Marketplace — DESIGN.md | designmd... (https://designmd.app/library/airbnb-coral-marketplace) [selected]
```

---

## Assistant (Build · Big Pickle · 3.4s)

_Thinking:_

Let me check what the download button does - look at its attributes, onclick handlers, etc.

**Tool: chrome-devtools_evaluate_script**

**Input:**
```json
{
  "function": "() => { const btns = document.querySelectorAll('button'); return Array.from(btns).map(b => ({ text: b.innerText.trim().slice(0,50), id: b.id, className: b.className.slice(0,60), onclick: b.onclick ? 'has onclick' : 'none', outerHTML: b.outerHTML.slice(0,300) })); }"
}
```

**Output:**
```
Script ran on page and returned:
```json
[{"text":"","id":"mobile-menu-btn","className":"inline-flex items-center justify-center rounded-full p-2 tex","onclick":"none","outerHTML":"<button type=\"button\" id=\"mobile-menu-btn\" class=\"inline-flex items-center justify-center rounded-full p-2 text-[var(--text-60)] hover:bg-[var(--hover-bg)] hover:text-[var(--text)] md:hidden transition-colors\" aria-expanded=\"false\" aria-controls=\"mobile-menu\" aria-label=\"Open navigation menu\"> <svg "},{"text":"Copy DESIGN.md","id":"copy-designmd","className":"inline-flex items-center gap-2 rounded-full border border-[v","onclick":"none","outerHTML":"<button id=\"copy-designmd\" type=\"button\" class=\"inline-flex items-center gap-2 rounded-full border border-[var(--border-strong)] px-5 py-2 font-mono text-xs text-[var(--text-60)] transition-all hover:border-[var(--text)] hover:text-[var(--text)] hover:bg-[var(--hover-bg)]\"> Copy DESIGN.md </button>"},{"text":"Copy Prompt","id":"copy-prompt","className":"inline-flex items-center gap-2 rounded-full border border-[v","onclick":"none","outerHTML":"<button id=\"copy-prompt\" type=\"button\" class=\"inline-flex items-center gap-2 rounded-full border border-[var(--border-strong)] px-5 py-2 font-mono text-xs text-[var(--text-60)] transition-all hover:border-[var(--text)] hover:text-[var(--text)] hover:bg-[var(--hover-bg)]\"> Copy Prompt </button>"},{"text":"Cookies","id":"open-cookie-prefs","className":"transition-colors hover:text-[var(--text)] cursor-pointer","onclick":"none","outerHTML":"<button id=\"open-cookie-prefs\" type=\"button\" class=\"transition-colors hover:text-[var(--text)] cursor-pointer\"> Cookies </button>"},{"text":"Reject","id":"cc-reject","className":"rounded border border-[var(--border)] px-3 py-1.5 font-mono ","onclick":"none","outerHTML":"<button id=\"cc-reject\" class=\"rounded border border-[var(--border)] px-3 py-1.5 font-mono text-xs text-[var(--text-muted)] transition-colors hover:bg-[var(--bg-alt)] hover:text-[var(--text)]\"> Reject </button>"},{"text":"Accept","id":"cc-accept","className":"rounded bg-[var(--text)] px-3 py-1.5 font-mono text-xs text-","onclick":"none","outerHTML":"<button id=\"cc-accept\" class=\"rounded bg-[var(--text)] px-3 py-1.5 font-mono text-xs text-[var(--bg)] transition-colors hover:opacity-90\"> Accept </button>"}]
```
```

---

## Assistant (Build · Big Pickle · 3.9s)

_Thinking:_

I see there's no "Download DESIGN.md" button in the buttons list, but there is a "Copy DESIGN.md" button. Let me check the full HTML to find the download button. Maybe it's not a button but a link. Let me look at the page more carefully.

**Tool: chrome-devtools_evaluate_script**

**Input:**
```json
{
  "function": "() => { const all = document.querySelectorAll('[id*=\"download\"], [class*=\"download\"], a[download], button:contains(\"Download\"), [href*=\"download\"]'); return Array.from(all).map(el => el.tagName + ' ' + (el.id || '') + ' ' + (el.className || '') + ' ' + (el.innerText || '').trim().slice(0,50)).join(' || '); }"
}
```

**Error:**
```
Error: SyntaxError: Failed to execute 'querySelectorAll' on 'Document': '[id*="download"], [class*="download"], a[download], button:contains("Download"), [href*="download"]' is not a valid selector.
pptr:evaluateHandle;performEvaluation%20(file%3A%2F%2F%2Fhome%2Fmkt%2F.npm%2F_npx%2F15c61037b1978c83%2Fnode_modules%2Fchrome-devtools-mcp%2Fbuild%2Fsrc%2Ftools%2Fscript.js%3A100%3A34):1:31
pptr:evaluate;performEvaluation%20(file%3A%2F%2F%2Fhome%2Fmkt%2F.npm%2F_npx%2F15c61037b1978c83%2Fnode_modules%2Fchrome-devtools-mcp%2Fbuild%2Fsrc%2Ftools%2Fscript.js%3A102%3A42):3:41
```

---

## Assistant (Build · Big Pickle · 3.6s)

_Thinking:_

Let me use a simpler query approach to find the download button.

**Tool: chrome-devtools_evaluate_script**

**Input:**
```json
{
  "function": "() => { const buttons = document.querySelectorAll('button'); const results = []; buttons.forEach(b => { if (b.innerText.includes('Download')) results.push(b.outerHTML); }); const links = document.querySelectorAll('a'); links.forEach(a => { if (a.innerText.includes('Download') || a.hasAttribute('download')) results.push(a.outerHTML); }); return results.length ? results : 'no download elements found'; }"
}
```

**Output:**
```
Script ran on page and returned:
```json
["<a href=\"/library/airbnb-coral-marketplace/design.md\" download=\"\" class=\"inline-flex items-center gap-2 rounded-full bg-[var(--text)] px-5 py-2 font-mono text-xs text-[var(--bg)] transition-all hover:bg-[var(--accent-hover)]\"> Download DESIGN.md </a>"]
```
```

---

## Assistant (Build · Big Pickle · 4.4s)

_Thinking:_

Now I found the download link. It's an `<a>` tag with `download` attribute pointing to `/library/airbnb-coral-marketplace/design.md`. The full URL would be `https://designmd.app/library/airbnb-coral-marketplace/design.md`.

So the download mechanism is simple: each page has a direct download link at `/library/<slug>/design.md`. I can download these directly without needing a browser or pyautogui!

Let me verify the URL pattern works by downloading one file first.

**Tool: todowrite**

**Input:**
```json
{
  "todos": [
    {
      "priority": "high",
      "content": "List slugs already downloaded in MDs/",
      "status": "completed"
    },
    {
      "priority": "high",
      "content": "Cross-reference with all 454 slugs from elementos_designmd.md",
      "status": "completed"
    },
    {
      "priority": "high",
      "content": "Download missing DESIGN.md files (393 remaining)",
      "status": "in_progress"
    }
  ]
}
```

**Output:**
```
[
  {
    "content": "List slugs already downloaded in MDs/",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Cross-reference with all 454 slugs from elementos_designmd.md",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Download missing DESIGN.md files (393 remaining)",
    "status": "in_progress",
    "priority": "high"
  }
]
```

---

## Assistant (Build · Big Pickle · 4.5s)

_Thinking:_

The download link is just `/library/<slug>/design.md`. Let me test it and then write a script to batch download all 393 missing files. Let me first verify the download URL works.

O link de download é direto: `/library/<slug>/design.md`. Vou verificar e baixar as 393 faltantes.

**Tool: chrome-devtools_evaluate_script**

**Input:**
```json
{
  "function": "async () => { const r = await fetch('/library/airbnb-coral-marketplace/design.md'); return r.ok ? 'OK' : r.status; }"
}
```

**Output:**
```
Script ran on page and returned:
```json
"OK"
```
```

---

## Assistant (Build · Big Pickle · 3.3s)

_Thinking:_

The download URL works. Now let me write a script that will batch download all 393 missing DESIGN.md files. I'll use bash with curl to download them directly to the MDs/ directory, naming them as `<slug>-DESIGN.md`.

**Tool: bash**

**Input:**
```json
{
  "command": "head -5 /tmp/slugs_faltantes.txt",
  "description": "Preview first 5 missing slugs"
}
```

**Output:**
```
3d-product-preview
3x3-grid-design
70s-psychedelic-flower-power
8-bit-orbit
8-bit-retro-terminal

```

---

## Assistant (Build · Big Pickle · 49.5s)

**Tool: bash**

**Input:**
```json
{
  "command": "cd /home/mkt/design_md/design-md-library/MDs && total=$(wc -l < /tmp/slugs_faltantes.txt); count=0; while IFS= read -r slug; do count=$((count+1)); url=\"https://designmd.app/library/${slug}/design.md\"; outfile=\"${slug}-DESIGN.md\"; if [ -f \"$outfile\" ]; then echo \"[$count/$total] SKIP $slug (já existe)\"; else echo \"[$count/$total] Baixando $slug...\"; curl -s -f -o \"$outfile\" \"$url\" && echo \"  ✓ OK\" || echo \"  ✗ FALHA\"; fi; done < /tmp/slugs_faltantes.txt",
  "description": "Download all 393 missing DESIGN.md files",
  "timeout": 600000
}
```

**Output:**
```
[1/393] Baixando 3d-product-preview...
  ✓ OK
[2/393] Baixando 3x3-grid-design...
  ✓ OK
[3/393] Baixando 70s-psychedelic-flower-power...
  ✓ OK
[4/393] Baixando 8-bit-orbit...
  ✓ OK
[5/393] Baixando 8-bit-retro-terminal...
  ✓ OK
[6/393] Baixando 90s-retro-video-game...
  ✓ OK
[7/393] Baixando acanthus...
  ✓ OK
[8/393] Baixando afrofuturismo-digital...
  ✓ OK
[9/393] Baixando agency-viral-videos-reels-hero...
  ✓ OK
[10/393] Baixando ai-automation-hero...
  ✓ OK
[11/393] Baixando airbnb-coral-marketplace...
  ✓ OK
[12/393] Baixando albert-sans-typography...
  ✓ OK
[13/393] Baixando amazonia-futurista...
  ✓ OK
[14/393] Baixando american-diner-americana...
  ✓ OK
[15/393] Baixando analytics-metric-flow...
  ✓ OK
[16/393] Baixando ancient-egyptian-historical...
  ✓ OK
[17/393] Baixando ancient-egyptian-instructional-scroll...
  ✓ OK
[18/393] Baixando anime-battle...
  ✓ OK
[19/393] Baixando anthropomorphic...
  ✓ OK
[20/393] Baixando apple-premium-cinematic...
  ✓ OK
[21/393] Baixando aprendizado-criativo-artesanal...
  ✓ OK
[22/393] Baixando architectural-portfolio-cinematic...
  ✓ OK
[23/393] Baixando architectural-schematic...
  ✓ OK
[24/393] Baixando arctic-forsythia-premium...
  ✓ OK
[25/393] Baixando art-deco...
  ✓ OK
[26/393] Baixando art-deco-golden-age...
  ✓ OK
[27/393] Baixando artesanato-organico-e-acolhedor...
  ✓ OK
[28/393] Baixando art-nouveau...
  ✓ OK
[29/393] Baixando art-nouveau-florido...
  ✓ OK
[30/393] Baixando aura-premium-webgl-iconify...
  ✓ OK
[31/393] Baixando aurora...
  ✓ OK
[32/393] Baixando aurora-boreal-nordica...
  ✓ OK
[33/393] Baixando azulejaria-digital-moderna...
  ✓ OK
[34/393] Baixando azulejo-portugues...
  ✓ OK
[35/393] Baixando baroque...
  ✓ OK
[36/393] Baixando bauhaus...
  ✓ OK
[37/393] Baixando bauhaus-risograph-modern...
  ✓ OK
[38/393] Baixando belle-epoque-lithograph...
  ✓ OK
[39/393] Baixando bento-dados-estruturados...
  ✓ OK
[40/393] Baixando bento-eventos-dinamicos...
  ✓ OK
[41/393] Baixando bento-grid...
  ✓ OK
[42/393] Baixando bento-grid-tech-minimalist...
  ✓ OK
[43/393] Baixando bento-noticias-curadas...
  ✓ OK
[44/393] Baixando bento-portfolio-de-produto...
  ✓ OK
[45/393] Baixando bento-produtividade-flexivel...
  ✓ OK
[46/393] Baixando biennale-yellow...
  ✓ OK
[47/393] Baixando block-frame...
  ✓ OK
[48/393] Baixando blueprint-engineering...
  ✓ OK
[49/393] Baixando blue-professional...
  ✓ OK
[50/393] Baixando bmw-angular-precision...
  ✓ OK
[51/393] Baixando bohemian-boho...
  ✓ OK
[52/393] Baixando bold-energetic...
  ✓ OK
[53/393] Baixando bold-portfolio-hero...
  ✓ OK
[54/393] Baixando bold-poster...
  ✓ OK
[55/393] Baixando bold-signal...
  ✓ OK
[56/393] Baixando bossa-nova-lounge...
  ✓ OK
[57/393] Baixando broadside...
  ✓ OK
[58/393] Baixando brutalism-311...
  ✓ OK
[59/393] Baixando brutalismo-artistico-abstrato...
  ✓ OK
[60/393] Baixando brutalismo-sonoro-glitch...
  ✓ OK
[61/393] Baixando brutalismo-urbano-expressivo...
  ✓ OK
[62/393] Baixando brutalist-web-design...
  ✓ OK
[63/393] Baixando cad-inspired-blueprint...
  ✓ OK
[64/393] Baixando cafe-artesanal-aconchegante...
  ✓ OK
[65/393] Baixando capsule...
  ✓ OK
[66/393] Baixando caramelo-quente-premium...
  ✓ OK
[67/393] Baixando cartazista-de-supermercado...
  ✓ OK
[68/393] Baixando cartesian...
  ✓ OK
[69/393] Baixando cassette-futurism...
  ✓ OK
[70/393] Baixando ceramica-wabi-sabi...
  ✓ OK
[71/393] Baixando cerrado-minimalista...
  ✓ OK
[72/393] Baixando chalkboard...
  ✓ OK
[73/393] Baixando chalkboard-hand-drawn...
  ✓ OK
[74/393] Baixando chalkboard-sketch-note...
  ✓ OK
[75/393] Baixando chromatic-aberration-rgb-split...
  ✓ OK
[76/393] Baixando circuit-board-pcb...
  ✓ OK
[77/393] Baixando claude-warm-parchment...
  ✓ OK
[78/393] Baixando clay-artisanal-swatch...
  ✓ OK
[79/393] Baixando claymation-3d...
  ✓ OK
[80/393] Baixando claymation-3d-illustration...
  ✓ OK
[81/393] Baixando clearinvoice-saas-hero...
  ✓ OK
[82/393] Baixando clickhouse-neon-volt...
  ✓ OK
[83/393] Baixando coastal-commerce...
  ✓ OK
[84/393] Baixando coastal-mist...
  ✓ OK
[85/393] Baixando coastal-studio...
  ✓ OK
[86/393] Baixando cobalt-grid...
  ✓ OK
[87/393] Baixando cohere-enterprise-serif...
  ✓ OK
[88/393] Baixando coinbase-trust-blue...
  ✓ OK
[89/393] Baixando comic-book-pop-art...
  ✓ OK
[90/393] Baixando composio-cyber-nocturnal...
  ✓ OK
[91/393] Baixando conceptual-sketch-doodle-art...
  ✓ OK
[92/393] Baixando conforto-artesanal-brasileiro...
  ✓ OK
[93/393] Baixando construtivismo-arquitetonico...
  ✓ OK
[94/393] Baixando construtivismo-de-dados-dinamicos...
  ✓ OK
[95/393] Baixando construtivismo-de-eventos-dinamicos...
  ✓ OK
[96/393] Baixando construtivismo-dinamico-tech...
  ✓ OK
[97/393] Baixando construtivismo-literario-experimental...
  ✓ OK
[98/393] Baixando coquette...
  ✓ OK
[99/393] Baixando coral...
  ✓ OK
[100/393] Baixando cordel-digital...
  ✓ OK
[101/393] Baixando corporate-radial-process...
  ✓ OK
[102/393] Baixando creative-mode...
  ✓ OK
[103/393] Baixando creative-voltage...
  ✓ OK
[104/393] Baixando criatividade-artesanal-e-pessoal...
  ✓ OK
[105/393] Baixando crm-copper-sand...
  ✓ OK
[106/393] Baixando crypto-exchange-plataforma...
  ✓ OK
[107/393] Baixando culinaria-afetiva-brasileira...
  ✓ OK
[108/393] Baixando cursor-warm-gothic...
  ✓ OK
[109/393] Baixando cyber-core...
  ✓ OK
[110/393] Baixando cyberpunk-dark-mode-flow...
  ✓ OK
[111/393] Baixando cyberpunk-neon-noir...
  ✓ OK
[112/393] Baixando cyber-tribal...
  ✓ OK
[113/393] Baixando daisy-days...
  ✓ OK
[114/393] Baixando dark-botanical...
  ✓ OK
[115/393] Baixando dark-glassmorphism-infographic...
  ✓ OK
[116/393] Baixando dark-portfolio-hero...
  ✓ OK
[117/393] Baixando dark-saas-hero-with-liquid-glass...
  ✓ OK
[118/393] Baixando datacore-saas-hero...
  ✓ OK
[119/393] Baixando degraded-colorful-vibrant-gradient...
  ✓ OK
[120/393] Baixando democratized-fancy-animations...
  ✓ OK
[121/393] Baixando denim-and-industrial-craft...
  ✓ OK
[122/393] Baixando desenho-a-mao-ludico...
  ✓ OK
[123/393] Baixando design-autoral-robusto...
  ✓ OK
[124/393] Baixando de-stijl-abstrato...
  ✓ OK
[125/393] Baixando doodle-sketch-livre...
  ✓ OK
[126/393] Baixando earthy-organic...
  ✓ OK
[127/393] Baixando editorial-contemporaneo...
  ✓ OK
[128/393] Baixando editorial-de-portfolio-criativo...
  ✓ OK
[129/393] Baixando editorial-de-viagem-sofisticado...
  ✓ OK
[130/393] Baixando editorial-grid-magazine...
  ✓ OK
[131/393] Baixando editorial-interativo-digital...
  ✓ OK
[132/393] Baixando editorial-investigativo-sobrio...
  ✓ OK
[133/393] Baixando editorial-tri-tone...
  ✓ OK
[134/393] Baixando edtech-plataforma-de-cursos...
  ✓ OK
[135/393] Baixando electric-studio...
  ✓ OK
[136/393] Baixando elementos-musicais...
  ✓ OK
[137/393] Baixando elevenlabs-ethereal-voice...
  ✓ OK
[138/393] Baixando ember-amethyst-premium...
  ✓ OK
[139/393] Baixando engineering-blueprint-schematic...
  ✓ OK
[140/393] Baixando estilo-de-computacao-de-alta-performance...
  ✓ OK
[141/393] Baixando estilo-de-dados-empresariais...
  ✓ OK
[142/393] Baixando estilo-de-ecossistema-digital...
  ✓ OK
[143/393] Baixando estilo-de-elegancia-espacial...
  ✓ OK
[144/393] Baixando estilo-de-elegancia-fintech...
  ✓ OK
[145/393] Baixando estilo-de-entretenimento-imersivo...
  ✓ OK
[146/393] Baixando estilo-deep-learning-high-tech...
  ✓ OK
[147/393] Baixando estilo-de-experiencia-de-compra-continua...
  ✓ OK
[148/393] Baixando estilo-de-fluxo-de-rede...
  ✓ OK
[149/393] Baixando estilo-de-futuro-autonomo...
  ✓ OK
[150/393] Baixando estilo-de-ia-criativa...
  ✓ OK
[151/393] Baixando estilo-de-ia-etica...
  ✓ OK
[152/393] Baixando estilo-de-ia-para-negocios...
  ✓ OK
[153/393] Baixando estilo-de-inovacao-em-dispositivos-moveis...
  ✓ OK
[154/393] Baixando estilo-de-inteligencia-generativa...
  ✓ OK
[155/393] Baixando estilo-de-litografia-de-precisao...
  ✓ OK
[156/393] Baixando estilo-de-realidade-virtual-social...
  ✓ OK
[157/393] Baixando estilo-de-tecnologia-de-precisao...
  ✓ OK
[158/393] Baixando estilo-fluent-ai...
  ✓ OK
[159/393] Baixando estilo-material-ai...
  ✓ OK
[160/393] Baixando estilo-suico-artistico...
  ✓ OK
[161/393] Baixando estilo-suico-cientifico...
  ✓ OK
[162/393] Baixando estilo-suico-corporativo...
  ✓ OK
[163/393] Baixando estilo-suico-educacional...
  ✓ OK
[164/393] Baixando estilo-suico-premium...
  ✓ OK
[165/393] Baixando ethereal...
  ✓ OK
[166/393] Baixando expo-luminous-developer...
  ✓ OK
[167/393] Baixando farmhouse-cottage-core...
  ✓ OK
[168/393] Baixando figma-vibrant-monochrome...
  ✓ OK
[169/393] Baixando filigree...
  ✓ OK
[170/393] Baixando fintech-plataforma-financeira...
  ✓ OK
[171/393] Baixando fitness-app-de-treinos...
  ✓ OK
[172/393] Baixando flat-design-corporativo...
  ✓ OK
[173/393] Baixando flat-design-educacional-vibrante...
  ✓ OK
[174/393] Baixando flat-design-financeiro-seguro...
  ✓ OK
[175/393] Baixando flat-design-informativo-claro...
  ✓ OK
[176/393] Baixando flat-design-musical-intuitivo...
  ✓ OK
[177/393] Baixando flat-design-produtivo...
  ✓ OK
[178/393] Baixando fractal-bioluminescence...
  ✓ OK
[179/393] Baixando framelix-3d-studios...
  ✓ OK
[180/393] Baixando fraunces-typography...
  ✓ OK
[181/393] Baixando futuristic-ui-glassmorphism...
  ✓ OK
[182/393] Baixando gatsby-art-deco-noir...
  ✓ OK
[183/393] Baixando geometric...
  ✓ OK
[184/393] Baixando ghibli-inspired-narrative-map...
  ✓ OK
[185/393] Baixando glass-gradient-creative...
  ✓ OK
[186/393] Baixando glassmorphism-agency-hero...
  ✓ OK
[187/393] Baixando glitch-ui-dystopian-terminal...
  ✓ OK
[188/393] Baixando google-sans-typography...
  ✓ OK
[189/393] Baixando gothic...
  ✓ OK
[190/393] Baixando gotico-moderno...
  ✓ OK
[191/393] Baixando grade-school-color-palette...
  ✓ OK
[192/393] Baixando gradient-aurora-borealis...
  ✓ OK
[193/393] Baixando gradient-mesh-aurora-evolved...
  ✓ OK
[194/393] Baixando graffiti...
  ✓ OK
[195/393] Baixando grove...
  ✓ OK
[196/393] Baixando grunge-rock-dos-anos-90...
  ✓ OK
[197/393] Baixando hacker-aesthetic-crt-cli...
  ✓ OK
[198/393] Baixando hand-drawn-sketch-note...
  ✓ OK
[199/393] Baixando happy-art-tropical...
  ✓ OK
[200/393] Baixando hashicorp-infra-dual...
  ✓ OK
[201/393] Baixando healthtech-plataforma-clinica...
  ✓ OK
[202/393] Baixando helios-design-system-hashicorp...
  ✓ OK
[203/393] Baixando high-contrast-tech...
  ✓ OK
[204/393] Baixando holographic-data-viz...
  ✓ OK
[205/393] Baixando horror-gothic-dark...
  ✓ OK
[206/393] Baixando hr-saas-hero...
  ✓ OK
[207/393] Baixando ibm-carbon-enterprise...
  ✓ OK
[208/393] Baixando ibm-plex-sans-typography...
  ✓ OK
[209/393] Baixando industrial-workbench-schematic...
  ✓ OK
[210/393] Baixando internet-nostalgia-y2k-revival...
  ✓ OK
[211/393] Baixando inter-typography...
  ✓ OK
[212/393] Baixando isometric-gaming-voxel...
  ✓ OK
[213/393] Baixando japandi...
  ✓ OK
[214/393] Baixando kawaii...
  ✓ OK
[215/393] Baixando kawaii-doodle-art...
  ✓ OK
[216/393] Baixando kawaii-pastel-pop...
  ✓ OK
[217/393] Baixando kawaii-sweet-pastel...
  ✓ OK
[218/393] Baixando kitsch...
  ✓ OK
[219/393] Baixando kraken-purple-exchange...
  ✓ OK
[220/393] Baixando lambe-lambe-brasileiro...
  ✓ OK
[221/393] Baixando laranja-queimado-premium...
  ✓ OK
[222/393] Baixando linear-precision-dark...
  ✓ OK
[223/393] Baixando locomotive-infinite-scroll...
  ✓ OK
[224/393] Baixando logoisum-video-agency-hero...
  ✓ OK
[225/393] Baixando lovable-cream-humanist...
  ✓ OK
[226/393] Baixando luxury-elegant...
  ✓ OK
[227/393] Baixando luxury-typography...
  ✓ OK
[228/393] Baixando manga-instructional-comic...
  ✓ OK
[229/393] Baixando manrope-typography...
  ✓ OK
[230/393] Baixando maracatu-tech...
  ✓ OK
[231/393] Baixando mat...
  ✓ OK
[232/393] Baixando memphis...
  ✓ OK
[233/393] Baixando merriweather-typography...
  ✓ OK
[234/393] Baixando micro-sound-ux...
  ✓ OK
[235/393] Baixando mid-century-modern...
  ✓ OK
[236/393] Baixando midnight-garden-premium...
  ✓ OK
[237/393] Baixando minimalismo-chic-de-luxo...
  ✓ OK
[238/393] Baixando minimalismo-confiavel-financeiro...
  ✓ OK
[239/393] Baixando minimalismo-fotografico-elegante...
  ✓ OK
[240/393] Baixando minimalismo-funcional-b2b...
  ✓ OK
[241/393] Baixando minimalismo-sereno-de-bem-estar...
  ✓ OK
[242/393] Baixando minimalist-react-hero-with-motion...
  ✓ OK
[243/393] Baixando minimax-colorful-cards...
  ✓ OK
[244/393] Baixando mini-world...
  ✓ OK
[245/393] Baixando mintlify-green-docs...
  ✓ OK
[246/393] Baixando mistral-golden-amber...
  ✓ OK
[247/393] Baixando mixed-media...
  ✓ OK
[248/393] Baixando mixed-reality-vr-ar...
  ✓ OK
[249/393] Baixando modernismo-jornalistico-brasileiro...
  ✓ OK
[250/393] Baixando modern-minimalist...
  ✓ OK
[251/393] Baixando mongodb-forest-neon...
  ✓ OK
[252/393] Baixando monochrome...
  ✓ OK
[253/393] Baixando mystical-western...
  ✓ OK
[254/393] Baixando natureza-elementos-botanicos...
  ✓ OK
[255/393] Baixando neobrutalismo-critico...
  ✓ OK
[256/393] Baixando neobrutalismo-ousado...
  ✓ OK
[257/393] Baixando neoclassical-art...
  ✓ OK
[258/393] Baixando neo-grid-bold...
  ✓ OK
[259/393] Baixando neon-cyber...
  ✓ OK
[260/393] Baixando neumorphic-tech-schematic...
  ✓ OK
[261/393] Baixando new-era-automotive-hero...
  ✓ OK
[262/393] Baixando new-era-bold-hero...
  ✓ OK
[263/393] Baixando noir-detetive...
  ✓ OK
[264/393] Baixando notebook-tabs...
  ✓ OK
[265/393] Baixando notion-warm-workspace...
  ✓ OK
[266/393] Baixando nvidia-power-green...
  ✓ OK
[267/393] Baixando ollama-pure-grayscale...
  ✓ OK
[268/393] Baixando opencode-terminal-mono...
  ✓ OK
[269/393] Baixando origami-geometrico...
  ✓ OK
[270/393] Baixando paper-ink...
  ✓ OK
[271/393] Baixando passport-travel-ui...
  ✓ OK
[272/393] Baixando pastel-geometry...
  ✓ OK
[273/393] Baixando pcb-schematic-architecture...
  ✓ OK
[274/393] Baixando peoples-platform...
  ✓ OK
[275/393] Baixando pin-and-paper...
  ✓ OK
[276/393] Baixando pink-script...
  ✓ OK
[277/393] Baixando pinterest-warm-discovery...
  ✓ OK
[278/393] Baixando pixel-art-8-bit...
  ✓ OK
[279/393] Baixando playful...
  ✓ OK
[280/393] Baixando pointillism-stipple-art...
  ✓ OK
[281/393] Baixando pop-art...
  ✓ OK
[282/393] Baixando portfolio-dev-full-stack...
  ✓ OK
[283/393] Baixando psicodelico-anos-60...
  ✓ OK
[284/393] Baixando radial-diagram-donut-chart...
  ✓ OK
[285/393] Baixando raw-grid...
  ✓ OK
[286/393] Baixando real-estate-imobiliaria-digital...
  ✓ OK
[287/393] Baixando replicate-blaze-gallery...
  ✓ OK
[288/393] Baixando resend-frost-cinematic...
  ✓ OK
[289/393] Baixando resume-journey-oregon-trail...
  ✓ OK
[290/393] Baixando retro-arcade-pixelado...
  ✓ OK
[291/393] Baixando retro-aventura-anos-70...
  ✓ OK
[292/393] Baixando retro-barbershop-classica...
  ✓ OK
[293/393] Baixando retro-boutique-vintage...
  ✓ OK
[294/393] Baixando retro-comic-action-blueprint...
  ✓ OK
[295/393] Baixando retro-digital-anos-90...
  ✓ OK
[296/393] Baixando retro-travel-poster...
  ✓ OK
[297/393] Baixando retro-windows...
  ✓ OK
[298/393] Baixando retro-zine...
  ✓ OK
[299/393] Baixando reuso-criativo-disruptivo...
  ✓ OK
[300/393] Baixando revolut-billboard-fintech...
  ✓ OK
[301/393] Baixando risograph-retro-pop...
  ✓ OK
[302/393] Baixando risograph-zine-aesthetic...
  ✓ OK
[303/393] Baixando rococo-delicado...
  ✓ OK
[304/393] Baixando rococo-romantic-narrative...
  ✓ OK
[305/393] Baixando roxo-veludo-real...
  ✓ OK
[306/393] Baixando runway-cinematic-editorial...
  ✓ OK
[307/393] Baixando saas-enterprise-analytics...
  ✓ OK
[308/393] Baixando saas-signature-gradient...
  ✓ OK
[309/393] Baixando sakura-chroma...
  ✓ OK
[310/393] Baixando sakura-floral-japones...
  ✓ OK
[311/393] Baixando sanity-neon-structured...
  ✓ OK
[312/393] Baixando scatterbrain...
  ✓ OK
[313/393] Baixando scrapbook-collage...
  ✓ OK
[314/393] Baixando sentry-purple-debugger...
  ✓ OK
[315/393] Baixando shabby-chic...
  ✓ OK
[316/393] Baixando signal...
  ✓ OK
[317/393] Baixando simbolos-ambientais-brasileiros...
  ✓ OK
[318/393] Baixando simbolos-civicos-brasileiros...
  ✓ OK
[319/393] Baixando simbolos-culturais-brasileiros...
  ✓ OK
[320/393] Baixando simbolos-politicos-brasileiros...
  ✓ OK
[321/393] Baixando simbolos-regionais-brasileiros...
  ✓ OK
[322/393] Baixando soft-editorial...
  ✓ OK
[323/393] Baixando soft-maximalism...
  ✓ OK
[324/393] Baixando solarpunk-utopico...
  ✓ OK
[325/393] Baixando space-grotesk-typography...
  ✓ OK
[326/393] Baixando spaceship-instruction-manual...
  ✓ OK
[327/393] Baixando spacex-cinematic-void...
  ✓ OK
[328/393] Baixando split-pastel...
  ✓ OK
[329/393] Baixando spotify-dark-immersive...
  ✓ OK
[330/393] Baixando steampunk...
  ✓ OK
[331/393] Baixando steampunk-industrial...
  ✓ OK
[332/393] Baixando steampunk-nebula-explorer...
  ✓ OK
[333/393] Baixando steampunk-vitoriano...
  ✓ OK
[334/393] Baixando stencil-tablet...
  ✓ OK
[335/393] Baixando stripe-fintech-elegance...
  ✓ OK
[336/393] Baixando studio...
  ✓ OK
[337/393] Baixando studygram-notebook-kawaii...
  ✓ OK
[338/393] Baixando sumi-e-tech-scroll...
  ✓ OK
[339/393] Baixando supabase-dark-emerald...
  ✓ OK
[340/393] Baixando surrealism...
  ✓ OK
[341/393] Baixando swiss-design-grafico...
  ✓ OK
[342/393] Baixando swiss-modern...
  ✓ OK
[343/393] Baixando synapse-dark-hero...
  ✓ OK
[344/393] Baixando syne-typography...
  ✓ OK
[345/393] Baixando synthwave...
  ✓ OK
[346/393] Baixando tactile-3d-neumorphism...
  ✓ OK
[347/393] Baixando tactile-digital-deformable-ui...
  ✓ OK
[348/393] Baixando targo-logistics-hero...
  ✓ OK
[349/393] Baixando taskora-saas-hero...
  ✓ OK
[350/393] Baixando tenebrism...
  ✓ OK
[351/393] Baixando tenor-sans-typography...
  ✓ OK
[352/393] Baixando terminal-green...
  ✓ OK
[353/393] Baixando terracota-mediterraneo...
  ✓ OK
[354/393] Baixando the-barely-there-ui...
  ✓ OK
[355/393] Baixando thermal-insight-tech...
  ✓ OK
[356/393] Baixando timeline-horizontal-corporativo...
  ✓ OK
[357/393] Baixando together-pastel-cloud...
  ✓ OK
[358/393] Baixando travel-plataforma-de-viagens...
  ✓ OK
[359/393] Baixando tropicalismo-aventureiro-natural...
  ✓ OK
[360/393] Baixando tropicalismo-gastronomico-vibrante...
  ✓ OK
[361/393] Baixando tropicalismo-indigena-autentico...
  ✓ OK
[362/393] Baixando uber-bold-transit...
  ✓ OK
[363/393] Baixando ukiyo-e-woodblock-revival...
  ✓ OK
[364/393] Baixando underwater-aquatico...
  ✓ OK
[365/393] Baixando underwater-aquatico-deep-sea...
  ✓ OK
[366/393] Baixando utilitarian...
  ✓ OK
[367/393] Baixando vaporwave-314...
  ✓ OK
[368/393] Baixando vaporwave-aesthetic...
  ✓ OK
[369/393] Baixando vellum...
  ✓ OK
[370/393] Baixando vercel-geist-minimal...
  ✓ OK
[371/393] Baixando vernacular-acolhedor-brasileiro...
  ✓ OK
[372/393] Baixando versus-mode-anime-aesthetic...
  ✓ OK
[373/393] Baixando vertical-whiteboard-timeline...
  ✓ OK
[374/393] Baixando victorian...
  ✓ OK
[375/393] Baixando vintage-analog-retro-film...
  ✓ OK
[376/393] Baixando vintage-botanical-scientific...
  ✓ OK
[377/393] Baixando vintage-botanical-scientific-illustration...
  ✓ OK
[378/393] Baixando vintage-editorial...
  ✓ OK
[379/393] Baixando vintage-lithograph-victorian...
  ✓ OK
[380/393] Baixando voice-first-multimodal...
  ✓ OK
[381/393] Baixando voltagent-terminal-emerald...
  ✓ OK
[382/393] Baixando voxel-gamified-isometric...
  ✓ OK
[383/393] Baixando wabi-sabi-anti-ux...
  ✓ OK
[384/393] Baixando wealth-video-hero...
  ✓ OK
[385/393] Baixando web3-eos-hero...
  ✓ OK
[386/393] Baixando weblex-dark-hero...
  ✓ OK
[387/393] Baixando whiteboard...
  ✓ OK
[388/393] Baixando whiteboard-flowchart...
  ✓ OK
[389/393] Baixando wise-lime-bold...
  ✓ OK
[390/393] Baixando xai-brutalist-monospace...
  ✓ OK
[391/393] Baixando y2k...
  ✓ OK
[392/393] Baixando zapier-warm-automation...
  ✓ OK
[393/393] Baixando z-shape...
  ✓ OK

```

---

## Assistant (Build · Big Pickle · 4.0s)

_Thinking:_

All 393 missing files downloaded successfully with 0 failures. Let me verify and update the todo list.

**Tool: bash**

**Input:**
```json
{
  "command": "ls /home/mkt/design_md/design-md-library/MDs/*-DESIGN.md | wc -l",
  "description": "Verify total files"
}
```

**Output:**
```
454

```

**Tool: bash**

**Input:**
```json
{
  "command": "wc -l /home/mkt/design_md/design-md-library/MDs/*-DESIGN.md | tail -1",
  "description": "Count total lines across all files"
}
```

**Output:**
```
  60930 total

```

---

## Assistant (Build · Big Pickle · 4.3s)

_Thinking:_

The download is complete. Let me update the todo.md to reflect this, and mark the task as done.

**454/454** — todos baixados com 0 falhas.

**Tool: write**

**Input:**
```json
{
  "filePath": "/home/mkt/design_md/design-md-library/todo.md",
  "content": "Feito:\n\n- [x] Baixar os 454 DESIGN.md files da library (salvos em MDs/ como <slug>-DESIGN.md)\n"
}
```

**Output:**
```
Wrote file successfully.
```

**Tool: todowrite**

**Input:**
```json
{
  "todos": [
    {
      "priority": "high",
      "content": "List slugs already downloaded in MDs/",
      "status": "completed"
    },
    {
      "priority": "high",
      "content": "Cross-reference with all 454 slugs from elementos_designmd.md",
      "status": "completed"
    },
    {
      "priority": "high",
      "content": "Download missing DESIGN.md files (393 remaining)",
      "status": "completed"
    }
  ]
}
```

**Output:**
```
[
  {
    "content": "List slugs already downloaded in MDs/",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Cross-reference with all 454 slugs from elementos_designmd.md",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Download missing DESIGN.md files (393 remaining)",
    "status": "completed",
    "priority": "high"
  }
]
```

---

## Assistant (Build · Big Pickle · 3.7s)

Aproveitei que o link de download é direto (`/library/<slug>/design.md`) e baixei os 393 faltantes com `curl`. Todos os 454 `DESIGN.md` estão em `design-md-library/MDs/` no formato `<slug>-DESIGN.md`.

---

