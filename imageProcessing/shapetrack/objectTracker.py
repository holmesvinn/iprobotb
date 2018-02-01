import cv2
import numpy as np
from shapetrack.distantdetector import CoOrdinateDistance
from shapetrack.shapedetector import ShapeDetector
import imutils


sd = ShapeDetector()
cd = CoOrdinateDistance()

cans = []

class ObjectTracking():
    def __init__(self):
        pass
    
    def trackObject(self,image):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower_red = np.array([0,150,100])
        upper_red = np.array([15,255,255])       
        mask = cv2.inRange(hsv,lower_red ,upper_red)
        print("mask properties: ", mask.shape,mask.size)
        eroded = cv2.erode(mask,None, iterations=2)
        dilated = cv2.dilate(mask,None, iterations=2)
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
	        cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        cv2.drawContours(mask, cnts, -1, (0,255,0), 3)
        cv2.imshow("cans contour", mask)

        
        for c in cnts:
            points = cd.getCoOrdinate(c,image,False)
            cans.append(points)

        print("position of the cans: ", cans)

        return mask

        