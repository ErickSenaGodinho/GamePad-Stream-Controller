import os
from pynput.keyboard import Key, Listener
from pyjoystick.sdl2 import Joystick, Key as GamePadKey, run_event_loop as re_loop
from gamepad_profile import Profile
from shortcuts import data
from notification import show_notification

CLOSE_PROGRAM_KEY = Key.alt_gr
pressed_buttons = {}

def load_profiles():
    for profile_name in data.keys():
        profile = Profile(profile_name)
        for shortcut, actions in data[profile_name]:
            profile.add_shortcut(shortcut, actions)
        Profile.profiles.append(profile)

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
    current_profile = Profile.current_profile
    Profile.profiles[current_profile].try_shortcut(pressed_buttons)