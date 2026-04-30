import pygame

pygame.init()

largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Tela de Login")

clock = pygame.time.Clock()

botao_Entrar = pygame.Rect(300, 450, 200, 50)


input_Login = pygame.Rect(300, 225, 200, 50)
input_Senha = pygame.Rect(300, 300, 200, 50)

cor_Ativa = pygame.Color(0, 0, 0)
cor_Inativa = pygame.Color(128, 128, 128)

cor_Botao = (255, 255, 255)

fonte = pygame.font.SysFont("arial", 20)
legenda_Fonte = pygame.font.SysFont("arial", 16)
titulo_Fonte = pygame.font.SysFont("arial", 30)

legenda_ETEC = titulo_Fonte.render("ETEC Júlio de Mesquita", True, (255, 255, 255))
legenda_Login = legenda_Fonte.render("Login", True, (255, 255, 255))
legenda_Senha = legenda_Fonte.render("Senha", True, (255, 255, 255))

caixaLogin_Ativa = False
caixaSenha_Ativa = False

texto_login = ""
texto_senha = ""

from Usuario import Usuario

meu_usuario = Usuario("1234","Euclides", False)

rodando = True

while rodando:
    clock.tick(60)
    tela.fill((0, 120, 255))


    cor_login = cor_Ativa if caixaLogin_Ativa else cor_Inativa
    cor_senha = cor_Ativa if caixaSenha_Ativa else cor_Inativa

    tela.blit(legenda_ETEC, (275, 100))
    tela.blit(legenda_Login, (input_Login.x, input_Login.y - 20))
    tela.blit(legenda_Senha, (input_Senha.x, input_Senha.y - 20))


    pygame.draw.rect(tela, (255, 255, 255), input_Login, border_radius=8)
    pygame.draw.rect(tela, cor_login, input_Login, 2, border_radius=8)


    pygame.draw.rect(tela, (255, 255, 255), input_Senha, border_radius=8)
    pygame.draw.rect(tela, cor_senha, input_Senha, 2, border_radius=8)


    textoLogin_Usuario = fonte.render(texto_login, True, (0, 0, 0))
    textoSenha_Usuario = fonte.render(texto_senha, True, (0, 0, 0))

    tela.blit(textoLogin_Usuario, (input_Login.x + 5, input_Login.y + 10))
    tela.blit(textoSenha_Usuario, (input_Senha.x + 5, input_Senha.y + 10))


    pygame.draw.rect(tela, cor_Botao, botao_Entrar, border_radius=8)
    texto_botao = fonte.render("Entrar", True, (0, 0, 0))
    tela.blit(texto_botao, texto_botao.get_rect(center=botao_Entrar.center))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if botao_Entrar.collidepoint(evento.pos):

                logado = meu_usuario.tentar_login(senha=texto_senha, nome=texto_login)
                
                if logado == True:
                    print("Usuário logado!")
                else:
                    print("O login ou senha incorretos!")

            caixaLogin_Ativa = input_Login.collidepoint(evento.pos)
            caixaSenha_Ativa = input_Senha.collidepoint(evento.pos)

        if evento.type == pygame.KEYDOWN:
            if caixaLogin_Ativa:
                if evento.key == pygame.K_BACKSPACE:
                    texto_login = texto_login[:-1]
                else:
                    texto_login += evento.unicode

            if caixaSenha_Ativa:
                if evento.key == pygame.K_BACKSPACE:
                    texto_senha = texto_senha[:-1]
                else:
                    texto_senha += evento.unicode

    pygame.display.flip()

pygame.quit()
