
from entities.enemy import Enemy

class SkelletonEnemy(Enemy):

    def __init__(self, path: str):
        image = "assets/enemies/skelleton/D_Walk.png"
        folder = "assets/enemies/skelleton/"
        super().__init__(path, image, folder)
        self.hp = 100
        self.speed = 10
        self.damage = 20
        self.folder = folder
