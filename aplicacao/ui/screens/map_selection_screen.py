import pygame
from maps.green_map import GreenMap

class MapSelectionScreen:
    def __init__(self, screen, font, background_path="assets/backgrounds/map_selection_bg.png"):
        self.screen = screen
        self.font = font
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load(background_path).convert()
        self.background = pygame.transform.scale(self.background, self.screen.get_size())
        self.selected_map_class = None

        self.maps = [
            {"name": "Mapa 1", "image": "assets/GreenMap.png", "class": GreenMap},
            {"name": "Mapa 2", "image": "assets/GreenMap.png", "class": GreenMap}
        ]

    def render_text_with_outline(self, text, color=(255, 255, 255), outline_color=(0, 0, 0)):
        text_surface = self.font.render(text, True, color)
        outline = pygame.Surface((text_surface.get_width() + 4, text_surface.get_height() + 4), pygame.SRCALPHA)
        for dx in [-2, 0, 2]:
            for dy in [-2, 0, 2]:
                if dx != 0 or dy != 0:
                    outline.blit(self.font.render(text, True, outline_color), (2 + dx, 2 + dy))
        outline.blit(text_surface, (2, 2))
        return outline

    def run(self):
        selected_map_class = None
        while not selected_map_class:
            self.screen.blit(self.background, (0, 0))

            # Título centralizado com contorno
            title_surface = self.render_text_with_outline("Escolha o Mapa")
            self.screen.blit(title_surface, (self.screen.get_width() // 2 - title_surface.get_width() // 2, 40))

            buttons = []

            total_width = len(self.maps) * 250 + (len(self.maps) - 1) * 60
            start_x = (self.screen.get_width() - total_width) // 2

            for i, map_data in enumerate(self.maps):
                x = start_x + i * (250 + 60)
                y = 180
                rect = pygame.Rect(x, y, 250, 250)

                shadow_rect = rect.copy().inflate(8, 8)
                pygame.draw.rect(self.screen, (0, 0, 0), shadow_rect, border_radius=8)

                image = pygame.image.load(map_data["image"]).convert()
                image = pygame.transform.scale(image, (250, 250))
                self.screen.blit(image, rect.topleft)

                # Nome com contorno
                name_surface = self.render_text_with_outline(map_data["name"])
                self.screen.blit(name_surface, (
                    rect.centerx - name_surface.get_width() // 2,
                    rect.bottom + 10
                ))

                buttons.append((rect, map_data["class"]))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for rect, map_class in buttons:
                        if rect.collidepoint(mouse_pos):
                            selected_map_class = map_class

            self.clock.tick(60)

        return selected_map_class
