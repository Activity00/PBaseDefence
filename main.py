import pygame as pg

from screen import ScreenManager
from screen.game_screen import GameScreen
from screen.login_screen import LoginScreen


class PBGame:
    def __init__(self, width, height, init_screen_cls, fps=60):
        self.size = self.width, self.height = width, height
        self.screen = pg.display.set_mode(self.size)
        self.clock = pg.time.Clock()
        self.fps = fps
        self.done = False
        self.screen_manager = ScreenManager(self.screen, init_screen_cls)

    def run(self):
        dt = self.clock.tick(self.fps)
        while not self.done:
            self._game_event_loop()
            self.screen_manager.update(dt)
            pg.display.update()

    def _game_event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.done = True


def run():
    pg.init()
    game = PBGame(640, 800, GameScreen)
    game.run()
    pg.quit()


if __name__ == '__main__':
    run()
