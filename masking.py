import cv2 as cv
import numpy as np

img = cv.imread("photos/cat.jpg")
cv.imshow('img', img)

blank = np.zeros(img.shape[:2], dtype="uint8")

mask = cv.circle(
    blank, (img.shape[1]//2, img.shape[0]//2), radius=100, color=255, thickness=-1)

masked = cv.bitwise_and(img, img, mask=mask)

cv.imshow('mask', mask)
cv.imshow('masked', masked)
cv.waitKey(0)
