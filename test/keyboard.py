from pynput import keyboard
from paddleocr import PaddleOCR
from PIL import ImageGrab
import pyperclip
import os
import clipboard_monitor

ocr = PaddleOCR(use_angle_cls=True, lang="japan")

def clipToText(ocr=ocr):
    img_clip = ImageGrab.grabclipboard()
    img_clip.save("OCR_temp.png", "PNG")
    img_path = "OCR_temp.png"
    result = ocr.ocr(img_path, cls=True)
    os.remove("OCR_temp.png")
    text = ""
    # combine text result
    for i in range(len(result[0])):
        text += result[0][i][1][0] + "\n"
    print(text)
    pyperclip.copy(text)

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
'''
clipboard_monitor.on_update(print())
clipboard_monitor.on_text(print("text"))
clipboard_monitor.on_image(clipToText())
clipboard_monitor.wait()
'''
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    clipboard_monitor.on_update(print())
    clipboard_monitor.on_text(print("text"))
    clipboard_monitor.on_image(clipToText())
    listener.join()
