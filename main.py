from paddleocr import PaddleOCR
from PIL import ImageGrab
import pyperclip
import os
import clipboard_monitor
import socket


# task 1 - add preset (box position) for applications (genshin, star rail, etc)
# task 2 - make the program loop so as to not wait long for the model to load

# dialogue box position
genshin = (444, 1390, 2110, 1494) # (x1, y1, x2, y2)
genshin_teapot = (444, 1370, 2110, 1470)
HSR = (310, 1230, 2240, 1350)
zzz = (600, 1200, 1900, 1480)

mode = zzz

ocr = PaddleOCR(use_angle_cls=True, lang="japan")

port = 4444
server = socket.socket()
server.bind(("127.0.0.1", port))
server.listen(1)

def isClipboardImg():
    try:
        img = ImageGrab.grabclipboard()
        img.save("test.png", "PNG")
        return True     # if can save img then clipboard = img
    except: 
        return False    # if couldn't then clipboard isn't

def clipToText(ocr=ocr, mode=mode):
    if isClipboardImg():
        img = ImageGrab.grabclipboard()
        img.save("OCR_temp.png", "PNG")
    else:
        img = ImageGrab.grab(bbox=mode, all_screens=False)
        img.save("OCR_temp.png", "PNG")

    img_path = "OCR_temp.png"
    result = ocr.ocr(img_path, cls=True)
    os.remove("OCR_temp.png")

    text = ""
    # combine text result
    try:
        for i in range(len(result[0])):
            text += result[0][i][1][0] # + "\n"
    except:
        pass
    
    pyperclip.copy(text)
    return text

while True:
    c, addr = server.accept()
    print("loading")
    print(clipToText()) 
    c.close()
