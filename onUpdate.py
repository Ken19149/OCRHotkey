import clipboard_monitor
from PIL import Image, ImageGrab
import pyperclip
import os
from paddleocr import PaddleOCR

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

    pyperclip.copy(text)

def print_text(text):
	print("got text")
	print(text)

def print_files(files):
	print("got files")
	print(files)

clipboard_monitor.on_update(print)
clipboard_monitor.on_text(print_text)
clipboard_monitor.on_files(print_files)
clipboard_monitor.on_image(clipToText())
clipboard_monitor.wait()
