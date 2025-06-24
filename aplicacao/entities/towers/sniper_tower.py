import pygame
from entities.tower  import TowerBase
from assets.drawAnimated import AnimatedSprite
from assets.effects.sniper_projectile import SniperProjectile

class SniperTower(TowerBase):
    COST = 80
    def __init__(self, grid_pos: tuple[int], image: str):
        super().__init__(grid_pos, image)
        self.damage = 45
        self.range = 200
        self.fire_rate = 1.2
        self.radius = 15
        self.cost = 80

    def method(self):
        print("Torre Sniper")

    def shoot(self, enemy):    
        enemy.take_damage(self.damage)
        return SniperProjectile(self.pos, enemy.pos)    

