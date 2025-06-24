from assets.effects.projectile_effects import ProjectileEffect

class IceProjectile(ProjectileEffect):
    def __init__(self, start_pos, target_pos):
        super().__init__(start_pos, target_pos, "assets/projectiles/ice_shard.png", speed=250)
