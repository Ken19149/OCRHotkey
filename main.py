from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang="japan")
img_path = "img/test.png"
result = ocr.ocr(img_path, cls=True)
for i in range(len(result)):
    res = result[i]
    for line in res:
        print(line)

for i in range(len(result[0])):
    print(result[0][i][1][0])

x = [[[[[51.0, 50.0], [318.0, 50.0], [318.0, 98.0], [51.0, 98.0]], ('ゲーム開始', 0.9999405145645142)], [[[13.0, 141.0], [405.0, 142.0], [405.0, 166.0], [13.0, 165.0]], ('何か悩み事?一緒に考えてあげるわ。', 0.91827791929245)], [[[17.0, 270.0], [462.0, 270.0], [462.0, 319.0], [17.0, 319.0]], ('あなたアナタ貴方', 0.9972425103187561)], [[[30.0, 400.0], [279.0, 410.0], [276.0, 485.0], [27.0, 475.0]], ('ちしよょう', 0.8684518933296204)]]]