import pygame
from settings import TILE_SIZE, GREEN, RED, MAP_ROWS, MAP_COLS
from entities.tower import Tower

class TowerPlacer:
    def __init__(self, game_map, towers):
        self.map = game_map
        self.towers = towers
        self.valid = False
        self.mouse_tile = (0, 0)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.mouse_tile = (mouse_pos[0] // TILE_SIZE, mouse_pos[1] // TILE_SIZE)
        self.valid = self.map.is_buildable(self.mouse_tile) and not self.is_occupied()

    def is_occupied(self):
        for tower in self.towers:
            tower_tile_x = tower.pos[0] // TILE_SIZE
            tower_tile_y = tower.pos[1] // TILE_SIZE
            if (tower_tile_x, tower_tile_y) == self.mouse_tile:
                return True
        return False

    def handle_click(self):
        if self.valid:
            tile_x, tile_y = self.mouse_tile
            pos = (tile_x * TILE_SIZE + TILE_SIZE // 2, tile_y * TILE_SIZE + TILE_SIZE // 2)
            new_tower = Tower(pos)
            self.towers.append(new_tower)

    def draw(self, surface):
        rect = pygame.Rect(self.mouse_tile[0] * TILE_SIZE, self.mouse_tile[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        color = GREEN if self.valid else RED
        pygame.draw.rect(surface, color, rect, 2)
