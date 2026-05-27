import pygame

class MaoBot:

    def __init__(self, pos_base):
        self.pos_base = pygame.Vector2(pos_base)
        self.pecas = []

    def adicionar(self, peca):
        self.pecas.append(peca)

    def remover(self, peca):
        if peca in self.pecas:
            self.pecas.remove(peca)

    def organizar(self):
        x = self.pos_base.x
        y = self.pos_base.y

        for peca in self.pecas:
            peca.set_posicao((x, y))
            x += 60
