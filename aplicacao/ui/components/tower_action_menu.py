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

        # Ajusta para ficar dentro da tela
        screen_width, screen_height = pygame.display.get_surface().get_size()
        if self.rect.right > screen_width:
            self.rect.right = screen_width - 10
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height - 10

        self.visible = True
        self._update_button_positions()

    def _update_button_positions(self):
        x, y = self.rect.topleft
        self.buttons["upgrade"].topleft = (x + 10, y + 10)
        self.buttons["sell"].topleft = (x + 10, y + 50)

    def draw(self, surface):
        if not self.visible:
            return

        mouse_pos = pygame.mouse.get_pos()

        # Sombra
        shadow_rect = self.rect.move(4, 4)
        pygame.draw.rect(surface, (0, 0, 0), shadow_rect)

        # Fundo do menu
        pygame.draw.rect(surface, (50, 50, 50), self.rect)
        pygame.draw.rect(surface, (255, 255, 255), self.rect, 2)

        for label, rect in self.buttons.items():
            # Se o botão for upgrade e a torre já estiver no nível máximo, pula o desenho
            if label == "upgrade" and self.tower and getattr(self.tower, "level", 0) >= getattr(self.tower, "max_level", 0):
                continue  # pula este botão, não desenha nem interage

            # Cor do botão muda ao passar o mouse
            color = (150, 150, 150) if rect.collidepoint(mouse_pos) else (100, 100, 100)
            pygame.draw.rect(surface, color, rect)

            if label == "upgrade" and self.tower:
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

        # Se clicou dentro dos botões, retorna a ação correspondente
        if self.buttons["upgrade"].collidepoint(event.pos):
            self.visible = False
            return "upgrade"
        elif self.buttons["sell"].collidepoint(event.pos):
            self.visible = False
            return "sell"
        
        # Se clicou fora do menu ou dos botões, fecha o menu e não retorna ação
        # (fechar menu ao clicar fora dele)
        if not self.rect.collidepoint(event.pos):
            self.visible = False
            return None

        # Se clicou dentro do menu, mas não em nenhum botão, mantém o menu aberto
        # (opcional, pode fechar também se preferir)
        return None

