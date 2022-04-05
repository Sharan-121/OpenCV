import cv2 as cv
import numpy as np

img = cv.imread('photos/2.jpg')
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow('img', resized)


blank = np.zeros(resized.shape[:2], dtype="uint8")

b, g, r = cv.split(resized)
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

merge = cv.merge([r, b, g])

cv.imshow('merge', merge)
# cv.imshow('green', green)
# cv.imshow('red', red)


cv.waitKey(0)
