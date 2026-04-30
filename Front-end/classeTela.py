class Tela:
    def __init__(self, largura=800, altura=600):
        import pygame
        pygame.init()
        self.tela = pygame.display.set_mode((largura, altura))
        self.rodando = True

    def executar(self):
        import pygame
        while self.rodando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.rodando = False

            self.desenhar()
            pygame.display.flip()

    def desenhar(self):
        pass
    
    #Criar métodos para adicionar botões, imputs, etc e depois chamar criarTela() dentro desses métodos e não no código da tela principal
