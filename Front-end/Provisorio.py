import pygame
from classeTela import Tela

class TelaLogin():
    def __init__(self):
        super().__init__()

        # seus botões prontos
        self.botao_Entrar = pygame.Rect(300, 450, 200, 50)

        self.fonte = pygame.font.SysFont("arial", 20)

    def desenhar(self):
        self.tela.fill((0, 120, 255))

        # legenda
        texto = self.fonte.render("Escolha uma opção:", True, (255,255,255))
        self.tela.blit(texto, (50, 50))

        # desenhar botões
        self.botao_Entrar.desenhar(self.tela)

        # detectar clique
        mouse = pygame.mouse.get_pos()
        clique = pygame.mouse.get_pressed()[0]

        if self.botao_Entrar.foi_clicado(mouse, clique):
            print("Jogar")
