import pygame

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, mainImage: str, pos: tuple[int, int], numImages: int, y_offset: int = 0, folder: str = None, frame_delay: float = 0.1, dynamic=True):
        super().__init__()
        self.folder = folder or ""
        self.num_images = numImages
        self.y_offset = y_offset
        self.frame_delay = frame_delay
        self.dynamic = dynamic
        self.current_image_name = mainImage.split("/")[-1]  # Ex: "D_Walk.png"
        self.full_path = self.folder + self.current_image_name
        self.images = self._load_images(self.full_path)
        self.index = 0
        self.time_since_last_frame = 0.0

        self.base_center = (pos[0], pos[1] - y_offset)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=self.base_center)

    def _load_images(self, full_path: str) -> list[pygame.Surface]:
        sprite_sheet = pygame.image.load(full_path).convert_alpha()
        sheet_width, sheet_height = sprite_sheet.get_size()
        frame_width = sheet_width // self.num_images
        frame_height = sheet_height

        frames = []
        for i in range(self.num_images):
            frame_rect = pygame.Rect(i * frame_width, 0, frame_width, frame_height)
            frame = sprite_sheet.subsurface(frame_rect)

            if sheet_height >= 200:
                frame = pygame.transform.scale(frame, (frame.get_width() // 2, frame.get_height() // 2))

            frames.append(frame)

        return frames

    def update(self, dt: float, animation_name: str = None):
        if self.dynamic and animation_name and animation_name != self.current_image_name:
            self.current_image_name = animation_name
            self.full_path = self.folder + animation_name
            self.images = self._load_images(self.full_path)
            self.index = 0
            self.time_since_last_frame = 0.0

        # Animação normal
        self.time_since_last_frame += dt
        if self.time_since_last_frame >= self.frame_delay:
            self.time_since_last_frame = 0.0
            self.index = (self.index + 1) % len(self.images)
            old_center = self.rect.center
            self.image = self.images[self.index]
            self.rect = self.image.get_rect(center=old_center)


    def set_position(self, pos: tuple[int, int]):
        self.base_center = (pos[0], pos[1] - self.y_offset)
        self.rect.center = self.base_center
