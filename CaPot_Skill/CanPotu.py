import pyautogui
import keyboard
import time

def can_basma():
    keyboard.press('1')
    time.sleep(0.2)
    keyboard.release("1")

can_konumx = 154
can_konumy = 1033



while True:
    try:
        can_konum_rgb = pyautogui.pixel(can_konumx, can_konumy)
        if (can_konum_rgb[0] == 43) and (can_konum_rgb[1] == 43):
            can_basma()

    except:
        pass
