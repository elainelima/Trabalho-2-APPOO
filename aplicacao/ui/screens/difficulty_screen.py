import pygame

class DifficultyScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 64)
        self.button_font = pygame.font.SysFont(None, 40)
        self.options = [("Fácil", "easy"), ("Médio", "medium"), ("Difícil", "hard"), ("Sem fim", "endless")]
        self.buttons = []
        self.create_buttons()
        self.bg_image = pygame.image.load("assets/backgrounds/difficulty_screen_bg.jpg") 
        self.bg_image = pygame.transform.scale(self.bg_image, screen.get_size())

    def create_buttons(self):
        center_x = self.screen.get_width() // 2
        start_y = self.screen.get_height() // 2 - 120
        for i, (label, difficulty) in enumerate(self.options):
            rect = pygame.Rect(center_x - 120, start_y + i * 90, 240, 70)
            self.buttons.append((label, difficulty, rect))

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
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for _, difficulty, rect in self.buttons:
                        if rect.collidepoint(event.pos):
                            return difficulty

            self.screen.blit(self.bg_image, (0, 0))

            title = self.font.render("Escolha a Dificuldade", True, (255, 255, 255))
            title_outline = self.font.render("Escolha a Dificuldade", True, (0, 0, 0))
            title_x = self.screen.get_width() // 2 - title.get_width() // 2
            self.draw_text_with_outline(title, title_outline, title_x, 100)

            for label, _, rect in self.buttons:
                pygame.draw.rect(self.screen, (50, 100, 220), rect, border_radius=12)
                text = self.button_font.render(label, True, (255, 255, 255))
                self.screen.blit(
                    text,
                    (rect.centerx - text.get_width() // 2, rect.centery - text.get_height() // 2)
                )

            pygame.display.flip()
