import cv2 as cv


def rescaleFrame(frame ,scale=0.75):
    width=int(frame.shape[1]+scale) #frame.shape[1] is the width of the image
    height=int(frame.shape[0]+scale) #frame.shape[0] is the height of the image
    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


#reading video

capture=cv.VideoCapture('video/dog.mp4')

while True:
    isTrue,frame=capture.read()

    frame_resized=rescaleFrame(frame,scale=0.2)


    cv.imshow('Video',frame)

    cv.imshow('Video resized',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()    