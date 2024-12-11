from python_imagesearch import imagesearch
import time
import pyautogui

buton0_konumx = 510
buton0_konumy = 660

buton1_konumx = 530
buton1_konumy = 600

buton2_konumx = 555
buton2_konumy = 660

buton3_konumx = 571
buton3_konumy = 600

buton4_konumx = 600
buton4_konumy = 660

buton5_konumx = 614
buton5_konumy = 600

buton6_konumx = 640
buton6_konumy = 660

buton7_konumx = 656
buton7_konumy = 600

buton8_konumx = 680
buton8_konumy = 660



def basma8():
    pyautogui.moveTo(buton8_konumx + 0, buton8_konumy - 0)
    time.sleep(2)
    pyautogui.click(buton8_konumx + 0, buton8_konumy - 0)
    time.sleep(3)
    pyautogui.moveTo(buton7_konumx + 0, buton7_konumy - 0)
    time.sleep(2)
    pyautogui.click(buton7_konumx + 0, buton7_konumy - 0)
    time.sleep(3)
    pyautogui.moveTo(buton6_konumx + 0, buton6_konumy - 0)
    time.sleep(2)
    pyautogui.click(buton6_konumx + 0, buton6_konumy - 0)
    time.sleep(3)
    pyautogui.moveTo(buton5_konumx + 0, buton5_konumy - 0)
    time.sleep(2)
    pyautogui.click(buton5_konumx + 0, buton5_konumy - 0)
    time.sleep(3)
    pyautogui.moveTo(buton4_konumx + 0, buton4_konumy - 0)
    time.sleep(2)
    pyautogui.click(buton4_konumx + 0, buton4_konumy - 0)
    time.sleep(3)
    pyautogui.moveTo(buton3_konumx + 0, buton3_konumy - 0)
    time.sleep(2)
    pyautogui.click(buton3_konumx + 0, buton3_konumy - 0)
    time.sleep(3)
    pyautogui.moveTo(buton2_konumx + 0, buton2_konumy - 0)
    time.sleep(2)
    pyautogui.click(buton2_konumx + 0, buton2_konumy - 0)
    time.sleep(3)
    pyautogui.moveTo(buton1_konumx + 0, buton1_konumy - 0)
    time.sleep(2)
    pyautogui.click(buton1_konumx + 0, buton1_konumy - 0)
    time.sleep(3)
    pyautogui.moveTo(buton0_konumx + 0, buton0_konumy - 0)
    time.sleep(2)
    pyautogui.click(buton0_konumx + 0, buton0_konumy - 0)
    time.sleep(3)

basla_konumx = 679
basla_konumy = 659

etkinlik_konumx = 1150
etkinlik_konumy = 70

kahin_konumx = 720
kahin_konumy = 225

start_konumx = 650
start_konumy = 675

evet_konumx = 605
evet_konumy = 560


while True:
    try:
        basla_konum_rgb = pyautogui.pixel(basla_konumx, basla_konumy)
        if (basla_konum_rgb[0] == 148) and (basla_konum_rgb[1] == 146):
            basma8()
            time.sleep(10)
        else:
            pyautogui.moveTo(etkinlik_konumx + 0, etkinlik_konumy - 0)
            time.sleep(2)
            pyautogui.click(etkinlik_konumx + 0, etkinlik_konumy - 0)
            time.sleep(3)
            pyautogui.moveTo(kahin_konumx + 0, kahin_konumy - 0)
            time.sleep(2)
            pyautogui.click(kahin_konumx + 0, kahin_konumy - 0)
            time.sleep(3)
            pyautogui.moveTo(start_konumx + 0, start_konumy - 0)
            time.sleep(2)
            pyautogui.click(start_konumx + 0, start_konumy - 0)
            time.sleep(3)
            pyautogui.moveTo(evet_konumx + 0, evet_konumy - 0)
            time.sleep(2)
            pyautogui.click(evet_konumx + 0, evet_konumy - 0)
            time.sleep(3)



    except:
        pass


