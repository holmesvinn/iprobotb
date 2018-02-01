import cv2
import numpy as np
from shapetrack.distantdetector import CoOrdinateDistance
from shapetrack.shapedetector import ShapeDetector
import imutils


sd = ShapeDetector()
cd = CoOrdinateDistance()

cans = []
bot_green = []
bot_blue = []

class ObjectTracking():
    def __init__(self):
        pass
    
    def trackObject(self,image,color):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        if color == "red":
            lower = np.array([0,100,100])
            upper = np.array([20,255,255])  
        elif color == "green":
            lower = np.array([30,150,150])
            upper = np.array([80,255,255]) 
        elif color == "blue":
            lower = np.array([90,100,100])
            upper = np.array([140,255,255]) 

        mask = cv2.inRange(hsv,lower ,upper)
        cv2.imshow("masked",mask)
        print("mask properties: ", mask.shape,mask.size)
        blurred = cv2.GaussianBlur(mask, (5, 5), 0)
        ret, thresh = cv2.threshold(blurred, 240, 255, cv2.THRESH_BINARY)
        cv2.imshow("threshold for mask:",thresh)   
        eroded = cv2.erode(thresh,None, iterations=2)
        cv2.imshow("eroded mask",eroded)
        dilated = cv2.dilate(eroded,None, iterations=2)
        cv2.imshow("dilated mask:", dilated)
        cnts = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL,
	        cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        
        for c in cnts:
            points = cd.getCoOrdinate(c,image,False)
    
            
            if color == "red":
                cans.append(points)

            if color == "green":
                bot_green.append(points)
                return bot_green
            if color == "blue":
                bot_blue.append(points)
                return bot_blue

        return cans

        