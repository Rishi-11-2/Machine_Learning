import cv2 as cv

img = cv.imread('Photos/ab.png')
cv.imshow('A', img)


# Averaging
average = cv.blur(img, (3, 3))
cv.imshow('AVerage Blur', average)


# Gaussian Blur
gauusain = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow('Gaussian', gauusain)


# Median Blurring

median = cv.medianBlur(img, 3)
cv.imshow('Median', median)


# Bilater Blurring

bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral', bilateral)
cv.waitKey(0)
