import cv2 as cv
import numpy as np


#reading videos 
'''capture=cv.VideoCapture("vedio/dog.mp4")
while True:
    isTrue,frame=capture.read()

    if not isTrue:
        break  

    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release() '''

'''capture=cv.VideoCapture("vedio/dog.mp4")
while True:
    isTrue,frame=capture.read()
    cv.imshow('Videooo',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()    '''

#resizing images and video


'''def rescaleFrame(frame,scale):
    height=int(frame.shape[0]*scale)
    width=int(frame,shape[1]*scale)


    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def changeRes(width,height):
        #live video
    capture.set(3,width)
    capture.set(3,height)

capture=cv.VideoCapture("vedio/dog.mp4")
while True:
    isTrue,frame=capture.read()

    if not isTrue:
        break  
    frame_resized=rescaleFrame(frame,scale=.5) 

    cv.imshow('Video',frame)
    cv.imshow("Video Resized ",frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()'''