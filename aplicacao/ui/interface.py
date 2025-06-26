import pygame

from ui.screens.nick_screen import NickScreen
from ui.screens.difficulty_screen import DifficultyScreen

class InterfaceInicial:
    def __init__(self, screen):
        self.screen = screen

    def run(self):
        nick_screen = NickScreen(self.screen)
        nick = nick_screen.run()
        if nick is None:
            return None

        difficulty_screen = DifficultyScreen(self.screen)
        difficulty = difficulty_screen.run()
        if difficulty is None:
            return None

        return difficulty, nick
