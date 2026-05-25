# Skill: Precision DESIGN.md Extractor

## Objetivo
Atuar como um Engenheiro de UI/UX de elite. Sua tarefa é visitar uma URL alvo fornecida pelo usuário e fazer engenharia reversa do design system do site, transformando-o em um arquivo `DESIGN.md` impecável e *pixel-perfect*, seguindo estritamente o padrão do Google Stitch.

## Pré-Requisitos (Pre-Flight)
1. **Aprender o Padrão (Schema):** Antes de iniciar qualquer extração, você DEVE obrigatoriamente usar a ferramenta `view_file` para ler e absorver a estrutura do arquivo de referência localizado em `/Users/fatima/Desktop/awesome_design/design-md/stripe/DESIGN.md` (ou `apple/DESIGN.md`).
2. Preste atenção rigorosa em como as cores (Hex), tipografia, raios de borda (border-radius), sombras e estados interativos são documentados.

## Passos de Execução

### Fase 1: Inspeção Visual e Técnica Profunda
Invoque o `browser_subagent` com a URL alvo. Instrua o subagente a realizar uma auditoria técnica rigorosa do DOM e do CSS (Computed Styles):
- **Cores (Colors):** Extraia os valores exatos em HEX para o fundo (background), texto (primário, secundário, mutado), cores primárias da marca e cores semânticas (sucesso, aviso, erro). Verifique se há variáveis CSS (`--var`).
- **Tipografia (Typography):** Identifique a stack exata de `font-family`. Extraia os pesos (weights - ex: 400, 500, 600) e tamanhos para os títulos (H1-H6) e texto base (body).
- **Elementos e Componentes (UI Elements):** Inspecione botões, inputs e cards. Extraia os valores matemáticos exatos para:
  - `border-radius` (ex: 4px, 8px, pill/9999px)
  - `box-shadow` (sombras de elevação, sombras suaves)
  - Escala de espaçamento (padding e margins padrão)
  - Estados de Hover e Active (transições, mudanças de cor)
- **Layout:** Identifique a largura máxima (max-width) do container principal e a estrutura do grid.

### Fase 2: Síntese e Mapeamento
Traduza o CSS bruto e os dados visuais capturados para a formatação rigorosa do `DESIGN.md`.
- **PROIBIDO ALUCINAR DADOS:** Se um valor não for óbvio visualmente, baseie-se nos estilos computados do CSS.
- **Filosofia do Design:** Escreva uma breve introdução que capture a "vibe" e a filosofia estética da marca (ex: "minimalista de luxo", "brutalista", "corporativo limpo").

### Fase 3: Geração do Arquivo
1. Determine o nome da marca a partir da URL (ex: `netflix`, `spotify`).
2. Use a ferramenta `write_to_file` para criar o novo arquivo exatamente no caminho: `/Users/fatima/Desktop/awesome_design/design-md/<nome_da_marca>/DESIGN.md`.
3. O arquivo gerado DEVE manter a exata hierarquia de Markdown (headings, blocos de código, listas) aprendida na fase de Pré-Requisitos.

## Garantia de Qualidade (QA)
Antes de finalizar a tarefa e retornar ao usuário, verifique internamente:
- Os códigos HEX são reais e foram extraídos do site?
- A tipografia reflete a identidade verdadeira da marca?
- A estrutura do Markdown bate 100% com o padrão Stitch adotado pelos exemplos?
