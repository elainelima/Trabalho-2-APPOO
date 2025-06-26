import pygame
from abc import ABC, abstractmethod
from util.utils import grid_to_pixel
from assets.drawAnimated import AnimatedSprite
from settings import TILE_SIZE
from entities.enemy import Enemy
import math

class TowerBase(ABC):
    def __init__(self, grid_pos: int, image: str,name:str,folder: str = "" ):
        self.grid_pos = grid_pos
        self.name = name
        self.pos = grid_to_pixel(grid_pos)
        self.time_since_last_shot = 0
        self.sprite = AnimatedSprite(image, self.pos, 6, 30,folder=folder)
        self.rect = self.sprite.image.get_rect(topleft=self.pos)
        self.level = 1
        self.max_level = 3

       

    def update(self, dt: float, enemies: list[Enemy]):
        self.time_since_last_shot += dt
        target = self.find_target(enemies)

        if target and self.time_since_last_shot >= 1 / self.fire_rate:
            self.time_since_last_shot = 0
            return self.shoot(target)

        self.sprite.update(dt)
        return None

    def find_target(self, enemies: list[Enemy]):
        for enemy in enemies:
            dist = ((self.pos[0] - enemy.pos[0]) ** 2 + (self.pos[1] - enemy.pos[1]) ** 2) ** 0.5
            if dist <= self.range and enemy.is_alive():
                return enemy
        return None
    
    @abstractmethod
    def shoot(self, enemy: Enemy):
        pass

   


    def draw(self, screen: pygame.Surface):
        mouse_pos = pygame.mouse.get_pos()
        is_hovered = self.sprite.rect.collidepoint(mouse_pos)

        # Desenha o sprite animado
        screen.blit(self.sprite.image, self.sprite.rect)

        # Se o mouse estiver sobre a torre, exibe o raio de alcance com efeitos visuais
        if is_hovered:
            # Superfície para o raio com alpha
            alcance_surface = pygame.Surface((self.range * 2, self.range * 2), pygame.SRCALPHA)

            # Animação de pulsação
            pulse = 4 * math.sin(pygame.time.get_ticks() / 300)
            dynamic_radius = int(self.range + pulse)

            # Desenha o raio com transparência
            pygame.draw.circle(
                alcance_surface,
                (100, 200, 255, 80),
                (self.range, self.range),
                dynamic_radius
            )
            screen.blit(alcance_surface, (self.pos[0] - self.range, self.pos[1] - self.range))

            # Destaque na borda da torre
            pygame.draw.rect(screen, (255, 255, 100), self.sprite.rect, 2, border_radius=8)

            # Tooltip da torre
            font = pygame.font.SysFont(None, 20)
            info_text = font.render(self.name, True, (255, 255, 255))
            tooltip_pos = (self.sprite.rect.centerx - info_text.get_width() // 2,
                        self.sprite.rect.bottom + 20)
            screen.blit(info_text, tooltip_pos)

        # Renderiza o nível da torre acima do sprite
        font = pygame.font.SysFont(None, 20)
        level_label = "MAX" if self.level >= self.max_level else f"Lv {self.level}"
        level_text = font.render(level_label, True, (255, 255, 0))
        text_x = self.sprite.rect.centerx - level_text.get_width() // 2
        text_y = self.sprite.rect.top - level_text.get_height()
        screen.blit(level_text, (text_x, text_y))

       

    def upgrade(self):
        if self.level < self.max_level:
            self.level += 1
            self.damage *= 1.5
            self.range += 10

    def get_upgrade_cost(self):
        if self.level >= self.max_level:
            return None 
        return self.UPGRADE_COSTS[self.level] 

    def get_sell_value(self):
        return int(self.cost * 0.5 + (self.level - 1) * 10)


    @abstractmethod
    def method(self):
        pass

