import pygame

class TowerMenu:
    def __init__(self, position, assets):
        self.position = position
        self.options = [
            ("Fire", assets["fogo"]),
            ("Ice", assets["gelo"]),
            ("Sniper", assets["alvo"])
        ]
        self.buttons = []
        self.visible = True
        self.create_buttons()

    def create_buttons(self):
        x, y = self.position
        for i, (label, image) in enumerate(self.options):
            rect = pygame.Rect(x, y + i * 70, 64, 64) # espaço vertical maior
            self.buttons.append((label, image, rect))

    def draw(self, surface):
        if not self.visible:
            return
        for label, image, rect in self.buttons:
            pygame.draw.rect(surface, (50, 50, 50), rect)  # fundo do botão

            # Redimensiona a imagem para caber no botão (ex: 64x64 ou menor)
            resized_image = pygame.transform.scale(image, (rect.width - 6, rect.height - 6))
            surface.blit(resized_image, (rect.x + 3, rect.y + 3))

            # Borda branca
            pygame.draw.rect(surface, (255, 255, 255), rect, 2)


    def handle_event(self, event):
        if not self.visible or event.type != pygame.MOUSEBUTTONDOWN:
            return None

        mouse_pos = event.pos
        for label, _, rect in self.buttons:
            if rect.collidepoint(mouse_pos):
                self.visible = False
                return label

        self.visible = False
        return None
