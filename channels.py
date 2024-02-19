import cv2 as cv
import numpy as np

img = cv.imread("Photos/park.jpg")
cv.imshow("park", img)

## Splitting color channels of BGR-image
b, g, r = cv.split(img)
# cv.imshow('Blue', b)
# cv.imshow("Green", g)
# cv.imshow("Red", r)
# print(f'BGR: {img.shape}, Blue: {b.shape}, Green: {g.shape}, Red: {r.shape}')


## Merging the channels of image
# merged = cv.merge([g, g, g])
# cv.imshow("Merged", merged)

# if we observe we are getting grayscale image of individual channesl to get actual blue, green and red color images insted of gray scale, we can do:
blank = np.zeros(img.shape[:2], dtype='uint8')
# cv.imshow("Blank", blank)
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])
# cv.imshow("Blue", blue)
# cv.imshow("Green", green)
# cv.imshow("Red", red)

cv.waitKey(0)