import cv2 as cv
import numpy as np

img = cv.imread('photos/2.jpg')
# cv.imshow('img', img)

resized = cv.resize(img, (1000, 1000), interpolation=cv.INTER_AREA)

blank = np.zeros(resized.shape, dtype="uint8")
# cv.imshow('blank', blank)

gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)


contours, hierachies = cv.findContours(
    canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('line', blank)


cv.waitKey(0)
