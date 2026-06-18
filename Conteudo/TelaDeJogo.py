from Conteudo.Acessibilidade import tamanho_fonte, ajustar_cor
from Conteudo.Tela import classeTela
from Conteudo.MaoBot import MaoBot
from Conteudo.Mesa import Mesa
# from Peca import Peca
from Conteudo.Mao import Mao
from Conteudo.JogoAplicado import Jogatina
import Conteudo.Imagens.CaminhosImagens as imgs_paths
import pygame

class TelaDeJogo(classeTela):

    def __init__(self, objUsuario):
        super().__init__(objUsuario=objUsuario)

        self.turno = "jogador"  # ou "bot"

        self.cor_notificacao = ajustar_cor(0, 128, 0)

        self.notificacao_rodando = False

        self.notificacao = ""
        self.tempo_notificacao = 0

        self.escala = self.altura / 1080
        self.botao_peca = []
        self.mao_bot = MaoBot((self.largura // 2 - int(200 * self.escala), int(self.altura * 0.18)),
        int(60 * self.escala))
        
        self.registrar_rect("botao_Monte", self.largura - 250, (self.altura - 250) // 2, 150, 250)
        self.registrar_rect("botao_Voltar", int(self.largura * 0.01),
                            int(self.altura * 0.86), int(200 * self.escala), int(50 * self.escala))
        self.registrar_rect("botao_Passar", int(self.largura * 0.8),
                            int(self.altura * 0.86), int(200 * self.escala), int(50 * self.escala))
        
        self.tamanho_peca_player = (int(70 * self.escala), int(140 * self.escala))
        self.tamanho_peca_bot = (int(50 * self.escala), int(100 * self.escala))
        self.tamanho_monte = (int(150 * self.escala), int(250 * self.escala))

        self.cor_botao_atual_voltar = [255, 255, 255]
        self.cor_botao_atual_passar = [255, 255, 255]
        self.velocidade_animacao = 0.1

        self.pecaPlayer = pygame.transform.scale(pygame.image.load(imgs_paths.PECAPLAYER_PATH),
        self.tamanho_peca_player)
      
        self.pecaBot = pygame.transform.scale(pygame.image.load(imgs_paths.PECABOT_PATH),
        self.tamanho_peca_bot)
        
        self.MontePecas = pygame.transform.scale(pygame.image.load(imgs_paths.MONTEPECA_PATH),
        self.tamanho_monte)
        
        self.fonte = pygame.font.SysFont("roboto", tamanho_fonte(20))
        
        self.logo = pygame.image.load(imgs_paths.LOGOTIPO_PATH)
        self.mesa = Mesa((self.largura // 2, self.altura // 2), (0.8 * self.escala))
        self.mao = Mao((self.largura // 2 - int(275 * self.escala), self.altura // 2 + int(220 * self.escala)), int(80 * self.escala))
        
        self.fonte = pygame.font.SysFont("roboto", tamanho_fonte(20))
        pygame.display.set_icon(self.logo)

        self.objJogatina = Jogatina(objAluno=self.objUsuario, tela_de_jogo=self)
        self.objJogatina.iniciar_partida()
    
    def mudar_turno(self, novo_turno):
        self.turno = novo_turno

        if self.notificacao_rodando == True:
            return
        
        self.notificacao_rodando = True

        if novo_turno == "jogador":
            self.notificacao = "Sua vez!"
        else:
            self.notificacao = "Vez do bot"
            
        self.cor_notificacao = ajustar_cor(0, 128, 0)
        self.tempo_notificacao = 45  # frames (~1.5s a 60fps)
    def tratar_eventos(self, evento):

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.botao_Monte.collidepoint(evento.pos):
                self.objJogatina.comprar_peca_usuario()
                # rect = pygame.Rect(1000, 300, 70, 140)
                # nova = Peca(self.pecaPlayer, rect, )
                # self.mao.adicionar(nova)
            
            if self.botao_Voltar.collidepoint(evento.pos):
                self.proxima_tela = "inicio"
                self.rodando = False

            if self.botao_Passar.collidepoint(evento.pos):
                self.objJogatina.rodada.incrementar()

            for peca in self.mao.pecas:
                if peca.get_rect().collidepoint(evento.pos):
                    peca.angulo = 180
                    self.objJogatina.fazer_jogada_usuario(peca)

    def recriar_fontes(self):
        self.fonte = pygame.font.SysFont("roboto", tamanho_fonte(20))

    def desenhar(self):

        if self.proxima_tela == "fim_de_jogo":
            self.rodando = False

        self.tela.fill(ajustar_cor(255, 255, 255))
        self.mao_bot.organizar()
        mouse_pos = pygame.mouse.get_pos()

        if self.botao_Voltar.collidepoint(mouse_pos):
            cor_alvo_voltar = ajustar_cor(200, 200, 200)
        else:
            cor_alvo_voltar = ajustar_cor(255, 255, 255)
        
        if self.botao_Passar.collidepoint(mouse_pos):
            cor_alvo_passar = ajustar_cor(200, 200, 200)
        else:
            cor_alvo_passar = ajustar_cor(255, 255, 255)

        for i in range(3):
            self.cor_botao_atual_voltar[i] += (cor_alvo_voltar[i] - self.cor_botao_atual_voltar[i]) * self.velocidade_animacao
        
        for i in range(3):
            self.cor_botao_atual_passar[i] += (cor_alvo_passar[i] - self.cor_botao_atual_passar[i]) * self.velocidade_animacao
        
        cor_botao_voltar = tuple(int(c) for c in self.cor_botao_atual_voltar)
        cor_botao_passar = tuple(int(c) for c in self.cor_botao_atual_passar)

        pygame.draw.rect(self.tela, cor_botao_voltar, self.botao_Voltar, border_radius=8)
        pygame.draw.rect(self.tela, ajustar_cor(128, 128, 128), self.botao_Voltar, 2, border_radius=8)

        pygame.draw.rect(self.tela, cor_botao_passar, self.botao_Passar, border_radius=8)
        pygame.draw.rect(self.tela, ajustar_cor(128, 128, 128), self.botao_Passar, 2, border_radius=8)

        texto_botao_voltar = self.fonte.render("Voltar", True, ajustar_cor(0, 0, 0))
        self.tela.blit(texto_botao_voltar, texto_botao_voltar.get_rect(center=self.botao_Voltar.center))

        texto_botao_passar = self.fonte.render("Passar vez", True, ajustar_cor(0, 0, 0))
        self.tela.blit(texto_botao_passar, texto_botao_passar.get_rect(center=self.botao_Passar.center))

        pecas_restantes_monte = self.fonte.render(f"Peças restantes: {len(self.objJogatina.jogo.monte)}", True, ajustar_cor(0, 0, 0))
        texto_rect = pecas_restantes_monte.get_rect(centerx=self.botao_Monte.centerx, top=self.botao_Monte.bottom + 10)

        pygame.draw.rect(self.tela, ajustar_cor(255, 0, 0), (0, 0, self.largura, int(self.altura * 0.15)))

        self.tela.blit(self.MontePecas, self.botao_Monte.topleft)
        self.tela.blit(pecas_restantes_monte, texto_rect)
        self.tela.blit(self.logo, (int(self.largura * 0.03), int(self.altura * 0.16)))

        if self.tempo_notificacao > 0:
            texto = self.fonte.render(
                self.notificacao,
                True,
                ajustar_cor(255, 255, 255)
            )

            fundo = pygame.Rect(
                self.largura // 2 - 120,
                int(self.altura * 0.05),
                240,
                50
            )

            pygame.draw.rect(self.tela, self.cor_notificacao, fundo, border_radius=10)

            self.tela.blit(texto, texto.get_rect(center=fundo.center))
            self.tempo_notificacao -= 1
        
        else:
            self.notificacao_rodando = False

        # PEÇAS DA MÃO (COM ANIMAÇÃO)
        for peca in self.mao.pecas:
            peca.atualizar()
            peca.desenhar(self.tela)

        # PEÇAS DA MESA (COM ANIMAÇÃO)
        for peca in self.mesa.pecas:
            peca.atualizar()
            peca.desenhar(self.tela)
        
        for peca in self.mao_bot.pecas:
            peca.desenhar(self.tela)

    def notificar_jogada_invalida(self):

        # if self.notificacao_rodando == True:
        #     return

        self.notificacao_rodando = True

        self.notificacao = "Jogada inválida!"
        self.tempo_notificacao = 55
        self.cor_notificacao = ajustar_cor(128, 0, 0)