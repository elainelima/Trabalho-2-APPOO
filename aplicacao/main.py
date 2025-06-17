# main.py
import pygame
from ui.interface import InterfaceInicial
from core.game_manager import GameManager
from maps.green_map import GreenMap

def main():
    pygame.init()
    screen = pygame.display.set_mode((960, 720))
    pygame.display.set_caption("Protect the Land")

    interface = InterfaceInicial(screen)
    difficulty = interface.run()

    if difficulty is None:
        pygame.quit()
        return
    map = GreenMap()

    game = GameManager(screen, difficulty,map)
    running = True

    while running:
        dt = game.clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            game.handle_event(event)

        game.update(dt)
        game.draw()
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
