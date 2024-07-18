from paddleocr import PaddleOCR
from PIL import ImageGrab
import json

ocr = PaddleOCR(use_angle_cls=True, lang="japan")


result = ocr.ocr("test.png", cls=True)

with open("result.json", "w", encoding="utf-8") as file:
    json.dump(result, file, ensure_ascii=False, indent=4)