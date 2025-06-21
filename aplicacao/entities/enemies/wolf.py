import pygame
from entities.enemy import Enemy
from assets.drawAnimated import AnimatedSprite


class WolfEnemy(Enemy):

    def __init__(self, path: str, image, folder):
        super().__init__(path, image, folder)

        self.hp = 1
        self.speed = 15
        self.damage = 10
        self.folder = folder