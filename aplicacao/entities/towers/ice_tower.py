import pygame
from entities.tower import TowerBase

class IceTower(TowerBase):
    def __init__(self, grid_pos):
        super().__init__(grid_pos)
        self.damage = 15
        self.range = 100
        self.fire_rate = 0.8

    def shoot(self, enemy):
        super().shoot(enemy)
        # enemy.slow(0.5, duration=2.0)  # Supondo que o inimigo tem método slow()

    def draw(self, screen):
        pygame.draw.circle(screen, (100, 200, 255), self.pos, self.radius)
        s = pygame.Surface((self.range * 2, self.range * 2), pygame.SRCALPHA)
        pygame.draw.circle(s, (100, 200, 255, 40), (self.range, self.range), self.range)
        screen.blit(s, (self.pos[0] - self.range, self.pos[1] - self.range))
