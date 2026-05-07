import pygame
from Tela import classeTela

class TelaDeJogo(classeTela):
    def __init__(self):
        super().__init__(1800, 900, "")

        xBotao_Player = 620
        yBotao_Player = 725
        
        self.botao_peca = []

        for i in range(7):
            rect = pygame.Rect(xBotao_Player, yBotao_Player, 70, 140)
            self.botao_peca.append(rect)
            xBotao_Player += 80

    def desenhar(self):
        self.tela.fill((0, 120, 255))

        pecaPlayer = pygame.image.load(r"C:\Users\26.01448-0\Desktop\PecaPlayer.png")
        pecaBot = pygame.image.load(r"C:\Users\26.01448-0\Desktop\PecaBot.png")
        MontePecas = pygame.image.load(r"C:\Users\26.01448-0\Desktop\MontePecas.png")
        mesaJogo = pygame.image.load(r"C:\Users\26.01448-0\Desktop\MesaJogo.jpg")

        pecaPlayer_redimensionada = pygame.transform.scale(pecaPlayer, (70, 140))
        pecaBot_redimensionada = pygame.transform.scale(pecaBot, (50, 100))
        monte_redimensionado = pygame.transform.scale(MontePecas, (150, 200))


        xPecaPlayer = 620
        yPecaPlayer = 725

        xPecaBot = 690
        yPecaBot = 100

        self.tela.blit(monte_redimensionado, (1400, 500))
        self.tela.blit(mesaJogo, (650, 300))

        for i in range(0, 7):
            self.tela.blit(pecaPlayer_redimensionada, (xPecaPlayer, yPecaPlayer))
            xPecaPlayer += 80
        
        for i in range(0, 7):
            self.tela.blit(pecaBot_redimensionada, (xPecaBot, yPecaBot))
            xPecaBot += 60

        
    def tratar_eventos(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            for i, rect in enumerate(self.botao_peca):
                if rect.collidepoint(evento.pos):
                    print(f'Peça {i + 1} clicada!')
        
iniciar = TelaDeJogo()
iniciar.executar()
