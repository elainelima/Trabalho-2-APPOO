from entities.enemy import Enemy

class GoblinEnemy(Enemy):

    def __init__(self, path: str,):
        image = "assets/enemies/goblin/D_Walk.png"
        folder = "assets/enemies/goblin/"
        super().__init__(path, image, folder)
        self.hp = 200
        self.speed = 20
        self.damage = 35
        self.folder = folder