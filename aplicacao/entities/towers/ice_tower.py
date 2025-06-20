import pygame
from entities.tower import TowerBase

class IceTower(TowerBase):
<<<<<<< HEAD
    def __init__(self, grid_pos, image):
        super().__init__(grid_pos, image)
=======
    COST = 60
    def __init__(self, grid_pos):
        super().__init__(grid_pos)
>>>>>>> c087b3443128c469a952b6add9881c281bcd8c65
        self.damage = 15
        self.range = 100
        self.fire_rate = 0.8
        self.radius = 10
        self.cost = 60

    def shoot(self, enemy):
        super().shoot(enemy)
        # enemy.slow(0.5, duration=2.0)  # Supondo que o inimigo tem método slow()

    def draw(self, screen):
        pygame.draw.circle(screen, (100, 200, 255), self.pos, self.radius)
        s = pygame.Surface((self.range * 2, self.range * 2), pygame.SRCALPHA)
        pygame.draw.circle(s, (100, 200, 255, 40), (self.range, self.range), self.range)
        screen.blit(s, (self.pos[0] - self.range, self.pos[1] - self.range))

    def method(self):
        print("Torre de Gelo")

