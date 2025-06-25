import pygame

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
        desired_height: int = 64  # Altura padrão para sprites dinâmicos
    ):
        super().__init__()
        self.folder = folder or ""
        self.num_images = numImages
        self.y_offset = y_offset
        self.frame_delay = frame_delay
        self.dynamic = dynamic
        self.desired_height = desired_height

        self.animations_frames = {}  # Cache: nome_animacao -> lista de frames normais
        self.animations_flipped_frames = {}  # Cache: nome_animacao -> lista de frames espelhados

        self.current_image_name = mainImage.split("/")[-1]  # ex: "S_Walk.png"
        self.base_center = (pos[0], pos[1] - y_offset)

        # Carregar frames da animação base (normal)
        self.animations_frames[self.current_image_name] = self._load_images(self.folder + self.current_image_name)
        # Gerar frames espelhados para essa animação (exemplo)
        self.animations_flipped_frames[self.current_image_name] = [
            pygame.transform.flip(img, True, False) for img in self.animations_frames[self.current_image_name]
        ]

        self.images = self.animations_frames[self.current_image_name]
        self.index = 0
        self.time_since_last_frame = 0.0

        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=self.base_center)

    def _load_images(self, full_path: str) -> list[pygame.Surface]:
        sprite_sheet = pygame.image.load(full_path).convert_alpha()
        sheet_width, sheet_height = sprite_sheet.get_size()
        frame_width = sheet_width // self.num_images

        frames = []
        for i in range(self.num_images):
            frame_rect = pygame.Rect(i * frame_width, 0, frame_width, sheet_height)
            frame = sprite_sheet.subsurface(frame_rect)

            if self.dynamic:
                # Redimensiona para altura fixa mantendo proporção
                scale_factor = self.desired_height / frame.get_height()
                new_width = int(frame.get_width() * scale_factor)
                frame = pygame.transform.scale(frame, (new_width, self.desired_height))
            else:
                # Mantém tamanho original (sem redimensionar)
                pass

            frames.append(frame)

        return frames

    def update(self, dt: float, animation_name: str = None, flip_h: bool = False):
        if self.dynamic and animation_name and animation_name != self.current_image_name:
            self.current_image_name = animation_name
            # Se animação ainda não está carregada, carregar agora
            if animation_name not in self.animations_frames:
                self.animations_frames[animation_name] = self._load_images(self.folder + animation_name)
                self.animations_flipped_frames[animation_name] = [
                    pygame.transform.flip(img, True, False) for img in self.animations_frames[animation_name]
                ]

            # Escolher frames baseados no flip
            if flip_h:
                self.images = self.animations_flipped_frames[animation_name]
            else:
                self.images = self.animations_frames[animation_name]

            self.index = 0
            self.time_since_last_frame = 0.0

        # Atualiza frame da animação
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
