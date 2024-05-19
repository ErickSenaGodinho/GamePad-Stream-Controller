from gamepad_profile import Profile, gamepad
from shortcuts import Key, set_scene, press_key

Profile.profiles = [Profile("Gameplay com Gamepad"), Profile("Livezinha de boa")]

def add_shortcuts(profile: Profile, shortcuts: list[tuple[list, list]]):
    for shortcut, actions in shortcuts:
        profile.add_shortcut(shortcut, actions)

# Add shortcuts to profile 0
shortcuts_0 = [
    ([gamepad.Key.START, gamepad.Key.RB, gamepad.Key.Y], [(set_scene, 1)]),
    ([gamepad.Key.START, gamepad.Key.RB, gamepad.Key.X], [(set_scene, 2)]),
    ([gamepad.Key.START, gamepad.Key.RB, gamepad.Key.B], [(set_scene, 3)]),
    ([gamepad.Key.START, gamepad.Key.RB, gamepad.Key.LB], [(press_key, Key.esc)])
]
add_shortcuts(Profile.profiles[0], shortcuts_0)

# Add shortcuts to profile 1
shortcuts_1 = [
    ([gamepad.Key.Y], [(set_scene, 1)]),
    ([gamepad.Key.X], [(set_scene, 2)]),
    ([gamepad.Key.B], [(set_scene, 3)])
]
add_shortcuts(Profile.profiles[1], shortcuts_1)