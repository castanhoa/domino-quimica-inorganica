from TelaCarregamento import TelaCarregamento
from TelaDeJogo import TelaDeJogo
from Tela import classeTela
import pygame

class TelaInicial(classeTela):
    def __init__(self):
        super().__init__()

        self.registrar_rect("botao_Iniciar", self.largura // 2 - 100, self.altura // 2 + 100, 200, 50)

        self.cor_botao_normal = (255, 255, 255)
        self.cor_botao_hover = (200, 200, 200)

        self.cor_botao_atual = [255, 255, 255]
        self.velocidade_animacao = 0.1

        self.fonte = pygame.font.SysFont("arial", 20)
        self.titulo_Fonte = pygame.font.SysFont("arial", 30)

        self.legenda_Iniciar = self.titulo_Fonte.render("Bem-Vindo(a) ao Dominó de Química Inorgânica", True, (0, 0, 0))
        

        self.cursor_visivel = True
        self.cursor_timer = 0

        self.logo = pygame.image.load(r"C:\Users\26.01448-0\Desktop\Logotipo.png")

        pygame.display.set_icon(self.logo)

    def tratar_eventos(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.botao_Iniciar.collidepoint(evento.pos):
                loading = TelaCarregamento(duracao = 0.8)
                loading.executar()
                
                self.proxima_tela = TelaDeJogo()
                self.proxima_tela.executar()

    def desenhar(self):
        self.tela.fill((255, 255, 255))
        mouse_pos = pygame.mouse.get_pos()

        tamanho_faixa = int(self.altura * 0.15)
        y_faixa = self.altura * 0
        
        pygame.draw.rect(self.tela,(255, 0, 0),(0, y_faixa, self.largura, tamanho_faixa))
        self.tela.blit(self.logo, (50, 175))

        self.cursor_timer += 1
        if self.cursor_timer >= 30:
            self.cursor_visivel = not self.cursor_visivel
            self.cursor_timer = 0
        if self.botao_Iniciar.collidepoint(mouse_pos):
            cor_alvo = self.cor_botao_hover
        else:
            cor_alvo = self.cor_botao_normal

        for i in range(3):
            self.cor_botao_atual[i] += (cor_alvo[i] - self.cor_botao_atual[i]) * self.velocidade_animacao

        cor_botao = tuple(int(c) for c in self.cor_botao_atual)

        titulo_rect = self.legenda_Iniciar.get_rect(center=(self.tela.get_width() // 2, int(self.tela.get_height() * 0.3)))
        
        self.tela.blit(self.legenda_Iniciar, titulo_rect)

        pygame.draw.rect(self.tela, cor_botao, self.botao_Iniciar, border_radius=8)
        pygame.draw.rect(self.tela, (128, 128, 128), self.botao_Iniciar, 2, border_radius=8)

        texto_botao = self.fonte.render("Começar partida", True, (0, 0, 0))
        self.tela.blit(texto_botao, texto_botao.get_rect(center=self.botao_Iniciar.center))
