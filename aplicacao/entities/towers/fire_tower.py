import pygame
from entities.tower import TowerBase
from assets.drawAnimated import AnimatedSprite

class FireTower(TowerBase):
    def __init__(self, grid_pos, image):
        super().__init__(grid_pos, image)
        self.damage = 50
        self.range = 80
        self.fire_rate = 1.2

    def method(self):
        print("Torre de Fogo")