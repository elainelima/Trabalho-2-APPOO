import pygame
from entities.tower import TowerBase
from assets.drawAnimated import AnimatedSprite

class IceTower(TowerBase):
    def __init__(self, grid_pos, image):
        super().__init__(grid_pos, image)
        self.damage = 15
        self.range = 100
        self.fire_rate = 0.8
        self.radius = 10
        self.cost = 60
        self.sprite = AnimatedSprite(image, self.pos, 14, 30)

    def shoot(self, enemy):
        super().shoot(enemy)
        # enemy.slow(0.5, duration=2.0)  # Supondo que o inimigo tem método slow()

    def method(self):
        print("Torre de Gelo")

