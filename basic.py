import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img = cv.imread('photos/222.jpg')
rescale = rescaleFrame(img)

# Converting into grayscale

# gray = cv.cvtColor(rescale, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# Blurring an image
# blur = cv.GaussianBlur(rescale, (77, 77), cv.BORDER_DEFAULT)


# Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

# Dilating the image

dilated = cv.dilate(canny, (3, 3), iterations=1)
cv.imshow('dilated', dilated)

# Eroding(dilated to cascasde)

eroded = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow('eroded', eroded)

# Resize(interarea when high to low,inter linear,cubic when low to high )

resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)

# cropping

cropped = img[50:200, 200:400]

cv.waitKey(0)
