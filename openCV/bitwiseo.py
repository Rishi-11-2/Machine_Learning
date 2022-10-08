import cv2 as cv
from cv2 import rectangle
from cv2 import circle
import numpy as np
from sklearn.metrics import recall_score

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)
cv.imshow('R', rectangle)
cv.imshow('C', circle)

# bitwise ANd --> Intersecting
bitwiseAnd = cv.bitwise_and(rectangle, circle)
cv.imshow('B', bitwiseAnd)

# bitwise Or --> Intersecting + Non-Intersecting
bitwiseOr = cv.bitwise_or(rectangle, circle)
cv.imshow('C', bitwiseOr)


# bitwise XOR --> Non Intersecting
bitwiseX = cv.bitwise_xor(circle, rectangle)
cv.imshow('D', bitwiseX)

# bitwise Not

bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('E', bitwise_not)
cv.waitKey(0)
