import pygame

from manager.game_manager import game_manager
from screen import Screen


class GameScreen(Screen):
    color = (0, 0, 0)

    def __init__(self, manager):
        super().__init__(manager)
        self.ball = pygame.image.load('asserts/ball.png')
        self.ball_rect = self.ball.get_rect()

    def update(self, dt):
        game_manager.update()
        self.manager.display.fill(self.color)
        self.manager.display.blit(self.ball, self.ball_rect)
