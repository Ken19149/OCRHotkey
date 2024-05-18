from paddleocr import PaddleOCR
from PIL import ImageGrab

ocr = PaddleOCR(use_angle_cls=True, lang="japan")

img_1 = "test.png"
img_2 = "test1.png"

def scan(img_path):
    result = ocr.ocr(img_path, cls=True)

    text = ""
    for i in range(len(result[0])):
        text += result[0][i][1][0] 

    return text

'''
print(scan(img_1))
print(scan(img_2))
'''

result = ocr.ocr("aaa.png", cls=True)
text = ""
for i in range(len(result[0])):
    text += result[0][i][1][0] 
print(text)