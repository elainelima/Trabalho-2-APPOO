import pygame
from entities.tower import TowerBase
from assets.drawAnimated import AnimatedSprite
from entities.enemy import Enemy
from assets.effects.ice_projectile import IceProjectile

class IceTower(TowerBase):
    COST=60
    UPGRADE_COSTS = [60, 120, 180]
    def __init__(self, grid_pos: tuple[int], image: str,folder:str):
        super().__init__(grid_pos, image,folder)
        self.damage = 15
        self.range = 100
        self.fire_rate = 0.8
        self.radius = 10
        self.cost = 60
        self.sprite = AnimatedSprite(image, self.pos, numImages=14, y_offset=30, folder=folder,dynamic=False)

    def shoot(self, enemy: Enemy): 
        enemy.take_damage(self.damage)
        return IceProjectile(self.pos, enemy.pos)    

    def method(self):
        print("Torre de Gelo")

