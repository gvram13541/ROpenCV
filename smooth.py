### SMOOTHING AND BLURING
# We smooth the image to reduce noise in the image
# bluring means we reduce the intesity of centre of window we chose
# the size of the window is called kernal size

import cv2 as cv

img = cv.imread("Photos/park.jpg")
cv.imshow("park", img)

## averaging
average = cv.blur(img, (7, 7)) #high the kernal size high the blur
cv.imshow("Average", average) 

## gausian blur
gauss = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow("Gauss", gauss) #though the sizes are similar for both methods gaussin blur is more effective since we assign weights to pixels

## median blur
median = cv.medianBlur(img, 7)
cv.imshow("Meadin", median)

## bilateral bluring
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("Bilateral", bilateral)

cv.waitKey(0)