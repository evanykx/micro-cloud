import numpy as np
import cv2 as cv

faceCascade = cv.CascadeClassifier("./xml/haarcascade_frontalface_default.xml")

cap = cv.VideoCapture(0)
flag = True

while flag:
    flag, img = cap.read()

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(40, 40)
    )

    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2)

    cv.show("Who", img)

    k = cv.waitKey(1)
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()
