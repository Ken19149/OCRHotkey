from PIL import ImageGrab

def isClipboardImg():
    try:
        img_clip = ImageGrab.grabclipboard()
        print("ya")
        img_clip.save("test2.png", "PNG")
        print("yes")
    except: 
        print("not img")

isClipboardImg()