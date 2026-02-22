import time
import os
import subprocess
import cv2
from meikiocr import MeikiOCR

print("Loading MeikiOCR model... (this takes a few seconds)")
ocr = MeikiOCR()
print("MeikiOCR Daemon is running and watching for screenshots!")

# We will save our temporary screenshots here
capture_path = "/tmp/meiki_capture.png"

while True:
    # If a new screenshot appears at this path...
    if os.path.exists(capture_path):
        try:
            # 1. Load the image using OpenCV (MeikiOCR expects a numpy array)
            img = cv2.imread(capture_path, cv2.IMREAD_COLOR)

            # 2. Read the text using the correct run_ocr method
            results = ocr.run_ocr(img)
            
            # 3. Extract the text (MeikiOCR returns a list of dicts)
            text = ''.join([line['text'] for line in results if line['text']])
            
            if text.strip():
                # 4. Copy the text directly to your Wayland clipboard for Yomitan
                subprocess.run(['wl-copy'], input=text.encode('utf-8'), check=True)
                print(f"Scanned and copied: {text}")
            else:
                print("No text detected.")
                
            # 5. Delete the image so we don't scan it twice
            os.remove(capture_path)
            
        except Exception as e:
            print(f"Error scanning: {e}")
            if os.path.exists(capture_path):
                os.remove(capture_path)
            
    # Check twice a second (uses almost zero CPU)
    time.sleep(0.5)
