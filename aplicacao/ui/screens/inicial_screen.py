import pygame

class StartScreen:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.button_font = pygame.font.SysFont(None, 40)
        self.bg_image = pygame.image.load("assets/backgrounds/start_screen_bg.jpg") 
        self.bg_image = pygame.transform.scale(self.bg_image, screen.get_size())

        self.title = self.font.render("Protect The Land", True, (255, 255, 255))
        self.title_outline = self.font.render("Protect The Land", True, (0, 0, 0))

        # Botões
        self.start_button = pygame.Rect(screen.get_width() // 2 - 150, 460, 300, 70)
        self.quit_button = pygame.Rect(screen.get_width() // 2 - 150, 550, 300, 70)

    def draw_text_with_outline(self, text_surf, outline_surf, x, y):
        for dx in [-2, 2]:
            for dy in [-2, 2]:
                self.screen.blit(outline_surf, (x + dx, y + dy))
        self.screen.blit(text_surf, (x, y))

    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            self.screen.blit(self.bg_image, (0, 0))

            title_x = self.screen.get_width() // 2 - self.title.get_width() // 2
            title_y = 120
            self.draw_text_with_outline(self.title, self.title_outline, title_x, title_y)

            # Desenha os botões
            pygame.draw.rect(self.screen, (0, 128, 0), self.start_button, border_radius=10)
            pygame.draw.rect(self.screen, (128, 0, 0), self.quit_button, border_radius=10)

            start_text = self.button_font.render("Iniciar", True, (255, 255, 255))
            quit_text = self.button_font.render("Sair", True, (255, 255, 255))

            self.screen.blit(start_text, (self.start_button.centerx - start_text.get_width() // 2,
                                          self.start_button.centery - start_text.get_height() // 2))
            self.screen.blit(quit_text, (self.quit_button.centerx - quit_text.get_width() // 2,
                                         self.quit_button.centery - quit_text.get_height() // 2))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.start_button.collidepoint(mouse_pos):
                        return  # prossegue
                    elif self.quit_button.collidepoint(mouse_pos):
                        pygame.quit()
                        exit()

            clock.tick(60)
