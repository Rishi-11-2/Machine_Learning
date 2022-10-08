import cv2 as cv
from cv2 import resize
img = cv.imread('Photos/ab.png')
cv.imshow('Cat', img)

# Converting To GrayScale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)


# Blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)


# Edge Cascade

canny = cv.Canny(blur, 125, 175)
cv.imshow('Edge', canny)


# Dilating the Image

dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow('dilated', dilated)

# Eroded
eroded = cv.erode(dilated, (3, 3), iterations=3)
cv.imshow('eroded', eroded)

# Resize
resize = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resize', resize)


# Cropping
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)
cv.waitKey(0)
