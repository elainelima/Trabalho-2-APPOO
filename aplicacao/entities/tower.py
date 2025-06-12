import pygame
from abc import ABC, abstractmethod
from util.utils import grid_to_pixel

class TowerBase(ABC):
    def __init__(self, grid_pos):
        self.grid_pos = grid_pos
        self.pos = grid_to_pixel(grid_pos)
        self.radius = 20
        self.range = 100
        self.fire_rate = 1
        self.time_since_last_shot = 0
        self.damage = 25

    def update(self, dt, enemies):
        self.time_since_last_shot += dt
        target = self.find_target(enemies)
        if target and self.time_since_last_shot >= 1 / self.fire_rate:
            self.shoot(target)
            self.time_since_last_shot = 0

    def find_target(self, enemies):
        for enemy in enemies:
            dist = ((self.pos[0] - enemy.pos[0]) ** 2 + (self.pos[1] - enemy.pos[1]) ** 2) ** 0.5
            if dist <= self.range and enemy.is_alive():
                return enemy
        return None

    def shoot(self, enemy):
        enemy.take_damage(self.damage)

    @abstractmethod
    def draw(self, screen):
        pass
