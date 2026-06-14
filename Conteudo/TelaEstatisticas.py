from Acessibilidade import tamanho_fonte, ajustar_cor
from Tela import classeTela
import pygame
import Imagens.CaminhosImagens as imgs_paths


class TelaEstatisticas(classeTela):
    def __init__(self):
        super().__init__()

        self.escala = self.altura / 1080
        self.registrar_rect("botao_Voltar", self.largura // 2 - 100, self.altura // 2 + 175, 200, 50)
        self.registrar_rect("tempo_jogado", self.largura // 2 - 225, self.altura // 2 - 50, 200, 100)
        self.registrar_rect("vitorias", self.largura // 2 + 25, self.altura // 2 - 50, 200, 100)
        
        self._texto_tempo_jogado = "Tempo Jogado:"
        self._texto_vitorias = "Vitórias:"

        self.cor_botao_atual_voltar = [255, 255, 255]
        self.velocidade_animacao = 0.1

        self.fonte = pygame.font.SysFont("roboto", tamanho_fonte(20))
        self.logo = pygame.image.load(imgs_paths.LOGOTIPO_PATH)

        pygame.display.set_icon(self.logo)
    
    def tratar_eventos(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.botao_Voltar.collidepoint(evento.pos):
                self.proxima_tela = "inicio"
                self.rodando = False

    def recriar_fontes(self):
        self.fonte = pygame.font.SysFont("roboto", tamanho_fonte(20))

    def desenhar(self):
        self.tela.fill(ajustar_cor(255, 255, 255))
        mouse_pos = pygame.mouse.get_pos()

        tamanho_faixa = int(self.altura * 0.15)
        y_faixa = int(self.altura * 0)
        
        pygame.draw.rect(self.tela, ajustar_cor(255, 0, 0), (0, y_faixa, self.largura, tamanho_faixa))
        self.tela.blit(self.logo, (50, 175))

        if self.botao_Voltar.collidepoint(mouse_pos):
            cor_alvo_voltar = ajustar_cor(200, 200, 200)
        else:
            cor_alvo_voltar = ajustar_cor(255, 255, 255)

        for i in range(3):
            self.cor_botao_atual_voltar[i] += (cor_alvo_voltar[i] - self.cor_botao_atual_voltar[i]) * self.velocidade_animacao

        cor_botao_voltar = tuple(int(c) for c in self.cor_botao_atual_voltar)

        pygame.draw.rect(self.tela, cor_botao_voltar, self.botao_Voltar, border_radius=8)
        pygame.draw.rect(self.tela, ajustar_cor(128, 128, 128), self.botao_Voltar, 2, border_radius=8)
        pygame.draw.rect(self.tela, ajustar_cor(0, 0, 0), self.tempo_jogado, 2, border_radius=8)
        pygame.draw.rect(self.tela, ajustar_cor(0, 0, 0), self.vitorias, 2, border_radius=8)

        texto_botao_voltar = self.fonte.render("Voltar", True, ajustar_cor(0, 0, 0))
        
        self.tela.blit(texto_botao_voltar, texto_botao_voltar.get_rect(center=self.botao_Voltar.center))
        self.tela.blit(self.fonte.render(self._texto_tempo_jogado, True, ajustar_cor(0, 0, 0)), self.tempo_jogado.move(25, 10))
        self.tela.blit(self.fonte.render(self._texto_vitorias, True, ajustar_cor(0, 0, 0)), self.vitorias.move(60, 10))
