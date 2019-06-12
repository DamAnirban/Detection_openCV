import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2
import numpy as np

#Capturing Video through webcam.
device = cv2.VideoCapture(0)

while True:
    ret, frame = device.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_range = np.array([110, 50, 50])
    upper_range = np.array([130, 255, 255])
    
    mask = cv2 .inRange(hsv, lower_range, upper_range)
    result = cv2.bitwise_and(frame,frame,mask = mask)
    
    cv2.imshow("mask",mask)
    cv2.imshow("result",result)
    cv2.imshow("Color Tracking",frame)
    
    if cv2.waitKey(1) == 27:
    	break
    	
device.release()
cv2.destroyAllWindows()
