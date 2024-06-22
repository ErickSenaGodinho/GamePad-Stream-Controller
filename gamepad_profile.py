from notification import show_notification

class Profile:    
    def __init__(self, name: str):
        self.name = name
        self.shortcuts = {}

    def add_shortcut(self, shortcut: list, actions: list):
        self.shortcuts[frozenset(shortcut)] = actions

    def __run_actions(self, actions):
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
    
    def notificate(self):
        show_notification("Profile Changed", self.name)

class ProfileManager():
    _profile_list: list[Profile] = []
    _current_profile = 0

    @classmethod
    def add_profile(cls, profile: Profile):
        cls._profile_list.append(profile)

    @classmethod
    def get_current_profile(cls) -> Profile:
        return cls._profile_list[cls._current_profile]

    @classmethod
    def increase_profile(cls):
        if cls._current_profile < len(cls._profile_list) - 1:
            cls._current_profile += 1
            cls._profile_list[cls._current_profile].notificate()

    @classmethod
    def decrease_profile(cls):
        if cls._current_profile > 0:
            cls._current_profile -= 1
            cls._profile_list[cls._current_profile].notificate()