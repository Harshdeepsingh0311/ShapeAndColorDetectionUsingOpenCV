import cv2 as cv
import numpy as np

# blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Blank', blank)

# blank[200:300, 200:300] = 255,0,0
# cv.imshow('Green', blank)

# #Draw rectangle
# cv.rectangle(blank, (0,0), (250,250), (255,0,0), thickness=cv.FILLED)
# cv.imshow('Rectangle', blank)

# img = cv.imread('Photos/cat.jpg')
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray",gray)

img = cv.imread('Photos/park.jpg')
cv.imshow('Normal', img)

blurred = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blurred', blurred)

cv.waitKey(0)