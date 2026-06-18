from Conteudo.Acessibilidade import ajustar_cor
from Conteudo.Tela import classeTela
import pygame
import math

class TelaCarregamento(classeTela):
    def __init__(self, duracao:float = 0.5):
        super().__init__()

        self.duracao = duracao
        self.tempo = 0
        self.fonte = pygame.font.SysFont("arial", 40)
        self.angulo = 0

    def desenhar_pontos(self, centro_x, centro_y, raio=30):
        pontos = 8  # quantidade de pontos no círculo

        for i in range(pontos):
            angulo = self.angulo + (2 * math.pi * i / pontos)
            x = centro_x + math.cos(angulo) * raio
            y = centro_y + math.sin(angulo) * raio
            intensidade = int(255 * (i / pontos))
            cor = (intensidade, intensidade, intensidade)

            pygame.draw.circle(self.tela, cor, (int(x), int(y)), 5)


    def executar(self):
        while self.rodando:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.rodando = False

            # fundo
            self.tela.fill(ajustar_cor(255, 255, 255))
            # calcula faixa superior
            tamanho_faixa = int(self.altura * 0.15)
            y_faixa = 0
            # desenha faixa vermelha
            pygame.draw.rect(self.tela, ajustar_cor(255, 0, 0), (0, y_faixa, self.largura, tamanho_faixa))
            # texto central
            texto = self.fonte.render("Carregando...", True, (0, 0, 0))
            texto_rect = texto.get_rect(center=(self.largura // 2, self.altura // 2 - 80))
            self.tela.blit(texto, texto_rect)
            # animação dos pontos
            self.desenhar_pontos(self.largura // 2, self.altura // 2)
            # rotação
            self.angulo += 0.1
            # tempo de execução
            self.tempo += self.clock.get_time() / 1000

            pygame.display.flip()

            if self.tempo >= self.duracao:
                self.rodando = False

    def mostrar_loading():
        loading = TelaCarregamento(duracao = 0.8)
        loading.executar()
