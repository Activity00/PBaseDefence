from abc import abstractmethod


class BaseSystem:

    @abstractmethod
    def update(self):
        pass
