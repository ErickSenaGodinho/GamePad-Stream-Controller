class Profile:    
    def __init__(self, name: str):
        self.name = name
        self.shortcuts = {}

    def add_shortcut(self, shortcut: list, actions: list):
        self.shortcuts[frozenset(shortcut)] = actions

    def __run_actions(self, actions, gamepad):
        for action, value in actions:
            if value is None:
                action(gamepad)
            elif isinstance(value, tuple):
                action(*value, gamepad)
            else:
                action(value, gamepad)

    def try_shortcut(self, gamepad):
        pressed_buttons = gamepad.get_pressed_buttons()
        combination = pressed_buttons | frozenset(gamepad.get_pressed_hats())
        for shortcut, actions in self.shortcuts.items():
            if shortcut in (pressed_buttons, gamepad.get_pressed_hats(), combination):
                self.__run_actions(actions, gamepad)

class ProfileManager():
    __profile_list: list[Profile] = []

    @classmethod
    def add_profile(cls, profile: Profile):
        cls.__profile_list.append(profile)

    @classmethod
    def get_profile_by_id(cls, profile_id: int) -> Profile:
        return cls.__profile_list[profile_id]
    
    @classmethod
    def get_profile_list_size(cls):
        return len(cls.__profile_list)
    