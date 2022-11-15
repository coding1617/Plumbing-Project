import numpy as np
import argparse
import cv2

# construct parse, parse arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to image")
args = vars(ap.parse_args())

image = cv2.imread('photos/coral.png')
resized = cv2.resize(image, (700,500), interpolation=cv2.INTER_CUBIC)

boundaries = [
	([90, 140, 35], [233, 254, 255])
]

for (lower, upper) in boundaries:
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")

    mask = cv2.inRange(resized, lower, upper)
    output = cv2.bitwise_and(resized, resized, mask = mask)

    cv2.imshow("images", np.hstack([resized, output]))
    cv2.waitKey(0)