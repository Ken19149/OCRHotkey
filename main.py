from paddleocr import PaddleOCR
from PIL import ImageGrab
import pyperclip
import os
import clipboard_monitor

genshin = (444, 1390, 2110, 1494) # (x1, y1, x2, y2)

ocr = PaddleOCR(use_angle_cls=True, lang="japan")

def isClipboardImg():
    try:
        img = ImageGrab.grabclipboard()
        img.save("test.png", "PNG")
        return True     # if can save img then clipboard = img
    except: 
        return False    # if couldn't then clipboard isn't

def clipToText(ocr=ocr):
    print(isClipboardImg())
    if isClipboardImg():
        img = ImageGrab.grabclipboard()
        img.save("OCR_temp.png", "PNG")
    else:
        img = ImageGrab.grab(bbox=genshin, all_screens=False)
        img.save("OCR_temp.png", "PNG")

    img_path = "OCR_temp.png"
    result = ocr.ocr(img_path, cls=True)
    os.remove("OCR_temp.png")

    text = ""
    # combine text result
    for i in range(len(result[0])):
        text += result[0][i][1][0] # + "\n"
    
    pyperclip.copy(text)
clipToText()