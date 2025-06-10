# game_manager.py
import pygame
from settings import FPS
from core.map import GameMap
from entities.tower import Tower
from entities.enemy import Enemy
from core.tower_placer import TowerPlacer
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
        self.tower_placer = TowerPlacer(self.map, self.towers)
        self.spawn_interval = 2  # segundos
        self.current_wave = 1
        self.base_hp = 100

    def update(self, dt):
        self.map.update()

        posT = (7,3)
        self.add_tower(posT)


        for tower in self.towers:
            tower.update(dt, self.enemies)

        for enemy in self.enemies:
            enemy.update(dt)

        # Remove inimigos que chegaram ao final ou morreram
        self.enemies = [e for e in self.enemies if not e.reached_end() and e.is_alive()]

        # Se não tiver inimigos vivos, inicia próxima onda
        if not self.enemies:
            self.current_wave += 1
            self.spawn_enemy_wave()

        self.spawn_timer += dt
        if self.spawn_timer >= self.spawn_interval:
            self.spawn_timer = 0
            self.spawn_enemy()

       
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

        wave_number = self.current_wave
        enemies_alive = len(self.enemies)
        base_hp = self.base_hp

        self.ui.draw(self.screen, wave_number, enemies_alive, base_hp)



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

