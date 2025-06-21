import pygame
from entities.enemy import Enemy
from assets.drawAnimated import AnimatedSprite

class BeeEnemy(Enemy):

    def __init__(self, path: str, image, folder):
        super().__init__(path, image, folder)
    
        self.speed = 15
        self.damage = 5
        self.folder = folder


