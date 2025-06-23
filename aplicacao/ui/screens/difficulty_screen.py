import pygame

class DifficultyScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 48)
        self.options = [("Fácil", "easy"), ("Médio", "medium"), ("Difícil", "hard"), ("Sem fim", "endless")]
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        center_x = self.screen.get_width() // 2
        start_y = self.screen.get_height() // 2 - 100
        for i, (label, difficulty) in enumerate(self.options):
            rect = pygame.Rect(center_x - 100, start_y + i * 80, 200, 60)
            self.buttons.append((label, difficulty, rect))

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

            self.screen.fill((30, 30, 30))
            title = self.font.render("Escolha a Dificuldade", True, (255, 255, 255))
            self.screen.blit(title, (self.screen.get_width() // 2 - title.get_width() // 2, 100))

            for label, _, rect in self.buttons:
                pygame.draw.rect(self.screen, (70, 70, 200), rect)
                text = self.font.render(label, True, (255, 255, 255))
                self.screen.blit(text, (rect.x + 20, rect.y + 10))

            pygame.display.flip()
