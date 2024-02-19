import cv2 as cv

img = cv.imread("Photos/park.jpg")
cv.imshow("BGRCat", img) # this is bgr image

## Converting to grascale image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("GrayCat", gray) #this is gray scale image

## Bluring the image
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT) # to increase the blur increase the tuple(kernal size)
cv.imshow("Blur", blur)

## Edge cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny", canny)

## Dilating the image
dilated = cv.dilate(canny, (3, 3), iterations = 1)
cv.imshow("Dilated", dilated)

## Eroding
eroded = cv.erode(dilated, (3, 3), iterations = 1)
cv.imshow("Eroded", eroded)

## Resize the image
resize = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA) # to enlarge we can change interpolation parameter
cv.imshow("Resized", resize)

## Crop the image
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)