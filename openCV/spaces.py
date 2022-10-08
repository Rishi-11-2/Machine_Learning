import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('Photos/ab.png')


# BGR to gRAy

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


# BGR TO HSV

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)


# BGR To RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)
# plt.imshow(rgb)
# plt.show()

# Similary for BGR to HSV
cv.waitKey(0)
