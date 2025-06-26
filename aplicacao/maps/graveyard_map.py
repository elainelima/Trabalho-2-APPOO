import pygame
from core.map import GameMapBase
from settings import TILE_SIZE
from entities.enemies.ghost import GhostEnemy
from entities.enemies.skelleton import SkelletonEnemy
from entities.enemies.goblin import GoblinEnemy



class GraveyardMap(GameMapBase):
    def generate_path(self):
        path = [
            (0, 5), (1, 5), (2, 5),
            (2, 4), (2, 3), (3, 3),
            (4, 3), (5, 3), (5, 4), (5, 5),
            (6, 5), (7, 5), (8, 5),
            (8, 6), (8, 7), (7, 7), (6, 7),
            (6, 8), (6, 9), (7, 9), (8, 9),
            (9, 9), (10, 9)
        ]
        for row, col in path:
            self.grid[row][col] = 1
        return path

    def generate_build_slots(self):
        return [
            (1, 3), (1, 7), (3, 1), (4, 6),
            (6, 2), (7, 8), (9, 7), (9, 5)
        ]
    def get_path(self):
        return [(col * TILE_SIZE + TILE_SIZE // 2, row * TILE_SIZE + TILE_SIZE // 2) for row, col in self.path]

    def draw_tile(self, surface: pygame.surface.Surface, rect: pygame.Rect, row: int, col: int):
        if self.grid[row][col] == 1:
            tile_image = "assets/tiles/GraveyardTile_45.png"
        else:
            tile_image = "assets/tiles/GraveyardTile_04.png"

        image = pygame.image.load(tile_image).convert_alpha()
        image_scaled = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
        surface.blit(image_scaled, rect.topleft)

        if (row, col) in self.build_slots:
            pygame.draw.rect(surface, (255, 215, 0), rect, 3)  # Amarelo ouro, espessura maior

        pygame.draw.rect(surface, (50, 50, 50), rect, 1)  # grade leve

    def get_enemy_types(self):
        return [GhostEnemy, SkelletonEnemy,GoblinEnemy]