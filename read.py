import cv2 as cv

# Reading Images

img = cv.imread('photos/1.jpg')
cv.imshow('Wallpaper', img)

# Capturing videos

capture = cv.VideoCapture('videos/video.mp4')

while True:
    isTrue, frame = capture.read()

    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
