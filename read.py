import cv2 as cv

## Reading the image and displaying:
# img = cv.imread('Photos/cat.jpg')
# cv.imshow('Cat', img)
# cv.waitKey(0)

## Dealing with large images(large images go off screen):
# img = cv.imread('Photos/cat_large.jpg')
# cv.imshow('Cat', img)
# cv.waitKey(0)

## Reaing the videos and playing:
capture = cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Videos', frame)
    if cv.waitKey(20) and 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
