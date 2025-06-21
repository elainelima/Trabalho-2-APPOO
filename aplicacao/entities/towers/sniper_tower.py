import pygame
from entities.tower  import TowerBase
from assets.drawAnimated import AnimatedSprite

class SniperTower(TowerBase):
    COST = 80
    def __init__(self, grid_pos, image):
        super().__init__(grid_pos, image)
        self.damage = 45
        self.range = 200
        self.fire_rate = 1.2
        self.radius = 15
        self.cost = 80

    def method(self):
        print("Torre Sniper")

