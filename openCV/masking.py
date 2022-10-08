from turtle import shape
import cv2 as cv
import numpy as np

img = cv.imread('Photos/ab.png')
cv.imshow('A', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('B', blank)

mask = cv.circle(
    blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('MASK', mask)
mask1 = cv.rectangle(
    blank.copy(), (30, 30), (370, 370), 255, -1)
cv.imshow('MASK1', mask1)

masked = cv.bitwise_and(mask, mask1)
cv.imshow('M1', masked)
masked2 = cv.bitwise_and(img, img, mask=masked)
cv.imshow('Masked Image', masked2)
cv.waitKey(0)
