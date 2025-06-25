import pygame
from settings import TILE_SIZE, GREEN, RED
from entities.tower import TowerBase
from util.utils import grid_to_pixel,pixel_to_grid
from core.map import GameMapBase
from entities.player import Player

class TowerPlacer:
    def __init__(self, game_map, towers, player):
        self.map = game_map
        self.towers = towers
        self.player = player
        self.selected_tower_type = None
        self.create_tower_fn = None
        self.message_manager = None

        self.mouse_tile = (0, 0)
        self.valid = False

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.mouse_tile = pixel_to_grid(mouse_pos)
        self.valid = self.map.is_buildable(self.mouse_tile) and not self.is_occupied()

    def is_occupied(self):
        return any(tower.grid_pos == self.mouse_tile for tower in self.towers)

    def set_selected_tower(self, tower_type, create_fn, message_manager):
        print(f"[DEBUG] Torre selecionada: {tower_type}")
        self.selected_tower_type = tower_type
        self.create_tower_fn = create_fn
        self.message_manager = message_manager

    def handle_click(self):
        if not self.selected_tower_type or not self.create_tower_fn:
            return False
        if not self.valid:
            self.message_manager.show("Local inválido ou já ocupado!")
            return False
        tower = self.create_tower_fn(self.mouse_tile)
        if not self.player.can_afford(tower.cost):
            self.message_manager.show("Ouro insuficiente!")
            self.selected_tower_type = None
            self.create_tower_fn = None
            return False
        self.player.gold -= tower.cost
        self.towers.append(tower)
        self.selected_tower_type = None
        self.create_tower_fn = None
        return True

    def clear_selection(self):
        self.selected_tower_type = None
        self.create_tower_fn = None

    def draw(self, surface):
        self.update()
        row, col = self.mouse_tile
        rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        color = (0, 255, 0) if self.valid else (255, 0, 0)
        pygame.draw.rect(surface, color, rect, 2)



    def can_afford_selected(self):
        if not self.selected_type:
            return False
        from entities.towers.fire_tower import FireTower
        from entities.towers.ice_tower import IceTower
        from entities.towers.sniper_tower import SniperTower
        cost_map = {
            "Fire": FireTower.COST,
            "Ice": IceTower.COST,
            "Sniper": SniperTower.COST
        }
        cost = cost_map.get(self.selected_type, float("inf"))
        return self.player.gold >= cost    
