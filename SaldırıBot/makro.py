import pyautogui
import keyboard
import time


def sag_basma():
    pyautogui.moveTo(sag_konumx + 0, sag_konumy - 0)
    time.sleep(2)
    pyautogui.click(sag_konumx + 0, sag_konumy - 0)
    time.sleep(10)


sag_konumx = 1282
sag_konumy = 684


def client6_acma():
    pyautogui.moveTo(client6_konumx + 0, client6_konumy - 0)
    time.sleep(2)
    pyautogui.click(client6_konumx + 0, client6_konumy - 0)
    time.sleep(10)


client6_konumx = 838
client6_konumy = 559


def client5_acma():
    pyautogui.moveTo(client5_konumx + 0, client5_konumy - 0)
    time.sleep(2)
    pyautogui.click(client5_konumx + 0, client5_konumy - 0)
    time.sleep(10)


client5_konumx = 838
client5_konumy = 522



while True:
    try:
        sag_konum_rgb = pyautogui.pixel(sag_konumx, sag_konumy)
        if (sag_konum_rgb[0] == 2) and (sag_konum_rgb[1] == 150):
            sag_basma()


            while True:
                try:
                    client6_konum_rgb = pyautogui.pixel(client6_konumx, client6_konumy)
                    if (client6_konum_rgb[0] == 0) and (client6_konum_rgb[1] == 153):
                        client6_acma()

            while True:
                try:
                    client5_konum_rgb = pyautogui.pixel(client5_konumx, client5_konumy)
                    if (client5_konum_rgb[0] == 0) and (client5_konum_rgb[1] == 153):
                        client5_acma()


                except:
                    pass

                except:
                    pass
    except:
        pass