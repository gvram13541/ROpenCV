import cv2 as cv

# a persons face
# img = cv.imread("Photos/lady.jpg")
img = cv.imread("Photos/group 1.jpg")
# cv.imshow("Lady", img)

# we don't need a color image to detect the face(0 or 1)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray", gray)

haar_cascade = cv.CascadeClassifier("haar_face.xml")

fases_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1) # adjust the minNeighbours to as min as possible if there were more faces in the image 
print(f"No of faces found: {len(fases_rect)}")

for (x,y,w,h) in fases_rect:
    cv.rectangle(img, (x, y), (x+w, y+w), (0, 255, 0), thickness=2)
    
cv.imshow('detected faces', img)

cv.waitKey(0)