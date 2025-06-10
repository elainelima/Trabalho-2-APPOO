import pygame
from settings import WHITE

class HUD:
    def __init__(self):
        pygame.font.init()
        
        self.font = pygame.font.SysFont("Arial", 24)

    def draw(self, surface, wave_number, enemies_alive, base_hp):
        wave_text = self.font.render(f"Fase: {wave_number}", True, WHITE)
        enemies_text = self.font.render(f"Inimigos vivos: {enemies_alive}", True, WHITE)
        hp_text = self.font.render(f"HP da base: {base_hp}", True, WHITE)

        surface.blit(wave_text, (10, 10))
        surface.blit(enemies_text, (10, 40))
        surface.blit(hp_text, (10, 70))
