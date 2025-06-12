import pygame
from entities.tower import TowerBase

class FireTower(TowerBase):
    def __init__(self, grid_pos):
        super().__init__(grid_pos)
        self.damage = 50
        self.range = 80
        self.fire_rate = 1.2

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 80, 0), self.pos, self.radius)
        s = pygame.Surface((self.range * 2, self.range * 2), pygame.SRCALPHA)
        pygame.draw.circle(s, (255, 100, 0, 60), (self.range, self.range), self.range)
        screen.blit(s, (self.pos[0] - self.range, self.pos[1] - self.range))
