import cv2 as cv


def rescaleFrame(frame ,scale=0.20):
    width=int(frame.shape[1]+scale) #frame.shape[1] is the width of the image
    height=int(frame.shape[0]+scale) #frame.shape[0] is the height of the image
    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

img=cv.imread('images/cat.jpg')
cv.imshow('Cat',img)

img_resized=rescaleFrame(img)
cv.imshow('Cat resized ',img_resized)


cv.waitKey(0)