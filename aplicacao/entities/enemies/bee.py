import pygame
from entities.enemy import Enemy
from assets.drawAnimated import AnimatedSprite

class BeeEnemy(Enemy):

    def __init__(self, path: str):
        image = "assets/enemies/bee/D_Walk.png"
        folder= "assets/enemies/bee/"
        super().__init__(path, image, 6,folder)
        self.hp = 60
        self.speed = 15
        self.damage = 10
        self.folder = folder


