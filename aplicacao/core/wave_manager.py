# wave_manager.py
from entities.enemy import Enemy
from entities.enemies.bee import BeeEnemy
from entities.enemies.slime import SlimeEnemy 
from entities.enemies.wolf import WolfEnemy 
from settings import TILE_SIZE
import random

class WaveManager:
    def __init__(self, path: list[tuple], difficulty, enemy_classes: list[type]):
        self.path = path
        self.difficulty = difficulty
        self.enemy_classes = enemy_classes  
        self.current_wave = 0
        self.wave_in_progress = False
        self.spawn_timer = 0
        self.enemies_to_spawn = 0
        self.enemies_spawned = 0
        self.spawn_delay = 0.8  # segundos
        self.is_endless = difficulty == "endless"



    def start_next_wave(self, auto=False):
        if not self.is_endless and auto:
            return  # Impede chamadas automáticas fora do endless

        self.current_wave += 1
        self.enemies_spawned = 0
        self.spawn_timer = 0
        self.wave_in_progress = True

        # Escalonamento progressivo
        base = 5
        fator = 3
        dificuldade_bonus = {
            "easy": 0,
            "medium": 5,
            "hard": 10,
            "endless": 0
        }
        bonus = dificuldade_bonus.get(self.difficulty, 0)

        self.enemies_to_spawn = base + self.current_wave * fator + bonus




    def update(self, dt: int, enemies: list):
        if not self.wave_in_progress:
            return

        self.spawn_timer += dt
        if self.spawn_timer >= self.spawn_delay and self.enemies_spawned < self.enemies_to_spawn:
            self.spawn_timer = 0
            self.enemies_spawned += 1

            # Exemplo de pesos baseados na wave
            if self.current_wave < 5:
                pool = self.enemy_classes[:1]
                pesos = [1]
            elif self.current_wave < 10:
                pool = self.enemy_classes[:2]
                pesos = [0.7, 0.3]
            else:
                pool = self.enemy_classes
                pesos = [0.5, 0.3, 0.2][:len(pool)]  # Garante que o tamanho de pesos corresponda

            enemy_class = random.choices(pool, weights=pesos, k=1)[0]
            new_enemy = enemy_class(self.path)
            enemies.append(new_enemy)

        if self.enemies_spawned >= self.enemies_to_spawn and len(enemies) == 0:
            self.wave_in_progress = False




    def is_wave_over(self, enemies: list[Enemy]):
        return self.enemies_spawned == self.enemies_to_spawn and not enemies

    def is_in_progress(self):
        return self.wave_in_progress
