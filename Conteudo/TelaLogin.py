from Conteudo.Acessibilidade import tamanho_fonte, ajustar_cor
from Conteudo.Aluno import Aluno
from Conteudo.Professor import Professor

from Conteudo.Banco import buscar_senha, pegar_dados_aluno, ver_existencia_de_aluno, ver_existencia_de_professor

from Conteudo.Tela import classeTela
from Conteudo.Seguranca.AjudaHash import hash_padrao, comparar_hashes
import pygame
import Conteudo.Imagens.CaminhosImagens as imgs_paths


class TelaLogin(classeTela):
    def __init__(self, cascaUsuario):
        super().__init__(objUsuario=cascaUsuario.objUsuario)

        self.cascaUsuario = cascaUsuario

        self.registrar_rect("input_Login", self.largura // 2 - 100, self.altura // 2 - 50, 200, 50)
        self.registrar_rect("input_Senha", self.largura // 2 - 100, self.altura // 2 + 25, 200, 50)
        self.registrar_rect("botao_Entrar", self.largura // 2 - 100, self.altura // 2 + 150, 200, 50)

        self.cor_botao_atual = [255, 255, 255]
        self.velocidade_animacao = 0.1

        self.fonte = pygame.font.SysFont("roboto", tamanho_fonte(20))
        self.legenda_Fonte = pygame.font.SysFont("roboto", tamanho_fonte(16))
        self.titulo_Fonte = pygame.font.SysFont("roboto", tamanho_fonte(32))

        self.legenda_Login = self.legenda_Fonte.render("Login", True, ajustar_cor(0, 0, 0))
        self.legenda_Senha = self.legenda_Fonte.render("Senha", True, ajustar_cor(0, 0, 0))

        self.placeholder_login = "Digite seu login"
        self.placeholder_senha = "Digite sua senha"

        self.texto_login = ""
        self.texto_senha = ""
        
        self.caixaLogin_Ativa = False
        self.caixaSenha_Ativa = False

        self.cursor_visivel = True
        self.cursor_timer = 0

        self.cursor_login_pos = 0
        self.cursor_senha_pos = 0

        self.mensagem = ""
        self.cor_mensagem = ajustar_cor(0, 0, 0)

        self.logo = pygame.image.load(imgs_paths.LOGOTIPO_PATH)

        pygame.display.set_icon(self.logo)
        pygame.key.set_repeat(400, 50)



    def fazer_login(self):

        e_aluno = None
        # True para aluno, False para professor, e None para incorreto

        if "@aluno.cps.sp.gov.br" in self.texto_login:
            e_aluno = True
        elif "@cps.sp.gov.br" in self.texto_login:
            e_aluno = False

        if e_aluno is None:
            self.mensagem = "Login incorreto! Utilize seu e-mail acadêmico."
            self.cor_mensagem = ajustar_cor(255, 0, 0)
            return

        if e_aluno:
            existe = ver_existencia_de_aluno(self.texto_login)

            if not existe:
                self.mensagem = "E-mail de aluno inexistente!"
                self.cor_mensagem = ajustar_cor(255, 0, 0)
                return 
        else:
            existe = ver_existencia_de_professor(self.texto_login)
            
            if not existe:
                self.mensagem = "E-mail de professor inexistente!"
                self.cor_mensagem = ajustar_cor(255, 0, 0)
                return 
        
        hash_senha_banco = buscar_senha(correio=self.texto_login, e_aluno=e_aluno)
        hash_senha_ui = hash_padrao(self.texto_senha)

        login_validado = comparar_hashes(hash0=hash_senha_banco, hash1=hash_senha_ui)

        if not login_validado:
            self.mensagem = "Login e/ou senha incorretos!"
            self.cor_mensagem = ajustar_cor(255, 0, 0)
            return   

        try:
            if e_aluno:
                objAluno = Aluno(self.texto_senha, self.texto_login, True)
                objAluno.set_dados_jogatinas(*pegar_dados_aluno(self.texto_login))

                self.cascaUsuario.objUsuario = objAluno
                
            else:
                self.cascaUsuario.objUsuario = Professor(self.texto_senha, self.texto_login, True)

            self.proxima_tela = "inicio"
            self.rodando = False
        
        except Exception as e:
            self.mensagem = "Algum erro ocorreu. Tente novamente."
            self.cor_mensagem = ajustar_cor(255, 0, 0)
            raise(e)

    def tratar_eventos(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.botao_Entrar.collidepoint(evento.pos):
                self.fazer_login()

            self.caixaLogin_Ativa = self.input_Login.collidepoint(evento.pos)
            self.caixaSenha_Ativa = self.input_Senha.collidepoint(evento.pos)

            if self.caixaLogin_Ativa:
                mouse_x = evento.pos[0] - (self.input_Login.x + 5)
                self.cursor_login_pos = len(self.texto_login)

                for i in range(len(self.texto_login)):

                    texto_antes = self.texto_login[:i]
                    texto_atual = self.texto_login[:i + 1]

                    largura_antes = self.fonte.size(texto_antes)[0]
                    largura_atual = self.fonte.size(texto_atual)[0]

                    meio_letra = (largura_antes + largura_atual) / 2

                    if mouse_x < meio_letra:
                        self.cursor_login_pos = i
                        break
                else:
                    self.cursor_login_pos = len(self.texto_login)

            if self.caixaSenha_Ativa:
                mouse_x = evento.pos[0] - (self.input_Senha.x + 5)
                self.cursor_senha_pos = len(self.texto_senha)
                senha_oculta = "*" * len(self.texto_senha)
                self.cursor_senha_pos = len(self.texto_senha)

                for i in range(len(senha_oculta)):

                    texto_antes = senha_oculta[:i]
                    texto_atual = senha_oculta[:i + 1]
                    largura_antes = self.fonte.size(texto_antes)[0]
                    largura_atual = self.fonte.size(texto_atual)[0]
                    meio_letra = (largura_antes + largura_atual) / 2

                    if mouse_x < meio_letra:
                        self.cursor_senha_pos = i
                        break
                else:
                    self.cursor_senha_pos = len(self.texto_senha)

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN or evento.key == pygame.K_KP_ENTER:
                self.fazer_login()
            
            if self.caixaLogin_Ativa:
                if evento.key == pygame.K_BACKSPACE:
                    if self.cursor_login_pos > 0:
                        self.texto_login = (self.texto_login[:self.cursor_login_pos - 1] + self.texto_login[self.cursor_login_pos:])
                        self.cursor_login_pos -= 1

                elif evento.key == pygame.K_LEFT:
                    if self.cursor_login_pos > 0:
                        self.cursor_login_pos -= 1

                elif evento.key == pygame.K_RIGHT:
                    if self.cursor_login_pos < len(self.texto_login):
                        self.cursor_login_pos += 1

                else:
                    self.texto_login = (self.texto_login[:self.cursor_login_pos] + evento.unicode + self.texto_login[self.cursor_login_pos:])
                    self.cursor_login_pos += 1


            if self.caixaSenha_Ativa:
                if evento.key == pygame.K_BACKSPACE:
                    if self.cursor_senha_pos > 0:
                        self.texto_senha = (self.texto_senha[:self.cursor_senha_pos - 1] + self.texto_senha[self.cursor_senha_pos:])
                        self.cursor_senha_pos -= 1

                elif evento.key == pygame.K_LEFT:
                    if self.cursor_senha_pos > 0:
                        self.cursor_senha_pos -= 1

                elif evento.key == pygame.K_RIGHT:
                    if self.cursor_senha_pos < len(self.texto_senha):
                        self.cursor_senha_pos += 1

                else:
                    self.texto_senha = (self.texto_senha[:self.cursor_senha_pos] + evento.unicode + self.texto_senha[self.cursor_senha_pos:])
                    self.cursor_senha_pos += 1

    def desenhar(self):
        self.tela.fill(ajustar_cor(255, 255, 255))
        mouse_pos = pygame.mouse.get_pos()

        tamanho_faixa = int(self.altura * 0.15)
        y_faixa = int(self.altura * 0)
        
        pygame.draw.rect(self.tela, ajustar_cor(255, 0, 0), (0, y_faixa, self.largura, tamanho_faixa))
        self.tela.blit(self.logo, (50, 175))

        self.cursor_timer += 1
        if self.cursor_timer >= 30:
            self.cursor_visivel = not self.cursor_visivel
            self.cursor_timer = 0

        cor_login = ajustar_cor(0, 0, 0) if self.caixaLogin_Ativa else ajustar_cor(128, 128, 128)
        cor_senha = ajustar_cor(0, 0, 0) if self.caixaSenha_Ativa else ajustar_cor(128, 128, 128)

        if self.botao_Entrar.collidepoint(mouse_pos):
            cor_alvo = ajustar_cor(200, 200, 200)
        else:
            cor_alvo = ajustar_cor(255, 255, 255)

        for i in range(3):
            self.cor_botao_atual[i] += (cor_alvo[i] - self.cor_botao_atual[i]) * self.velocidade_animacao

        cor_botao = tuple(int(c) for c in self.cor_botao_atual)
        
        texto_ETEC = self.titulo_Fonte.render(
            "ETEC Júlio de Mesquita", True, ajustar_cor(0, 0, 0)
        )

        titulo_rect = texto_ETEC.get_rect(
            center=(self.largura // 2,
                    int(self.altura * 0.30))
        )

        self.tela.blit(texto_ETEC, titulo_rect)
        self.tela.blit(self.legenda_Login, (self.input_Login.x, self.input_Login.y - 20))
        self.tela.blit(self.legenda_Senha, (self.input_Senha.x, self.input_Senha.y - 20))

        pygame.draw.rect(self.tela, ajustar_cor(255, 255, 255), self.input_Login, border_radius=8)
        pygame.draw.rect(self.tela, cor_login, self.input_Login, 2, border_radius=8)

        pygame.draw.rect(self.tela, ajustar_cor(255, 255, 255), self.input_Senha, border_radius=8)
        pygame.draw.rect(self.tela, cor_senha, self.input_Senha, 2, border_radius=8)

        if self.texto_login == "":
            textoLogin = self.fonte.render(self.placeholder_login, True, ajustar_cor(150, 150, 150))
        else:
            textoLogin = self.fonte.render(self.texto_login, True, ajustar_cor(0, 0, 0))

        if self.texto_senha == "":
            textoSenha = self.fonte.render(self.placeholder_senha, True, ajustar_cor(150, 150, 150))
        else:
            senha_oculta = "*" * len(self.texto_senha)
            textoSenha = self.fonte.render(senha_oculta, True, ajustar_cor(0, 0, 0))

        self.tela.blit(textoLogin, (self.input_Login.x + 5, self.input_Login.y + 10))
        self.tela.blit(textoSenha, (self.input_Senha.x + 5, self.input_Senha.y + 10))

        if self.cursor_visivel:
            if self.caixaLogin_Ativa:
                if self.texto_login == "":
                    x = self.input_Login.x + 5
                    y = self.input_Login.y + 10
                    pygame.draw.line(self.tela, ajustar_cor(0, 0, 0), (x, y), (x, y + 25), 2)
                else:
                    largura_cursor = self.fonte.size(self.texto_login[:self.cursor_login_pos])[0]
                    x = self.input_Login.x + 5 + largura_cursor
                    y = self.input_Login.y + 10
                    pygame.draw.line(self.tela, ajustar_cor(0, 0, 0), (x, y), (x, y + 25), 2)

            if self.caixaSenha_Ativa:
                if self.texto_senha == "":
                    x = self.input_Senha.x + 5
                    y = self.input_Senha.y + 10
                    pygame.draw.line(self.tela, ajustar_cor(0, 0, 0), (x, y), (x, y + 25), 2)
                else:
                    senha_visivel = "*" * self.cursor_senha_pos
                    largura_cursor = self.fonte.size(senha_visivel)[0]
                    x = self.input_Senha.x + 5 + largura_cursor
                    y = self.input_Senha.y + 10
                    pygame.draw.line(self.tela, ajustar_cor(0, 0, 0), (x, y), (x, y + 25), 2)

        pygame.draw.rect(self.tela, cor_botao, self.botao_Entrar, border_radius=8)
        pygame.draw.rect(self.tela, ajustar_cor(128, 128, 128), self.botao_Entrar, 2, border_radius=8)

        texto_botao = self.fonte.render("Entrar", True, ajustar_cor(0, 0, 0))
        self.tela.blit(texto_botao, texto_botao.get_rect(center=self.botao_Entrar.center))

        if self.mensagem != "":
            texto_mensagem = self.fonte.render(self.mensagem, True, self.cor_mensagem)
            mensagem_rect = texto_mensagem.get_rect(center=(self.tela.get_width() // 2, int(self.tela.get_height() * 0.87)))
            self.tela.blit(texto_mensagem, mensagem_rect)
    
    def recriar_fontes(self):
        self.fonte = pygame.font.SysFont("roboto", tamanho_fonte(20))
        self.legenda_Fonte = pygame.font.SysFont("roboto", tamanho_fonte(16))
        self.titulo_Fonte = pygame.font.SysFont("roboto", tamanho_fonte(32))
