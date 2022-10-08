import cv2 as cv

img = cv.imread('../Photos/ab.png')
cv.imshow('A', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier('haar_cascade.xml')


faces_rect = haar_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=10)

print(len(faces_rect))


for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 234), thickness=2)

cv.imshow('Detected Face', img)
cv.waitKey(0)
