class classeTela:
    def __init__(self, largura=800, altura=600, titulo=""):
        import pygame
        pygame.init()

        self.pygame = pygame

        self.largura_base = largura
        self.altura_base = altura

        self.tela = pygame.display.set_mode((largura, altura), pygame.RESIZABLE)

        self.proxima_tela = None

        pygame.display.set_caption(titulo)

        self.clock = pygame.time.Clock()
        self.rodando = True

        self.elementos_responsivos = []

    def registrar_rect(self, nome, x, y, largura, altura):
        self.elementos_responsivos.append({"nome": nome, "x": x, "y": y, "largura": largura, "altura": altura})

        setattr(self, nome, self.pygame.Rect(x, y, largura, altura))

    def atualizar_layout(self):
        largura_atual = self.tela.get_width()
        altura_atual = self.tela.get_height()

        escala_x = largura_atual / self.largura_base
        escala_y = altura_atual / self.altura_base

        for item in self.elementos_responsivos:
            novo_rect = self.pygame.Rect(
                int(item["x"] * escala_x),
                int(item["y"] * escala_y),
                int(item["largura"] * escala_x),
                int(item["altura"] * escala_y))

            setattr(self, item["nome"], novo_rect)

    def executar(self):
        while self.rodando:
            self.clock.tick(60)

            for evento in self.pygame.event.get():

                if evento.type == self.pygame.QUIT:
                    self.rodando = False

                if evento.type == self.pygame.VIDEORESIZE:
                    self.tela = self.pygame.display.set_mode((evento.w, evento.h), self.pygame.RESIZABLE)
                    self.atualizar_layout()

                self.tratar_eventos(evento)

            self.desenhar()
            self.pygame.display.flip()

            if self.proxima_tela:
                self.transicao()
                return self.proxima_tela

        self.pygame.quit()

    def transicao(self):
        fade = self.pygame.Surface(self.tela.get_size())
        fade.fill((0, 0, 0))

        for alpha in range(0, 255, 10):
            fade.set_alpha(alpha)
            self.desenhar()
            self.tela.blit(fade, (0, 0))
            self.pygame.display.flip()
            self.pygame.time.delay(20)

    def tratar_eventos(self, evento):
        pass

    def desenhar(self):
        pass
