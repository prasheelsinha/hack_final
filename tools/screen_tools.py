import pyautogui
from PIL import Image
from datetime import datetime

def capture_screen():
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    img = pyautogui.screenshot()
    img.convert("RGB").save(f"screen_{ts}.jpg", "JPEG")