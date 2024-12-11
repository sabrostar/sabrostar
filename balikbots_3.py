import cv2 as cv
import  numpy as np

cember_img = cv.imread('opencv.png', cv.IMREAD_UNCHANGED)
havuzdakibalik_img = cv.imread('balk_2.png', cv.IMREAD_UNCHANGED)

Result = cv.matchTemplate(cember_img, havuzdakibalik_img, cv.TM_CCOEFF_NORMED)

# en yakın değeri getir
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(Result)

print('Best match top left position: %s' % str(max_loc))
print('Best match confidence: %s' % max_val)
thresold = 0.8
if max_val >= thresold:
    print('Found havuzdakibalik.')

    havuzdakibalik_w = havuzdakibalik_img.shape[1]
    havuzdakibalik_h = havuzdakibalik_img.shape[0]

    top_left = max_loc
    bottom_right = (top_left[0] + havuzdakibalik_w, top_left[1] + havuzdakibalik_h)

    cv.rectangle(cember_img, top_left, bottom_right,
                    color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)

    cv.imshow('Result', cember_img)
    cv.waitKey()

else:
    print('havuzdakibalik not found.')