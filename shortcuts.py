from gamepad import Gamepad
from commands import set_scene, press_key

profile_shortcuts = {
    "Profile 1": [
        ([Gamepad.Button.START, Gamepad.Button.RB, Gamepad.Button.Y], [(set_scene, 1)]),
        ([Gamepad.Button.START, Gamepad.Button.RB, Gamepad.Button.X], [(set_scene, 2)]),
        ([Gamepad.Button.START, Gamepad.Button.RB, Gamepad.Button.B], [(set_scene, 3)]),
        ([Gamepad.Button.START, Gamepad.Button.RB, Gamepad.Button.LB], [(press_key, 'esc')]),
    ],
    "Profile 2": [
        ([Gamepad.Button.Y], [(set_scene, 1)]),
        ([Gamepad.Button.X], [(set_scene, 2)]),
        ([Gamepad.Button.B], [(set_scene, 3)]),
        ([Gamepad.Button.A], [(set_scene, 4)]),
    ]
}

general_shortcuts = [([Gamepad.Button.SELECT, Gamepad.Button.RB], [(Gamepad.increase_profile, None)]),
                    ([Gamepad.Button.SELECT, Gamepad.Button.LB], [(Gamepad.decrease_profile, None)])]