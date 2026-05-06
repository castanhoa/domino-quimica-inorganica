import pygame
from Tela import classeTela
from Usuario import Usuario

class TelaLogin(classeTela):
    def __init__(self):
        super().__init__(800, 600, "")

        self.input_Login = pygame.Rect(300, 225, 200, 50)
        self.input_Senha = pygame.Rect(300, 300, 200, 50)
        self.botao_Entrar = pygame.Rect(300, 450, 200, 50)

        self.cor_Ativa = pygame.Color(0, 0, 0)
        self.cor_Inativa = pygame.Color(128, 128, 128)
        self.cor_placeholder = (150, 150, 150)

        self.cor_botao_normal = (255, 255, 255)
        self.cor_botao_hover = (200, 200, 200)

        self.cor_botao_atual = [255, 255, 255]
        self.velocidade_animacao = 0.1

        self.fonte = pygame.font.SysFont("arial", 20)
        self.legenda_Fonte = pygame.font.SysFont("arial", 16)
        self.titulo_Fonte = pygame.font.SysFont("arial", 30)

        self.legenda_ETEC = self.titulo_Fonte.render("ETEC Júlio de Mesquita", True, (255, 255, 255))
        self.legenda_Login = self.legenda_Fonte.render("Login", True, (255, 255, 255))
        self.legenda_Senha = self.legenda_Fonte.render("Senha", True, (255, 255, 255))

        self.placeholder_login = "Digite seu login"
        self.placeholder_senha = "Digite sua senha"

        self.texto_login = ""
        self.texto_senha = ""
        
        self.caixaLogin_Ativa = False
        self.caixaSenha_Ativa = False

        self.cursor_visivel = True
        self.cursor_timer = 0

        self.mensagem = ""
        self.cor_mensagem = (0, 0, 0)

        self.usuario = Usuario("1234", "Euclides", False)

    def fazer_login(self):
        logado = self.usuario.tentar_login(
            nome=self.texto_login,
            senha=self.texto_senha
        )

        if logado:
            self.mensagem = "Login realizado com sucesso!"
            self.cor_mensagem = (0, 255, 0)
        else:
            self.mensagem = "Login ou senha incorretos!"
            self.cor_mensagem = (255, 0, 0)

    def tratar_eventos(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.botao_Entrar.collidepoint(evento.pos):
                self.fazer_login()

            self.caixaLogin_Ativa = self.input_Login.collidepoint(evento.pos)
            self.caixaSenha_Ativa = self.input_Senha.collidepoint(evento.pos)

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                self.fazer_login()

            if self.caixaLogin_Ativa:
                if evento.key == pygame.K_BACKSPACE:
                    self.texto_login = self.texto_login[:-1]
                else:
                    self.texto_login += evento.unicode

            if self.caixaSenha_Ativa:
                if evento.key == pygame.K_BACKSPACE:
                    self.texto_senha = self.texto_senha[:-1]
                else:
                    self.texto_senha += evento.unicode

    def desenhar(self):
        self.tela.fill((0, 120, 255))
        mouse_pos = pygame.mouse.get_pos()

        self.cursor_timer += 1
        if self.cursor_timer >= 30:
            self.cursor_visivel = not self.cursor_visivel
            self.cursor_timer = 0

        cor_login = self.cor_Ativa if self.caixaLogin_Ativa else self.cor_Inativa
        cor_senha = self.cor_Ativa if self.caixaSenha_Ativa else self.cor_Inativa

        if self.botao_Entrar.collidepoint(mouse_pos):
            cor_alvo = self.cor_botao_hover
        else:
            cor_alvo = self.cor_botao_normal

        for i in range(3):
            self.cor_botao_atual[i] += (cor_alvo[i] - self.cor_botao_atual[i]) * self.velocidade_animacao

        cor_botao = tuple(int(c) for c in self.cor_botao_atual)

        self.tela.blit(self.legenda_ETEC, (275, 100))
        self.tela.blit(self.legenda_Login, (self.input_Login.x, self.input_Login.y - 20))
        self.tela.blit(self.legenda_Senha, (self.input_Senha.x, self.input_Senha.y - 20))

        pygame.draw.rect(self.tela, (255, 255, 255), self.input_Login, border_radius=8)
        pygame.draw.rect(self.tela, cor_login, self.input_Login, 2, border_radius=8)

        pygame.draw.rect(self.tela, (255, 255, 255), self.input_Senha, border_radius=8)
        pygame.draw.rect(self.tela, cor_senha, self.input_Senha, 2, border_radius=8)

        if self.texto_login == "":
            textoLogin = self.fonte.render(self.placeholder_login, True, self.cor_placeholder)
        else:
            textoLogin = self.fonte.render(self.texto_login, True, (0, 0, 0))

        if self.texto_senha == "":
            textoSenha = self.fonte.render(self.placeholder_senha, True, self.cor_placeholder)
        else:
            senha_oculta = "*" * len(self.texto_senha)
            textoSenha = self.fonte.render(senha_oculta, True, (0, 0, 0))

        self.tela.blit(textoLogin, (self.input_Login.x + 5, self.input_Login.y + 10))
        self.tela.blit(textoSenha, (self.input_Senha.x + 5, self.input_Senha.y + 10))

        if self.cursor_visivel:
            if self.caixaLogin_Ativa:
                if self.texto_login == "":
                    x = self.input_Login.x + 5
                    y = self.input_Login.y + 10
                    pygame.draw.line(self.tela, (0, 0, 0), (x, y), (x, y + 25), 2)
                else:
                    x = self.input_Login.x + 5 + textoLogin.get_width()
                    y = self.input_Login.y + 10
                    pygame.draw.line(self.tela, (0, 0, 0), (x, y), (x, y + 25), 2)

            if self.caixaSenha_Ativa:
                if self.texto_senha == "":
                    x = self.input_Senha.x + 5
                    y = self.input_Senha.y + 10
                    pygame.draw.line(self.tela, (0, 0, 0), (x, y), (x, y + 25), 2)
                else:
                    x = self.input_Senha.x + 5 + textoSenha.get_width()
                    y = self.input_Senha.y + 10
                    pygame.draw.line(self.tela, (0, 0, 0), (x, y), (x, y + 25), 2)

        pygame.draw.rect(self.tela, cor_botao, self.botao_Entrar, border_radius=8)
        texto_botao = self.fonte.render("Entrar", True, (0, 0, 0))
        self.tela.blit(texto_botao, texto_botao.get_rect(center=self.botao_Entrar.center))

        if self.mensagem != "":
            texto_msg = self.fonte.render(self.mensagem, True, self.cor_mensagem)
            self.tela.blit(texto_msg, (300, 520))

tela = TelaLogin()
tela.executar()
