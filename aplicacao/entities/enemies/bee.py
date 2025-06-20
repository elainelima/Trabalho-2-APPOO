import pygame
from entities.enemy import Enemy
from assets.drawAnimated import AnimatedSprite
import assets.enemies.bee

class BeeEnemy(Enemy):

    def __init__(self, path: str, par: int, image):
        super.__init__(path)

        self.speed = 15
        self.damage = 5

    

    def draw(self, screen):
        
        AnimatedSprite()