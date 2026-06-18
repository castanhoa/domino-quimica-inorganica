from Conteudo.Acessibilidade import tamanho_fonte, ajustar_cor
from Conteudo.Tela import classeTela
import pygame
import Conteudo.Imagens.CaminhosImagens as imgs_paths

from Conteudo.Aluno import Aluno

def seg_para_min(seg:float, d:int=2):
    return round(seg / 60, d)

class TelaEstatisticas(classeTela):
    def __init__(self, objUsuario):
        super().__init__(objUsuario=objUsuario)

        self.objUsuario = objUsuario

        self.escala = self.altura / 1080
        self.registrar_rect("botao_Voltar", self.largura // 2 - 100, self.altura // 2 + 350, 200, 50)
        self.registrar_rect("tempo_jogado", self.largura // 2 - 100, self.altura // 2 - 100, 200, 100)
        self.registrar_rect("tempo_por_partida", self.largura // 2 - 100, self.altura // 2 - 50, 200, 100)
    
        self.registrar_rect("conexoes", self.largura // 2 - 100, self.altura // 2, 200, 100)
        self.registrar_rect("conexoes_corretas", self.largura // 2 - 100, self.altura // 2 + 50, 200, 100)
        self.registrar_rect("razao_conexoes", self.largura // 2 - 100, self.altura // 2 + 100, 200, 100)

        self.registrar_rect("partidas", self.largura // 2 - 100, self.altura // 2 + 250, 200, 100)
        self.registrar_rect("partidas_vitoriosas", self.largura // 2 - 100, self.altura // 2 + 200, 200, 100)
        self.registrar_rect("razao_partidas", self.largura // 2 - 100, self.altura // 2 + 150, 200, 100)


        # self._texto_tempo_jogado = "Tempo Jogado:"
        # self._texto_vitorias = "Vitórias:"

        self.cor_botao_atual_voltar = [255, 255, 255]
        self.velocidade_animacao = 0.1

        self.fonte = pygame.font.SysFont("roboto", tamanho_fonte(20))
        self.titulo_Fonte = pygame.font.SysFont("roboto", tamanho_fonte(32))
        self.logo = pygame.image.load(imgs_paths.LOGOTIPO_PATH)

        pygame.display.set_icon(self.logo)
    
    def tratar_eventos(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.botao_Voltar.collidepoint(evento.pos):
                self.proxima_tela = "inicio"
                self.rodando = False

    def recriar_fontes(self):
        self.fonte = pygame.font.SysFont("roboto", tamanho_fonte(20))
        self.titulo_Fonte = pygame.font.SysFont("roboto", tamanho_fonte(32)) #NOVO


    def desenhar(self):

        if not isinstance(self.objUsuario, Aluno):
            print("Só alunos podem abrir esta tela")
            return

        self.tela.fill(ajustar_cor(255, 255, 255))
        mouse_pos = pygame.mouse.get_pos()

        tamanho_faixa = int(self.altura * 0.15)
        y_faixa = int(self.altura * 0)
        
        pygame.draw.rect(self.tela, ajustar_cor(255, 0, 0), (0, y_faixa, self.largura, tamanho_faixa))
        self.tela.blit(self.logo, (50, 175))

        texto_estatisticas = self.titulo_Fonte.render("Suas estatísticas!", True, ajustar_cor(0, 0, 0))
        rect_estatisticas = texto_estatisticas.get_rect(center=(self.largura // 2, int(self.altura * 0.3)))
        self.tela.blit(texto_estatisticas, rect_estatisticas)
        #----------------------------------

        if self.botao_Voltar.collidepoint(mouse_pos):
            cor_alvo_voltar = ajustar_cor(200, 200, 200)
        else:
            cor_alvo_voltar = ajustar_cor(255, 255, 255)

        for i in range(3):
            self.cor_botao_atual_voltar[i] += (cor_alvo_voltar[i] - self.cor_botao_atual_voltar[i]) * self.velocidade_animacao

        cor_botao_voltar = tuple(int(c) for c in self.cor_botao_atual_voltar)

        pygame.draw.rect(self.tela, cor_botao_voltar, self.botao_Voltar, border_radius=8)
        pygame.draw.rect(self.tela, ajustar_cor(128, 128, 128), self.botao_Voltar, 2, border_radius=8)
        pygame.draw.rect(self.tela, ajustar_cor(255, 255, 255), self.tempo_jogado, 1, border_radius=8)
        pygame.draw.rect(self.tela, ajustar_cor(255, 255, 255), self.tempo_por_partida, 1, border_radius=8)
        
        pygame.draw.rect(self.tela, ajustar_cor(255, 255, 255), self.conexoes, 1, border_radius=8)
        pygame.draw.rect(self.tela, ajustar_cor(255, 255, 255), self.conexoes_corretas, 1, border_radius=8)
        pygame.draw.rect(self.tela, ajustar_cor(255, 255, 255), self.razao_conexoes, 1, border_radius=8)

        pygame.draw.rect(self.tela, ajustar_cor(255, 255, 255), self.partidas, 1, border_radius=8)
        pygame.draw.rect(self.tela, ajustar_cor(255, 255, 255), self.partidas_vitoriosas, 1, border_radius=8)
        pygame.draw.rect(self.tela, ajustar_cor(255, 255, 255), self.razao_partidas, 1, border_radius=8)

        estatisticas_partidas, estatisticas_tentativas_conexao, estatisticas_tempo = self.objUsuario.get_estatisticas()

        texto_botao_voltar = self.fonte.render("Voltar", True, ajustar_cor(0, 0, 0))
        
        texto_tempo_jogado = self.fonte.render(f"Tempo total Jogado: {seg_para_min(estatisticas_tempo[0])} minutos", True, ajustar_cor(0, 0, 0))
        texto_tempo_por_partida = self.fonte.render(f"Tempo médio por partida: {seg_para_min(estatisticas_tempo[1])} minutos", True, ajustar_cor(0, 0, 0))
        
        texto_conexoes = self.fonte.render(f"Tentativas totais de conectar peças: {estatisticas_tentativas_conexao[1]}", True, ajustar_cor(0, 0, 0))
        texto_conexoes_corretas = self.fonte.render(f"Tentativas corretas de conectar peças: {estatisticas_tentativas_conexao[0]}", True, ajustar_cor(0, 0, 0))
        texto_razao_conexoes = self.fonte.render(f"Taxa de acerto na conexão de peças: {round(estatisticas_tentativas_conexao[2]*100, 2)}%", True, ajustar_cor(0, 0, 0))

        texto_partidas = self.fonte.render(f"Partidas totais: {estatisticas_partidas[1]}", True, ajustar_cor(0, 0, 0))
        texto_partidas_vitoriosas = self.fonte.render(f"Tentativas corretas de conectar peças: {estatisticas_partidas[0]}", True, ajustar_cor(0, 0, 0))
        texto_razao_partidas = self.fonte.render(f"Taxa de acerto na conexão de peças: {round(estatisticas_partidas[2]*100, 2)}%", True, ajustar_cor(0, 0, 0))

        self.tela.blit(texto_botao_voltar, texto_botao_voltar.get_rect(center=self.botao_Voltar.center))
        
        self.tela.blit(texto_tempo_jogado, texto_tempo_jogado.get_rect(top=self.tempo_jogado.top + 10, centerx=self.tempo_jogado.centerx))
        self.tela.blit(texto_tempo_por_partida, texto_tempo_por_partida.get_rect(top=self.tempo_por_partida.top + 10, centerx=self.tempo_por_partida.centerx))
    
        self.tela.blit(texto_conexoes, texto_conexoes.get_rect(top=self.conexoes.top + 10, centerx=self.conexoes.centerx))
        self.tela.blit(texto_conexoes_corretas, texto_conexoes_corretas.get_rect(top=self.conexoes_corretas.top + 10, centerx=self.conexoes_corretas.centerx))
        self.tela.blit(texto_razao_conexoes, texto_razao_conexoes.get_rect(top=self.razao_conexoes.top + 10, centerx=self.razao_conexoes.centerx))

        self.tela.blit(texto_partidas, texto_partidas.get_rect(top=self.partidas.top + 10, centerx=self.partidas.centerx))
        self.tela.blit(texto_partidas_vitoriosas, texto_partidas_vitoriosas.get_rect(top=self.partidas_vitoriosas.top + 10, centerx=self.partidas_vitoriosas.centerx))
        self.tela.blit(texto_razao_partidas, texto_razao_partidas.get_rect(top=self.razao_partidas.top + 10, centerx=self.razao_partidas.centerx))


        
        #----------------------------------
