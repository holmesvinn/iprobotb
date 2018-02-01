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
        cnts = sd.getContour(mask)
        
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



        