import pygame

class NickInput:
    def __init__(self, rect, font, placeholder="Digite seu nome"):
        self.rect = pygame.Rect(rect)
        self.color_inactive = pygame.Color("gray")
        self.color_active = pygame.Color("white")
        self.color = self.color_inactive
        self.font = font
        self.text = ""
        self.placeholder = placeholder
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Ativa input se clicar dentro do campo
            self.active = self.rect.collidepoint(event.pos)
            self.color = self.color_active if self.active else self.color_inactive

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.active = False
                self.color = self.color_inactive
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif len(self.text) < 15:
                self.text += event.unicode

    def draw(self, surface):
        # Exibe texto digitado ou placeholder
        display_text = self.text if self.text else self.placeholder
        text_surface = self.font.render(display_text, True, (100, 100, 100) if self.text else (150, 150, 150))
        pygame.draw.rect(surface, self.color, self.rect, 2)
        surface.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

    def get_text(self):
        return self.text