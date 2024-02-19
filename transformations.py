import cv2 as cv
import numpy as np

img = cv.imread("Photos/park.jpg")
cv.imshow("BGRCat", img)

## Translation - shifting image along the x or y axis
# def translate(img, x, y):
#     transMat = np.float32([[1, 0, x], [0, 1, y]])
#     dimensions = (img.shape[1], img.shape[0])
#     return cv.warpAffine(img, transMat, dimensions)
    
# translated = translate(img, 100, 100)
# cv.imshow("Tranlated", translated)


## Rotation 
# def rotate(img, angle, rotPoint=None):
#     (height, width) = img.shape[:2]
    
#     if rotPoint is None:
#         rotPoint = (width//2, height//2)
        
#     rotMat = cv.getRotationMatrix2D(rotPoint, angle, scale=1.0)
#     dimensions = (width, height)
    
#     return cv.warpAffine(img, rotMat, dimensions)

# rotated = rotate(img, -370)
# cv.imshow("Rotated", rotated)


## Resizing
# resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC) #for enlarging we can use INTER_CUBIC, INTER_LINEAR or for shirnking INTER_AREA
# cv.imshow("Resized", resized)


## Flipping
# flipped = cv.flip(img, -1) # 0 tells image flipping vertically, 1 horizontally and -1 both
# cv.imshow('Flipped', flipped)


## Cropping
cropped = img[200:400, 500:600]
cv.imshow("Cropped", cropped)

cv.waitKey(0)