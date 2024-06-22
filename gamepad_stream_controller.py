import os
from pynput.keyboard import Key, Listener
from pyjoystick.sdl2 import Joystick, Key as GamePadKey, run_event_loop as re_loop
from gamepad_profile import Profile, ProfileManager
from shortcuts import profile_shortcuts, general_shortcuts
from notification import show_notification

CLOSE_PROGRAM_KEY = Key.alt_gr
pressed_buttons = {}

def load_profile_list():
    for profile_name in profile_shortcuts.keys():
        profile = Profile(profile_name)
        for shortcut, actions in profile_shortcuts[profile_name]:
            profile.add_shortcut(shortcut, actions)
        for shortcut, actions in general_shortcuts:
            profile.add_shortcut(shortcut, actions)
        ProfileManager.add_profile(profile)

def run():
    # Start Keyboard Listener Thread
    listener = Listener(on_press=on_press)
    listener.start()

    show_notification("GameDesk Controller Started", f"Press {CLOSE_PROGRAM_KEY.name.upper()} to close")

    re_loop(notify_connect, notify_remove, key_received)

def close_app():
    os._exit(1)

def on_press(key):
    if key == CLOSE_PROGRAM_KEY:
        close_app()

def notify_connect(joy: Joystick):
    """Notifies when a gamepad is connected."""
    if joy.name != "": # False if the gamepad is already connected when starting
        show_notification("New GamePad", f"{joy.name} is connected")

def notify_remove(joy: Joystick):
    """Notifies when a gamepad is disconnected."""
    show_notification("Lost Connection", f"{joy.name} was removed")

def key_received(key: GamePadKey):
    """Handle received gamepad key."""
    if key.keytype != GamePadKey.BUTTON:
        return
    pressed_buttons[key.number] = not pressed_buttons.get(key.number, False)
    ProfileManager.get_current_profile().try_shortcut(pressed_buttons)