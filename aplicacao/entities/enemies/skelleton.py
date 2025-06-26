
from entities.enemy import Enemy

class SkelletonEnemy(Enemy):
    NUM_IMAGES_MAP = {
        "D_Walk.png": 13,
        "S_Walk.png": 13,
        "D_Death.png":18,
        "U_Death.png":18,

    }

    def __init__(self, path: str):
        image = "assets/enemies/skelleton/D_Walk.png"
        folder = "assets/enemies/skelleton/"
        super().__init__(path, image, 15,folder,num_images_map=self.NUM_IMAGES_MAP)
        self.hp = 100
        self.speed = 10
        self.damage = 20
        self.folder = folder
