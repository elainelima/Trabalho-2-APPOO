
from entities.enemy import Enemy
from assets.drawAnimated import AnimatedSprite

class SlimeEnemy(Enemy):

    def __init__(self, path: str):
        image = "assets/enemies/slime/D_Walk.png"
        folder = "assets/enemies/slime/"
        super().__init__(path, image,6, folder)
        self.hp = 100
        self.speed = 10
        self.damage = 20
        self.folder = folder
