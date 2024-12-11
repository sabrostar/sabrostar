from python_imagesearch import imagesearch
import time
import keyboard
import pyautogui


while True:



    time.sleep(0.5)

metin_1 = imagesearch.imagesearch()
metin_2 = imagesearch.imagesearch()
metin_3 = imagesearch.imagesearch()
metin1_x = metin_1[0]
metin1_y = metin_1[1]
metin2_x = metin_2[0]
metin2_y = metin_2[1]
metin3_x = metin_3[0]
metin3_y = metin_3[1]
print(metin_1)
print(metin_2)
print(metin_3)

if metin_1x != -1:
    pyautogui.moveTo(metin1_x+30,metin1_y+60)
    time.sleep(0.4)
    pyautogui.click(metin1_x+30,metin1_y+60)
    time.sleep(600) 
if metin2_x != -1:
    pyautogui.moveTo(metin1_x+30,metin1_y+60)
    time.sleep(0.4)
    pyautogui.click(metin1_x+30,metin1_y+60)
    time.sleep(600)
if metin3_x != -1:
    pyautogui.moveTo(metin1_x+30,metin1_y+60)
    time.sleep(0.4)
    pyautogui.click(metin1_x+30,metin1_y+60)
    time.sleep(600)

if metin1_x == -1 and metin2_x == -1:
    if metin3_x == -1:
        keyboard.press("w")
        keyboard.release("w")
        keyboard.press("w")
        time.sleep("1.0")
        keyboard.release("w") 
        time.sleep("0.3")
        keyboard.press("e")
        keyboard.release("e")
        keyboard.press("e")
        time.sleep("0.3")
        keyboard.release("e")
        time.sleep("0.5")
        keyboard.sleep("g")
        keyboard.release("g")

        keyboard.press("g")
        time.sleep("1.5")
        keyboard.release("g")
        time.sleep("0.5")
        keyboard.press("t")
        keyboard.release("t")

        keyboard.press("t")
        time.sleep("0.7")
        keyboard.release("t")
        time.sleep("0.5")
        keyboard.press("f")
        keyboard.release("f")


        keyboard.press("f")
        time.sleep("0.5")
        keyboard.release("f")
        time.sleep("0.5")


        
 

    

    