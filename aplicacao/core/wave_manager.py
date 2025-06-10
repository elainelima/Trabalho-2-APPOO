# wave_manager.py
from enemy import Enemy
from settings import TILE_SIZE

class WaveManager:
    def __init__(self, path):
        self.path = path
        self.current_wave = 0
        self.wave_in_progress = False
        self.spawn_timer = 0
        self.enemies_to_spawn = 0
        self.enemies_spawned = 0
        self.spawn_delay = 0.8  # segundos

    def start_next_wave(self):
        self.current_wave += 1
        self.enemies_to_spawn = 5 + self.current_wave * 2
        self.enemies_spawned = 0
        self.spawn_timer = 0
        self.wave_in_progress = True

    def update(self, dt, enemies):
        if not self.wave_in_progress:
            return

        self.spawn_timer += dt
        if self.spawn_timer >= self.spawn_delay and self.enemies_spawned < self.enemies_to_spawn:
            self.spawn_timer = 0
            new_enemy = Enemy(self.path)
            enemies.append(new_enemy)
            self.enemies_spawned += 1

        if self.enemies_spawned >= self.enemies_to_spawn and not enemies:
            self.wave_in_progress = False

    def is_wave_over(self, enemies):
        return self.enemies_spawned == self.enemies_to_spawn and not enemies

    def is_in_progress(self):
        return self.wave_in_progress
