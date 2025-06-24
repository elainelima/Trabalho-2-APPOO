import pygame
from entities.tower import TowerBase
from assets.drawAnimated import AnimatedSprite
from assets.effects.fire_projectile import FireProjectile

class FireTower(TowerBase):
    def __init__(self, grid_pos: tuple[int], image: str, folder: str):
        super().__init__(grid_pos, image,folder)
        self.damage = 50
        self.range = 80
        self.fire_rate = 0.2
        self.radius = 20
        self.cost = 50
        self.sprite = AnimatedSprite(image, self.pos, 11, y_offset=30, folder=folder, dynamic=False)

    def method(self):
        print("Torre de Fogo")

    def shoot(self, enemy):
        enemy.take_damage(self.damage)
        return FireProjectile(self.pos, enemy.pos)
    