import os
from pyjoystick.sdl2 import Joystick, Key as GamePadKey, run_event_loop 
from pynput.keyboard import Listener, Key
from gamepad import Gamepad, GamePadManager
from gamepad_profile import Profile, ProfileManager
from shortcuts import profile_shortcuts, general_shortcuts
from notification import show_notification

CLOSE_PROGRAM_KEY = Key.alt_gr

def close_app():
    os._exit(1)

def on_press(key):
    if key == CLOSE_PROGRAM_KEY:
        close_app()

def load_profile_list():
    for profile_name in profile_shortcuts.keys():
        profile = Profile(profile_name)
        for shortcut, actions in profile_shortcuts[profile_name]:
            profile.add_shortcut(shortcut, actions)
        for shortcut, actions in general_shortcuts:
            profile.add_shortcut(shortcut, actions)
        ProfileManager.add_profile(profile)

def run():
    show_notification("GameDesk Controller Started", f"Press {CLOSE_PROGRAM_KEY.name.upper()} to close")
    # Start gamepads already connected
    Joystick.get_joysticks()
    
    # Start Keyboard Listener Thread
    listener = Listener(on_press=on_press)
    listener.start()
    run_event_loop(joystick_connected, joystick_disconnected, handle_key_event)

def joystick_connected(joystick: Joystick):
    """Notifies when a gamepad is connected."""
    gamepad = Gamepad(**joystick.__dict__)
    GamePadManager.add_gamepad(gamepad)
    show_notification("Gamepad Connected", f"{gamepad.name} added")
    
def joystick_disconnected(joystick: Joystick):
    """Notifies when a gamepad is disconnected."""
    gamepad = GamePadManager.get_gamepad_by_id(joystick.get_id())
    GamePadManager.remove_gamepad(gamepad)
    show_notification("Gamepad Disconnected", f"{gamepad.name} was removed")

def handle_key_event(key: GamePadKey):
    """Handle received gamepad key."""
    gamepad = GamePadManager.get_gamepad_by_id(key.joystick.get_id())

    if gamepad is None:
        return
    
    match key.keytype:
        case GamePadKey.BUTTON:
            gamepad.set_pressed_button(key.number, key.get_proper_value())
        case GamePadKey.HAT:
            gamepad.set_pressed_hats(key.get_hat_name(), key.get_proper_value())
            gamepad.set_hat_range(key.get_hat_range())
    gamepad.try_shortcut()