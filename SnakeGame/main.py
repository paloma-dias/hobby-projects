
import pygame
import random

# Inicializa o pygame
pygame.init()

# Define o título da janela do jogo
pygame.display.set_caption("Joguinho da Cobrinha")

# Define as dimensões da janela
largura, altura = 1200, 800
tela = pygame.display.set_mode((largura, altura))

# Cria um objeto para controlar o tempo
relogio = pygame.time.Clock()

# Definição de cores em formato RGB
preta = (0, 0, 0)
branca = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)

# Tamanho do quadrado que representa a cobrinha e a comida
tamanho_quadrado = 20

# Velocidade inicial da cobrinha
velocidade_inicial = 5

# Aumento de velocidade a cada comida
aumento_velocidade = 2

# Velocidade de atualização do jogo
velocidade_atualizacao = velocidade_inicial

# Função para desenhar a comida
def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])

# Função para desenhar a cobrinha
def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])

# Função para gerar uma nova posição para a comida
def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 20.0) * 20.0
    return comida_x, comida_y

# Função para desenhar a pontuação
def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Franklin Gothic", 25)
    texto = fonte.render(f"PONTOS: {pontuacao}", True, vermelho)
    tela.blit(texto, [2, 2])

# Função para selecionar a direção da cobra com base na tecla pressionada
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

# Função principal que roda o jogo
def rodar_jogo():
    while True:
        fim_jogo = False

        # Posição inicial da cobrinha
        x_cobrinha = largura / 2
        y_cobrinha = altura / 2

        velocidade_x = 0
        velocidade_y = 0 

        global tamanho_cobra
        tamanho_cobra = 1
        pixels = []

        comida_x, comida_y = gerar_comida()

        while not fim_jogo:
            tela.fill(preta)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    fim_jogo = True
                elif evento.type == pygame.KEYDOWN:
                    velocidade_x, velocidade_y = selecionar_velocidade(evento.key, velocidade_x, velocidade_y)

            desenhar_comida(tamanho_quadrado, comida_x, comida_y)

            # Checa se a cobra colidiu com a borda da janela
            if x_cobrinha < 0 or x_cobrinha >= largura or y_cobrinha < 0 or y_cobrinha >= altura:
                fim_jogo = True

            x_cobrinha += velocidade_x
            y_cobrinha += velocidade_y

            pixels.append([x_cobrinha, y_cobrinha])
            if len(pixels) > tamanho_cobra:
                del pixels[0]
            
            # Checa se a cobra colidiu com ela mesma
            for pixel in pixels[:-1]:
                if pixel == [x_cobrinha, y_cobrinha]:
                    fim_jogo = True

            desenhar_cobra(tamanho_quadrado, pixels)
            desenhar_pontuacao(tamanho_cobra - 1)

            pygame.display.update()

            # Checa se a cobra comeu a comida
            if x_cobrinha == comida_x and y_cobrinha == comida_y:
                tamanho_cobra += 1
                comida_x, comida_y = gerar_comida()
                global velocidade_atualizacao
                velocidade_atualizacao += aumento_velocidade

            relogio.tick(velocidade_atualizacao)
        else:
            break

    pygame.quit()

# Loop principal para manter a janela aberta
rodar_jogo()