# settings.py

# Tamanho da janela
WIDTH = 1280
HEIGHT = 720

# FPS
FPS = 60

FONT = "arial"

# Cores (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GRAY = (50, 50, 50)
LIGHT_GRAY = (180, 180, 180)
GREEN = (34, 177, 76)
RED = (200, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)

# Caminho para recursos
PATHS = {
    "enemy": "assets/enemies/",
    "tower": "assets/towers/",
    "tiles": "assets/tiles/",
    "sounds": "assets/sounds/",
    "fonts": "assets/fonts/",
}

# Tile/mapa
TILE_SIZE = 64
MAP_ROWS = HEIGHT // TILE_SIZE
MAP_COLS = WIDTH // TILE_SIZE

# Torres
TOWER_RANGE = 150
TOWER_DAMAGE = 10
TOWER_FIRE_RATE = 1  # tiros por segundo

COLOR_TOWER = RED
COLOR_ENEMY = BLACK


# Inimigos
ENEMY_HEALTH = 100
ENEMY_SPEED = 2  # pixels por frame
