from gamepad import CustomGamePad as gamepad
from notification import show_notification

class Profile:
    profiles = []
    current_profile = 0
    general_shortcuts = []

    def __init__(self, name: str):
        self.name = name
        self.shortcuts = {}

    def add_shortcut(self, shortcut: list, actions: list):
        self.shortcuts[frozenset(shortcut)] = actions

    @staticmethod
    def __run_actions(actions):
        for action, value in actions:
            if value is None:
                action()
            elif isinstance(value, tuple):
                action(*value)
            else:
                action(value)

    def try_shortcut(self, pressed_buttons: dict):
        frozen_pressed_buttons = frozenset(button for button, is_pressed in pressed_buttons.items() if is_pressed)
        for shortcut, actions in self.shortcuts.items():
            if frozen_pressed_buttons == shortcut:
                self.__run_actions(actions)
        for shortcut, actions in Profile.general_shortcuts:
            if frozen_pressed_buttons == frozenset(shortcut):
                self.__run_actions(actions)

    @classmethod
    def increase_profile(cls):
        if cls.current_profile < len(cls.profiles) - 1:
            cls.current_profile += 1
            cls.notificate()

    @classmethod
    def decrease_profile(cls):
        if cls.current_profile > 0:
            cls.current_profile -= 1
            cls.notificate()

    @classmethod
    def notificate(cls):
            show_notification("Profile Changed", Profile.profiles[Profile.current_profile].name)


Profile.general_shortcuts = [([gamepad.Key.SELECT, gamepad.Key.RB], [(Profile.increase_profile, None)]),
                             ([gamepad.Key.SELECT, gamepad.Key.LB], [(Profile.decrease_profile, None)])]
