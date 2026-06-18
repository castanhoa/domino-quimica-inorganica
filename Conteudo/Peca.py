import pygame
from Conteudo.Domino import Pedra

def calcular_tamanho_fonte(texto:str):
    length = len(texto)

    tamanho = int(20 * 4/max(1, length))

    return max(14, min(tamanho, 20))

class Peca:
    def __init__(self, imagem, rect, referenciaBackend, publica:bool=True):

        self.imagem = imagem
        self.rect = rect
        self.pos = pygame.Vector2(rect.topleft)
        self.destino = pygame.Vector2(rect.topleft)
        self.referenciaBackend = referenciaBackend

        self.texto_cima = f"0: {referenciaBackend.valor_0}" if publica else ""
        self.texto_baixo = f"1: {referenciaBackend.valor_1}" if publica else ""

        self.angulo_fator = 0

        self.angulo = 180
        self.velocidade = 0.15

        fonte_cima = pygame.font.SysFont("roboto", calcular_tamanho_fonte(self.texto_cima))
        fonte_baixo = pygame.font.SysFont("roboto", calcular_tamanho_fonte(self.texto_baixo))
        # Renderiza os textos apenas uma vez

        self.txt_cima = fonte_cima.render(self.texto_cima, True, (0, 0, 0))
        self.txt_baixo = fonte_baixo.render(self.texto_baixo, True, (0, 0, 0))

        self.txt_cima_rot = pygame.transform.rotate(self.txt_cima, self.angulo)
        self.txt_baixo_rot = pygame.transform.rotate(self.txt_baixo, self.angulo)


    def __eq__(self, value):

        if not isinstance(value, Peca) and not isinstance(value, Pedra):
            return False
        
        if isinstance(value, Pedra) and self.referenciaBackend.ver_igualdade(value):
            return True

        elif isinstance(value, Peca) and self.referenciaBackend.ver_igualdade(value.referenciaBackend):
            return True

        return False

    def atualizar(self):
        self.pos += (self.destino - self.pos) * self.velocidade

    def desenhar(self, tela):
        rect_atual = pygame.Rect(
            int(self.pos.x),
            int(self.pos.y),
            self.rect.width,
            self.rect.height
        )

        imagem = pygame.transform.rotate(self.imagem, self.angulo)
        rect_img = imagem.get_rect(center=rect_atual.center)

        tela.blit(imagem, rect_img)

        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)

        rect_rotacionado = imagem_rotacionada.get_rect(center=rect_atual.center)

        tela.blit(imagem_rotacionada, rect_rotacionado)

        if self.angulo % 180 == 0:
            pos_cima = (rect_img.centerx, rect_img.y + rect_img.height // 4)
            pos_baixo = (rect_img.centerx, rect_img.y + 3 * rect_img.height // 4)

        else:
            pos_cima = (rect_img.x + rect_img.width // 4, rect_img.centery)
            pos_baixo = (rect_img.x + 3 * rect_img.width // 4, rect_img.centery)

        tela.blit(
            self.txt_cima,
            self.txt_cima.get_rect(center=pos_cima)
        )

        tela.blit(
            self.txt_baixo,
            self.txt_baixo.get_rect(center=pos_baixo)
        )

    def set_posicao(self, pos):
        self.rect.topleft = pos
        self.pos = pygame.Vector2(pos)
        self.destino = pygame.Vector2(pos)

    def mover_para(self, pos):
        self.rect.topleft = pos
        self.destino = pygame.Vector2(pos)

    def set_angulo(self, angulo):
        self.angulo = angulo + self.angulo_fator

    def get_rect(self):
        return pygame.Rect(
            int(self.pos.x),
            int(self.pos.y),
            self.rect.width,
            self.rect.height
        )