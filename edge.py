### Edge detection

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("Photos/cats.jpg")
cv.imshow("Cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)


## laplacian method
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian", lap)

## sobel
soblex = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobley = cv.Sobel(gray, cv.CV_64F, 0, 1)
combine_sobel = cv.bitwiase_or(soblex, sobley)
cv.imshow("Sobel x", soblex)
cv.imshow('Sobel y', sobley)
cv.imshow("Combine Sobel", combine_sobel)


## canny
canny = cv.Canny(gray, 150, 175)
cv.imshow("CannyEdges", canny)

cv.waitKey(0)