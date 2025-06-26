
import pygame
import random

class Particle:
    def __init__(self, pos, color, lifetime=0.5):
        self.pos = pygame.Vector2(pos)
        self.velocity = pygame.Vector2(random.uniform(-30, 30), random.uniform(-30, 30))
        self.lifetime = lifetime
        self.initial_lifetime = lifetime
        self.color = color
        self.radius = 3

    def update(self, dt):
        self.lifetime -= dt
        self.pos += self.velocity * dt
        self.radius = max(0, self.radius - dt * 2)

    def draw(self, surface):
        alpha = max(0, int(255 * (self.lifetime / self.initial_lifetime)))
        if alpha > 0:
            s = pygame.Surface((self.radius*2, self.radius*2), pygame.SRCALPHA)
            pygame.draw.circle(s, (*self.color, alpha), (self.radius, self.radius), int(self.radius))
            surface.blit(s, s.get_rect(center=self.pos))


class AnimatedProjectileEffect:
    def __init__(self, start_pos, target_pos, sprite_sheet, frame_rects, speed=300, frame_duration=0.08,trail_color=(255, 200, 50)):
        self.frames = [sprite_sheet.subsurface(rect) for rect in frame_rects]
        self.current_frame = 0
        self.frame_timer = 0
        self.frame_duration = frame_duration

        self.pos = pygame.Vector2(start_pos)
        self.target = pygame.Vector2(target_pos)
        self.speed = speed
        self.finished = False
        self.direction = (self.target - self.pos).normalize()

        # Partículas
        self.particles = []
        self.glow_color = trail_color

    def update(self, dt):
        distance = self.speed * dt
        move_vector = self.direction * distance

        if self.pos.distance_to(self.target) <= distance:
            self.pos = self.target
            self.finished = True
        else:
            self.pos += move_vector

        # Atualiza animação
        self.frame_timer += dt
        if self.frame_timer >= self.frame_duration:
            self.frame_timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)

        # Adiciona partículas
        self.particles.append(Particle(self.pos, self.glow_color))
        self.particles = [p for p in self.particles if p.lifetime > 0]
        for p in self.particles:
            p.update(dt)

    def draw(self, surface):
        # Brilho (aura)
        glow_surface = pygame.Surface((40, 40), pygame.SRCALPHA)
        pygame.draw.circle(glow_surface, (255, 200, 50, 50), (20, 20), 20)
        surface.blit(glow_surface, glow_surface.get_rect(center=self.pos))

        # Projétil
        image = self.frames[self.current_frame]
        rotated_image = pygame.transform.rotate(image, -self.direction.angle_to(pygame.Vector2(1, 0)))
        rect = rotated_image.get_rect(center=self.pos)
        surface.blit(rotated_image, rect)

        # Partículas
        for p in self.particles:
            p.draw(surface)

    def has_reached_target(self):
        return self.finished
