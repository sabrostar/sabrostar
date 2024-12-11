import keyboard
import pyautogui
import time


while True:
    try:
        a = pyautogui.position()
        a_1 = a[0]
        a_2 = a[1]
        r, g, b = pyautogui.pixel(a_1,a_2)
        print(r, " ", g, " ", b)
        time.sleep(0.5)
    except:
        pass

