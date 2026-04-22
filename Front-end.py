import pygame
import pygame_gui
# Inicialização
pygame.init()
# Configuração da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Primeiro front end")
# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

# Cor de fundo (Preto)
tela.fill((0, 0, 0))
# --- Desenhe seus botões/textos aqui ---
# Atualiza a tela
pygame.display.flip()
pygame.quit()