import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

offset = 20
imgsize = 300


while(True):
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x,y,w,h = hand['bbox']

        imgwhite = np.ones((imgsize , imgsize,3), np.unit8)*255

        imgcrop = img[y - offset:y+h+offset, x-offset:x+w+offset]
        imgwhite[] = imgcrop
        cv2.imshow('Imgcrop', imgcrop)
        cv2.imshow('imgwhite', imgwhite)



    cv2.imshow('Img', img)
    cv2.waitKey(1)
