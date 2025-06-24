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
from ui.screens.map_selection_screen import MapSelectionScreen
from ui.screens.inicial_screen import StartScreen
from ui.screens.game_screen import GameScreen

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

    state = "start"
    difficulty = None
    nick = None
    selected_map_class = None

    while True:
        if state == "start":
            start_screen = StartScreen(screen, font)
            start_screen.run()
            state = "nick_difficulty"

        elif state == "nick_difficulty":
            interface = InterfaceInicial(screen)
            difficulty, nick = interface.run()
            if difficulty is None:
                break
            state = "map_select"

        elif state == "map_select":
            map_selector = MapSelectionScreen(screen, button_font)
            selected_map_class = map_selector.run()
            state = "game"

        elif state == "game":
            game_screen = GameScreen(screen, difficulty, nick, ranking, selected_map_class)
            next_state = game_screen.run()
            if next_state == "exit":
                break
            else:
                state = next_state  # pode voltar para "difficulty" se sair no pause, etc

    pygame.quit()


if __name__ == "__main__":
    db = Base_Dados()
    db.connect()
    db.execute_script()
    ranking = RankService(db)
    main(ranking)
    db.close()