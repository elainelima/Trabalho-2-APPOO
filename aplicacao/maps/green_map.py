import pygame
from core.map import GameMapBase
from entities.enemies.bee import BeeEnemy
from entities.enemies.slime import SlimeEnemy
from entities.enemies.wolf import WolfEnemy
from settings import TILE_SIZE

class GreenMap(GameMapBase):
    def generate_path(self):
        path = [
            (3, 0), (3, 1), (3, 2), (3, 3),
            (3, 4), (3, 5), (4, 5), (5, 5),
            (6, 5), (7, 5), (7, 6), (7, 7), (7, 8),
            (7, 9), (7, 10), (7, 11),(8, 11),(9, 11) , (10,11),  
        ]
        for row, col in path:
            self.grid[row][col] = 1
        return path

    def generate_build_slots(self):
        return [
            (2, 0), (2, 4), (6, 4), (6, 6),
            (6, 8), (5, 6), (8, 6), (8, 8)
        ]
    
    def get_path(self):
     return [(col * TILE_SIZE + TILE_SIZE // 2, row * TILE_SIZE + TILE_SIZE // 2) for row, col in self.path]

    def draw_tile(self, surface: pygame.surface.Surface, rect: pygame.Rect, row: int, col: int):
        if self.grid[row][col] == 1:
            tileImage = "assets/tiles/FieldsTile_01.png"
        else:
            tileImage = "assets/tiles/FieldsTile_38.png"
        
        # Gera imagem de cada quadrado do caminho ou do restante do
        image = pygame.image.load(tileImage).convert_alpha()
        image_amplified = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
        surface.blit(image_amplified, rect.topleft)

        if (row, col) in self.build_slots:
            pygame.draw.rect(surface, (0, 100, 200), rect, 4)  # Slots de construção em azul escuro

        pygame.draw.rect(surface, (30, 30, 30), rect, 1)  # Grade

    def get_enemy_types(self):
        return [BeeEnemy, SlimeEnemy,WolfEnemy]