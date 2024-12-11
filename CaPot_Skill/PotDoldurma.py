from python_imagesearch import imagesearch
import time
import pyautogui

while True:

    time.sleep(0.2)

    buton_1 = imagesearch.imagesearch("1.png")
    buton_2 = imagesearch.imagesearch("2.png")
    buton_3 = imagesearch.imagesearch("3.png")
    buton_4 = imagesearch.imagesearch("4.png")
    buton_5 = imagesearch.imagesearch("5.png")
    buton_6 = imagesearch.imagesearch("6.png")
    buton_7 = imagesearch.imagesearch("7.png")
    buton_8 = imagesearch.imagesearch("8.png")
    buton_9 = imagesearch.imagesearch("9.png")
    buton_0 = imagesearch.imagesearch("0.png")
    buton_tik = imagesearch.imagesearch("tik.png")

    kod_1 = imagesearch.imagesearch("11.png", region=(100, 1001, 300, 3036))
    kod_2 = imagesearch.imagesearch("22.png", region=(100, 1002, 300, 3009))
    kod_3 = imagesearch.imagesearch("33.png", region=(100, 1003, 300, 3008))
    kod_4 = imagesearch.imagesearch("44.png", region=(100, 1004, 300, 3007))
    kod_5 = imagesearch.imagesearch("55.png", region=(100, 1005, 300, 3006))
    kod_6 = imagesearch.imagesearch("66.png", region=(100, 1006, 300, 3005))
    kod_7 = imagesearch.imagesearch("77.png", region=(100, 1007, 300, 3004))
    kod_8 = imagesearch.imagesearch("88.png", region=(100, 1008, 300, 3003))
    kod_9 = imagesearch.imagesearch("99.png", region=(100, 1009, 300, 3002))
    kod_0 = imagesearch.imagesearch("00.png", region=(100, 1024, 300, 3001))

    kod1_x = kod_1[0]
    kod1_y = kod_1[1]
    kod2_x = kod_2[0]
    kod2_y = kod_2[1]
    kod3_x = kod_3[0]
    kod3_y = kod_3[1]
    kod4_x = kod_4[0]
    kod4_y = kod_4[1]
    kod5_x = kod_5[0]
    kod5_y = kod_5[1]
    kod6_x = kod_6[0]
    kod6_y = kod_6[1]
    kod7_x = kod_7[0]
    kod7_y = kod_7[1]
    kod8_x = kod_8[0]
    kod8_y = kod_8[1]
    kod9_x = kod_9[0]
    kod9_y = kod_9[1]
    kod0_x = kod_0[0]
    kod0_y = kod_0[1]

    buton1_x = buton_1[0]
    buton1_y = buton_1[1]
    buton2_x = buton_2[0]
    buton2_y = buton_2[1]
    buton3_x = buton_3[0]
    buton3_y = buton_3[1]
    buton4_x = buton_4[0]
    buton4_y = buton_4[1]
    buton5_x = buton_5[0]
    buton5_y = buton_5[1]
    buton6_x = buton_6[0]
    buton6_y = buton_6[1]
    buton7_x = buton_7[0]
    buton7_y = buton_7[1]
    buton8_x = buton_8[0]
    buton8_y = buton_8[1]
    buton9_x = buton_9[0]
    buton9_y = buton_9[1]
    buton0_x = buton_0[0]
    buton0_y = buton_0[1]
    butontik_x = buton_tik[0]
    butontik_y = buton_tik[1]

    print(kod_1)
    print(kod_2)
    print(kod_3)
    print(kod_4)
    print(kod_5)
    print(kod_6)
    print(kod_7)
    print(kod_8)
    print(kod_9)
    print(kod_0)


    def basma1():
        pyautogui.moveTo(buton1_x + 0, buton1_y - 0)
        time.sleep(2)
        pyautogui.click(buton1_x + 0, buton1_y - 0)
        time.sleep(3)


    def basma2():
        pyautogui.moveTo(buton2_x + 0, buton2_y - 0)
        time.sleep(0.4)
        pyautogui.click(buton2_x + 0, buton2_y - 0)
        time.sleep(3)


    def basma3():
        pyautogui.moveTo(buton3_x + 0, buton3_y - 0)
        time.sleep(0.4)
        pyautogui.click(buton3_x + 0, buton3_y - 0)
        time.sleep(3)


    def basma4():
        pyautogui.moveTo(buton4_x + 0, buton4_y - 0)
        time.sleep(0.4)
        pyautogui.click(buton4_x + 0, buton4_y - 0)
        time.sleep(3)


    def basma5():
        pyautogui.moveTo(buton5_x + 0, buton5_y - 0)
        time.sleep(0.4)
        pyautogui.click(buton5_x + 0, buton5_y - 0)
        time.sleep(3)


    def basma6():
        pyautogui.moveTo(buton6_x + 0, buton6_y - 0)
        time.sleep(0.4)
        pyautogui.click(buton6_x + 0, buton6_y - 0)
        time.sleep(3)


    def basma7():
        pyautogui.moveTo(buton7_x + 0, buton7_y - 0)
        time.sleep(0.4)
        pyautogui.click(buton7_x + 0, buton7_y - 0)
        time.sleep(3)


    def basma8():
        pyautogui.moveTo(buton8_x + 0, buton8_y - 0)
        time.sleep(0.4)
        pyautogui.click(buton8_x + 0, buton8_y - 0)
        time.sleep(3)


    def basma9():
        pyautogui.moveTo(buton9_x + 0, buton9_y - 0)
        time.sleep(0.4)
        pyautogui.click(buton9_x + 0, buton9_y - 0)
        time.sleep(3)


    def basma0():
        pyautogui.moveTo(buton0_x + 0, buton0_y - 0)
        time.sleep(0.4)
        pyautogui.click(buton0_x + 0, buton0_y - 0)
        time.sleep(3)


    if kod1_x != -1:
        basma1()

    if kod1_x != -1:
        basma2()

    if kod1_x != -1:
        basma3()

    if kod1_x != -1:
        basma4()

    if kod1_x != -1:
        basma5()

    if kod1_x != -1:
        basma6()

    if kod1_x != -1:
        basma7()

    if kod1_x != -1:
        basma8()

    if kod1_x != -1:
        basma9()

    if kod1_x != -1:
        basma0()

    while True:

        time.sleep(0.2)

        kod_1 = imagesearch.imagesearch("11.png", region=(100, 100, 3600, 555))
        kod_2 = imagesearch.imagesearch("22.png", region=(100, 100, 3700, 555))
        kod_3 = imagesearch.imagesearch("33.png", region=(100, 100, 3900, 555))
        kod_4 = imagesearch.imagesearch("44.png", region=(100, 100, 3070, 555))
        kod_5 = imagesearch.imagesearch("55.png", region=(100, 100, 3080, 555))
        kod_6 = imagesearch.imagesearch("66.png", region=(100, 100, 3060, 555))
        kod_7 = imagesearch.imagesearch("77.png", region=(100, 100, 3050, 555))
        kod_8 = imagesearch.imagesearch("88.png", region=(100, 100, 3040, 555))
        kod_9 = imagesearch.imagesearch("99.png", region=(100, 100, 3030, 555))
        kod_0 = imagesearch.imagesearch("00.png", region=(100, 100, 3020, 555))


        def basma1():
            pyautogui.moveTo(buton1_x + 0, buton1_y - 0)
            time.sleep(2)
            pyautogui.click(buton1_x + 0, buton1_y - 0)
            time.sleep(3)


        def basma2():
            pyautogui.moveTo(buton2_x + 0, buton2_y - 0)
            time.sleep(0.4)
            pyautogui.click(buton2_x + 0, buton2_y - 0)
            time.sleep(3)


        def basma3():
            pyautogui.moveTo(buton3_x + 0, buton3_y - 0)
            time.sleep(0.4)
            pyautogui.click(buton3_x + 0, buton3_y - 0)
            time.sleep(3)


        def basma4():
            pyautogui.moveTo(buton4_x + 0, buton4_y - 0)
            time.sleep(0.4)
            pyautogui.click(buton4_x + 0, buton4_y - 0)
            time.sleep(3)


        def basma5():
            pyautogui.moveTo(buton5_x + 0, buton5_y - 0)
            time.sleep(0.4)
            pyautogui.click(buton5_x + 0, buton5_y - 0)
            time.sleep(3)


        def basma6():
            pyautogui.moveTo(buton6_x + 0, buton6_y - 0)
            time.sleep(0.4)
            pyautogui.click(buton6_x + 0, buton6_y - 0)
            time.sleep(3)


        def basma7():
            pyautogui.moveTo(buton7_x + 0, buton7_y - 0)
            time.sleep(0.4)
            pyautogui.click(buton7_x + 0, buton7_y - 0)
            time.sleep(3)


        def basma8():
            pyautogui.moveTo(buton8_x + 0, buton8_y - 0)
            time.sleep(0.4)
            pyautogui.click(buton8_x + 0, buton8_y - 0)
            time.sleep(3)


        def basma9():
            pyautogui.moveTo(buton9_x + 0, buton9_y - 0)
            time.sleep(0.4)
            pyautogui.click(buton9_x + 0, buton9_y - 0)
            time.sleep(3)


        def basma0():
            pyautogui.moveTo(buton0_x + 0, buton0_y - 0)
            time.sleep(0.4)
            pyautogui.click(buton0_x + 0, buton0_y - 0)
            time.sleep(3)


        if kod1_x != -1:
            basma1()

        if kod1_x != -1:
            basma2()

        if kod1_x != -1:
            basma3()

        if kod1_x != -1:
            basma4()

        if kod1_x != -1:
            basma5()

        if kod1_x != -1:
            basma6()

        if kod1_x != -1:
            basma7()

        if kod1_x != -1:
            basma8()

        if kod1_x != -1:
            basma9()

        if kod1_x != -1:
            basma0()

        while True:

            time.sleep(0.2)

            kod_1 = imagesearch.imagesearch("11.png", region=(100, 1900, 300, 444))
            kod_2 = imagesearch.imagesearch("22.png", region=(100, 1800, 300, 444))
            kod_3 = imagesearch.imagesearch("33.png", region=(100, 1700, 300, 444))
            kod_4 = imagesearch.imagesearch("44.png", region=(100, 600, 300, 444))
            kod_5 = imagesearch.imagesearch("55.png", region=(100, 1500, 300, 444))
            kod_6 = imagesearch.imagesearch("66.png", region=(100, 1400, 300, 444))
            kod_7 = imagesearch.imagesearch("77.png", region=(100, 1300, 300, 444))
            kod_8 = imagesearch.imagesearch("88.png", region=(100, 1200, 300, 444))
            kod_9 = imagesearch.imagesearch("99.png", region=(100, 100, 300, 444))
            kod_0 = imagesearch.imagesearch("00.png", region=(100, 1020, 300, 444))


            def basma1():
                pyautogui.moveTo(buton1_x + 0, buton1_y - 0)
                time.sleep(2)
                pyautogui.click(buton1_x + 0, buton1_y - 0)
                time.sleep(3)


            def basma2():
                pyautogui.moveTo(buton2_x + 0, buton2_y - 0)
                time.sleep(0.4)
                pyautogui.click(buton2_x + 0, buton2_y - 0)
                time.sleep(3)


            def basma3():
                pyautogui.moveTo(buton3_x + 0, buton3_y - 0)
                time.sleep(0.4)
                pyautogui.click(buton3_x + 0, buton3_y - 0)
                time.sleep(3)


            def basma4():
                pyautogui.moveTo(buton4_x + 0, buton4_y - 0)
                time.sleep(0.4)
                pyautogui.click(buton4_x + 0, buton4_y - 0)
                time.sleep(3)


            def basma5():
                pyautogui.moveTo(buton5_x + 0, buton5_y - 0)
                time.sleep(0.4)
                pyautogui.click(buton5_x + 0, buton5_y - 0)
                time.sleep(3)


            def basma6():
                pyautogui.moveTo(buton6_x + 0, buton6_y - 0)
                time.sleep(0.4)
                pyautogui.click(buton6_x + 0, buton6_y - 0)
                time.sleep(3)


            def basma7():
                pyautogui.moveTo(buton7_x + 0, buton7_y - 0)
                time.sleep(0.4)
                pyautogui.click(buton7_x + 0, buton7_y - 0)
                time.sleep(3)


            def basma8():
                pyautogui.moveTo(buton8_x + 0, buton8_y - 0)
                time.sleep(0.4)
                pyautogui.click(buton8_x + 0, buton8_y - 0)
                time.sleep(3)


            def basma9():
                pyautogui.moveTo(buton9_x + 0, buton9_y - 0)
                time.sleep(0.4)
                pyautogui.click(buton9_x + 0, buton9_y - 0)
                time.sleep(3)


            def basma0():
                pyautogui.moveTo(buton0_x + 0, buton0_y - 0)
                time.sleep(0.4)
                pyautogui.click(buton0_x + 0, buton0_y - 0)
                time.sleep(3)


            if kod1_x != -1:
                basma1()

            if kod1_x != -1:
                basma2()

            if kod1_x != -1:
                basma3()

            if kod1_x != -1:
                basma4()

            if kod1_x != -1:
                basma5()

            if kod1_x != -1:
                basma6()

            if kod1_x != -1:
                basma7()

            if kod1_x != -1:
                basma8()

            if kod1_x != -1:
                basma9()

            if kod1_x != -1:
                basma0()

            while True:

                time.sleep(0.2)

                kod_1 = imagesearch.imagesearch("11.png", region=(100, 100, 3300, 333))
                kod_2 = imagesearch.imagesearch("22.png", region=(100, 100, 3020, 333))
                kod_3 = imagesearch.imagesearch("33.png", region=(100, 100, 3100, 333))
                kod_4 = imagesearch.imagesearch("44.png", region=(100, 100, 3030, 333))
                kod_5 = imagesearch.imagesearch("55.png", region=(100, 100, 3040, 333))
                kod_6 = imagesearch.imagesearch("66.png", region=(100, 100, 3090, 333))
                kod_7 = imagesearch.imagesearch("77.png", region=(100, 100, 3080, 333))
                kod_8 = imagesearch.imagesearch("88.png", region=(100, 100, 3070, 333))
                kod_9 = imagesearch.imagesearch("99.png", region=(100, 100, 3060, 333))
                kod_0 = imagesearch.imagesearch("00.png", region=(100, 100, 3050, 333))


                def basma1():
                    pyautogui.moveTo(buton1_x + 0, buton1_y - 0)
                    time.sleep(2)
                    pyautogui.click(buton1_x + 0, buton1_y - 0)
                    time.sleep(3)


                def basma2():
                    pyautogui.moveTo(buton2_x + 0, buton2_y - 0)
                    time.sleep(0.4)
                    pyautogui.click(buton2_x + 0, buton2_y - 0)
                    time.sleep(3)


                def basma3():
                    pyautogui.moveTo(buton3_x + 0, buton3_y - 0)
                    time.sleep(0.4)
                    pyautogui.click(buton3_x + 0, buton3_y - 0)
                    time.sleep(3)


                def basma4():
                    pyautogui.moveTo(buton4_x + 0, buton4_y - 0)
                    time.sleep(0.4)
                    pyautogui.click(buton4_x + 0, buton4_y - 0)
                    time.sleep(3)


                def basma5():
                    pyautogui.moveTo(buton5_x + 0, buton5_y - 0)
                    time.sleep(0.4)
                    pyautogui.click(buton5_x + 0, buton5_y - 0)
                    time.sleep(3)


                def basma6():
                    pyautogui.moveTo(buton6_x + 0, buton6_y - 0)
                    time.sleep(0.4)
                    pyautogui.click(buton6_x + 0, buton6_y - 0)
                    time.sleep(3)


                def basma7():
                    pyautogui.moveTo(buton7_x + 0, buton7_y - 0)
                    time.sleep(0.4)
                    pyautogui.click(buton7_x + 0, buton7_y - 0)
                    time.sleep(3)


                def basma8():
                    pyautogui.moveTo(buton8_x + 0, buton8_y - 0)
                    time.sleep(0.4)
                    pyautogui.click(buton8_x + 0, buton8_y - 0)
                    time.sleep(3)


                def basma9():
                    pyautogui.moveTo(buton9_x + 0, buton9_y - 0)
                    time.sleep(0.4)
                    pyautogui.click(buton9_x + 0, buton9_y - 0)
                    time.sleep(3)


                def basma0():
                    pyautogui.moveTo(buton0_x + 0, buton0_y - 0)
                    time.sleep(0.4)
                    pyautogui.click(buton0_x + 0, buton0_y - 0)
                    time.sleep(3)


                if kod1_x != -1:
                    basma1()

                if kod1_x != -1:
                    basma2()

                if kod1_x != -1:
                    basma3()

                if kod1_x != -1:
                    basma4()

                if kod1_x != -1:
                    basma5()

                if kod1_x != -1:
                    basma6()

                if kod1_x != -1:
                    basma7()

                if kod1_x != -1:
                    basma8()

                if kod1_x != -1:
                    basma9()

                if kod1_x != -1:
                    basma0()

                while True:

                    time.sleep(0.2)


                    def basmatik():
                        pyautogui.moveTo(butontik_x + 0, butontik_y - 0)
                        time.sleep(0.4)
                        pyautogui.click(butontik_x + 0, butontik_y - 0)
                        time.sleep(3)


                    if kod1_x != -1:
                        basmatik()
