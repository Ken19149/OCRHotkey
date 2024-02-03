from paddleocr import PaddleOCR
from PIL import ImageGrab
import pyperclip
import os

img_clip = ImageGrab.grabclipboard()
img_clip.save("OCR_temp.png", "PNG")

ocr = PaddleOCR(use_angle_cls=True, lang="japan")
img_path = "OCR_temp.png"
result = ocr.ocr(img_path, cls=True)
os.remove("OCR_temp.png")

text = ""
# combine text result
for i in range(len(result[0])):
    text += result[0][i][1][0] + "\n"

print(text)

pyperclip.copy(text)