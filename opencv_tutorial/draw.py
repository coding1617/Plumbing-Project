#drawing shapes on top of images

import cv2 as cv
import numpy as np

# creating a blank black window:
# blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('Blank', blank)

img = cv.imread('photos/cat.jpg')
cv.imshow('Cat', img)

cv.circle(img, (img.shape[1]//2, img.shape[0]//2), 40, (0,0,0), thickness=-1)
cv.imshow('Circle', img)

cv.waitKey(0)