from entities.enemy import Enemy
from assets.drawAnimated import AnimatedSprite

class GhostEnemy(Enemy):

    NUM_IMAGES_MAP = {
        "D_Walk.png": 4,
        "S_Walk.png": 3,
        # Coloque aqui outras animações e seus frames
    }

    def __init__(self, path: str):
        image = "assets/enemies/ghost/D_Walk.png"
        folder = "assets/enemies/ghost/"
        super().__init__(path, image, folder)

        # Passa o dicionário para o sprite, assumindo que você pode fazer algo assim:
        self.sprite = AnimatedSprite(
            mainImage=image.split("/")[-1], 
            pos=(0,0),  # Aqui defina posição inicial correta, ou depois atualize
            numImages=self.NUM_IMAGES_MAP[image.split("/")[-1]], 
            folder=folder
        )

        self.hp = 60
        self.speed = 15
        self.damage = 10
        self.folder = folder
