import pygame

class TowerActionMenu:
    def __init__(self):
        self.visible = False
        self.tower = None
        self.rect = pygame.Rect(0, 0, 140, 90)  # Largura aumentada para texto
        self.font = pygame.font.SysFont(None, 24)

        self.buttons = {
            "upgrade": pygame.Rect(0, 0, 120, 30),
            "sell": pygame.Rect(0, 0, 120, 30)
        }

    def open(self, tower, pos):
        self.tower = tower
        self.rect.topleft = pos
        self.visible = True
        self._update_button_positions()

    def _update_button_positions(self):
        x, y = self.rect.topleft
        self.buttons["upgrade"].topleft = (x + 10, y + 10)
        self.buttons["sell"].topleft = (x + 10, y + 50)

    def draw(self, surface):
        if not self.visible:
            return

        pygame.draw.rect(surface, (50, 50, 50), self.rect)
        pygame.draw.rect(surface, (255, 255, 255), self.rect, 2)

        for label, rect in self.buttons.items():
            pygame.draw.rect(surface, (100, 100, 100), rect)
            if label == "upgrade" and self.tower:
                # Supondo que sua torre tem método ou atributo para custo upgrade
                upgrade_cost = getattr(self.tower, "get_upgrade_cost", lambda: None)()
                if upgrade_cost is None:
                    upgrade_text = "Upgrade"
                else:
                    upgrade_text = f"Upgrade (${upgrade_cost})"
                text = self.font.render(upgrade_text, True, (255, 255, 255))
            else:
                text = self.font.render(label.capitalize(), True, (255, 255, 255))

            surface.blit(text, (rect.centerx - text.get_width() // 2, rect.centery - text.get_height() // 2))

    def handle_event(self, event):
        if not self.visible or event.type != pygame.MOUSEBUTTONDOWN:
            return None

        if self.buttons["upgrade"].collidepoint(event.pos):
            self.visible = False
            return "upgrade"
        elif self.buttons["sell"].collidepoint(event.pos):
            self.visible = False
            return "sell"
        else:
            self.visible = False
        return None
