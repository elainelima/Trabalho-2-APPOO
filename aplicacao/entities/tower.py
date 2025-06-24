import pygame
from abc import ABC, abstractmethod
from util.utils import grid_to_pixel
from assets.drawAnimated import AnimatedSprite
from settings import TILE_SIZE
from entities.enemy import Enemy

class TowerBase(ABC):
    def __init__(self, grid_pos: int, image: str,folder: str = ""):
        self.grid_pos = grid_pos
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

    def draw(self, screen: pygame.surface.Surface):
        # Desenha o sprite animado centralizado na posição
        screen.blit(self.sprite.image, self.sprite.rect)

        # Desenha o raio de alcance com transparência
        alcance_surface = pygame.Surface((self.range * 2, self.range * 2), pygame.SRCALPHA)
        pygame.draw.circle(alcance_surface, (100, 200, 255, 40), (self.range, self.range), self.range)
        screen.blit(alcance_surface, (self.pos[0] - self.range, self.pos[1] - self.range))

        # Remove o círculo azul central (comentado ou removido)
        # pygame.draw.circle(screen, (100, 200, 255), self.pos, self.radius, 1)

        # Renderiza o nível ou "MAX" centralizado acima da torre
        font = pygame.font.SysFont(None, 20)
        level_label = "MAX" if self.level >= self.max_level else f"Lv {self.level}"
        level_text = font.render(level_label, True, (255, 255, 0))

        # Centraliza o texto horizontalmente acima da torre (considerando self.sprite.rect)
        text_x = self.sprite.rect.centerx - level_text.get_width() // 2
        text_y = self.sprite.rect.top - level_text.get_height() # 5 pixels acima da torre

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

