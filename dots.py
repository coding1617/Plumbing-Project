import cv2 as cv
import numpy as np


# Load image, grayscale, Otsu's threshold
image = cv.imread('photos/unnamed.png')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]

# Filter out large non-connecting objects
cnts = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    area = cv.contourArea(c)
    if area < 500:
        cv.drawContours(thresh,[c],0,0,-1)

# Morph open using elliptical shaped kernel
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3,3))
opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=3)

# Find circles 
cnts = cv.findContours(opening, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    area = cv.contourArea(c)
    if area > 10 and area < 10:
        ((x, y), r) = cv.minEnclosingCircle(c)
        cv.circle(image, (int(x), int(y)), int(r), (36, 255, 12), 2)

print ("\nDots number: {}".format(len(cnts)))
cv.imshow('thresh', thresh)
cv.imshow('opening', opening)
cv.imshow('image', image)
cv.waitKey()