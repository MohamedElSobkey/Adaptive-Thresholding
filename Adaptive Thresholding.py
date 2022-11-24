import cv2 as cv 
import numpy as np 

img = cv.imread('sudoku.png', 0)

_,Th1 = cv.threshold(img, 55, 255, cv.THRESH_BINARY)
Th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 111, 2)
Th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 111, 2)



cv.imshow('Image', img)
cv.imshow('Th1', Th1)
cv.imshow('Th2', Th2)
cv.imshow('Th3', Th3)




cv.waitKey(0)
cv.destroyAllWindows()
