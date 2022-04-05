import cv2 as cv
import numpy as np

img = cv.imread('photos/1.jpg')
cv.imshow('img', img)

# Translation(shifting the image)


def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


# -x implies left
# x implies right
# y implies down
# -y implies up
trans = translate(img, 100, -200)
cv.imshow('translated', trans)


# Rotation
def rotate(img, angle, rotpoint=None):
    height, width = img.shape[:2]

    if rotpoint is None:
        rotpoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotpoint, angle, scale=1.0)

    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)


rot = rotate(img, 90)
cv.imshow('rot', rot)

#Flipping(0-vertically,1-hor,-1-both )

flip = cv.flip(img, -1)
cv.imshow('flip', flip)

cv.waitKey(0)
