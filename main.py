# для работы скачай прогу на пк
# https://iriun.com/
#
#
#

import cv2

image = cv2.VideoCapture(1)

while True:
    rez, img = image.read()
    cv2.imshow('Camera', img)

    k = cv2.waitKey(60) & 0xFF
    if k == 27:  # if cv2.waitKey(60) & OxFF == ord('q')
        break

cv2.destroyAllWindows()
cv2.waitKey(0)
cv2.destroyAllWindows()
