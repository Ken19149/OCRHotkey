import win32clipboard
from PIL import ImageGrab


win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

print(type(data))

# data = ImageGrab.grabclipboard()
'''
genshin = (444, 1390, 2110, 1494) # (x1, y1, x2, y2)

ss = ImageGrab.grab(bbox=genshin, all_screens=False)
ss.save("test.png", "PNG")
'''