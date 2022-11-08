import cv2 as cv

# /Users/aparnarenjithpillai/Desktop/Computer_Science/Capstone/Plumbing-Project/photos/polka-dot-black-vector-6757353.jpg

path = "photos/dots.jpg"

#make the image grayscale
gray = cv.imread(path, 0)

#threshold
th, threshold = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)

#find countours --> mainly connects the black dots of the image 
cnts = cv.findContours(threshold, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) [-2]

#filter by area --> when it gets a black dot it will calculate the area and if it satifies
# the condition of minimum area to be count as a dot, then it will push the value of its area to the list xcnts
s1 = 1
s2 = 2
xcnts = []
for cnt in cnts:
    if s1 < cv.contourArea(cnt) <s2:
        xcnts.append(cnt)

print ("\nDots number: {}".format(len(xcnts)))
