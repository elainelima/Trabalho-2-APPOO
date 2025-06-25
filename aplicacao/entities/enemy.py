import pygame
from settings import TILE_SIZE
from assets.drawAnimated import AnimatedSprite

class Enemy:
    def __init__(self, path: list[tuple], image: str, numImage:str, folder: str,num_images_map=None):
        self.path = path
        self.current_point = 0
        self.image = image
        self.pos = list(self.path[0])
        self.reward = 10
        self.alive = True
        self.rewarded = False

        self.folder = folder
        self.last_direction = "D"  # Começa olhando para a direita

        self.sprite = AnimatedSprite(f"{folder}D_Walk.png", self.pos, numImages=numImage, folder=folder,num_images_map=num_images_map)
        self.dead_sprite = None
        self.is_dying = False

    def update(self, dt):
        if self.is_dying:
            if self.dead_sprite:
                self.dead_sprite.update(dt)
                self.dead_sprite.set_position(self.pos)
                if self.dead_sprite.index == len(self.dead_sprite.images) - 1:
                    self.is_dying = False  # Encerra a animação de morte
            return

        if self.current_point + 1 < len(self.path):
            target = self.path[self.current_point + 1]
            dir_vec = (target[0] - self.pos[0], target[1] - self.pos[1])
            dist = (dir_vec[0] ** 2 + dir_vec[1] ** 2) ** 0.5

            if dist != 0:
                dir_norm = (dir_vec[0] / dist, dir_vec[1] / dist)
            else:
                dir_norm = (0, 0)

            move_dist = self.speed * dt

            if move_dist >= dist:
                self.pos = list(target)
                self.current_point += 1
            else:
                self.pos[0] += dir_norm[0] * move_dist
                self.pos[1] += dir_norm[1] * move_dist

            # Atualiza direção e animação
            if abs(dir_vec[0]) > abs(dir_vec[1]):
                if dir_vec[0] < 0:
                    direction = "S_Walk.png"
                    flip = bool(self.sprite.num_images_map)
                    self.last_direction = "S"
                else:
                    direction = "S_Walk.png"
                    flip = not bool(self.sprite.num_images_map)
                    self.last_direction = "D"
            else:
                if dir_vec[1] < 0:
                    direction = "U_Walk.png"
                    flip = False
                    self.last_direction = "U"
                else:
                    direction = "D_Walk.png"
                    flip = False
                    self.last_direction = "D"


            self.sprite.update(dt, animation_name=direction, flip_h=flip)
            self.sprite.set_position(self.pos)
            
    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0 and self.alive:
            self.alive = False
            self.is_dying = True
            death_path = f"{self.folder}{self.last_direction}_Death.png"
            self.dead_sprite = AnimatedSprite(death_path, self.pos, 6, folder=self.folder)
            self.dead_sprite.set_position(self.pos)

    def is_alive(self):
        return self.alive or self.is_dying

    def reached_end(self):
        return self.current_point >= len(self.path) - 1

    def draw(self, screen):
        if self.is_dying and self.dead_sprite:
            screen.blit(self.dead_sprite.image, self.dead_sprite.rect)
        else:
            screen.blit(self.sprite.image, self.sprite.rect)

        # (opcional) HUD de hitbox transparente
            transparente = pygame.Surface(self.sprite.rect.size, pygame.SRCALPHA)
            pygame.draw.rect(transparente, (255, 100, 0, 0), transparente.get_rect(), 2)
            screen.blit(transparente, self.sprite.rect.center)
