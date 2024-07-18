from paddleocr import PaddleOCR
from PIL import ImageGrab, Image, ImageDraw
import numpy as np
import json
import os

ocr = PaddleOCR(use_angle_cls=True, lang="japan")
ss = ImageGrab.grab()   # screenshot
ss.save("screen_temp.png")
ss.close()

result = ocr.ocr("screen_temp.png", cls=True)
# os.remove("screen_temp.png")

def drawBox(path="screen_temp.png", result=result):
    img_box = Image.open(path) 
    draw = ImageDraw.Draw(img_box)  
    for i, box in enumerate(result[0]):
        box = np.array(box[0]).astype(np.int32)
        xmin = min(box[:, 0])
        ymin = min(box[:, 1])
        xmax = max(box[:, 0])
        ymax = max(box[:, 1])
        draw.rectangle((xmin, ymin, xmax, ymax), outline="red", width=1)
        draw.text((xmin, ymin), f"{i}", fill="black")
    img_box.show()

drawBox()

print(result)

with open("result.json", "w", encoding="utf-8") as file:
    json.dump(result, file, ensure_ascii=False, indent=4)