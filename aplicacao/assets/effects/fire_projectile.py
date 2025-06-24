from assets.effects.projectile_effects import ProjectileEffect
import pygame

class FireProjectile(ProjectileEffect):
    def __init__(self, start_pos, target_pos):
        super().__init__(start_pos, target_pos, "assets/projectiles/fireball.png", speed=300)
        self.image = pygame.transform.scale(self.image, (30, 30))
