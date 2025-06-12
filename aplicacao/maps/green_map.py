import pygame
from core.map import GameMapBase
from settings import TILE_SIZE, DARK_GRAY, GREEN

class GreenMap(GameMapBase):
    def generate_path(self):
        path = [
            (0, 3), (1, 3), (2, 3), (3, 3),
            (3, 4), (3, 5), (4, 5), (5, 5),
            (5, 6), (5, 7), (6, 7), (7, 7), (8, 7), (9, 7)
        ]
        for row, col in path:
            self.grid[row][col] = 1
        return path

    def generate_build_slots(self):
        return [
            (1, 2), (2, 4), (4, 4), (6, 6),
            (6, 8), (7, 6), (8, 6), (8, 8)
        ]

    def draw_tile(self, surface, rect, row, col):
        if self.grid[row][col] == 1:
            color = GREEN  # Caminho
        else:
            color = DARK_GRAY  # Chão comum

        pygame.draw.rect(surface, color, rect)

        if (row, col) in self.build_slots:
            pygame.draw.rect(surface, (0, 100, 200), rect, 2)  # Slots de construção em azul escuro

        pygame.draw.rect(surface, (30, 30, 30), rect, 1)  # Grade
