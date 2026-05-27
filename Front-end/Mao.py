import pygame

class Mao:
    def __init__(self, pos_base):
        self.pos_base = pygame.Vector2(pos_base)
        self.pecas = []
        self.espaco = 80

    def adicionar(self, peca):
        self.pecas.append(peca)
        self.reorganizar()

    def remover(self, peca):
        if peca in self.pecas:
            self.pecas.remove(peca)
            self.reorganizar()

    def reorganizar(self):
        x = self.pos_base.x

        for peca in self.pecas:
            destino = (x, self.pos_base.y)
            peca.mover_para(destino)
            x += self.espaco
