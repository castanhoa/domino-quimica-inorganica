import pygame

class Peca:
    def __init__(self, imagem, rect):

        self.imagem = imagem
        self.rect = rect
        self.pos = pygame.Vector2(rect.topleft)
        self.destino = pygame.Vector2(rect.topleft)
        self.velocidade = 0.15

    def atualizar(self):
        self.pos += (self.destino - self.pos) * self.velocidade

    def desenhar(self, tela):
        tela.blit(self.imagem, self.pos)

    def set_posicao(self, pos):
        self.rect.topleft = pos
        self.pos = pygame.Vector2(pos)
        self.destino = pygame.Vector2(pos)

    def mover_para(self, pos):
        self.rect.topleft = pos
        self.destino = pygame.Vector2(pos)

    def get_rect(self):
        return pygame.Rect(self.pos.x, self.pos.y,
                           self.rect.width, self.rect.height)
