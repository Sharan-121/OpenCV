import cv2 as cv
import numpy as np

img = cv.imread('photos/cat.jpg')
cv.imshow('img', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Gray Histogram

gray_hist = cv.calcHist()
cv.waitKey(0)
