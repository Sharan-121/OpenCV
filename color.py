import cv2 as cv
import numpy as np

img = cv.imread('photos/2.jpg')
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
# cv.imshow('img', resized)

# grayscale

gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# BGR to hsv

hsv = cv.cvtColor(resized, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

# BGR to lab

lab = cv.cvtColor(resized, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

# BGR to RGB

rgb = cv.cvtColor(resized, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

# Inverse is possible (ex: cv.COLOR_GRAY2BGR ETC)

cv.waitKey(0)
