## DRAWING SHAPES AND WRITING TEXT ON IMAGES

import cv2 as cv
import numpy as np

#black image
blank = np.zeros((500, 500, 3), dtype = 'uint8')
cv.imshow('Blank', blank)

#colored image
color = np.zeros((500, 500, 3), dtype = 'uint8')
color[:] = 0, 0, 255  #Change here for different color
# cv.imshow('Green', color)

#coloring certain portion of image
color_portion = np.zeros((500, 500, 3), dtype = 'uint8')
color_portion[100:300, 200:400] = 0, 0, 255  #Change here for different color
cv.imshow('Green', color_portion)

#drawing a rectangle
cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness = -1) #to fill the shape drawn give thickness = -1 or  cv.FILLED
cv.imshow("Rectangle", blank)

#drawing a circle
cv.circle(blank, (250, 250), 50, (0, 0, 255), thickness = 3)
cv.imshow("Circle", blank)

#drawing a line
cv.line(blank, (0, 0), (250, 250), (255, 255, 255), thickness = 3)
cv.imshow("Circle", blank)

#writing the text
cv.putText(blank, "Gunavardhan Reddy", (255, 255), cv.FONT_HERSHEY_COMPLEX, 1.0, (255, 255, 255), 3)
cv.imshow("Guna", blank)

cv.waitKey(10000) #The image will appear for 5sec and then automatically diasspears