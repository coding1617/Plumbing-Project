import numpy as np
import argparse
import cv2
#import mathplotlib.pyplot as plt
#import imutils

# construct parse, parse arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to image")
args = vars(ap.parse_args())

image = cv2.imread('coralPhotos/coral.png')
resized = cv2.resize(image, (750,550), interpolation=cv2.INTER_CUBIC)

blurred = cv2.GaussianBlur(resized, (11, 11), 0)

eroded = cv2.erode(blurred, (20,20), iterations=1)

boundaries = [
	([100, 130, 35], [246, 254, 255])
]

for (lower, upper) in boundaries:
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")

    mask = cv2.inRange(eroded, lower, upper)
    output = cv2.bitwise_and(eroded, eroded, mask = mask)

#print ("\nTentacles number: {}".format(len(cnts)))

#making everything gray in the display
gray_pic = cv2.cvtColor(eroded, cv2.COLOR_BGR2GRAY)
gray_count = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)

#cv2.imshow("images", np.hstack([gray_pic, gray_count]))

cv2.imshow("images", gray_count)

cv2.waitKey(0)