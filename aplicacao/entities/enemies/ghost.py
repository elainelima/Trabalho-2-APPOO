from entities.enemy import Enemy
from assets.drawAnimated import AnimatedSprite

class GhostEnemy(Enemy):
    NUM_IMAGES_MAP = {
        "D_Walk.png": 3,
        "S_Walk.png": 4,
        "D_Death.png":6
    }

    def __init__(self, path: str):
        image = "assets/enemies/ghost/D_Walk.png"
        folder = "assets/enemies/ghost/"
        self.hp = 60
        self.speed = 15
        self.damage = 10
        self.folder = folder
        super().__init__(path, image, 3, folder, num_images_map=self.NUM_IMAGES_MAP)