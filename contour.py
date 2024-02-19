import cv2 as cv
import numpy as np

img = cv.imread("Photos/cats.jpg")
cv.imshow("Cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

canny = cv.Canny(img, 125, 175)
cv.imshow("CannyEdges", canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(len(contours)) #since contours is a list we can print its length

#if you get more contours blur the image before finding canny image and then find cannu and find contour

#Theres another way of finding contours by using thresh
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Thresh", thresh) 

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(len(contours))

#We can visualize the contours found by drawing over the image
blank = np.zeros(img.shape, dtype= 'uint8')
cv.imshow("Blank", blank)

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow("Contours Drawn", blank)

cv.waitKey(0)