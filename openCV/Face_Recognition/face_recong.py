from cProfile import label
import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar_cascade.xml')
people = ['Elton John', 'Mindy Kaling',
          'Madonna', 'Ben Afflek', 'Jerry Seinfield']

features = np.load('features.npy')

labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(
    r'Faces/val/elton_john/3.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('a', gray)


# Detect The Face in the Image

faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]

label, confidence = face_recognizer.predict(faces_roi)


print(f'Label ={people[label]} with a confidence of {confidence}')

cv.putText(img, str(people[label]), (20, 20),
           cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow('A', img)

cv.waitKey(0)
