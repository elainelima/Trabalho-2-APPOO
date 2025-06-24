from assets.effects.projectile_effects import ProjectileEffect


class FireProjectile(ProjectileEffect):
    def __init__(self, start_pos, target_pos):
        super().__init__(start_pos, target_pos, "assets/projectiles/fireball.png", speed=300)
