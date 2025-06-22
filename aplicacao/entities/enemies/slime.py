import pygame
from entities.enemy import Enemy
from assets.drawAnimated import AnimatedSprite

class SlimeEnemy(Enemy):

    def __init__(self, path: str, image: str, folder: str):
        super().__init__(path, image, folder)

        self.speed = 10
        self.damage = 10
        self.folder = folder
