import pygame

class Mesa:
    def __init__(self, centro, escala):

        self.centro = pygame.Vector2(centro)
        self.pecas = []

        self.escala = escala

        self.direcao = pygame.Vector2(1, 0)
        self.angulo_pecas = 90

    def adicionar_peca(self, peca, extremidade):

        if len(self.pecas) == 0:
            peca.mover_para(self.centro)
            peca.set_angulo(self.angulo_pecas)
            self.pecas.append(peca)
            return

        ultima = self.pecas[extremidade]

        ultima_rect = ultima.get_rect()

        espaco = 35

        if ultima.angulo != self.angulo_pecas:
            espaco -= ultima_rect.width + 5

        espaco += ultima_rect.height

        espaco *= self.escala


        nova_pos = pygame.Vector2(ultima.destino) + self.direcao * espaco * (-1 if extremidade == -1 else 1)

        peca.mover_para(nova_pos)
        peca.set_angulo(self.angulo_pecas)

        self.pecas.insert((len(self.pecas) if extremidade == -1 else extremidade), peca)

        self._ajustar_direcao()

    def _ajustar_direcao(self):

        length_pecas = len(self.pecas)

        if length_pecas % 7 == 0:
            self.direcao = pygame.Vector2(0, 1)
            self.angulo_pecas = 180

        elif length_pecas % 9 == 0:
            self.direcao = pygame.Vector2(-1, 0)
            self.angulo_pecas = 90
        
        elif length_pecas % 16 == 0:
            self.direcao = pygame.Vector2(0, 1)
            self.angulo_pecas = 180

        
        elif length_pecas % 18 == 0:
            self.direcao = pygame.Vector2(1, 0)
            self.angulo_pecas = 90

    def desenhar(self, tela):

        for peca in self.pecas:
            peca.desenhar(tela)
