import time
import keyboard
from python_imagesearch import imagesearch

while True:


    time.sleep(8)

    skl_1 = imagesearch.imagesearch("havaklc_2.png")
    skl_2 = imagesearch.imagesearch("ofke_2.png")

    skl1_x = skl_1[0]
    skl1_y = skl_1[1]
    skl2_x = skl_2[0]
    skl2_y = skl_2[1]

    print(skl_1)
    print(skl_2)

    if skl1_x != -1:
        keyboard.press('2')
        time.sleep(0.3)
        keyboard.release("2")
        time.sleep(0.5)
        keyboard.press('3')
        time.sleep(0.3)
        keyboard.release('3')

    if skl2_x != -1:
        keyboard.press('4')
        time.sleep(0.3)
        keyboard.release("4")
        time.sleep(0.5)
        keyboard.press('3')
        time.sleep(0.3)
        keyboard.release('3')
