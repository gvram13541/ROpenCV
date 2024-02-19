import os
import cv2 as cv
import numpy as np

DIR = r'C:/Users/91934/OneDrive/Desktop/OpenCV/Faces/train'

haar_cascade = cv.CascadeClassifier("haar_face.xml")

people = []
for i in os.listdir(DIR):
    people.append(i)
    
print(people)

features = []
labels = []
def create_train():
    # we will enter into every directory of train directory which has different angle of same persons image for creating the dataset
    for person in people: 
        path = os.path.join(DIR, person)
        label = people.index(person)
        
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            
            rect_faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            
            for (x, y, w, h) in rect_faces:
                faces_roi = gray[y:y+h, x:x+w] #we ignore other than face part in image
                features.append(faces_roi)
                labels.append(label)

create_train()

# print(f"Length of features = {len(features)}") # checking whether dataset is created or not
# print(f"Length of labels = {len(labels)}")

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# train the face_recognizer on created dataset
face_recognizer.train(np.array(features, dtype='object'), np.array(labels))

face_recognizer.save('face_trained_model.yml')
np.save('Features.npy', np.array(features, dtype='object'))
np.save('Labels.npy', np.array(labels))