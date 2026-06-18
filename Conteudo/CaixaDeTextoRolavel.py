import pygame

# CÓDIGO GERADO POR IA, MAS REVISADO E MELHORADO POR HUMANOS

class CaixaDeTextoRolavel:
    def __init__(self, x, y, largura, altura, lista_strings):
        self.rect = pygame.Rect(x-largura//2, y-altura//2, largura, altura)
        self.fonte = pygame.font.SysFont("Roboto", 20)
        self.scroll_y = 0
        self.scroll_speed = 20
        
        self.text_surfaces = [self.fonte.render(line, True, (255, 255, 255)) for line in lista_strings]
        self.line_height = self.fonte.get_linesize()
        
        self.total_height = len(self.text_surfaces) * self.line_height
        
        self.text_canvas = pygame.Surface((largura, max(self.total_height, altura)), pygame.SRCALPHA)
        for i, surf in enumerate(self.text_surfaces):
            self.text_canvas.blit(surf, (10, i * self.line_height))
            
        self.max_scroll = max(0, self.total_height - altura + 20)

    def tratar_eventos(self, evento):

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(evento.pos):
                if evento.button == 4:
                    self.scroll_y = max(0, self.scroll_y - self.scroll_speed)
                elif evento.button == 5:
                    self.scroll_y = min(self.max_scroll, self.scroll_y + self.scroll_speed)

    def desenhar(self, surface):
        pygame.draw.rect(surface, (30, 30, 30), self.rect)
        pygame.draw.rect(surface, (200, 200, 200), self.rect, 2)
        
        area_visivel = pygame.Rect(0, self.scroll_y, self.rect.width, self.rect.height)
        
        surface.blit(self.text_canvas, self.rect.topleft, area_visivel)