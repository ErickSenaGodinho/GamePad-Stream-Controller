from enum import IntEnum, StrEnum
from pyjoystick import Joystick
from gamepad_profile import Profile, ProfileManager
from notification import show_notification

class GamepadButtonMapping(IntEnum):
    A = 0
    B = 1
    X = 3
    Y = 4
    LB = 6
    RB = 7
    LT = 8
    RT = 9
    SELECT = 10
    START = 11

class GamepadDPadMapping(StrEnum):
    UP = 'Up'
    RIGHT = 'Right'
    LEFT = 'Left'
    DOWN = 'Down'

class Gamepad(Joystick):
    """Custom gamepad that uses our own button mapping."""
    Button = GamepadButtonMapping
    DPad = GamepadDPadMapping

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.__pressed_buttons = []
        self.__pressed_hats = []
        self.__hat_range = ()
        self.__current_profile = 0
        self.__profile: Profile | None = ProfileManager.get_profile_by_id(self.__current_profile)

    def get_pressed_buttons(self) -> frozenset:
        return frozenset(button for button in self.__pressed_buttons)

    def set_pressed_button(self, button: int, is_pressed: bool) -> None:
        self.__pressed_buttons.append(button) if is_pressed else self.__pressed_buttons.remove(button)

    def get_pressed_hats(self) -> list:
        return self.__pressed_hats
    
    def set_pressed_hats(self, pressed_hat: str, is_pressed: bool) -> None:
        self.__pressed_hats.clear()
        if is_pressed:
            for hat_button_pressed in pressed_hat.split():
                self.__pressed_hats.append(hat_button_pressed)

    def set_hat_range(self, hat_range: tuple) -> None:
        self.__hat_range = hat_range

    def get_hat_range(self) -> tuple:
        return self.__hat_range

    def increase_profile(self) -> None:
        if self.__current_profile < ProfileManager.get_profile_list_size() - 1:
            self.__current_profile += 1
            self.__profile = ProfileManager.get_profile_by_id(self.__current_profile)
            self.__send_change_profile_notification()

    def decrease_profile(self) -> None:
        if self.__current_profile > 0:
            self.__current_profile -= 1
            self.__profile = ProfileManager.get_profile_by_id(self.__current_profile)
            self.__send_change_profile_notification()   

    def __send_change_profile_notification(self) -> None:
        show_notification("Change profile", f"{self.name} changed to profile {self.__profile.name}")

    def try_shortcut(self) -> None:
        self.__profile.try_shortcut(self)

class GamePadManager():
    __gamepad_list: list[Gamepad] = []

    @classmethod
    def add_gamepad(cls, gamepad: Gamepad) -> None:
        cls.__gamepad_list.append(gamepad)

    @classmethod
    def remove_gamepad(cls, gamepad: Gamepad) -> None:
        cls.__gamepad_list.remove(gamepad)

    @classmethod
    def get_gamepad_by_id(cls, id: int) -> Gamepad | None:
        for gamepad in cls.__gamepad_list:
            if gamepad.get_id() == id:
                return gamepad
        return None

