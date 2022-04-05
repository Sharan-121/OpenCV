import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype="uint8")

rect = cv.rectangle(blank.copy(), (30, 30), (370, 370),
                    color=255, thickness=-1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)
cv.imshow('rect', rect)
cv.imshow('cir', circle)

# bitwise and(intersecting region)

bitwise_and = cv.bitwise_and(rect, circle)
cv.imshow('bit_and', bitwise_and)

# bitwise or(int+non-int)

bitwise_or = cv.bitwise_or(rect, circle)
cv.imshow('bit_or', bitwise_or)

# bitwise xor(only non-int)

bitwise_xor = cv.bitwise_xor(rect, circle)
cv.imshow('bit_xor', bitwise_xor)

# bitwise not(not)

bitwise_not = cv.bitwise_not(rect)
cv.imshow('bit_not', bitwise_not)


cv.waitKey(0)
