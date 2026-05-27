from Tela import classeTela
from MaoBot import MaoBot
from Mesa import Mesa
from Peca import Peca
from Mao import Mao
import pygame

class TelaDeJogo(classeTela):

    def __init__(self):
        super().__init__()  # SEM MEXER NO VISUAL

        self.botao_peca = []
        self.mao_bot = MaoBot((self.largura // 2 - 275, int(self.altura * 0.18)))
        self.registrar_rect("botao_monte", 1600, 600, 150, 250)

        x = self.largura // 2 - 275
        y = self.altura // 2 + 150

        for i in range(7):
            nome = f"botao_peca_{i}"
            self.registrar_rect(nome, x, y, 70, 140)
            x += 80

        self.tamanho_peca_player = (70, 140)
        self.tamanho_peca_bot = (50, 100)
        self.tamanho_monte = (150, 250)

        # IMAGENS (NÃO ALTERADO)
        self.logo = pygame.image.load(r"C:\Users\26.01448-0\Desktop\Logotipo.png")
        self.pecaPlayer = pygame.transform.scale(
            pygame.image.load(r"C:\Users\26.01448-0\Desktop\PecaPlayer.png"),
            self.tamanho_peca_player
        )
        self.pecaBot = pygame.transform.scale(
            pygame.image.load(r"C:\Users\26.01448-0\Desktop\PecaBot.png"),
            self.tamanho_peca_bot
        )
        self.MontePecas = pygame.transform.scale(
            pygame.image.load(r"C:\Users\26.01448-0\Desktop\MontePeca.png"),
            self.tamanho_monte
        )

        pygame.display.set_icon(self.logo)

        # NOVO SISTEMA (COMPATÍVEL)
        self.mesa = Mesa((self.largura // 2, self.altura // 2))
        self.mao = Mao((self.largura // 2 - 275, self.altura // 2 + 150))

        # CRIA PEÇAS USANDO SEU RECT EXISTENTE
        for i in range(7):

            rect = getattr(self, f"botao_peca_{i}")

            rect.width = self.tamanho_peca_player[0]
            rect.height = self.tamanho_peca_player[1]

            peca = Peca(self.pecaPlayer, rect)

            self.mao.adicionar(peca)

        x = self.largura // 2 - 275
        y = int(self.altura * 0.18)

        for i in range(7):

            rect = pygame.Rect(x, y, 50, 100)

            peca = Peca(self.pecaBot, rect)

            self.mao_bot.adicionar(peca)

            x += 60

    def tratar_eventos(self, evento):

        if evento.type == pygame.MOUSEBUTTONDOWN:

            if self.botao_monte.collidepoint(evento.pos):

                rect = pygame.Rect(1000, 300, 70, 140)

                nova = Peca(self.pecaPlayer, rect)

                self.mao.adicionar(nova)

            for peca in self.mao.pecas:

                if peca.get_rect().collidepoint(evento.pos):

                    self.mao.remover(peca)
                    self.mesa.adicionar_peca(peca)

    def desenhar(self):

        self.tela.fill((255, 255, 255))
        self.mao_bot.organizar()

        pygame.draw.rect(
            self.tela,
            (255, 0, 0),
            (0, 0, self.largura, int(self.altura * 0.15))
        )

        self.tela.blit(self.MontePecas, self.botao_monte.topleft)
        self.tela.blit(self.logo, (50, 175))

        # PEÇAS DA MÃO (COM ANIMAÇÃO)
        for peca in self.mao.pecas:
            peca.atualizar()
            peca.desenhar(self.tela)

        # PEÇAS DA MESA (COM ANIMAÇÃO)
        for peca in self.mesa.pecas:
            peca.atualizar()
            peca.desenhar(self.tela)
        
        for peca in self.mao_bot.pecas:
            peca.desenhar(self.tela)
