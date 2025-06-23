import pygame
from ui.components.nick_input import NickInput


class NickScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 48)
        self.input_font = pygame.font.SysFont(None, 36)
        self.nick_input = NickInput((screen.get_width() // 2 - 150, 300, 300, 40), self.input_font)

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

            self.screen.fill((20, 20, 20))
            title = self.font.render("Digite seu nome", True, (180, 200, 200))
            self.screen.blit(title, (self.screen.get_width() // 2 - title.get_width() // 2, 150))
            self.nick_input.draw(self.screen)
            pygame.display.flip()
