import pyautogui

def press_key(key: str):
    pyautogui.press(key)

def press_keys(keys: list):
    pyautogui.hotkey(keys, interval = 0.05)

def set_scene(scene):
    press_keys(['ctrl', 'shift', str(scene)])