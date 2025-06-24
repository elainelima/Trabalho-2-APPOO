import pygame
from abc import ABC, abstractmethod
from util.utils import grid_to_pixel
from assets.drawAnimated import AnimatedSprite
from settings import TILE_SIZE
from entities.enemy import Enemy

class TowerBase(ABC):
    COST = 25

    def __init__(self, grid_pos: int, image: str):
        self.grid_pos = grid_pos
        self.pos = grid_to_pixel(grid_pos)
        self.time_since_last_shot = 0
        self.sprite = AnimatedSprite(image, self.pos, 6, 30)  # já deve posicionar pelo centro

    def update(self, dt: float, enemies: list[Enemy]):
        self.time_since_last_shot += dt
        target = self.find_target(enemies)
        projectile = None

        if target and self.time_since_last_shot >= 1 / self.fire_rate:
            projectile = self.shoot(target)
            self.time_since_last_shot = 0

        self.sprite.update(dt)
        return projectile

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
        # Desenha o sprite animado centralizado
        screen.blit(self.sprite.image, self.sprite.rect)

        # Desenha o raio de alcance com transparência
        alcance_surface = pygame.Surface((self.range * 2, self.range * 2), pygame.SRCALPHA)
        pygame.draw.circle(alcance_surface, (100, 200, 255, 40), (self.range, self.range), self.range)
        screen.blit(alcance_surface, (self.pos[0] - self.range, self.pos[1] - self.range))

        # Desenha um círculo no centro da torre (útil para debugging ou efeitos)
        pygame.draw.circle(screen, (100, 200, 255), self.pos, self.radius, 1)


    @abstractmethod
    def method(self):
        pass

