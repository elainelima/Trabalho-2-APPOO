import pygame
import math

class ProjectileEffect:
    def __init__(self, start_pos, target_pos, image_path, speed=300):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))  # Ajuste do tamanho

        self.pos = pygame.Vector2(start_pos)
        self.target = pygame.Vector2(target_pos)
        self.speed = speed

        self.direction = (self.target - self.pos).normalize()
        self.finished = False

    def update(self, dt):
        distance = self.speed * dt
        move_vector = self.direction * distance

        if self.pos.distance_to(self.target) <= distance:
            self.pos = self.target
            self.finished = True
        else:
            self.pos += move_vector

    def draw(self, surface):
        rotated_image = pygame.transform.rotate(self.image, -self.direction.angle_to(pygame.Vector2(1, 0)))
        rect = rotated_image.get_rect(center=self.pos)
        surface.blit(rotated_image, rect)

    def has_reached_target(self):
        return self.finished
