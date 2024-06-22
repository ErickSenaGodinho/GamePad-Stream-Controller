from gamepad_profile import gamepad
from commands import set_scene, press_key

data = {
    "Profile 1": [
        ([gamepad.Key.START, gamepad.Key.RB, gamepad.Key.Y], [(set_scene, 1)]),
        ([gamepad.Key.START, gamepad.Key.RB, gamepad.Key.X], [(set_scene, 2)]),
        ([gamepad.Key.START, gamepad.Key.RB, gamepad.Key.B], [(set_scene, 3)]),
        ([gamepad.Key.START, gamepad.Key.RB, gamepad.Key.LB], [(press_key, 'esc')])
    ],
    "Profile 2": [
        ([gamepad.Key.Y], [(set_scene, 1)]),
        ([gamepad.Key.X], [(set_scene, 2)]),
        ([gamepad.Key.B], [(set_scene, 3)]),
        ([gamepad.Key.A], [(set_scene, 4)])
    ]
}