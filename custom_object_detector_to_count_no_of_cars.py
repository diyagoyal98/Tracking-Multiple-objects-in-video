import cv2
import numpy as np
import math
from object_detection import ObjectDetection


od=ObjectDetection() #Making object 


cap=cv2.VideoCapture("los_angeles.mp4")  #This is to read the video file

count=0    #This is for counting the number of cars 
centre_points_prev=[]
tracking_objects={}
trak_id=0

while True:
    ret,frame=cap.read()  # reading one frame from the video
    count+=1
    if not ret:  #This means if their are no more frames to read then we will exit 
        break

    centre_points_curr=[] #This will store the center points of the current frame 


    #Now we will detect objects from frame
    (class_ids,score,boxes)=od.detect(frame)
    for box in boxes:
        #print(box) This will print x-y co-ordinate height-width 
        (x,y,w,h)=box
        cx=int((x+x+w)/2)
        cy=int((y+y+h)/2)
        centre_points_curr.append((cx,cy))

        print("Frame number  ",count,"  ",x,y,w,h) #Try to print the frame number and co-ordinates 

        #cv2.circle(frame,(cx,cy),5,(0,0,255),-1)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)  #With the help of this we are able to make boundary boxes around the objects
        
    #for pt in centre_points_curr:
        #cv2.circle(frame,pt,5,(0,0,255),-1)

    if count<=2:
        for pt1 in centre_points_curr:
            for pt2 in centre_points_prev:
                distance=math.hypot(pt2[0]-pt1[0],pt2[1]-pt1[1])
            
                if distance<20:       #if condition is true it means it is the same object 
                    tracking_objects[trak_id]=pt1
                    trak_id+=1
    else:
        tracking_object_copy=tracking_objects.copy()
        centre_points_curr_copy=centre_points_curr.copy()

        for object_id,pt2 in tracking_object_copy.items():
            object_exists=False
            for pt1 in centre_points_curr_copy:
                distance=math.hypot(pt2[0]-pt1[0],pt2[1]-pt1[1])
                if distance<20:              #Checking the distance and updating the ids
                    tracking_objects[object_id]=pt1
                    object_exists=True
                    if pt1 in centre_points_curr:
                        centre_points_curr.remove(pt1)
                    continue
            if not object_exists:
                tracking_objects.pop(object_id)    

        for pt in centre_points_curr:
        
            tracking_objects[trak_id]=pt
            trak_id+=1



    for object_id,pt in tracking_objects.items(): 
        cv2.circle(frame,pt,5,(0,0,255),-1) #This is to put a small filled red circle at the centre
        cv2.putText(frame, str(object_id), (pt[0], pt[1] - 7), 0, 1, (0, 0, 255), 2) #This is to display id number at the of the car



    '''print("Tracking objects")
    print(tracking_objects)                        

    print("Current frame ")
    print(centre_points_curr)

    print("Previous fraame")
    print(centre_points_prev) 
   
    This part is just to get an idea about the co-ordinates  
    '''

    cv2.imshow("Frame",frame) #Showing the frame one by one


    #We will store the centre points of the current frame so that we can use these for comparision
    centre_points_prev=centre_points_curr.copy() 

    key=cv2.waitKey(1)  # this will wait only for 1 milli second between two frames
    if key==27:      # 27 key is equal to escape key in the keyboard (if we press escape then we will exist from the window)
        break

cap.release()
cv2.destroyAllWindows()    


