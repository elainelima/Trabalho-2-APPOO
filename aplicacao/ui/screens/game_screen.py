import pygame
from core.game_manager import GameManager
from ui.components.pause_menu import draw_pause_menu
from ui.screens.victory_screen import draw_victory_screen
from ui.screens.ranking_screen import draw_ranking_screen
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
        self.pause_buttons = None
        self.ranking_screen = False

        # carrega música, etc

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            dt = clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return "exit"
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    if self.ranking_screen:
                        self.ranking_screen = False
                    else:
                        self.paused = not self.paused

                if self.paused:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if self.pause_buttons and self.pause_buttons["continuar"].collidepoint(mouse_pos):
                            self.paused = False
                        elif self.pause_buttons and self.pause_buttons["sair"].collidepoint(mouse_pos):
                            running = False
                            return "nick_difficulty"  # voltar para dificuldade
                elif not self.game_over and not self.victory:
                    result = self.game.handle_event(event)
                    if result == "pause":
                        self.paused = True
            if not self.game_over and not self.victory and not self.paused:
                self.game.update(dt)
                if self.game.base_hp <= 0:
                    self.game_over = True
                    if self.difficulty == "endless":
                        self.ranking.cadastra_pontuacao(self.game.player_nick, self.game.score)
                elif self.game.game_won:
                    self.victory = True

            self.game.draw()

            if self.paused:
                self.pause_buttons = draw_pause_menu(self.screen, self.screen.get_width(), self.screen.get_height(), pygame.font.SysFont(None, 72), pygame.font.SysFont(None, 36))
            elif self.game_over:
                ranking_buttons = draw_ranking_screen(self.screen, self.screen.get_width(), self.screen.get_height(), pygame.font.SysFont(None, 72), pygame.font.SysFont(None, 36), self.ranking)
                if pygame.mouse.get_pressed()[0]:
                    mouse_pos = pygame.mouse.get_pos()
                    if ranking_buttons["menu"].collidepoint(mouse_pos):
                        return "start"
                    elif ranking_buttons["retry"].collidepoint(mouse_pos):
                        self.game = GameManager(self.screen, self.difficulty, GreenMap())
                        self.game.player_nick = self.nick
                        self.game_over = False

            elif self.victory:
                button_rect = draw_victory_screen(self.screen, self.screen.get_width(), self.screen.get_height(), pygame.font.SysFont(None, 72), pygame.font.SysFont(None, 36))

            pygame.display.flip()

        return "exit"