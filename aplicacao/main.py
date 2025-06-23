# main.py
import pygame
from ui.interface import InterfaceInicial
from core.game_manager import GameManager
from maps.green_map import GreenMap
from ui.game_over_screen import draw_game_over_screen
from ui.victory_screen import draw_victory_screen
from ui.pause_menu import draw_pause_menu


def main():
    pygame.init()
    WIDTH, HEIGHT = 960, 720
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Protect the Land")

    font = pygame.font.SysFont(None, 72)
    button_font = pygame.font.SysFont(None, 36)

    interface = InterfaceInicial(screen)
    victory = False
    paused = False
    pause_buttons = None

    difficulty, nick = interface.run()
    if difficulty is None:
        pygame.quit()
        return
    
    game_map = GreenMap()
    game = GameManager(screen, difficulty, game_map)
    game.player_nick = nick

    game_over = False
    running = True

    while running:
        dt = game.clock.tick(60) / 1000

        #Loop Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                paused = not paused

            if paused:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if pause_buttons["continuar"].collidepoint(mouse_pos):
                        paused = False
                    elif pause_buttons["sair"].collidepoint(mouse_pos):
                        running = False   # Sai do loop do jogo e volta ao menu
            elif not game_over and not victory:
                game.handle_event(event)


        if not game_over and not victory and not paused:
            game.update(dt)
            if game.base_hp <= 0:
                game_over = True
            elif game.game_won:
                victory = True

        game.draw()

        if paused:
            pause_buttons = draw_pause_menu(screen, WIDTH, HEIGHT, font, button_font)
        elif game_over:
            button_rect = draw_game_over_screen(screen, WIDTH, HEIGHT, font, button_font)
        elif victory:
            button_rect = draw_victory_screen(screen, WIDTH, HEIGHT, font, button_font)


        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()