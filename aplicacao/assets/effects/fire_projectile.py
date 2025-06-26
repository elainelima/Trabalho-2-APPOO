from assets.effects.projectile_effects import AnimatedProjectileEffect
import pygame

class FireProjectile(AnimatedProjectileEffect):
    def __init__(self, start_pos, target_pos):
        self.sprite_sheet = pygame.image.load("assets/projectiles/fireball.png").convert_alpha()
        self.frame_rects = [pygame.Rect(x * 16, 0, 16, 16) for x in range(6)]
        super().__init__(start_pos, target_pos, self.sprite_sheet, self.frame_rects, speed=200, frame_duration=0.1)
