from paddleocr import PaddleOCR
from PIL import ImageGrab
import json
import os

ocr = PaddleOCR(use_angle_cls=True, lang="japan")
ss = ImageGrab.grab()   # screenshot
ss.save("screen_temp.png")
ss.close()

result = ocr.ocr("screen_temp.png", cls=True)
# os.remove("screen_temp.png")



print(result)

with open("result.json", "w", encoding="utf-8") as file:
    json.dump(result, file, ensure_ascii=False, indent=4)