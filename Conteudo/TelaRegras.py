from Acessibilidade import tamanho_fonte, ajustar_cor
from Tela import classeTela
import pygame
import Imagens.CaminhosImagens as imgs_paths


class TelaRegras(classeTela):
    def __init__(self):
        super().__init__()

        self.escala = self.altura / 1080
        self.registrar_rect("botao_Voltar", self.largura // 2 - 100, self.altura // 2 + 225, 200, 50)
        self.registrar_rect("regras", self.largura // 2 - 350, self.altura // 2 - 200, 700, 400)

        self.texto_regras = ("Regras do Jogo:\n\n"
                             "1. O jogo consiste em formar pares de peças com elementos\n"
                             "químicos e propriedades correspondentes.\n\n"
                             "2. O jogador e o bot alternam turnos para posicionar suas\n"
                             "peças no tabuleiro.\n\n"
                             "3. O jogo termina quando o jogador ou o bot estiverem sem\npeças.\n\n")

        self.cor_botao_normal = ajustar_cor(255, 255, 255)
        self.cor_botao_hover = ajustar_cor(200, 200, 200)

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
        pygame.draw.rect(self.tela, ajustar_cor(0, 0, 0), self.regras, 2, border_radius=8)

        texto_botao_voltar = self.fonte.render("Voltar", True, ajustar_cor(0, 0, 0))
        
        self.tela.blit(texto_botao_voltar, texto_botao_voltar.get_rect(center=self.botao_Voltar.center))
        self.tela.blit(self.fonte.render(self.texto_regras, True, ajustar_cor(0, 0, 0)), self.regras.move(25, 10))