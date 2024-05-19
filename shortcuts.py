import time
from pynput.keyboard import Key, KeyCode, Controller

keyboard = Controller()

def set_scene(scene):
    press_keys([Key.ctrl, Key.shift, str(scene)])

def press_key(key: str | Key | KeyCode):
    keyboard.press(key)
    time.sleep(0.05)
    keyboard.release(key)

def press_keys(keys: list):
    for key in keys:
        keyboard.press(key)
        time.sleep(0.05)
    for key in keys:
        keyboard.release(key)