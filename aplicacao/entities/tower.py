import pygame
from settings import TILE_SIZE, COLOR_TOWER

class Tower:
    def __init__(self, grid_pos):
        self.grid_pos = grid_pos  # posição no grid (coluna, linha)
        self.pos = (grid_pos[0] * TILE_SIZE + TILE_SIZE // 2,
                    grid_pos[1] * TILE_SIZE + TILE_SIZE // 2)  # centro do tile em pixels

        self.radius = 20
        self.range = 100
        self.fire_rate = 1  # tiros por segundo
        self.damage = 25
        self.time_since_last_shot = 0

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

    def draw(self, screen):
        pygame.draw.circle(screen, COLOR_TOWER, self.pos, self.radius)
        # desenha alcance
        s = pygame.Surface((self.range * 2, self.range * 2), pygame.SRCALPHA)
        pygame.draw.circle(s, (0, 0, 255, 50), (self.range, self.range), self.range)
        screen.blit(s, (self.pos[0] - self.range, self.pos[1] - self.range))
