import pygame

class Mesa:
    def __init__(self, centro, espaco):

        self.centro = pygame.Vector2(centro)
        self.pecas = []

        self.espaco = espaco
        self.direcao = pygame.Vector2(1, 0)

    def adicionar_peca(self, peca, extremidade):

        if len(self.pecas) == 0:
            peca.mover_para(self.centro)
            self.pecas.append(peca)
            return

        ultima = self.pecas[extremidade]

        nova_pos = pygame.Vector2(ultima.destino) + self.direcao * self.espaco
        if extremidade  == -1:
            nova_pos *= -1

        peca.mover_para(nova_pos)

        self.pecas.insert((len(self.self.pecas) if extremidade == -1 else extremidade), peca)

        self._ajustar_direcao()

    def _ajustar_direcao(self):

        if len(self.pecas) % 6 == 0:
            self.direcao = pygame.Vector2(0, 1)
        elif len(self.pecas) % 12 == 0:
            self.direcao = pygame.Vector2(-1, 0)

    def desenhar(self, tela):

        for peca in self.pecas:
            peca.desenhar(tela)
