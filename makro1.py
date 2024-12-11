import pyautogui
import time

def click_and_wait(x, y):
    pyautogui.click(x, y)
    time.sleep(5)



def open_client(x, y, color):
    rgb = pyautogui.pixel(x, y)
    if rgb[0] == color[0] and rgb[1] == color[1]:
        time.sleep(60)
        click_and_wait(x, y)


client1_konum = (1410, 735)
client2_konum = (1410, 775)
client3_konum = (1410, 813)
client4_konum = (1410, 850)
sag_konum = (1856, 900)
client5_konum = (1410, 735)
client6_konum = (1410, 775)
sol_konum = (1799, 902)


client1_color = (0, 153, 213)
client2_color = (0, 153, 213)
client3_color = (0, 153, 213)
client4_color = (0, 153, 213)
sag_konum_color = (2, 150, 210)
client5_color = (0, 153, 213)
client6_color = (0, 153, 213)
sol_konum_color = (2, 150, 210)


while True:
    try:
        open_client(*client1_konum, client1_color)
        open_client(*client2_konum, client2_color)
        open_client(*client3_konum, client3_color)
        open_client(*client4_konum, client4_color)
        open_client(*sag_konum, sag_konum_color)
        open_client(*client5_konum, client5_color)
        open_client(*client6_konum, client6_color)
        open_client(*sol_konum, sol_konum_color)
    except pyautogui.FailSafeException:
        break
    except Exception as e:
        print("An error occurred:", e)
        pass