from Conteudo.Acessibilidade import tamanho_fonte, ajustar_cor
from Conteudo.Tela import classeTela

from Conteudo.Imagens import CaminhosImagens as images_paths

import pygame

class TelaFimDeJogo(classeTela):
    def __init__(self, objUsuario, vitoria, correcoes_string):
        super().__init__(objUsuario=objUsuario)

        self.vitoria = vitoria
        self.correcoes_string = correcoes_string

        self.registrar_rect("botao_Voltar", self.largura // 2 - 100, self.altura // 2 + 225, 200, 50)
        self.registrar_rect("tempo_jogado", self.largura // 2 - 125, self.altura // 2 - 50, 250, 100)

        self.cor_botao_atual_voltar = [255, 255, 255]
        self.velocidade_animacao = 0.1
        
        self.fonte = pygame.font.SysFont("roboto", tamanho_fonte(20))
        self.titulo_Fonte = pygame.font.SysFont("roboto", tamanho_fonte(32))
        self.logo = pygame.image.load(images_paths.LOGOTIPO_PATH)

        pygame.display.set_icon(self.logo)
    
    def tratar_eventos(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.botao_Voltar.collidepoint(evento.pos):
                self.proxima_tela = "inicio"
                self.rodando = False
                
    def recriar_fontes(self):
        self.fonte = pygame.font.SysFont("roboto", tamanho_fonte(20))
        self.titulo_Fonte = pygame.font.SysFont("roboto", tamanho_fonte(32))

    def desenhar(self, vitoria:bool, string_correcoes_erros:str):

        self.vitoria = vitoria

        self.tela.fill(ajustar_cor(255, 255, 255))
        self.tela.blit(self.logo, (50, 175))
        mouse_pos = pygame.mouse.get_pos()

        # Faixa vermelha
        tamanho_faixa = int(self.altura * 0.15)
        y_faixa = int(self.altura * 0)
        pygame.draw.rect(self.tela, ajustar_cor(255, 0, 0), (0, y_faixa, self.largura, tamanho_faixa))

        #Mensagem de vitória ou derrota
        if self.vitoria:
            texto_vitoria = self.titulo_Fonte.render("Parabéns, você venceu a partida!", True, ajustar_cor(0, 128, 0))
            rect_vitoria = texto_vitoria.get_rect(center=(self.largura // 2, int(self.altura * 0.35)))
            self.tela.blit(texto_vitoria, rect_vitoria)

        else:
            texto_derrota = self.titulo_Fonte.render("Que pena, você perdeu a partida!", True, ajustar_cor(255, 0, 0))
            rect_derrota = texto_derrota.get_rect(center=(self.largura // 2, int(self.altura * 0.35)))
            self.tela.blit(texto_derrota, rect_derrota)


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

        texto_tempo_jogado = self.fonte.render("Tempo da partida:", True, ajustar_cor(0, 0, 0))
        texto_botao_voltar = self.fonte.render("Voltar", True, ajustar_cor(0, 0, 0))
        self.tela.blit(texto_botao_voltar, texto_botao_voltar.get_rect(center=self.botao_Voltar.center))
        self.tela.blit(texto_tempo_jogado, texto_tempo_jogado.get_rect(top=self.tempo_jogado.top + 10, centerx=self.tempo_jogado.centerx))