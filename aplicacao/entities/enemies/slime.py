import pygame
from entities.enemy import Enemy
from assets.drawAnimated import AnimatedSprite

class SlimeEnemy(Enemy):

    def __init__(self, path: str, image):
        super().__init__(path, image)

        self.speed = 10
        self.damage = 10

