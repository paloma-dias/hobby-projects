import pygame
import random
import math  # Adicione esta importação

# Inicializa o pygame
pygame.init()

# Define o título da janela do jogo
pygame.display.set_caption("Jogo do Pac-Man")

# Define as dimensões da janela
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))

# Cria um objeto para controlar o tempo
relogio = pygame.time.Clock()

# Definição de cores em formato RGB
preta = (0, 0, 0)
branca = (255, 255, 255)
amarela = (255, 255, 0)
vermelho = (255, 0, 0)
azul = (0, 0, 255)
verde = (0, 255, 0)

# Tamanho do Pac-Man e dos inimigos
tamanho_quadrado = 20

# Labirinto representado como uma matriz
labirinto = [
    "############################",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#.####.#####.##.#####.####.#",
    "#..........................#",
    "#.####.##.########.##.####.#",
    "#......##....##....##......#",
    "######.##### ## #####.######",
    "######.##          ##.######",
    "######.## ###  ### ##.######",
    "#..........#    #..........#",
    "#.####.##.########.##.####.#",
    "#.####.##.########.##.####.#",
    "#..........................#",
    "############################"
]

# Função para desenhar o labirinto
def desenhar_labirinto(labirinto):
    for y, linha in enumerate(labirinto):
        for x, caractere in enumerate(linha):
            if caractere == "#":
                pygame.draw.rect(tela, azul, [x * tamanho_quadrado, y * tamanho_quadrado, tamanho_quadrado, tamanho_quadrado])
            elif caractere == ".":
                pygame.draw.circle(tela, verde, [x * tamanho_quadrado + tamanho_quadrado // 2, y * tamanho_quadrado + tamanho_quadrado // 2], 5)

# Função para desenhar o Pac-Man com boca
def desenhar_pacman(x, y, angulo_boca):
    centro = (x + tamanho_quadrado // 2, y + tamanho_quadrado // 2)
    raio = tamanho_quadrado // 2
    arco = pygame.Surface((tamanho_quadrado, tamanho_quadrado), pygame.SRCALPHA)
    pygame.draw.arc(arco, amarela, (0, 0, tamanho_quadrado, tamanho_quadrado), angulo_boca, 2 * math.pi - angulo_boca, tamanho_quadrado // 2)
    tela.blit(arco, (x, y))

# Função para desenhar os inimigos
def desenhar_inimigos(inimigos):
    for inimigo in inimigos:
        pygame.draw.rect(tela, vermelho, [inimigo[0], inimigo[1], tamanho_quadrado, tamanho_quadrado])

# Função para gerar inimigos em posições aleatórias válidas
def gerar_inimigos():
    inimigos = []
    for _ in range(4):  # número de inimigos
        while True:
            x = random.randint(0, len(labirinto[0]) - 1) * tamanho_quadrado
            y = random.randint(0, len(labirinto) - 1) * tamanho_quadrado
            if labirinto[y // tamanho_quadrado][x // tamanho_quadrado] != "#":
                inimigos.append([x, y])
                break
    return inimigos

# Função para desenhar a pontuação
def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Franklin Gothic", 25)
    texto = fonte.render(f"PONTOS: {pontuacao}", True, branca)
    tela.blit(texto, [10, 10])

# Função para selecionar a direção do Pac-Man com base na tecla pressionada
def selecionar_velocidade(tecla, velocidade_x, velocidade_y):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0
    return velocidade_x, velocidade_y

# Função para desenhar a tela de "Game Over"
def tela_game_over(pontuacao):
    fonte = pygame.font.SysFont("Franklin Gothic", 40)
    tela.fill(preta)
    texto = fonte.render(f"Game Over! Pontuação: {pontuacao}", True, branca)
    tela.blit(texto, [largura // 4, altura // 2 - 20])
    pygame.display.update()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    return True
                elif evento.key == pygame.K_q:
                    pygame.quit()
                    exit()

# Função para desenhar a tela de vitória
def tela_vitoria():
    fonte = pygame.font.SysFont("Franklin Gothic", 40)
    tela.fill(preta)
    texto = fonte.render("Você ganhou! Parabéns!", True, branca)
    tela.blit(texto, [largura // 4, altura // 2 - 20])
    pygame.display.update()
    pygame.time.wait(2000)

# Função principal que roda o jogo
def rodar_jogo():
    while True:
        # Inicializa as variáveis
        x_pacman = largura // 2
        y_pacman = altura // 2
        velocidade_x = 0
        velocidade_y = 0
        inimigos = gerar_inimigos()
        pontuacao = 0
        comidas_restantes = sum(linha.count(".") for linha in labirinto)

        while True:
            tela.fill(preta)
            desenhar_labirinto(labirinto)
            desenhar_pacman(x_pacman, y_pacman, 0.5)
            desenhar_inimigos(inimigos)
            desenhar_pontuacao(pontuacao)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif evento.type == pygame.KEYDOWN:
                    velocidade_x, velocidade_y = selecionar_velocidade(evento.key, velocidade_x, velocidade_y)

            # Movimento do Pac-Man
            novo_x_pacman = x_pacman + velocidade_x
            novo_y_pacman = y_pacman + velocidade_y

            if labirinto[novo_y_pacman // tamanho_quadrado][novo_x_pacman // tamanho_quadrado] != "#":
                x_pacman = novo_x_pacman
                y_pacman = novo_y_pacman

            # Movimento dos inimigos
            for inimigo in inimigos:
                direcao = random.choice([(0, tamanho_quadrado), (0, -tamanho_quadrado), (tamanho_quadrado, 0), (-tamanho_quadrado, 0)])
                novo_x_inimigo = inimigo[0] + direcao[0]
                novo_y_inimigo = inimigo[1] + direcao[1]

                if labirinto[novo_y_inimigo // tamanho_quadrado][novo_x_inimigo // tamanho_quadrado] != "#":
                    inimigo[0] = novo_x_inimigo
                    inimigo[1] = novo_y_inimigo

            desenhar_inimigos(inimigos)

            # Verifica colisão com os inimigos
            for inimigo in inimigos:
                if x_pacman == inimigo[0] and y_pacman == inimigo[1]:
                    if not tela_game_over(pontuacao):
                        break

            # Verifica se o Pac-Man está em uma posição de comida
            if labirinto[y_pacman // tamanho_quadrado][x_pacman // tamanho_quadrado] == ".":
                pontuacao += 10
                comidas_restantes -= 1
                linha = list(labirinto[y_pacman // tamanho_quadrado])
                linha[x_pacman // tamanho_quadrado] = " "
                labirinto[y_pacman // tamanho_quadrado] = "".join(linha)

            if comidas_restantes == 0:
                tela_vitoria()
                break

            pygame.display.update()
            relogio.tick(10)  # controla a velocidade do jogo

# Loop principal para manter a janela aberta
rodar_jogo()
