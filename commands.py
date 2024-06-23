import pyautogui
from gamepad import Gamepad

def press_key(key: str, _: Gamepad):
    pyautogui.press(key)

def press_keys(keys: list, _: Gamepad):
    pyautogui.hotkey(keys, interval = 0.05)

def set_scene(scene, gamepad: Gamepad):
    press_keys(['ctrl', 'shift', str(scene)], gamepad)