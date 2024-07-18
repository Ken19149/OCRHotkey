from paddleocr import PaddleOCR
from PIL import ImageGrab, Image, ImageDraw, ImageFont
import numpy as np
import json
import os

ocr = PaddleOCR(use_angle_cls=True, lang="japan")
ss = ImageGrab.grab()   # screenshot
ss.save("web/output/screen_temp.png")
ss.close()

result = ocr.ocr("web/output/screen_temp.png", cls=True)
# os.remove("screen_temp.png")

def drawBox(path="web/output/screen_temp.png", result=result):
    img_box = Image.open(path) 
    draw = ImageDraw.Draw(img_box)  
    font = ImageFont.load_default(size=16)
    for i, box in enumerate(result[0]):
        box = np.array(box[0]).astype(np.int32)
        xmin = min(box[:, 0])
        ymin = min(box[:, 1])
        xmax = max(box[:, 0])
        ymax = max(box[:, 1])
        draw.rectangle((xmin, ymin, xmax, ymax), outline="#00ffff", width=4)
        draw.text((xmin, ymin), f" {i}", fill="#ffffff", font=font, stroke_width=1)
    img_box.save("web/output/screen_box.png")
    # img_box.show()
    img_box.close

# save result file
with open("web/output/result.json", "w", encoding="utf-8") as file:
    json.dump(result, file, ensure_ascii=False, indent=4)

print(result)

drawBox()

