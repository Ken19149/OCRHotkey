from pynput import keyboard
import subprocess

pressed = set()

COMBINATIONS = [
    {
        "keys": [
            {keyboard.Key.alt_l, keyboard.KeyCode(char="x")},
            {keyboard.Key.alt_l, keyboard.KeyCode(char="X")},
        ],
        "command": ""
    }
]

def switchMode(mode):
    return not mode

mode = True
def on_press(key):
    global mode
    pressed.add(key)
    print(pressed)
    for c in COMBINATIONS:
        for keys in c["keys"]:
            if keys.issubset(pressed):
                mode = switchMode(mode)
                print(mode)

def on_release(key):
    if key in pressed:
        pressed.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()