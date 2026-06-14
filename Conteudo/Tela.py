import Acessibilidade
import pygame
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = '0, 30'

class classeTela:
    def __init__(self):
        
        pygame.init()
        
        infoTela = pygame.display.Info()
        largura_monitor = infoTela.current_w
        altura_monitor = infoTela.current_h
        self.largura = largura_monitor
        self.altura = altura_monitor
        self.tela = pygame.display.set_mode((self.largura, self.altura), pygame.RESIZABLE)
        self.proxima_tela = None

        pygame.display.set_caption("")

        self.clock = pygame.time.Clock()
        self.rodando = True
        self.elementos_responsivos = []

    def registrar_rect(self, nome, x, y, largura, altura):
        self.elementos_responsivos.append({"nome": nome, "x": x, "y": y, "largura": largura, "altura": altura})
        setattr(self, nome, pygame.Rect(x, y, largura, altura))

    def atualizar_layout(self):

        largura_atual = self.tela.get_width()
        altura_atual = self.tela.get_height()

        escala_x = largura_atual / self.largura
        escala_y = altura_atual / self.altura

        for item in self.elementos_responsivos:

            novo_rect = pygame.Rect(
                int(item["x"] * escala_x),
                int(item["y"] * escala_y),
                int(item["largura"] * escala_x),
                int(item["altura"] * escala_y)
            )

            setattr(self, item["nome"], novo_rect)

    def executar(self):

        while self.rodando:

            self.clock.tick(120)

            for evento in pygame.event.get():

                if evento.type == pygame.QUIT:
                    self.rodando = False

                elif evento.type == pygame.VIDEORESIZE:
                    self.tela = pygame.display.set_mode(
                        (evento.w, evento.h),
                        pygame.RESIZABLE
                    )
                    self.atualizar_layout()

                elif evento.type == pygame.KEYDOWN:

                    if evento.key == pygame.K_F1:
                        Acessibilidade.diminuir_fonte()
                        self.recriar_fontes()

                    elif evento.key == pygame.K_F2:
                        Acessibilidade.aumentar_fonte()
                        self.recriar_fontes()

                    elif evento.key == pygame.K_F3:
                        Acessibilidade.definir_modo_daltonismo(Acessibilidade.MODO_NORMAL)

                    elif evento.key == pygame.K_F4:
                            Acessibilidade.definir_modo_daltonismo(Acessibilidade.MODO_DEUTERANOPIA)

                    elif evento.key == pygame.K_F5:
                        Acessibilidade.definir_modo_daltonismo(Acessibilidade.MODO_PROTANOPIA)

                    elif evento.key == pygame.K_F6:
                        Acessibilidade.definir_modo_daltonismo(Acessibilidade.MODO_TRITANOPIA)

                self.tratar_eventos(evento)

            if not self.rodando:
                break

            self.desenhar()

            if self.tela:
                pygame.display.flip()

    def tratar_eventos(self, evento):
        pass

    def desenhar(self):
        pass

    def recriar_fontes(self):
        pass
