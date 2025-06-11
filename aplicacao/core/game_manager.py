# game_manager.py
import pygame
from settings import FPS
from core.map import GameMap
from entities.tower import Tower
from entities.enemy import Enemy
from entities.player import Player
from core.tower_placer import TowerPlacer
from core.wave_manager import WaveManager
from ui.hud import HUD

class GameManager:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.map = GameMap()
        self.towers = []
        self.enemies = []
        self.ui = HUD()
        self.spawn_timer = 0
        self.player = Player()
        self.tower_placer = TowerPlacer(self.map, self.towers, self.player)
        self.wave_manager = WaveManager(self.map.get_path())
        self.spawn_interval = 2  # segundos
        self.current_wave = 1
        self.base_hp = 100

    def update(self, dt):
        self.map.update()
        self.tower_placer.update()

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


        # Remove inimigos mortos ou que chegaram ao fim
        self.enemies = [e for e in self.enemies if e.is_alive() and not e.reached_end()]
       

        # Inicia próxima onda se não houver nenhuma em progresso e não houver inimigos vivos
        if not self.wave_manager.is_in_progress() and not self.enemies:
            self.wave_manager.start_next_wave()

       
    def spawn_enemy_wave(self):
        # Spawn múltiplos inimigos para a nova onda
        for _ in range(self.current_wave * 3):  # exemplo: 3 inimigos por onda
            self.spawn_enemy()


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

        self.ui.draw(self.screen, wave_number, enemies_alive, base_hp)
        self.ui.draw(self.screen, wave_number, enemies_alive, base_hp)
        self.draw_gold(self.screen, self.player, pygame.font.SysFont(None, 30))



    def spawn_enemy(self):
        # Pega o caminho em pixels que o inimigo deve seguir
        path = self.map.get_path()
        
        # Cria um novo inimigo passando o caminho
        new_enemy = Enemy(path)
        
        # Adiciona o inimigo na lista de inimigos ativos
        self.enemies.append(new_enemy)

    

    def add_tower(self, pos):
        self.towers.append(Tower(pos))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.tower_placer.handle_click()


    def draw_gold(self, surface, player, font):
        text = font.render(f"Ouro: {player.gold}", True, (255, 255, 0))
        surface.blit(text, (10, 100))