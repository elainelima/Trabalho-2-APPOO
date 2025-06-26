import pygame
from entities.enemy import Enemy
from assets.drawAnimated import AnimatedSprite


class WolfEnemy(Enemy):

    def __init__(self, path: str,):
        image = "assets/enemies/wolf/D_Walk.png"
        folder = "assets/enemies/wolf/"
        super().__init__(path, image, 6, folder)
        self.hp = 200
        self.speed = 20
        self.damage = 35
        self.folder = folder