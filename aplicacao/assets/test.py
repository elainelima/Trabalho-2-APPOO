import pygame

pygame.init()

# Configurações da tela

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Carregar a imagem do sprite

sprite_sheet = pygame.image.load('enemies/bee/D_Walk.png')

# Configurações de animação

FRAME_WIDTH = 48
FRAME_HEIGHT = 48
NUM_FRAMES = 6

# Extrair quadros individuais
frames = []

for i in range(NUM_FRAMES):
    frame = sprite_sheet.subsurface(pygame.Rect(i * FRAME_WIDTH, 0, FRAME_WIDTH, FRAME_HEIGHT))
    frames.append(frame)

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, images, x, y):
        super().__init__()
        self.images = images
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(topleft=(x,y))


    def update(self):
        self.index = (self.index + 1) % len(self.images)
        self.image = self.images[self.index]
    
# Criar grupo de sprites

all_sprites = pygame.sprite.Group()
animated_sprite = AnimatedSprite(frames, 300, 300)
all_sprites.add(animated_sprite)

# Loop

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    all_sprites.update()
    screen.fill((0,0,0))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(10) # Velocidade da animação

pygame.quit()
