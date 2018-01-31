import cv2
import numpy as np
from shapetrack.shapedetector import ShapeDetector
import imutils


sd = ShapeDetector()
class ObjectTracking():
    def __init__(self):
        pass
    
    def trackObject(self,image):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower_red = np.array([0,50,50])
        upper_red = np.array([50,255,255])       
        mask = cv2.inRange(hsv,lower_red ,upper_red)
        """resized = imutils.resize(mask, width=300)
        ratio = mask.shape[0] / float(resized.shape[0])
    
        print("cans: ",mask.shape, mask.size)
        mask_blurred  = cv2.GaussianBlur(mask, (5, 5), 0)
        cnts = cv2.findContours(mask_blurred, cv2.RETR_EXTERNAL,
	        cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        for c in cnts:
            M = cv2.moments(c)
            if((M["m00"] != 0) & (M["m00"] != 0)):
                cx = int(((M["m10"])/(M["m00"]))*ratio)
                cy = int(((M["m01"])/(M["m00"]))*ratio)

            shape = sd.detect(c)
            c = c.astype("float")
            c *= ratio
            c = c.astype("int") 
            cv2.drawContours(mask, [c], -1, (0, 255, 255), 2)
            cv2.putText(mask, shape, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)
        """

        return mask

        