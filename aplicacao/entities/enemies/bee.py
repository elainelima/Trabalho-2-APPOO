import pygame
from entities.enemy import Enemy
from assets.drawAnimated import AnimatedSprite
import assets.enemies.bee

class BeeEnemy(Enemy):

    def __init__(self, path: str, image):
        super().__init__(path, image)

        self.speed = 15
        self.damage = 5


