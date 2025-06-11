import pygame
from settings import TILE_SIZE, GREEN, RED, MAP_ROWS, MAP_COLS
from entities.tower import Tower
from util.utils import grid_to_pixel,pixel_to_grid
class TowerPlacer:
    def __init__(self, game_map, towers, player):
        self.map = game_map
        self.towers = towers
        self.player = player
        self.valid = False
        self.mouse_tile = (0, 0)  # (row, col)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.mouse_tile = pixel_to_grid(mouse_pos)  # converte pixels -> (row, col)
        self.valid = self.map.is_buildable(self.mouse_tile) and not self.is_occupied()

    def is_occupied(self):
        for tower in self.towers:
            if tower.grid_pos == self.mouse_tile:
                return True
        return False

    def handle_click(self):
        if self.valid:
            new_tower = Tower(self.mouse_tile)
            if self.player.spend(Tower.COST):  # só gasta se puder
                self.towers.append(new_tower)

    def draw(self, surface):
        row, col = self.mouse_tile
        rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        color = GREEN if self.valid else RED
        pygame.draw.rect(surface, color, rect, 2)