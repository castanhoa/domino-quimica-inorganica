import pygame

pygame.init()

largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Tela de Login")

clock = pygame.time.Clock()

botao_Entrar = pygame.Rect(300, 375, 200, 50)


input_Login = pygame.Rect(300, 130, 200, 50)
input_Senha = pygame.Rect(300, 220, 200, 50)

cor_Ativa = pygame.Color(0, 0, 0)
cor_Inativa = pygame.Color(128, 128, 128)

cor_Botao = (255, 255, 255)

fonte = pygame.font.SysFont("arial", 20)
fonte_label = pygame.font.SysFont("arial", 16)


label_login = fonte_label.render("Login", True, (255, 255, 255))
label_senha = fonte_label.render("Senha", True, (255, 255, 255))


active_login = False
active_senha = False

texto_login = ""
texto_senha = ""

rodando = True

while rodando:
    clock.tick(60)
    tela.fill((0, 120, 255))


    cor_login = cor_Ativa if active_login else cor_Inativa
    cor_senha = cor_Ativa if active_senha else cor_Inativa


    tela.blit(label_login, (input_Login.x, input_Login.y - 20))
    tela.blit(label_senha, (input_Senha.x, input_Senha.y - 20))


    pygame.draw.rect(tela, (255, 255, 255), input_Login, border_radius=8)
    pygame.draw.rect(tela, cor_login, input_Login, 2, border_radius=8)


    pygame.draw.rect(tela, (255, 255, 255), input_Senha, border_radius=8)
    pygame.draw.rect(tela, cor_senha, input_Senha, 2, border_radius=8)


    txt_login_surface = fonte.render(texto_login, True, (0, 0, 0))
    txt_senha_surface = fonte.render(texto_senha, True, (0, 0, 0))

    tela.blit(txt_login_surface, (input_Login.x + 5, input_Login.y + 10))
    tela.blit(txt_senha_surface, (input_Senha.x + 5, input_Senha.y + 10))


    pygame.draw.rect(tela, cor_Botao, botao_Entrar, border_radius=8)
    texto_botao = fonte.render("Entrar", True, (0, 0, 0))
    tela.blit(texto_botao, texto_botao.get_rect(center=botao_Entrar.center))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if botao_Entrar.collidepoint(evento.pos):
                if texto_login == "Caio" and texto_senha == "1234":
                    print("Usuário logado")
                else:
                    print("Login ou senha incorretos")

            active_login = input_Login.collidepoint(evento.pos)
            active_senha = input_Senha.collidepoint(evento.pos)

        if evento.type == pygame.KEYDOWN:
            if active_login:
                if evento.key == pygame.K_BACKSPACE:
                    texto_login = texto_login[:-1]
                else:
                    texto_login += evento.unicode

            if active_senha:
                if evento.key == pygame.K_BACKSPACE:
                    texto_senha = texto_senha[:-1]
                else:
                    texto_senha += evento.unicode

    pygame.display.flip()

pygame.quit()
