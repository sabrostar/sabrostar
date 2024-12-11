import time
import cv2
import numpy as np
import win32api, win32con
from PIL import ImageGrab

# Başlangıç koordinatları
x, y = 309, 265
center_x, center_y = 244, 172
radius = 65

# Hedef görüntü
target_image_path = 'image/deneme.png'

# Benzerlik eşik değeri
threshold = 0.68

while True:
    # Ekran görüntüsü al
    screenshot = ImageGrab.grab(bbox=(0, 0, 1920, 1080))  # Ekran boyutlarına göre ayarlayın

    # OpenCV için uygun formata dönüştür
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Belirlenen alan içinde ROI (Region of Interest) oluştur
    roi = frame[y - radius:y + radius, x - radius:x + radius]

    # Hedef görüntüyü yükle
    target_image = cv2.imread(target_image_path, cv2.IMREAD_COLOR)

    # Template matching işlemi
    result = cv2.matchTemplate(roi, target_image, cv2.TM_CCOEFF_NORMED)

    # Benzerlik değeri ve konumu al
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    # Benzerlik değeri belirli bir eşik değerinden büyükse
    if max_val > threshold:
        # Hedef görüntü bulundu
        target_x, target_y = max_loc

        # Hedef görüntüyü içeren alanın merkezi
        target_center_x = x - radius + target_x + int(target_image.shape[1] / 2)
        target_center_y = y - radius + target_y + int(target_image.shape[0] / 2)

        # Sol tıklamayı bir tık önüne yap
        win32api.SetCursorPos((target_center_x, target_center_y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, target_center_x, target_center_y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, target_center_x, target_center_y, 0, 0)
        time.sleep(0.2)
        continue
    # Her turda bir süre bekle
    cv2.waitKey(1)