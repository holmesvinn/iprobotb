import cv2
import math
import numpy as np
from shapetrack.shapedetector import ShapeDetector


sd = ShapeDetector()

class CoOrdinateDistance():
    def __init__(self):
        pass

    def getCoOrdinate(self,c,image,what):
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(image, (x, y), (x+w,y+h), (255,255, 255),1)
        rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rect)
        box = np.int0(box)    
        (x, y), radius = cv2.minEnclosingCircle(c)
        center = (int(x), int(y))
        radius = int(radius)
        shape = sd.detect(c)
        if(what):
            return center,shape
        else:
            return center

    def distance_between_points(self,p1,p2):
        dist = math.sqrt(((p2[0]-p1[0])**2)+((p2[1]-p1[1])**2))
        return dist


