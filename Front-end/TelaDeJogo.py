import pygame
from Tela import classeTela

class TelaDeJogo(classeTela):
    def __init__(self):
        super().__init__(1800, 900, "")

        self.botao_peca = []

        self.registrar_rect("botao_monte", 1380, 500, 148, 250)

        x = 680
        y = 725

        for i in range(7):
            nome = f"botao_peca_{i}"
            self.registrar_rect(nome, x, y, 70, 140)
            self.botao_peca.append(getattr(self, nome))
            x += 80
        
        self.pecaPlayer = pygame.image.load(r"C:\Users\26.01448-0\Desktop\PecaPlayer.png")
        self.pecaBot = pygame.image.load(r"C:\Users\26.01448-0\Desktop\PecaBot.png")
        self.MontePecas = pygame.image.load(r"C:\Users\26.01448-0\Desktop\MontePeca.png")
        self.logo = pygame.image.load(r"C:\Users\26.01448-0\Desktop\Logotipo.png")
        self.transparente = pygame.image.load(r"C:\Users\26.01448-0\Desktop\Transparente.png")

        pygame.display.set_icon(self.transparente)

    def desenhar(self):
        self.tela.fill((255, 255, 255))

        largura = self.tela.get_width()
        altura = self.tela.get_height()

        tamanho_faixa = int(altura * 0.15)
        y_faixa = int(altura * 0)
        
        pygame.draw.rect(self.tela,(255, 0, 0),(0, y_faixa, largura, tamanho_faixa))

        pecaPlayer_redimensionada = pygame.transform.scale(self.pecaPlayer, (70, 140))
        pecaBot_redimensionada = pygame.transform.scale(self.pecaBot, (50, 100))
        monte_redimensionado = pygame.transform.scale(self.MontePecas, (150, 200))

        xPecaBot = int(largura * 0.4)
        yPecaBot = int(altura * 0.18)

        self.tela.blit(monte_redimensionado, self.botao_monte.topleft)
        self.tela.blit(self.logo, (50, 150))

        for rect in self.botao_peca:
            self.tela.blit(pecaPlayer_redimensionada, rect.topleft)
        
        for i in range(7):
            self.tela.blit(pecaBot_redimensionada, (xPecaBot, yPecaBot))
            xPecaBot += int(largura * 0.03)
        
    def tratar_eventos(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:

            if self.botao_monte.collidepoint(evento.pos):
                print("Monte clicado!")

            for i, rect in enumerate(self.botao_peca):
                if rect.collidepoint(evento.pos):
                    print(f'Peça {i + 1} clicada!')
        
iniciar = TelaDeJogo()
iniciar.executar()
