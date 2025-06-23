import pygame

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, mainImage: str, par: int, numImages: int, y_offset: int = 0, folder: str = None, frame_delay: float = 0.1):
        super().__init__()
        self.mainImage = mainImage
        self.numImages = numImages
        self.images = self.separateImages(numImages)
        self.index = 0
        self.image = self.images[self.index]
        self.y_offset = y_offset
        self.base_center = (par[0], par[1] - y_offset)
        self.rect = self.image.get_rect(center=self.base_center)
        self.folder = folder

        # Controle de animação
        self.frame_delay = frame_delay  # segundos por frame
        self.time_since_last_frame = 0.0

    def separateImages(self, numImages: int, horizontal: bool = None) -> list:
        sprite_sheet = pygame.image.load(self.mainImage).convert_alpha()
        sheet_width, sheet_height = sprite_sheet.get_size()
        frame_width = sheet_width // numImages
        frame_height = sheet_height

        frames = []
        for i in range(numImages):
            frame_rect = pygame.Rect(i * frame_width, 0, frame_width, frame_height)
            frame = sprite_sheet.subsurface(frame_rect)

            if sheet_height >= 200:
                frame = pygame.transform.scale_by(frame, 0.5)

            if horizontal is not None:
                frame = pygame.transform.flip(frame, horizontal, False)

            frames.append(frame)

        return frames

    def update(self, dt: float, horizontal: bool = None):
        # Atualiza direção se necessário
        if horizontal is not None:
            self.mainImage = self.folder + ("S_Walk.png" if horizontal else "D_Walk.png")
            self.images = self.separateImages(self.numImages, horizontal)

        # Acumula o tempo
        self.time_since_last_frame += dt
        if self.time_since_last_frame >= self.frame_delay:
            self.time_since_last_frame = 0.0
            self.index = (self.index + 1) % len(self.images)
            old_center = self.rect.center
            self.image = self.images[self.index]
            self.rect = self.image.get_rect(center=old_center)
