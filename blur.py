import cv2 as cv
import numpy as np

img = cv.imread('photos/2.jpg')
resized = cv.resize(img, (500, 500))

# Smoothing when image has lot of noice
# Averaging
avg = cv.blur(resized, (3, 3))
cv.imshow('avg', avg)

# Gaussian Blur
gb = cv.GaussianBlur(resized, (3, 3), sigmaX=0)
cv.imshow('gb', gb)

# Median Blur

med = cv.medianBlur(resized, 3)
cv.imshow('med', med)

# Bilateral Blur

bil = cv.bilateralFilter(resized, d=100, sigmaColor=35, sigmaSpace=25)

cv.imshow('bil', bil)
cv.waitKey(0)
