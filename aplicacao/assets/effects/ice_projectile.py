
import pygame
from assets.effects.projectile_effects import AnimatedProjectileEffect
class IceProjectile(AnimatedProjectileEffect):
   
    def __init__(self, start_pos, target_pos):
        self.sprite_sheet = pygame.image.load("assets/projectiles/ice_shard.png").convert_alpha()
        self.frame_rects = [pygame.Rect(1 * 16, y*16, 16, 16) for y in range(6)]
        super().__init__(start_pos, target_pos, self.sprite_sheet, self.frame_rects, speed=200, frame_duration=0.1,trail_color=(18, 32, 47))