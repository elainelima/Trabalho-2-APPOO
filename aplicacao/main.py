# main.py
import pygame
from ui.interface import InterfaceInicial
from core.game_manager import GameManager
from maps.green_map import GreenMap
from ui.screens.game_over_screen import draw_game_over_screen
from ui.screens.victory_screen import draw_victory_screen
from ui.components.pause_menu import draw_pause_menu
from util.ranking_service import RankService
from ui.screens.ranking_screen import draw_ranking_screen
from pygame import mixer

def carregar_rankings():

    return [("Jogador1", 1500), ("Jogador2", 1200), ("Jogador3", 1100)]

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from base_de_dados.base_dados import Base_Dados


def main(ranking: RankService):
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
    

    mixer.music.load('assets/sounds/watery-graves-181198.mp3')
    mixer.music.play(-1)

    game_map = GreenMap()
    game = GameManager(screen, difficulty, game_map)
    game.player_nick = nick

    game_over = False
    running = True

    ranking_screen = False
    rankings = carregar_rankings()

    while running:
        dt = game.clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                if ranking_screen:
                    ranking_screen = False
                else:
                    paused = not paused

            if paused:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if pause_buttons["continuar"].collidepoint(mouse_pos):
                        paused = False
                    elif pause_buttons["sair"].collidepoint(mouse_pos):
                        running = False
            elif not game_over and not victory:
                game.handle_event(event)

        if not game_over and not victory and not paused:
            game.update(dt)
            if game.base_hp <= 0:
                game_over = True
                if difficulty == "endless":
                    ranking.cadastra_pontuacao(game.player_nick, game.score)
            elif game.game_won:
                victory = True

        game.draw()

        if paused:
            pause_buttons = draw_pause_menu(screen, WIDTH, HEIGHT, font, button_font)
        elif game_over:
            ranking_buttons = draw_ranking_screen(screen, WIDTH, HEIGHT, font, button_font, ranking)
            if pygame.mouse.get_pressed()[0]:  # Botão esquerdo clicado
                mouse_pos = pygame.mouse.get_pos()
                if ranking_buttons["menu"].collidepoint(mouse_pos):
                    main(ranking)  
                    return
                elif ranking_buttons["retry"].collidepoint(mouse_pos):
                    game = GameManager(screen, difficulty, GreenMap())  # reinicia o jogo
                    game.player_nick = nick
                    game_over = False

        elif victory:
            button_rect = draw_victory_screen(screen, WIDTH, HEIGHT, font, button_font)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    db = Base_Dados()
    db.connect()
    db.execute_script()
    ranking = RankService(db)
    main(ranking)
    db.close()
