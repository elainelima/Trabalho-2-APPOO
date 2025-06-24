import pygame
from ui.components.nick_input import NickInput

class NickScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 64)
        self.input_font = pygame.font.SysFont(None, 36)
        self.nick_input = NickInput((screen.get_width() // 2 - 150, 320, 300, 40), self.input_font)

        self.button_rect = pygame.Rect(screen.get_width() // 2 - 100, 400, 200, 60)
        self.bg_image = pygame.image.load("assets/backgrounds/nick_screen_bg.png") 
        self.bg_image = pygame.transform.scale(self.bg_image, screen.get_size())

    def draw_text_with_outline(self, text_surf, outline_surf, x, y):
        for dx in [-2, 2]:
            for dy in [-2, 2]:
                self.screen.blit(outline_surf, (x + dx, y + dy))
        self.screen.blit(text_surf, (x, y))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None

                self.nick_input.handle_event(event)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    nick = self.nick_input.get_text().strip()
                    return nick if nick else "Jogador"

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_rect.collidepoint(event.pos):
                        nick = self.nick_input.get_text().strip()
                        return nick if nick else "Jogador"

            self.screen.blit(self.bg_image, (0, 0))

            title = self.font.render("Digite seu nome", True, (255, 255, 255))
            title_outline = self.font.render("Digite seu nome", True, (0, 0, 0))
            title_x = self.screen.get_width() // 2 - title.get_width() // 2
            self.draw_text_with_outline(title, title_outline, title_x, 200)

            self.nick_input.draw(self.screen)

            # Botão "Continuar"
            pygame.draw.rect(self.screen, (0, 128, 255), self.button_rect, border_radius=10)
            button_text = self.input_font.render("Continuar", True, (255, 255, 255))
            self.screen.blit(button_text, (
                self.button_rect.centerx - button_text.get_width() // 2,
                self.button_rect.centery - button_text.get_height() // 2
            ))

            pygame.display.flip()
