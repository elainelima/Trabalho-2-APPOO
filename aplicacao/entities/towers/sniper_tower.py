import pygame
from entities.tower  import TowerBase

class SniperTower(TowerBase):
    COST = 80
    def __init__(self, grid_pos):
        super().__init__(grid_pos)
        self.damage = 45
        self.range = 200
        self.fire_rate = 1.2
        self.radius = 15
        self.cost = 80

    def draw(self, screen):
        pygame.draw.circle(screen, (200, 200, 200), self.pos, self.radius)
        s = pygame.Surface((self.range * 2, self.range * 2), pygame.SRCALPHA)
        pygame.draw.circle(s, (200, 200, 200, 30), (self.range, self.range), self.range)
        screen.blit(s, (self.pos[0] - self.range, self.pos[1] - self.range))
