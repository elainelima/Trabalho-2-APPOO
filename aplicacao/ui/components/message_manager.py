# ui/message_manager.py
import pygame

class MessageManager:
    def __init__(self, duration: int =2.5):
        self.message = ""
        self.duration = duration
        self.timer = 0

    def show(self, message: str):
        self.message = message
        self.timer = self.duration

    def update(self, dt: int):
        if self.timer > 0:
            self.timer -= dt
            if self.timer <= 0:
                self.message = ""

    def draw(self, surface: pygame.Surface):
        if self.message and self.timer > 0:
            font = pygame.font.SysFont(None, 30)
            alpha = int(255 * (self.timer / self.duration))
            text_surface = font.render(self.message, True, (255, 80, 80))
            text_surface.set_alpha(alpha)
            temp_surface = pygame.Surface(text_surface.get_size(), pygame.SRCALPHA)
            temp_surface.blit(text_surface, (0, 0))
            surface.blit(temp_surface, (
                surface.get_width() // 2 - text_surface.get_width() // 2,
                surface.get_height() // 2 - text_surface.get_height() // 2
            ))
