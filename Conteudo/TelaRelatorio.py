from Conteudo.Acessibilidade import tamanho_fonte, ajustar_cor
from Conteudo.Tela import classeTela
import pygame
import matplotlib.pyplot as plt
import numpy as np
import Conteudo.Imagens.CaminhosImagens as imgs_paths


class TelaRelatorio(classeTela):
    def __init__(self, objUsuario):
        super().__init__(objUsuario=objUsuario)

        self.registrar_rect("botao_GerarRelatorio", self.largura // 2 - 100, self.altura // 2 + 50, 200, 50)
        self.registrar_rect("botao_Voltar", self.largura // 2 - 100, self.altura // 2 + 125, 200, 50)

        self.cor_botao_atual_gerar = [255, 255, 255]
        self.cor_botao_atual_voltar = [255, 255, 255]
        self.velocidade_animacao = 0.1
        
        self.fonte = pygame.font.SysFont("roboto", tamanho_fonte(20))
        self.logo = pygame.image.load(imgs_paths.LOGOTIPO_PATH)

        pygame.display.set_icon(self.logo)
    
    def tratar_eventos(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.botao_GerarRelatorio.collidepoint(evento.pos):
                
                dados = np.array([25, 35, 20, 20])
                destaque = [0.1, 0, 0, 0] 
                fig, ax = plt.subplots(figsize=(5, 5))
                ax.pie(dados, autopct='%1.1f%%', startangle=90, explode=destaque, shadow=True, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
                ax.set_title('Gráfico de pizza (exemplo)')

                plt.show()

                
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

        if self.botao_GerarRelatorio.collidepoint(mouse_pos):
            cor_alvo_gerar = ajustar_cor(200, 200, 200)
        else:
            cor_alvo_gerar = ajustar_cor(255, 255, 255)

        if self.botao_Voltar.collidepoint(mouse_pos):
            cor_alvo_voltar = ajustar_cor(200, 200, 200)
        else:
            cor_alvo_voltar = ajustar_cor(255, 255, 255)

        for i in range(3):
            self.cor_botao_atual_gerar[i] += (cor_alvo_gerar[i] - self.cor_botao_atual_gerar[i]) * self.velocidade_animacao

        for i in range(3):
            self.cor_botao_atual_voltar[i] += (cor_alvo_voltar[i] - self.cor_botao_atual_voltar[i]) * self.velocidade_animacao

        cor_botao_gerar = tuple(int(c) for c in self.cor_botao_atual_gerar)
        cor_botao_voltar = tuple(int(c) for c in self.cor_botao_atual_voltar)

        pygame.draw.rect(self.tela, cor_botao_gerar, self.botao_GerarRelatorio, border_radius=8)
        pygame.draw.rect(self.tela, ajustar_cor(128, 128, 128), self.botao_GerarRelatorio, 2, border_radius=8)

        pygame.draw.rect(self.tela, cor_botao_voltar, self.botao_Voltar, border_radius=8)
        pygame.draw.rect(self.tela, ajustar_cor(128, 128, 128), self.botao_Voltar, 2, border_radius=8)

        texto_botao = self.fonte.render("Gerar Relatório", True, (0, 0, 0))
        self.tela.blit(texto_botao, texto_botao.get_rect(center=self.botao_GerarRelatorio.center))

        texto_botao_voltar = self.fonte.render("Voltar", True, (0, 0, 0))
        self.tela.blit(texto_botao_voltar, texto_botao_voltar.get_rect(center=self.botao_Voltar.center))
