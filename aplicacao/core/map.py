# map.py
import pygame
from settings import TILE_SIZE, MAP_ROWS, MAP_COLS, DARK_GRAY, GREEN

class GameMap:
    def __init__(self):
       
        self.grid = [[0 for _ in range(MAP_COLS)] for _ in range(MAP_ROWS)]
        self.path = self.generate_path()

    def generate_path(self):
        # Exemplo fixo de caminho (linha, coluna)
        path = [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7),(7,8),(7,9)]
        for row, col in path:
            self.grid[row][col] = 1  # Marca o caminho no grid
        return path



    def get_path(self):
        # Retorna o caminho em pixels para os inimigos seguirem
        return [(col * TILE_SIZE, row * TILE_SIZE) for row, col in self.path]

    def update(self):
        pass  # Placeholder para interações futuras com o mapa

    def draw(self, surface):
        for row in range(MAP_ROWS):
            for col in range(MAP_COLS):
                rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                color = (0, 255, 0) if self.grid[row][col] == 1 else (50, 50, 50)  # Verde para caminho, cinza para chão
                pygame.draw.rect(surface, color, rect)
                pygame.draw.rect(surface, (30, 30, 30), rect, 1)  # grade fina para visualização

    
    def is_buildable(self, tile_pos):
        row, col = tile_pos
        # Verifica limites
        if row < 0 or col < 0 or row >= MAP_ROWS or col >= MAP_COLS:
            return False
        # Terreno 0 é construtível, 1 é caminho (não construtível)
        return self.grid[row][col] == 0