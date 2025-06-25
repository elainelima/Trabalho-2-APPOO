import pygame
from abc import ABC, abstractmethod
from settings import TILE_SIZE, MAP_ROWS, MAP_COLS

class GameMapBase(ABC):
    def __init__(self):
        self.grid = [[0 for _ in range(MAP_COLS)] for _ in range(MAP_ROWS)]
        self.path = self.generate_path()
        self.build_slots = self.generate_build_slots()

    @abstractmethod
    def generate_path(self):
        pass

    @abstractmethod
    def generate_build_slots(self):
        pass

    def get_path(self):
        return [(col * TILE_SIZE, row * TILE_SIZE) for row, col in self.path]

    def update(self):
        pass

    def draw(self, surface: pygame.surface.Surface):
        for row in range(MAP_ROWS):
            for col in range(MAP_COLS):
                rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                self.draw_tile(surface, rect, row, col)

    @abstractmethod
    def draw_tile(self, surface: pygame.surface.Surface, rect: pygame.Rect, row: int, col: int):
        pass

    @abstractmethod
    def get_enemy_types(self):
        pass

    def is_buildable(self, tile_pos: tuple):
        row, col = tile_pos
        if row < 0 or col < 0 or row >= MAP_ROWS or col >= MAP_COLS:
            return False
        return self.grid[row][col] == 0 and (row, col) in self.build_slots
