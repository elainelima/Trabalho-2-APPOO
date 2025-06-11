# map.py
import pygame
from settings import TILE_SIZE, MAP_ROWS, MAP_COLS, DARK_GRAY, GREEN

class GameMap:
    def __init__(self):
        self.grid = [[0 for _ in range(MAP_COLS)] for _ in range(MAP_ROWS)]
        self.path = self.generate_path()
        self.build_slots = self.generate_build_slots()

    def generate_path(self):
        path = [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (7, 8), (7, 9)]
        for row, col in path:
            self.grid[row][col] = 1  # Caminho
        return path

    def generate_build_slots(self):
        # Define manualmente onde o jogador pode construir
        return [(1, 4), (2, 4), (3, 4), (5, 6), (6, 6), (7, 7)]

    def get_path(self):
        return [(col * TILE_SIZE, row * TILE_SIZE) for row, col in self.path]

    def update(self):
        pass

    def draw(self, surface):
        for row in range(MAP_ROWS):
            for col in range(MAP_COLS):
                rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)

                if self.grid[row][col] == 1:
                    color = GREEN  # Caminho
                else:
                    color = DARK_GRAY  # Chão comum

                pygame.draw.rect(surface, color, rect)
                
                # Slots de construção visuais
                if (row, col) in self.build_slots:
                    pygame.draw.rect(surface, (0, 0, 255), rect, 2)  # Azul para slots

                pygame.draw.rect(surface, (30, 30, 30), rect, 1)  # grade

    def is_buildable(self, tile_pos):
        row, col = tile_pos
        if row < 0 or col < 0 or row >= MAP_ROWS or col >= MAP_COLS:
            return False
        return self.grid[row][col] == 0 and (row, col) in self.build_slots
