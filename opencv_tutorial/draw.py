import cv2 as cv
import numpy as np

blank = np.zeros((500,500), dtype=''

img = cv.imread('photos/cat.jpg')
cv.imshow('Cat', img)

cv.waitKey(0)