# v2 will use websockets to transfer data 

from paddleocr import PaddleOCR
from PIL import ImageGrab, Image, ImageDraw, ImageFont
import numpy as np
import json
import asyncio
import websockets
import os
import time

ocr = PaddleOCR(use_gpu=True, use_angle_cls=True, lang="japan")

def drawBox(path="web/output/screen_temp.png", result=[]):
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
    img_box.close()


def start(ocr=ocr, save_screen=True, box=True):
    try:
        ss = ImageGrab.grab()   # screenshot
        ss.save("web/output/screen_temp.png")
        ss.close()
        
        result = ocr.ocr("web/output/screen_temp.png", cls=True)
        result.append([ss.width, ss.height])

        if box:
            drawBox(result=result)
        if not save_screen:
            os.remove("web/output/screen_temp.png")

        return json.dumps(result, ensure_ascii=False)

    except Exception as e:
        print(f"Error in start function: {e}")
        return json.dumps({"error": str(e)})


# A sample data-generating function that sends data to the client every second.
async def send_data(websocket, path):
    while True:
        # Create a sample message (e.g., a counter value)
        message = start()

        # print("msg: " + message)
        await websocket.send(message)

        print(f"Sent: {message}")
        await asyncio.sleep(1)

# Start the WebSocket server
start_server = websockets.serve(send_data, "localhost", 6789)

# Run the server
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
