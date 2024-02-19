#how to switch between colorspaces in opencv
#color spaces - space of colors - system of representing an array of pixel colors
#eg: rgb, grayscale, etc.

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Photos/park.jpg")
cv.imshow("Boston", img)

# opencv's default  way of reading images is BGR

# bgr -> grayscale
# gray scale images generally show the pixel intensities at particular locations of your image
# gray = cv.imread(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

# # bgr -> hsv(hue saturation value)
# # hsv is kind of based on how humans think and condeive of color
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow("HSV", hsv)

# # bgr -> l*a*b
# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow("LAB", lab)

# and outside opencv we view images in rgb format inverse of bgr
plt.imshow(img) #here we are taking bgr image and displying is as rgb so we see inversion of colors when we diplay it.
plt.show()

# bgr -> rgb
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)
plt.imshow(rgb)
plt.show()


# we can convert hsv -> bgr, grayscale -> bgr, etc., but cannot directly convert hsv -> grasclae and vis a vis.
