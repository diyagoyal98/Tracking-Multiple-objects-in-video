import cv2 as cv

img=cv.imread('images/cat.jpg')

cv.imshow('Cat',img)

cv.waitKey(0)