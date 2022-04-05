import cv2 as cv


# Function for rescaling frames and images
# This method is suitable for images,videos,live videos
def rescaleFrame(frame, scale=0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Function for resclaing live videos in particular


def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)


# Reading Video frame by frame
capture = cv.VideoCapture('videos/video.mp4')

while True:
    isTrue, frame = capture.read()
    resize = rescaleFrame(frame)
    cv.imshow('scaled', resize)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
