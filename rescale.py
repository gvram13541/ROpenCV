# ## Rescaling and resing the image:
# import cv2 as cv

# img = cv.imread('Photos/cat_large.jpg')
# cv.imshow('Cat', img) # before resizing the image

# def rescaleFrame(frame, scale = 0.75):
#     width = int(frame.shape[1]*scale)
#     height = int(frame.shape[0]*scale)
#     dimensions = (width, height)
#     return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)


# resized_image = rescaleFrame(img, scale = 0.2)
# cv.imshow('Resized_img', resized_image) # after resizing the image

# cv.waitKey(0)


# ## Rescaling and resing the image:
# import cv2 as cv

# capture = cv.VideoCapture('Videos/kitten.mp4')

# def rescaleFrame(frame, scale = 0.75):
#     width = int(frame.shape[1]*scale)
#     height = int(frame.shape[0]*scale)
#     dimensions = (width, height)
#     return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Actual', frame)
#     cv.imshow('Resized', rescaleFrame(frame, scale = 0.5))
#     if cv.waitKey(20) and 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()


## Rescaling the LiveVideo:
## The above rescaling function created works for images, videos and live videos
## There is another method for rescaling live video

import cv2 as cv

def liveRescale(capture, width, height):
    capture.set(3, width)
    capture.set(4, height)
    
capture = cv.VideoCapture(0)  # 0 for webcam, or 'filename.mp4'
liveRescale(capture, 640, 480)

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    
    if cv.waitKey(0) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()