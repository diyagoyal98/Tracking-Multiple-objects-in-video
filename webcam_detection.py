import cv2
import cv2
import numpy as np
from object_detection import ObjectDetection

COLORS = [(0, 255, 0), (0, 0, 255), (255, 0, 0),(255, 255, 0), (255, 0, 255), (0, 255, 255)]


ob=ObjectDetection()

cap = cv2.VideoCapture(0) #For webcam 

class_names=[]
with open("dnn_model/coco.txt","r")as f:
    class_names=[cnames.strip() for cnames in f.readlines()]
print(class_names)   



while True:
    ret,frame=cap.read()
    if not ret:
        break

    (classes,scores,boxes)=ob.detect(frame)
    for (class_id,score,box) in zip(classes,scores,boxes):
        color = COLORS[int(class_id) % len(COLORS)]
        label = "%s" % (class_names[class_id])
        cv2.rectangle(frame,box,color,1)
        cv2.putText(frame,label,(box[0],box[1]-10),cv2.FONT_HERSHEY_COMPLEX,0.5,color,2)




    cv2.imshow("Frame",frame)
    key=cv2.waitKey(1)  # this will wait only for 1 milli second between two frames
    if key==27:      # 27 key is equal to escape key in the keyboard (if we press escape then we will exist from the window)
        break

cap.release()
cv2.destroyAllWindows()    
