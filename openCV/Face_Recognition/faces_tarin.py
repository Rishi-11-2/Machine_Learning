from cProfile import label
import os
from pyexpat import features
import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier('haar_cascade.xml')


p = []
DIR = r'/home/rishi/Desktop/MachineLearning/openCV/Face_Recognition/Faces/train'
for i in os.listdir(DIR):
    p.append(i)
feautres = []
labels = []

print(p)


def create_train():
    for person in p:
        path = os.path.join(DIR, person)
        label = p.index(person)
        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=5)
            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                feautres.append(faces_roi)
                labels.append(label)


create_train()
print('Training Done ------------')

feautres = np.array(feautres, dtype='object')
labels = np.array(labels)
face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train  the Recognizer on features list and labels list
face_recognizer.train(feautres, labels)
face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)
