import pygame
from core.game_manager import GameManager
from ui.components.pause_menu import draw_pause_menu
from ui.screens.victory_screen import draw_victory_screen
from ui.screens.ranking_screen import draw_ranking_screen
from ui.screens.game_over_screen import draw_game_over_screen
from maps.green_map import GreenMap
class GameScreen:
    def __init__(self, screen, difficulty, nick, ranking, map_class):
        self.screen = screen
        self.difficulty = difficulty
        self.nick = nick
        self.ranking = ranking
        self.game_map = map_class()
        self.game = GameManager(screen, difficulty, self.game_map)
        self.game.player_nick = nick

        self.paused = False
        self.game_over = False
        self.victory = False
        self.ranking_screen = False
        self.pause_buttons = None

        self.font = pygame.font.SysFont(None, 72)
        self.button_font = pygame.font.SysFont(None, 36)

    def run(self):
        clock = pygame.time.Clock()
        running = True
        show_game_over_screen = False

        while running:
            dt = clock.tick(60) / 1000
            for event in pygame.event.get():
                action = self.handle_event(event)
                if action in ("exit", "start", "nick_difficulty"):
                    return action

            if not self.game_over and not self.victory and not self.paused:
                self.update_game_state(dt)
                if self.check_end_conditions():
                    show_game_over_screen = not self.ranking_screen

            self.game.draw()
            overlay_result = self.render_overlay(show_game_over_screen)
            if overlay_result:
                return overlay_result

            pygame.display.flip()

        return "exit"

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            return "exit"
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.ranking_screen = False if self.ranking_screen else self.toggle_pause()

        if self.paused and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.pause_buttons:
                if self.pause_buttons["continuar"].collidepoint(mouse_pos):
                    self.paused = False
                elif self.pause_buttons["sair"].collidepoint(mouse_pos):
                    return "nick_difficulty"

        elif not self.game_over and not self.victory:
            result = self.game.handle_event(event)
            if result == "pause":
                self.paused = True

    def toggle_pause(self):
        self.paused = not self.paused

    def update_game_state(self, dt):
        self.game.update(dt)

    def check_end_conditions(self):
        if self.game.base_hp <= 0:
            self.game_over = True
            if self.difficulty == "endless":
                self.ranking.cadastra_pontuacao(self.game.player_nick, self.game.score, self.game_map)
                self.ranking_screen = True
            return True
        elif self.game.game_won:
            self.victory = True
            return True
        return False

    def render_overlay(self, show_game_over_screen):
        width, height = self.screen.get_width(), self.screen.get_height()
        mouse_pos = pygame.mouse.get_pos()

        if self.paused:
            self.pause_buttons = draw_pause_menu(self.screen, width, height, self.font, self.button_font)

        elif self.game_over:
            if self.ranking_screen:
                buttons = draw_ranking_screen(self.screen, width, height, self.font, self.button_font, self.ranking, self.game_map)
            else:
                buttons = draw_game_over_screen(self.screen, width, height, self.font, self.button_font)

            if pygame.mouse.get_pressed()[0]:
                if buttons["retry"].collidepoint(mouse_pos):
                    self.restart_game()
                elif buttons["menu"].collidepoint(mouse_pos):
                    return "start"

        elif self.victory:
            buttons = draw_victory_screen(self.screen, width, height, self.button_font)
            if pygame.mouse.get_pressed()[0]:
                if buttons["retry"].collidepoint(mouse_pos):
                    self.restart_game()
                elif buttons["menu"].collidepoint(mouse_pos):
                    return "start"

        return None  # Garantir retorno explícito

    def restart_game(self):
        self.game = GameManager(self.screen, self.difficulty, self.game_map)
        self.game.player_nick = self.nick
        self.game_over = False
        self.victory = False
        self.ranking_screen = False
