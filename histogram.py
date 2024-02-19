### HISTOGRAMS COMPUTATION

# allows us to visualize the ditribution of pixel intensities in an image
# 

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def plot_hist(name, image, color = None):
    plt.title(f"{name} Histogram")
    plt.xlabel("Bins")
    plt.ylabel("no of pixels")
    plt.plot(image, color)
    plt.xlim([0, 256])

img = cv.imread("Photos/cats.jpg")
cv.imshow("Cats", img)

blank = np.zeros(img.shape[:2], dtype='uint8')

## Gray scale histogram
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])
# plot_hist(gray_hist)


## histogram for particular portion of image
# circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
# masked_img = cv.bitwise_and(gray, gray, mask = circle)
# cv.imshow("Maksed image",masked_img)

# gray_hist = cv.calcHist([gray], [0], masked_img, [256], [0, 256])
# plot_hist(gray_hist)

## histogram for color image
plt.figure()

circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
masked_img = cv.bitwise_and(gray, gray, mask = circle)
cv.imshow("Maksed image",masked_img)

colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], masked_img, [256], [0, 256])
    plot_hist("Colored", hist, color = col)

plt.show()

cv.waitKey(0)