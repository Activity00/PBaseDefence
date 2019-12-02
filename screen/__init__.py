from abc import abstractmethod


class Screen:
    def __init__(self, manager):
        self.manager = manager

    @abstractmethod
    def update(self, dt):
        pass


class ScreenManager:
    def __init__(self, display, screen_cls):
        self.screen = screen_cls(self)
        self.display = display

    def update(self, dt):
        self.screen.update(dt)

    def replace_screen(self, screen_cls):
        self.screen = screen_cls(self)
