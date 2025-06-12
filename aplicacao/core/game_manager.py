# game_manager.py
import pygame
from settings import TILE_SIZE
from entities.towers.fire_tower import FireTower
from entities.towers.ice_tower import IceTower
from entities.towers.sniper_tower import SniperTower
from entities.player import Player
from core.tower_placer import TowerPlacer
from core.wave_manager import WaveManager
from maps.green_map import GreenMap
from ui.hud import HUD
from ui.tower_menu import TowerMenu
from ui.message_manager import MessageManager

from util.utils import pixel_to_grid

class GameManager:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.map = GreenMap()
        self.towers = []
        self.enemies = []
        self.ui = HUD()
        self.spawn_timer = 0
        self.player = Player()
        self.message_manager = MessageManager()
        self.tower_placer = TowerPlacer(self.map, self.towers, self.player)
        self.wave_manager = WaveManager(self.map.get_path())
        self.spawn_interval = 2  # segundos
        self.current_wave = 1
        self.base_hp = 100
        self.TOWER_TYPES = {
            "Fire": FireTower,
            "Ice": IceTower,
            "Sniper": SniperTower
        }
        self.tower_images = {
            "fire": pygame.image.load("assets/towers/fogo.png").convert_alpha(),
            "ice": pygame.image.load("assets/towers/gelo.png").convert_alpha(),
            "sniper": pygame.image.load("assets/towers/alvo.png").convert_alpha()
        }
        self.tower_menu = TowerMenu((10, 300), self.tower_images, [
        ("Fire", self.tower_images["fire"], 50),
        ("Ice", self.tower_images["ice"], 60),
        ("Sniper", self.tower_images["sniper"], 80),
    ])






    def update(self, dt):
        self.map.update()
        self.tower_placer.update()
        self.message_manager.update(dt)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.tower_placer.handle_click()

        # Atualiza onda (spawn de inimigos)
        self.wave_manager.update(dt, self.enemies)

        # Atualiza torres e inimigos
        for tower in self.towers:
            tower.update(dt, self.enemies)

        for enemy in self.enemies:
            enemy.update(dt)
        
        
        for e in self.enemies:
            if e.reached_end():
                self.base_hp -= e.damage

        for e in self.enemies:
            if not e.is_alive() and not e.rewarded:
               self.player.gold += e.reward
               e.rewarded  =  True    

        if self.tower_menu:
            self.tower_menu.update()    

        # Remove inimigos mortos ou que chegaram ao fim
        self.enemies = [e for e in self.enemies if e.is_alive() and not e.reached_end()]
       

        # Inicia próxima onda se não houver nenhuma em progresso e não houver inimigos vivos
        if not self.wave_manager.is_in_progress() and not self.enemies:
            self.wave_manager.start_next_wave()




    def draw(self):
        self.map.draw(self.screen)

        for tower in self.towers:
            tower.draw(self.screen)

        for enemy in self.enemies:
            enemy.draw(self.screen)

        self.tower_placer.draw(self.screen)

        wave_number = self.wave_manager.current_wave
        enemies_alive = len(self.enemies)
        base_hp = self.base_hp

        self.message_manager.draw(self.screen)


        self.tower_menu.draw(self.screen)
        if self.tower_menu.selected:
            mouse_pos = pygame.mouse.get_pos()
            tower_image = self.tower_images[self.tower_menu.selected.lower()]
            preview = pygame.transform.scale(tower_image, (TILE_SIZE, TILE_SIZE))
            self.screen.blit(preview, (mouse_pos[0] - TILE_SIZE // 2, mouse_pos[1] - TILE_SIZE // 2))

        self.ui.draw(self.screen, wave_number, enemies_alive, base_hp)
        self.draw_gold(self.screen, self.player, pygame.font.SysFont(None, 30))


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.tower_menu.handle_event(event)
            if self.tower_menu.selected:
                self.try_build_tower(self.tower_menu.selected)


    def try_build_tower(self, tower_type):
        pos = pygame.mouse.get_pos()
        grid_pos = pixel_to_grid(pos)
        tower_class = self.TOWER_TYPES.get(tower_type)

        if tower_class and self.map.is_buildable(grid_pos):
            cost = tower_class.COST
            if self.player.can_afford(cost):
                tower = tower_class(grid_pos)
                self.towers.append(tower)
                self.player.gold -= cost
                self.tower_menu.selected = None  # só limpa se construiu
            else:
                self.message_manager.show("Ouro insuficiente para construir essa torre!")

                   




    def draw_gold(self, surface, player, font):
        text = font.render(f"Ouro: {player.gold}", True, (255, 255, 0))
        surface.blit(text, (10, 100))

    def create_tower_by_type(self, tower_type, grid_pos):
            if tower_type == "Fire":
                from entities.towers.fire_tower import FireTower
                return FireTower(grid_pos)
            elif tower_type == "Ice":
                from entities.towers.ice_tower import IceTower
                return IceTower(grid_pos)
            elif tower_type == "Sniper":
                from entities.towers.sniper_tower import SniperTower
                return SniperTower(grid_pos)
            return None     