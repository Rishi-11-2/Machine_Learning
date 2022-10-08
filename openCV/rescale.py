import cv2
from matplotlib.pyplot import sca


def rescaleFrame(frame, scale=0.75):
    # images,Videos and Live Videos
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)


img = cv2.imread('Photos/ab.png')
resized_img = rescaleFrame(img)
cv2.imshow('Cat', img)
cv2.imshow('CAt1', resized_img)
cv2.waitKey(0)


def changeRes(width, height):
    # Live Video
    cap.set(3, width)
    cap.set(4, height)
    cap.set(10, 100)


cap = cv2.VideoCapture(0)
changeRes(40, 10)
while True:
    isTrue, frame = cap.read()
    frame_resize = rescaleFrame(frame, 2)

    #cv2.imshow('Video', frame)
    cv2.imshow('Video', frame_resize)
    if (cv2.waitKey(20) & 0xFF == ord('q')):
        break
cap.release()
cv2.destroyAllWindows()
