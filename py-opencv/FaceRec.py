import numpy as np
import cv2 as cv

faceCascade = cv.CascadeClassifier("./xml/haarcascade_frontalface_default.xml")

img = cv.imread("./resources/emma.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.2,
    minNeighbors=5,
    minSize=(100, 100)
)

for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv.imshow("Emma", img)
cv.waitKey(0)
cv.destroyAllWindows()     

