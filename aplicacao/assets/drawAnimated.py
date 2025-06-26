import pygame
class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(
        self,
        mainImage: str,
        pos: tuple[int, int],
        numImages: int,
        y_offset: int = 0,
        folder: str = None,
        frame_delay: float = 0.1,
        dynamic: bool = True,
        desired_height: int = 64,
        num_images_map: dict[str, int] = None
    ):
        super().__init__()
        self.folder = folder or ""
        self.num_images = numImages
        self.y_offset = y_offset
        self.frame_delay = frame_delay
        self.dynamic = dynamic
        self.desired_height = desired_height
        self.num_images_map = num_images_map or {}

        self.animations_frames = {}
        self.animations_flipped_frames = {}

        self.current_image_name = mainImage.split("/")[-1]

        frame_count = self.num_images_map.get(self.current_image_name, self.num_images)
        self.animations_frames[self.current_image_name] = self._load_images(self.folder + self.current_image_name, frame_count)
        self.animations_flipped_frames[self.current_image_name] = [
            pygame.transform.flip(img, True, False) for img in self.animations_frames[self.current_image_name]
        ]

        self.images = self.animations_frames[self.current_image_name]
        self.index = 0
        self.time_since_last_frame = 0.0

        # Calcular base_center considerando o y_offset
        self.base_center = (pos[0], pos[1] - y_offset)

        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=self.base_center)

    def _load_images(self, full_path: str, frame_count: int) -> list[pygame.Surface]:
        sprite_sheet = pygame.image.load(full_path).convert_alpha()
        sheet_width, sheet_height = sprite_sheet.get_size()
        frame_width = sheet_width // frame_count

        frames = []
        for i in range(frame_count):
            frame_rect = pygame.Rect(i * frame_width, 0, frame_width, sheet_height)
            frame = sprite_sheet.subsurface(frame_rect)

            if self.dynamic:
                scale_factor = self.desired_height / frame.get_height()
                new_width = int(frame.get_width() * scale_factor)
                frame = pygame.transform.scale(frame, (new_width, self.desired_height))
            else:
                # Torre estática: usar altura maior (exemplo 1.5x) e ajustar
                static_height = int(self.desired_height * 1.5)
                scale_factor = static_height / frame.get_height()
                new_width = int(frame.get_width() * scale_factor)
                frame = pygame.transform.scale(frame, (new_width, static_height))

            frames.append(frame)

        return frames

    def update(self, dt: float, animation_name: str = None, flip_h: bool = False):
        if self.dynamic and animation_name and animation_name != self.current_image_name:
            self.current_image_name = animation_name
            if animation_name not in self.animations_frames:
                frame_count = self.num_images_map.get(animation_name, self.num_images)
                self.animations_frames[animation_name] = self._load_images(self.folder + animation_name, frame_count)
                self.animations_flipped_frames[animation_name] = [
                    pygame.transform.flip(img, True, False) for img in self.animations_frames[animation_name]
                ]

            self.images = self.animations_flipped_frames[animation_name] if flip_h else self.animations_frames[animation_name]
            self.index = 0
            self.time_since_last_frame = 0.0

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
