import pygame
from entities.enemy import Enemy
from assets.drawAnimated import AnimatedSprite

class BeeEnemy(Enemy):

    def __init__(self, path: str, image: str, folder: str):
        super().__init__(path, image, folder)
    
        self.speed = 15
        self.damage = 25
        self.folder = folder


