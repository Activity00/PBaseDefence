from manager.achivevment import AchievementSystem
from manager.ap import ApSystem
from manager.camp import CampSystem
from manager.character import CharacterSystem
from manager.event import EventSystem
from manager.stage import StageSystem
from ui.camp import CampInfoUI
from ui.solider import SoliderInfoUI


class GameManager:
    def __init__(self):
        self.event_system = EventSystem(self)
        self.achievement_system = AchievementSystem(self)
        self.ap_system = ApSystem(self)
        self.camp_system = CampSystem(self)
        self.character_system = CharacterSystem(self)
        self.stage_system = StageSystem(self)

        self.camp_info_ui = CampInfoUI(self)
        self.solider_info_ui = SoliderInfoUI()

    def update_event(self):
        self.event_system.update()

    def update(self):
        self.achievement_system.update()
        self.ap_system.update()
        self.camp_system.update()
        self.character_system.update()
        self.stage_system.update()

    def draw(self):
        pass

    def update_solider(self):
        self.character_system.update_solider()

    def show_camp_info(self, camp_obj):
        self.camp_info_ui.show_info(camp_obj)
        self.solider_info_ui.hide()

    def register_game_event(self, event, observer):
        self.event_system.register_game_event(event, observer)

    def notify(self, event, *args, **kwargs):
        self.event_system.notify(event, *args, **kwargs)


game_manager = GameManager()
