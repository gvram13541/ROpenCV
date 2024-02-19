### Thresholding

# thresholding is binarising the image
# we will chose a threshlod ans set evey pixle before that threshold to 0 else 255
# 0 - black and 255 - white


import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("Photos/cats.jpg")
cv.imshow("Cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

## Simple thresholding
threshold_value = 1
threshold, thresh = cv.threshold(gray, threshold_value, 255, cv.THRESH_BINARY)
cv.imshow("Thresholded image", thresh)

threshold, thresh_inv = cv.threshold(gray, threshold_value, 255, cv.THRESH_BINARY_INV)
cv.imshow("Inverse Thresholded image", thresh_inv)


## Adaptive thresholding
# computes threshold value automaticaally based on mean and uses it
adaptive_threshold = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("Adaptive threshold image", adaptive_threshold)

adaptive_threshold_inv = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow("Inverse Adaptive threshold image", adaptive_threshold_inv)




cv.waitKey(0)