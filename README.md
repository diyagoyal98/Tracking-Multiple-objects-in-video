
# Tracking multiple objects in video

With the help of this project we will detect multiple objects at the same time in the video or through webcam.




## Requirements for the project
1) Latest version of python

2) OpenCV

3) Yolov4

    i)   Yolov4.cfg 

    ii)  Yolov4.weights

    iii) coco.txt
        
4) Code Editor (Vscode or whatever you like )




## Different files present in the repository

1) Object_detection file :- This contains the code that is necessary to run the yolo.
And we will import this file in our another files so that we don't have to write the whole code again.

2) Tracking_all file :- This file is able to produce a boundary upon all the detected objects and it will also label them according o their class(object) name.
Yolo can detect upto 80 classes and the names of that classes is given in the coco.txt file.

3) Webcam_detection file :- This file is able to open the camera and take that as a input perform object detection on that.

4) Custom_object_detector_that_counts_no_of_Cars :- This file contains the code which is able to count the number of cars in a video.


## Screen shots of the different videos and the webcam


<img src="https://user-images.githubusercontent.com/87846440/179008966-15b44045-ce1a-4f45-991f-eb6d1f7aa035.png" width="800" height="400">

<img src="https://user-images.githubusercontent.com/87846440/179009280-3caaf805-f78a-4600-9289-0a2351a0b4d6.png" width="800" height="400">

<img src="https://user-images.githubusercontent.com/87846440/179009344-13141d74-a4c1-4f2f-a7ec-9ea73d10edf6.png" width="800" height="400">

<img src="https://user-images.githubusercontent.com/87846440/179009425-321dae50-3bc7-4fb3-93bc-6bcb44ffe0a9.png" width="800" height="400">

<img src="https://user-images.githubusercontent.com/87846440/179009548-78e2a668-9903-42d1-af12-6e466943575d.png" width="800" height="400">

<img src="https://user-images.githubusercontent.com/87846440/179009674-54d68d70-4537-4232-87cf-c4750275df08.png" width="800" height="400">



