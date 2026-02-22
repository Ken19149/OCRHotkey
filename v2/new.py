import subprocess
import json
import asyncio
import websockets
import os
import warnings

# Hide the annoying PaddleOCR deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Bypass the C++ bug
os.environ['FLAGS_enable_pir_api'] = '0'
os.environ['FLAGS_use_mkldnn'] = '0'

from paddleocr import PaddleOCR
from PIL import Image

# Initialize the Chinese model
print("Loading PaddleOCR Model...")
ocr = PaddleOCR(use_textline_orientation=True, lang="ch")
print("Model Loaded!")

def start(save_screen=True, box=False):
    try:
        path = "web/output/screen_temp.png"
        
        print(" -> Capturing screen...")
        subprocess.run(["grim", "-o", "eDP-2", path], check=True)
        file_size = os.path.getsize(path)
        
        print(f" -> Screen captured ({file_size} bytes). Scanning...")
        raw_result = ocr.ocr(path) 
        
        print(" -> Scan complete! Formatting data...")
        if not isinstance(raw_result, list):
            raw_result = list(raw_result)

        detections = []
        if raw_result and len(raw_result) > 0 and raw_result[0] is not None:
            res = raw_result[0]
            
            if isinstance(res, list):
                # Standard v2 List Format
                for item in res:
                    if isinstance(item, list) and len(item) == 2:
                        box = item[0]
                        if hasattr(box, 'tolist'): box = box.tolist() # Fix Numpy Crash
                        detections.append([box, item[1]])
                        
            elif isinstance(res, dict):
                # Robust Dict Extraction (Catches ALL known Paddle v3/PaddleX keys)
                boxes = res.get('dt_polys') or res.get('rec_boxes') or res.get('boxes') or []
                texts = res.get('rec_text') or res.get('rec_texts') or res.get('texts') or []
                scores = res.get('rec_score') or res.get('rec_scores') or res.get('scores') or []
                
                for b, t, s in zip(boxes, texts, scores):
                    if hasattr(b, 'tolist'): 
                        b = b.tolist() # Convert Numpy arrays to JSON-safe lists
                    detections.append([b, (t, s)])
                    
            elif hasattr(res, 'boxes'):
                # Object Attribute Format
                for b, t, s in zip(res.boxes, res.txts, res.scores):
                    if hasattr(b, 'tolist'): b = b.tolist()
                    detections.append([b, (t, s)])

        img = Image.open(path)
        width, height = img.size
        img.close()

        formatted_result = [detections, [width, height]]

        if not save_screen and os.path.exists(path):
            os.remove(path)
            
        print(f" -> Success! Found {len(detections)} text blocks.\n")
        return json.dumps(formatted_result, ensure_ascii=False)

    except Exception as e:
        print(f"Error in start function: {e}")
        return json.dumps([[], [2560, 1600]])

async def send_data(websocket):
    print("\n[SUCCESS] Browser connected! Starting continuous scan...\n")
    try:
        while True:
            # Run the heavy OCR task in a separate thread to prevent freezing
            message = await asyncio.to_thread(start)
            await websocket.send(message)
            await asyncio.sleep(0.5)
    except websockets.exceptions.ConnectionClosed:
        print("\n[INFO] Browser disconnected. Waiting for reconnect...")

async def main():
    async with websockets.serve(send_data, "localhost", 6789):
        print("\n[INFO] Server is running! Open index.html in your browser.")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
