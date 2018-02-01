import cv2
import numpy as np
from shapetrack.shapedetector import ShapeDetector


sd = ShapeDetector()

class CoOrdinateDistance():
    def __init__(self):
        pass

    def getCoOrdinate(self,c,image,what):
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(image, (x, y), (x+w,y+h), (0, 255, 0),10)
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
