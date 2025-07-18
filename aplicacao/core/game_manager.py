import pygame
from settings import TILE_SIZE
from entities.player import Player
from core.tower_placer import TowerPlacer
from core.wave_manager import WaveManager
from ui.hud import HUD
from ui.components.message_manager import MessageManager
from ui.components.tower_menu import TowerMenu
from ui.components.tower_action_menu import TowerActionMenu
from util.utils import pixel_to_grid
from entities.towers.fire_tower import FireTower
from entities.towers.ice_tower import IceTower
from entities.towers.sniper_tower import SniperTower
from core.map import GameMapBase

class GameManager:
    def __init__(self, screen: pygame.Surface, difficulty: str, map_class: GameMapBase):
        self.screen = screen
        self.score = 0
        self.clock = pygame.time.Clock()
        self.difficulty = difficulty
        self.map = map_class

        self.towers = []
        self.enemies = []
        self.enemy_types = self.map.get_enemy_types()
        self.projectiles = []
        self.player = Player()
        self.game_won = False
        self.base_hp = 100
        self.max_waves_by_difficulty = {
            "easy": 10,
            "medium": 30,
            "hard": 45
        }
        if difficulty != "endless":
            self.max_waves = self.max_waves_by_difficulty.get(difficulty, 5)
        else:
            self.max_waves = float("inf")
        self.ui = HUD()
        self.message_manager = MessageManager()
        self.tower_placer = TowerPlacer(self.map, self.towers, self.player)
        self.wave_manager = WaveManager(self.map.get_path(), difficulty,self.enemy_types)
        self.tower_action_menu = TowerActionMenu()

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
            ("Fire", self.tower_images["fire"], FireTower.COST),
            ("Ice", self.tower_images["ice"], IceTower.COST),
            ("Sniper", self.tower_images["sniper"], SniperTower.COST),
        ])

    def update(self, dt: int):
        if self.game_won:
            return

       
        self._update_components(dt)
        self._update_projectiles(dt)
        self._update_enemies(dt)
        self._remove_defeated_enemies()
        self._progress_waves()



    def _update_components(self, dt: int):
        self.map.update()
        self.tower_placer.update()
        self.message_manager.update(dt)
        self.tower_menu.update()
        self.wave_manager.update(dt, self.enemies)

        for tower in self.towers:
            projectile = tower.update(dt, self.enemies)  # só uma chamada
            tower.sprite.update(dt)
            if projectile:
                self.projectiles.append(projectile)
            
        for enemy in self.enemies:
            enemy.update(dt)

    def _update_enemies(self, dt: int):
        for enemy in self.enemies:
            enemy.update(dt)
            if enemy.reached_end():
                self.base_hp -= enemy.damage
            elif not enemy.is_alive() and not enemy.rewarded:
                self.player.gold += enemy.reward
                enemy.rewarded = True
                if self.difficulty == "endless":
                    self.score += 1     

    def _remove_defeated_enemies(self):
      self.enemies = [e for e in self.enemies if e.is_alive() and not e.reached_end()]   

    def _progress_waves(self):
        wave_over = self.wave_manager.is_wave_over(self.enemies)

        if self.difficulty == "endless":
            if wave_over and not self.wave_manager.is_in_progress():
                self.wave_manager.start_next_wave()
        else:
            if wave_over:
                if self.wave_manager.current_wave >= self.max_waves:
                    self.game_won = True
                else:
                    self.wave_manager.start_next_wave()
    
    def _update_projectiles(self, dt: float):
        for proj in self.projectiles:
            proj.update(dt)
        # Remove projéteis que chegaram ao destino
        self.projectiles = [p for p in self.projectiles if not p.has_reached_target()]

    def draw(self):
        self.map.draw(self.screen)

        for tower in self.towers:
            tower.draw(self.screen)

        for enemy in self.enemies:
            enemy.draw(self.screen)

        for proj in self.projectiles:
            proj.draw(self.screen)

        self.tower_placer.draw(self.screen)    

    
        self.message_manager.draw(self.screen)

        self.tower_menu.draw(self.screen)
        if self.tower_menu.selected:
            mouse_pos = pygame.mouse.get_pos()
            tower_image = self.tower_images[self.tower_menu.selected.lower()]
            preview = pygame.transform.scale(tower_image, (TILE_SIZE, TILE_SIZE))
            self.screen.blit(preview, (mouse_pos[0] - TILE_SIZE // 2, mouse_pos[1] - TILE_SIZE // 2))

        self.tower_action_menu.draw(self.screen)    

        self.ui.draw(
            self.screen,
            self.wave_manager.current_wave,
            len(self.enemies),
            self.base_hp,
            self.player.gold,
            is_endless=(self.difficulty == "endless"),
            score=self.score,
            max_waves=self.max_waves if self.difficulty != "endless" else 0
        )

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos

            # 1. Botão Pause
            if self.ui.pause_button_rect.collidepoint(mouse_pos):
                return "pause"

            # 2. Seleciona torre no menu lateral
            selected_type = self.tower_menu.handle_event(event)
            if selected_type:
                def create_fn(grid_pos):
                    return self.create_tower_by_type(selected_type, grid_pos)

                self.tower_placer.set_selected_tower(
                    selected_type,
                    create_fn,
                    self.message_manager
                )
                self.tower_action_menu.visible = False  # fecha menu ação
                return

            # 3. Clicar em torre já construída abre menu de ação
            for tower in self.towers:
                if tower.rect.collidepoint(mouse_pos):
                    self.tower_action_menu.open(tower, mouse_pos)
                    self.tower_menu.selected = None  # cancela seleção menu torre
                    self.tower_placer.clear_selection()
                    return

            # 4. Clique no menu de ação (upgrade, vender)
            result = self.tower_action_menu.handle_event(event)
            if result == "sell" and self.tower_action_menu.tower:
                self.sell_tower(self.tower_action_menu.tower)
                return
            elif result == "upgrade" and self.tower_action_menu.tower:
                self.upgrade_tower(self.tower_action_menu.tower)
                return

            # 5. Clique no mapa para construir torre se estiver selecionada
            if self.tower_placer.selected_tower_type:
                built = self.tower_placer.handle_click()
                if built:
                    print("[DEBUG] Torre construída com sucesso")
                else:
                    print("[DEBUG] Falha ao construir torre")
            return


                



    def try_build_tower(self, tower_type: str):
        pos = pygame.mouse.get_pos()
        grid_pos = pixel_to_grid(pos)
        tower_class = self.TOWER_TYPES.get(tower_type)

        if tower_class and self.map.is_buildable(grid_pos):
            cost = tower_class.COST
            if self.player.can_afford(cost):
                tower = self.create_tower_by_type(tower_type, grid_pos)
                self.towers.append(tower)
                self.player.gold -= cost
                self.tower_menu.selected = None
            else:
                self.message_manager.show("Ouro insuficiente para construir essa torre!")

    def draw_gold(self, surface: pygame.surface.Surface, player: Player, font):
        text = font.render(f"Ouro: {player.gold}", True, (255, 255, 0))
        surface.blit(text, (10, 100))

    def create_tower_by_type(self, tower_type: str, grid_pos: tuple[int]):
            if tower_type == "Fire":
                from entities.towers.fire_tower import FireTower
                return FireTower(grid_pos, "redMoon.png",folder="assets/towers/")
            elif tower_type == "Ice":
                from entities.towers.ice_tower import IceTower
                return IceTower(grid_pos, "Obelisk.png",folder="assets/towers/")
            elif tower_type == "Sniper":
                from entities.towers.sniper_tower import SniperTower
                return SniperTower(grid_pos, "4.png",folder="assets/towers/")
            return None     
    
    def draw_score(self, surface, font):
        text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        surface.blit(text, (10, 130))


    def sell_tower(self, tower):
        self.player.gold += tower.get_sell_value()  
        self.towers.remove(tower)

    def upgrade_tower(self, tower):
        upgrade_cost = tower.get_upgrade_cost()
        if self.player.gold >= upgrade_cost:
            self.player.gold -= upgrade_cost
            tower.upgrade()
        else:
            self.message_manager.show("Ouro insuficiente para upgrade!")
