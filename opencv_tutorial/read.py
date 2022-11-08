import cv2 as cv

#playing around with images 

img = cv.imread('photos/cat.jpg')

cv.imshow('Cat', img)
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
   
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

cv.waitKey(0)