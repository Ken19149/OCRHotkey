from paddleocr import PaddleOCR
import pyperclip

ocr = PaddleOCR(use_angle_cls=True, lang="japan")
img_path = "img/test.png"
result = ocr.ocr(img_path, cls=True)

# print each line
for i in range(len(result)):
    res = result[i]
    for line in res:
        print(line)

text = ""
# combine text result
for i in range(len(result[0])):
    text += result[0][i][1][0] + "\n"
    print(result[0][i][1][0])

print(text)

pyperclip.copy(text)