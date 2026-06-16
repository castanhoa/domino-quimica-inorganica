from Conteudo.Acessibilidade import tamanho_fonte, ajustar_cor
from Conteudo.Tela import classeTela
import pygame
import Conteudo.Imagens.CaminhosImagens as imgs_paths


class TelaInicial(classeTela):
    def __init__(self, objUsuario):
        super().__init__(objUsuario=objUsuario)

        self.registrar_rect("botao_Iniciar", self.largura // 2 - 100, self.altura // 2 + 25, 200, 50)
        self.registrar_rect("botao_Tela_Relatorio", self.largura // 2 - 100, self.altura // 2 + 100, 200, 50)
        self.registrar_rect("botao_Estatisticas", self.largura // 2 - 100, self.altura // 2 + 175, 200, 50)
        self.registrar_rect("botao_Regras", self.largura // 2 - 100, self.altura // 2 + 250, 200, 50)

        self.cor_botao_normal = ajustar_cor(255, 255, 255)
        self.cor_botao_hover = ajustar_cor(200, 200, 200)

        self.cor_botao_atual_iniciar = [255, 255, 255]
        self.cor_botao_atual_relatorio = [255, 255, 255]
        self.cor_botao_atual_estatisticas = [255, 255, 255]
        self.cor_botao_atual_regras = [255, 255, 255]
        
        self.velocidade_animacao = 0.1

        self.fonte = pygame.font.SysFont("roboto", tamanho_fonte(20))
        self.titulo_Fonte = pygame.font.SysFont("roboto", tamanho_fonte(32))

        self.cursor_visivel = True
        self.cursor_timer = 0

        self.logo = pygame.image.load(imgs_paths.LOGOTIPO_PATH)
        pygame.display.set_icon(self.logo)

    def tratar_eventos(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.botao_Iniciar.collidepoint(evento.pos):
                self.proxima_tela = "jogo"
                self.rodando = False
            
            if self.botao_Tela_Relatorio.collidepoint(evento.pos):
                self.proxima_tela = "relatorio"
                self.rodando = False
            
            if self.botao_Estatisticas.collidepoint(evento.pos):
                self.proxima_tela = "estatisticas"
                self.rodando = False
            
            if self.botao_Regras.collidepoint(evento.pos):
                self.proxima_tela = "regras"
                self.rodando = False

    def recriar_fontes(self):
        self.fonte = pygame.font.SysFont("roboto", tamanho_fonte(20))
        self.titulo_Fonte = pygame.font.SysFont("roboto", tamanho_fonte(32))

    def desenhar(self):
        self.tela.fill(ajustar_cor(255, 255, 255))
        mouse_pos = pygame.mouse.get_pos()

        tamanho_faixa = int(self.altura * 0.15)
        y_faixa = self.altura * 0
        
        pygame.draw.rect(self.tela, ajustar_cor(255, 0, 0), (0, y_faixa, self.largura, tamanho_faixa))
        self.tela.blit(self.logo, (50, 175))

        self.cursor_timer += 1

        if self.cursor_timer >= 30:
            self.cursor_visivel = not self.cursor_visivel
            self.cursor_timer = 0

        if self.botao_Iniciar.collidepoint(mouse_pos):
            cor_alvo_iniciar = ajustar_cor(200, 200, 200)
        else:
            cor_alvo_iniciar = ajustar_cor(255, 255, 255)
        
        if self.botao_Tela_Relatorio.collidepoint(mouse_pos):
            cor_alvo_relatorio = ajustar_cor(200, 200, 200)
        else:
            cor_alvo_relatorio = ajustar_cor(255, 255, 255)
        
        if self.botao_Estatisticas.collidepoint(mouse_pos):
            cor_alvo_estatisticas = ajustar_cor(200, 200, 200)
        else:
            cor_alvo_estatisticas = ajustar_cor(255, 255, 255)

        if self.botao_Regras.collidepoint(mouse_pos):
            cor_alvo_regras = ajustar_cor(200, 200, 200)
        else:
            cor_alvo_regras = ajustar_cor(255, 255, 255)

        for i in range(3):
            self.cor_botao_atual_iniciar[i] += (cor_alvo_iniciar[i] - self.cor_botao_atual_iniciar[i]) * self.velocidade_animacao

        for i in range(3):
            self.cor_botao_atual_relatorio[i] += (cor_alvo_relatorio[i] - self.cor_botao_atual_relatorio[i]) * self.velocidade_animacao
        
        for i in range(3):
            self.cor_botao_atual_estatisticas[i] += (cor_alvo_estatisticas[i] - self.cor_botao_atual_estatisticas[i]) * self.velocidade_animacao
        
        for i in range(3):
            self.cor_botao_atual_regras[i] += (cor_alvo_regras[i] - self.cor_botao_atual_regras[i]) * self.velocidade_animacao

        cor_botao_iniciar = tuple(int(c) for c in self.cor_botao_atual_iniciar)
        cor_botao_relatorio = tuple(int(c) for c in self.cor_botao_atual_relatorio)
        cor_botao_estatisticas = tuple(int(c) for c in self.cor_botao_atual_estatisticas)
        cor_botao_regras = tuple(int(c) for c in self.cor_botao_atual_regras)

        texto_bem_vindo = self.titulo_Fonte.render("Bem-Vindo(a) ao Dominó de Química Inorgânica",
            True, ajustar_cor(0, 0, 0))

        titulo_rect = texto_bem_vindo.get_rect(center=(self.largura // 2, int(self.altura * 0.35)))

        self.tela.blit(texto_bem_vindo, titulo_rect)

        pygame.draw.rect(self.tela, cor_botao_iniciar, self.botao_Iniciar, border_radius=8)
        pygame.draw.rect(self.tela, ajustar_cor(128, 128, 128), self.botao_Iniciar, 2, border_radius=8)

        pygame.draw.rect(self.tela, cor_botao_relatorio, self.botao_Tela_Relatorio, border_radius=8)
        pygame.draw.rect(self.tela, ajustar_cor(128, 128, 128), self.botao_Tela_Relatorio, 2, border_radius=8)

        pygame.draw.rect(self.tela, cor_botao_estatisticas, self.botao_Estatisticas, border_radius=8)
        pygame.draw.rect(self.tela, ajustar_cor(128, 128, 128), self.botao_Estatisticas, 2, border_radius=8)

        pygame.draw.rect(self.tela, cor_botao_regras, self.botao_Regras, border_radius=8)
        pygame.draw.rect(self.tela, ajustar_cor(128, 128, 128), self.botao_Regras, 2, border_radius=8)

        texto_botao = self.fonte.render("Começar partida", True, ajustar_cor(0, 0, 0))
        texto_relatorio = self.fonte.render("Ver relatórios", True, ajustar_cor(0, 0, 0))
        texto_estatisticas = self.fonte.render("Ver estatísticas", True, ajustar_cor(0, 0, 0))
        texto_regras = self.fonte.render("Regras do Jogo", True, ajustar_cor(0, 0, 0))
        
        self.tela.blit(texto_botao, texto_botao.get_rect(center=self.botao_Iniciar.center))
        self.tela.blit(texto_relatorio, texto_relatorio.get_rect(center=self.botao_Tela_Relatorio.center))
        self.tela.blit(texto_estatisticas, texto_estatisticas.get_rect(center=self.botao_Estatisticas.center))
        self.tela.blit(texto_regras, texto_regras.get_rect(center=self.botao_Regras.center))
