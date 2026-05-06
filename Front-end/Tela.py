class classeTela:
    def __init__(self, largura=800, altura=600, titulo=""):
        import pygame
        pygame.init()
        self.pygame = pygame
        self.tela = pygame.display.set_mode((largura, altura))
        self.proxima_tela = None

        pygame.display.set_caption(titulo)

        self.clock = pygame.time.Clock()
        self.rodando = True

    def executar(self):
        while self.rodando:
            self.clock.tick(60)

            for evento in self.pygame.event.get():
                if evento.type == self.pygame.QUIT:
                    self.rodando = False

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
