from python_imagesearch import imagesearch
import time
import keyboard
import pyautogui


while True:



    time.sleep(0.2)

    metin_1 = imagesearch.imagesearch("mtn_1.png")
    metin_2 = imagesearch.imagesearch("mtn_2.png")
    metin_3 = imagesearch.imagesearch("mtn_3.png")
    metin1_x = metin_1[0]
    metin1_y = metin_1[1]
    metin2_x = metin_2[0]
    metin2_y = metin_2[1]
    metin3_x = metin_3[0]
    metin3_y = metin_3[1]

    print(metin_1)
    print(metin_2)
    print(metin_3)

    if metin1_x != -1:
        pyautogui.moveTo(metin1_x+30,metin1_y+90)
        time.sleep(0.4)
        pyautogui.click(metin1_x+30,metin1_y+90)
        time.sleep(600)
    if metin2_x != -1:
        pyautogui.moveTo(metin2_x+30,metin2_y+90)
        time.sleep(0.4)
        pyautogui.click(metin2_x+30,metin2_y+90)
        time.sleep(600)
    if metin3_x != -1:
        pyautogui.moveTo(metin3_x+30,metin3_y+90)
        time.sleep(0.4)
        pyautogui.click(metin3_x+30,metin3_y+60)
        time.sleep(600)

    if metin1_x == -1 and metin2_x == -1:
        if metin3_x == -1:

            keyboard.press("w")
            keyboard.release("w")
            keyboard.press("w")
            time.sleep(3)
            keyboard.release("w")
            time.sleep(0.2)

            keyboard.press("e")
            keyboard.release("e")
            keyboard.press("e")
            time.sleep(0.3)
            keyboard.release("e")
            time.sleep(0.2)
            keyboard.press("g")
            keyboard.release("g")

            keyboard.press("g")
            time.sleep(0.3)
            keyboard.release("g")
            time.sleep(0.2)
            keyboard.press("t")
            keyboard.release("t")

            keyboard.press("t")
            time.sleep(0.4)
            keyboard.release("t")
            time.sleep(0.2)
            keyboard.press("f")
            keyboard.release("f")


            keyboard.press("f")
            time.sleep(0.5)
            keyboard.release("f")
            time.sleep(0.2)


        
 

    

    