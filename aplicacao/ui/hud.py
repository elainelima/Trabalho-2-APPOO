import pygame
from settings import WHITE

class HUD:
    def __init__(self):
        self.font = pygame.font.SysFont(None, 28)
        self.large_font = pygame.font.SysFont(None, 32)

        # Carregar ícones
        self.heart_icon = pygame.image.load("assets/icons/heart.png").convert_alpha()
        self.coin_icon = pygame.image.load("assets/icons/coin.png").convert_alpha()
        self.pause_icon = pygame.image.load("assets/icons/pause.png").convert_alpha()
        self.pause_icon = pygame.transform.scale(self.pause_icon, (24, 24))
        self.pause_button_rect = pygame.Rect(900, 10, 30, 30)  # Ajustado ao tamanho do ícone

        # Redimensionar ícones para caber na barra
        self.heart_icon = pygame.transform.scale(self.heart_icon, (24, 24))
        self.coin_icon = pygame.transform.scale(self.coin_icon, (24, 24))

        self.pause_button_rect = pygame.Rect(900, 10, 50, 30) 

    def draw(self, surface, current_wave, enemy_count, base_hp, player_gold, is_endless=False, score=0, max_waves=0):
        # Barra de fundo
        pygame.draw.rect(surface, (0, 0, 0, 150), pygame.Rect(0, 0, surface.get_width(), 50))  
        pygame.draw.rect(surface, (30, 30, 30), pygame.Rect(0, 0, surface.get_width(), 50))
        pygame.draw.rect(surface, (60, 60, 60), self.pause_button_rect, border_radius=6)
        surface.blit(self.pause_icon, (
            self.pause_button_rect.x + (self.pause_button_rect.width - self.pause_icon.get_width()) // 2,
            self.pause_button_rect.y + (self.pause_button_rect.height - self.pause_icon.get_height()) // 2
        ))

        def render_info(label, value, icon=None, icon_color=None, text_color=(255, 255, 255), x_offset=0):
            if icon:
                surface.blit(icon, (x_offset, 13))
                x_offset += icon.get_width() + 6
            label_surf = self.font.render(f"{label}", True, (180, 180, 180))
            value_surf = self.large_font.render(str(value), True, text_color)
            surface.blit(label_surf, (x_offset, 10))
            surface.blit(value_surf, (x_offset, 25))

        # Vida - vermelho com coração
        render_info("Vida", base_hp, icon=self.heart_icon, text_color=(220, 20, 60), x_offset=20)
        # Ouro - dourado com moeda
        render_info("Ouro", player_gold, icon=self.coin_icon, text_color=(255, 215, 0), x_offset=140)

        # Wave ou Score
        wave_x = 260
        wave_label = "Score" if is_endless else "Wave"
        wave_value = score if is_endless else f"{current_wave}/{max_waves}"
        render_info(wave_label, wave_value, x_offset=wave_x)

        # Inimigos restantes
        render_info("Inimigos", enemy_count, x_offset=400)
        

