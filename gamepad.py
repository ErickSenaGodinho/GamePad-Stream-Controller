from enum import IntEnum
from pyjoystick import Joystick

class GamePadMapping(IntEnum):
    """Gamepad button mapping."""
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

class CustomGamePad(Joystick):
    """Custom gamepad that uses our own button mapping."""
    Button = GamePadMapping
