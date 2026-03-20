import time
import os
import subprocess
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

from paddleocr import PaddleOCR

print("Loading PaddleOCR model for Chinese...")
ocr = PaddleOCR(use_textline_orientation=True, lang="ch")
print("PaddleOCR Daemon is running and watching for screenshots!")

# Notice this is a DIFFERENT path than Meiki!
capture_path = "/tmp/paddle_capture.png"

while True:
    if os.path.exists(capture_path):
        try:
            raw_result = ocr.ocr(capture_path)
            
            text_lines = []
            if raw_result and len(raw_result) > 0 and raw_result[0] is not None:
                res = raw_result[0]
                
                if isinstance(res, list):
                    for item in res:
                        if isinstance(item, list) and len(item) == 2:
                            text_lines.append(item[1][0]) # Grab just the string
                elif isinstance(res, dict):
                    texts = res.get('rec_text') or res.get('rec_texts') or res.get('texts') or []
                    text_lines.extend(texts)
                elif hasattr(res, 'boxes'):
                    text_lines.extend(res.txts)

            # Join without spaces just like we did for Meiki
            final_text = ''.join(text_lines)
            
            if final_text.strip():
                subprocess.run(['wl-copy'], input=final_text.encode('utf-8'), check=True)
                print(f"Scanned Chinese: {final_text}")
            else:
                print("No Chinese text detected.")
                
            os.remove(capture_path)
            
        except Exception as e:
            print(f"Error scanning: {e}")
            if os.path.exists(capture_path):
                os.remove(capture_path)
            
    time.sleep(0.5)
