from assets.effects.projectile_effects import ProjectileEffect

class SniperProjectile(ProjectileEffect):
    def __init__(self, start_pos, target_pos):
        super().__init__(start_pos, target_pos, "assets/projectiles/sniper_bullet.png", speed=600)
