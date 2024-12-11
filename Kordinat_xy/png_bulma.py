from python_imagesearch import imagesearch
import time
import keyboard
import pyautogui


while True:



    time.sleep(0.3)

    metin_1 = imagesearch.imagesearch("dolu_bar.png")
    metin_2 = imagesearch.imagesearch("can_bas.png")

    metin1_x = metin_1[0]
    metin1_y = metin_1[1]
    metin2_x = metin_2[0]
    metin2_y = metin_2[1]

    print(metin_1)
    print(metin_2)