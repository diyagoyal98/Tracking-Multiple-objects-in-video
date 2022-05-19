import this
import cv2 as cv
from cv2 import rectangle
from cv2 import FILLED
import numpy as np


blank=np.zeros((500,500,3),dtype='uint8') #(height,width,colur channel number)
cv.imshow("Blank",blank)

#1->paint the image by certain colour
blank[:]=0,255,0        #[:] -> means referring to all the pixel (0,255,0 -> shows green colour )
cv.imshow('Green',blank)

#2-> We can also change a certain portion of the image by giving the range of pixels
blank[200:300,300:400]=0,0,255   #blank[200:300,300:400] -> defines the range (0,0,255)->shows red colour
cv.imshow('New blank',blank) 

#3-> Now we will a rectangle
cv.rectangle(blank,(0,0),(250,250),(0,0,255),thickness=2) # parameters-> image,starting address(pixel) , ending address(pixel),thickness of the rectangle border lines
cv.imshow("Rectangle ",blank)

#4-> we can also fill the colour inside the rectangle 
cv.rectangle(blank,(0,0),(250,250),(0,0,255),thickness=cv.FILLED) #instead of cv.FILED we can also use -1 it will also give the same result
cv.imshow("Colour filled rectangle",blank)

#5->instead of giving(250,250) we can also use as shown below
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,0,255),thickness=-1) # It has dimension half of the real(given) image
cv.imshow("New filled rectangle",blank)

#6->circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=3) #Arguments -> image , centre , radius , ythickness of circle boundary
cv.imshow("Circle",blank)

#7->We can also fill the colour inside the circle as we have done in the rectangle by  giving thickness=-1

#8->Line
cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=3) #Arguments ->image,two pints(starting and ending point , colour,thickness)
cv.imshow("Line",blank)

#9->How to write text on the image
cv.putText(blank,'Hello Diya',(255,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,0,255),thickness=2) #Arguments-> image,Text whatever you want to write on the image , starting point(pixels),font type,scale,thickness
cv.imshow('Text',blank)




cv.waitKey(0)