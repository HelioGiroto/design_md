import os
import re
import time
import random
import webbrowser

try:
    import pyautogui
except ImportError:
    print("Por favor, instale o pyautogui abrindo o terminal e rodando: pip3 install pyautogui")
    exit(1)

# Caminho do arquivo
md_file = 'elementos_designmd.md'
VISITADOS_FILE = 'visitados.txt'

# ==============================================================================
# CONFIGURAÇÃO DE COMO CLICAR NO BOTÃO (ESCOLHA OPÇÃO 1 OU OPÇÃO 2)
# ==============================================================================

# OPÇÃO 1: Coordenadas Fixas da Tela (Mais fácil, rápida e confiável)
# Para descobrir essas coordenadas, coloque o mouse em cima do seu favorito 
# e rode este comando num terminal: python3 -c "import pyautogui; print(pyautogui.position())"
# OPÇÃO 1: Coordenadas Fixas da Tela (desativada — usando imagem)
# BOTAO_X = 350
# BOTAO_Y = 100
USAR_COORDENADAS = False

# OPÇÃO 2: Reconhecimento de Imagem (Requer salvar um print do botão)
# Se USAR_COORDENADAS for False, o script vai procurar essa imagem na tela.
# Para isso, tire um "print" BEM PEQUENO contendo apenas o texto do botão do 
# favorito, salve como "botao_favorito.png" na mesma pasta deste script.
# Obs: É preciso instalar a biblioteca opencv-python para o confidence=0.8 funcionar.
NOME_DA_IMAGEM = 'botao_favorito.png'

# ==============================================================================

# 1. Lê a tabela para extrair as URLs
with open(md_file, 'r') as f:
    lines = f.readlines()

urls = []
for line in lines:
    if line.startswith('|'):
        # Extrai o link da terceira coluna
        match = re.search(r'(https://designmd\.app/(?:en/)?library/[^)]+)', line)
        if match:
            urls.append(match.group(1))

# Carrega URLs já visitadas para retomar de onde parou
visitadas = set()
if os.path.exists(VISITADOS_FILE):
    with open(VISITADOS_FILE, 'r') as f:
        visitadas = set(line.strip() for line in f if line.strip())
    print(f"{len(visitadas)} URLs já processadas (lido de {VISITADOS_FILE}).")

urls_pendentes = [u for u in urls if u not in visitadas]
print(f"Total: {len(urls)} URLs. Pendentes: {len(urls_pendentes)}. Já visitadas: {len(visitadas)}.")
print("AVISO: Deixe o seu navegador visível e na mesma posição.")
print("Iniciando em 5 segundos...")
print()
print("⚠️  BOTÃO DE EMERGÊNCIA DO PYAUTOGUI:")
print("Se o script começar a clicar em coisas erradas ou abrir abas infinitas e você perder")
print("o controle, JOGUE O MOUSE RAPIDAMENTE PARA QUALQUER UM DOS 4 CANTOS DA TELA —")
print("o script abortará imediatamente!")
print()
time.sleep(5)

# 2. Executa o fluxo para cada URL pendente
for i, url in enumerate(urls_pendentes, start=1):
    print(f"\n[{i}/{len(urls_pendentes)}] Abrindo página: {url}")
    
    # Abre a URL em uma nova aba do navegador padrão
    webbrowser.open_new_tab(url)
    
    # Tempo randômico entre 4 e 15 segundos para simular comportamento humano e carregar a página
    tempo_espera = random.randint(4, 15)
    print(f"Aguardando {tempo_espera} segundos para o carregamento...")
    time.sleep(tempo_espera)
    
    # 3. Clica no Bookmarklet
    clicou = False
    if USAR_COORDENADAS:
        # Move o mouse e clica
        pyautogui.moveTo(BOTAO_X, BOTAO_Y, duration=0.5)
        pyautogui.click()
        print(f"Clicado nas coordenadas ({BOTAO_X}, {BOTAO_Y})")
        clicou = True
    else:
        try:
            # Procura a imagem do botão na tela
            posicao = pyautogui.locateCenterOnScreen(NOME_DA_IMAGEM, confidence=0.8)
            if posicao:
                pyautogui.moveTo(posicao.x, posicao.y, duration=0.5)
                pyautogui.click()
                print("Clicado via reconhecimento de imagem!")
                clicou = True
            else:
                print("ERRO: Não encontrei a imagem do botão na tela.")
        except Exception as e:
            print(f"Erro ao procurar a imagem: {e}. (Verifique se instalou o opencv-python)")

    if clicou:
        with open(VISITADOS_FILE, 'a') as f:
            f.write(url + '\n')
        print(f"✓ URL registrada em {VISITADOS_FILE}")

    # Pequena pausa antes de abrir a próxima URL para dar tempo do download iniciar
    time.sleep(2)

print("\nProcesso concluído!")


# UTILIZAÇÃO:
'''
Sim, é totalmente possível e criei exatamente esse script para você! 

Acabei de salvá-lo em: `@[/Users/fatima/Desktop/awesome_design/design-md-library/automacao_bookmarklet.py]`

Sobre a sua dúvida de como o PyAutoGUI reconhece o botão: **Sim, há duas alternativas principais**, e eu deixei ambas preparadas no script para você escolher:

### Alternativa 1: Coordenadas Fixas (Recomendado, Mais Fácil)
O PyAutoGUI não precisa "enxergar" o botão. Se você deixar o navegador em tela cheia e não mexer, a posição do botão na sua tela será sempre a mesma (por exemplo, `X=350, Y=100`). O script simplesmente joga o mouse cegamente nessa coordenada e clica.
No arquivo que criei, deixei essa opção ativada por padrão (`USAR_COORDENADAS = True`). Coloquei no código um comando que você pode usar para descobrir qual é o `X` e `Y` exato do seu mouse.

### Alternativa 2: Reconhecimento de Imagem (Mais Avançado)
Nessa opção (`locateCenterOnScreen`), o PyAutoGUI vai "escanear" a tela do seu computador inteira pixel por pixel caçando uma imagem específica.
**Como funciona:** Você tira um *print* (captura de tela) bem pequenininho apenas do botão do seu favorito e salva como `botao_favorito.png` na mesma pasta do script. O script vai procurar por essa imagem, descobrir onde ela está e clicar. É excelente se você costuma mudar o tamanho da janela, mas é um pouco mais pesado.

### Como usar o Script criado:
1. Abra um terminal.
2. Se não tiver as bibliotecas instaladas, rode: `pip3 install pyautogui opencv-python`
3. Abra o script `automacao_bookmarklet.py`, edite as variáveis `BOTAO_X` e `BOTAO_Y` com os números do seu botão de favorito.
4. Rode: `python3 automacao_bookmarklet.py`

**Dica de Ouro:** O PyAutoGUI tem um "botão de emergência". Se o script começar a clicar em coisas erradas ou abrir abas infinitas e você perder o controle, basta dar um "fio terra": **Jogue o seu mouse rapidamente e bruscamente para qualquer um dos 4 cantos extremos do seu monitor** e o script abortará imediatamente!
'''
