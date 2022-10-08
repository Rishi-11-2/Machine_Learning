import cv2 as cv
from cv2 import threshold

img = cv.imread('Photos/ab.png')
cv.imshow("I", img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
# Simple Thresholding

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('T', thresh)
threshold, thresh_INV = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('T1', thresh_INV)


# Adaptive Thresholfing

adaptive_thresh = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 10)
cv.imshow('Ada', adaptive_thresh)
cv.waitKey(0)
