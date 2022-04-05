import cv2 as cv
import numpy as np

# img = cv.imread('photos/1.jpg')
# cv.imshow('img', img)
# cv.waitKey(0)

# ******Creating a blank image*******

blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('blank', blank)

# Painting the image with a colour
# blank[:] = (0, 255, 0)  # (we can alson pass a range)
# cv.imshow('Green', blank)


# Painting a rectangle

# cv.rectangle(blank, (0, 0), (250, 250), color=(0, 255, 0), thickness=2)

# cv.imshow('Rectangle', blank)
# cv.waitKey(0)

# Filling with a colour(thickness=-1)
# cv.rectangle(blank, (0, 0), (250, 250), color=(0, 255, 0), thickness=cv.FILLED)

# cv.imshow('Rectangle', blank)
# cv.waitKey(0)

# Circle

# cv.circle(blank, (blank.shape[1]//2,
#           blank.shape[0]//2), 100, (0, 0, 255), thickness=3)

# cv.imshow('Circle', blank)
# cv.waitKey(0)

# Line

# cv.line(blank, (0, 0), (250, 250), color=(0, 255, 0), thickness=1)
# cv.imshow('line', blank)
# cv.waitKey(0)

# Text on image

cv.putText(blank, 'hello world', (225, 225),
           cv.FONT_HERSHEY_TRIPLEX, 1.0, color=(0, 255, 0))

cv.imshow('text', blank)

cv.waitKey(0)
