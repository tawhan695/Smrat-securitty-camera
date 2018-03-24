import requests
import cv2
import sys
from Line import senLineNotify
#from camera import VideoCamera
import time
import threading
i =0
cam = cv2.VideoCapture(0)
email_update_interval = 600 # sends an email only once in this time interval
object_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") # an opencv classifier
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
        ret, im =cam.read()
        gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces = object_classifier.detectMultiScale(gray, 1.2,5)
        for(x,y,w,h) in faces:

           cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)        
           Id = "person"      
           cv2.putText(im, str(Id), (x,y-40), font, 2, (255,255,255), 3)
           resized_image = cv2.resize(im, (400, 400))
           print(i)
           if i == 200 :
               time.sleep(5)
               print("save")
               cv2.imwrite("save/User.jpg",resized_image)
               senLineNotify()
           i +=1
           if i==800:
               i=0

        cv2.imshow('im',im) 
        
        if cv2.waitKey(10) & 0xFF == ord('q'):
           break

cam.release()
cv2.destroyAllWindows()
