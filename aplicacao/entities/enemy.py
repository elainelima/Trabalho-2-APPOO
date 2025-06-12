import pygame
from settings import TILE_SIZE, COLOR_ENEMY

class Enemy:
    def __init__(self, path):
        self.path = path  # lista de posições em pixels para seguir
        self.current_point = 0
        self.speed = 100  # pixels por segundo

        # Começa na posição do primeiro ponto do caminho
        self.pos = list(self.path[0])  # posição em pixels (x, y)
        self.radius = 15
        self.hp = 100
        self.damage = 6
        self.reward = 10
        self.alive = True
        self.rewarded = False

    def update(self, dt):
        if self.current_point + 1 < len(self.path):
            target = self.path[self.current_point + 1]
            dir_vec = (target[0] - self.pos[0], target[1] - self.pos[1])
            dist = (dir_vec[0] ** 2 + dir_vec[1] ** 2) ** 0.5

            if dist != 0:
                dir_norm = (dir_vec[0] / dist, dir_vec[1] / dist)
            else:
                dir_norm = (0, 0)

            move_dist = self.speed * dt

            if move_dist >= dist:
                self.pos = list(target)
                self.current_point += 1
            else:
                self.pos[0] += dir_norm[0] * move_dist
                self.pos[1] += dir_norm[1] * move_dist

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0 and self.alive:
            self.alive = False
        # ...

    def is_alive(self):
        return self.alive

    def reached_end(self):
        return self.current_point >= len(self.path) - 1

    def draw(self, screen):
        pygame.draw.circle(screen, COLOR_ENEMY, (int(self.pos[0]), int(self.pos[1])), self.radius)
