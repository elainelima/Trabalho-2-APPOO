from assets.effects.projectile_effects import ProjectileEffect
import pygame
class SniperProjectile(ProjectileEffect):
    def __init__(self, start_pos, target_pos):
        super().__init__(start_pos, target_pos, "assets/projectiles/sniper_bullet.png", speed=600)
        self.image = pygame.transform.scale(self.image, (60, 30))
