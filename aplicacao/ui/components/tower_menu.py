import pygame

class TowerMenu:
    def __init__(self, position, assets, tower_data):
        self.position = position
        self.assets = assets
        self.options = tower_data  # (label, image, cost)
        self.cards = []
        self.selected = None
        self.visible = True
        self.card_width = 160
        self.card_height = 80
        self.padding = 10
        self.animation_speed = 8
        self.font = pygame.font.SysFont(None, 20)  # Criar fonte uma vez
        self.create_cards()

    def create_cards(self):
        x, start_y = self.position
        for i, (label, image, cost) in enumerate(self.options):
            target_y = start_y + i * (self.card_height + self.padding)
            card = {
                "label": label,
                "image": image,
                "cost": cost,
                "rect": pygame.Rect(x, start_y, self.card_width, self.card_height),
                "current_y": start_y - 100,  # começa fora da tela
                "target_y": target_y
            }
            self.cards.append(card)

    def update(self):
        for card in self.cards:
            dy = card["target_y"] - card["current_y"]
            if abs(dy) > 1:
                card["current_y"] += dy * 0.2  # interpolação suave
            else:
                card["current_y"] = card["target_y"]

    def draw(self, surface):
        if not self.visible:
            return
        for card in self.cards:
            rect = pygame.Rect(card["rect"].x, card["current_y"], self.card_width, self.card_height)

            pygame.draw.rect(surface, (40, 40, 40), rect, border_radius=6)
            # Borda diferente se selecionado
            border_color = (255, 215, 0) if card["label"] == self.selected else (255, 255, 255)
            pygame.draw.rect(surface, border_color, rect, 3 if card["label"] == self.selected else 2, border_radius=6)

            resized_img = pygame.transform.scale(card["image"], (48, 48))
            surface.blit(resized_img, (rect.x + 10, rect.y + 16))

            name = self.font.render(card["label"], True, (255, 255, 255))
            cost = self.font.render(f"Custo: {card['cost']}", True, (255, 215, 0))
            surface.blit(name, (rect.x + 70, rect.y + 10))
            surface.blit(cost, (rect.x + 70, rect.y + 40))

    def handle_event(self, event):
        if not self.visible or event.type != pygame.MOUSEBUTTONDOWN:
            return None
        mouse_pos = event.pos
        for card in self.cards:
            rect = pygame.Rect(card["rect"].x, card["current_y"], self.card_width, self.card_height)
            if rect.collidepoint(mouse_pos):
                self.selected = card["label"]
                return card["label"]
        # Clique fora dos cards deseleciona
        self.selected = None
        return None

