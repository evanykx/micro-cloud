import numpy as np
import cv2 as cv

faceCascade = cv.CascadeClassifier("./xml/haarcascade_frontalface_default.xml")

eyeCascade = cv.CascadeClassifier("./xml/haarcascade_eye.xml")

img = cv.imread("./resources/emma.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

eyes = eyeCascade.detectMultiScale(
    gray,
    1.3,
    2
)

for (x, y, w, h) in eyes:
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv.imshow("Emma", img)
cv.waitKey(0)
cv.destroyAllWindows()    

