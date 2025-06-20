import pygame

class AnimatedSprite(pygame.sprite.Sprite):
    
    def __init__(self, mainImage, par, numImages):
        super().__init__()
        self.mainImage = mainImage
        self.images = self.separateImages(numImages)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(topleft=par)


    def separateImages(self, numImages: int) -> list:
        sprite_sheet = pygame.image.load(self.mainImage).convert_alpha()
        sheet_width, sheet_height = sprite_sheet.get_size()
        frame_width = sheet_width // numImages
        frame_height = sheet_height

        frames = []
        for i in range(numImages):
            frame_rect = pygame.Rect(i * frame_width, 0, frame_width, frame_height)
            frame = sprite_sheet.subsurface(frame_rect)
            frames.append(frame)

        return frames

    def update(self):
        self.index = (self.index + 1) % len(self.images)
        self.image = self.images[self.index]