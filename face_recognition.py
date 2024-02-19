import cv2 as cv
import numpy as np

haar_cacade = cv.CascadeClassifier('haar_face.xml')

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained_model.yml')

img = cv.imread("Faces/val/elton_john/1.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Person", gray)


# detect the face in the image
faces_rect = haar_cacade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

for (x, y, w, h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]
    
    label, confidence = face_recognizer.predict(faces_roi)
    
    print(f"Person with Name = {people[label]}  detected with a confidence of {confidence}")
    cv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness = 2)

cv.imshow("Detected_face", img)

cv.waitKey(0)