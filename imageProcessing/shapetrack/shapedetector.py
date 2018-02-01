import cv2
import imutils

class ShapeDetector():
    def __init__(self):
        pass

    def getContour(self,image):
        blurred = cv2.GaussianBlur(image, (5,5), 0)
        ret, thresh = cv2.threshold(blurred, 240, 255, cv2.THRESH_BINARY)
        cv2.imshow("threshold",thresh)
        eroded = cv2.erode(thresh,None, iterations=3)
        dilated = cv2.dilate(eroded,None, iterations=3)
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	    cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        return cnts

    def detect(self,c):
        shape = "undefined"
        perimeter = cv2.arcLength(c,True)
        approx = cv2.approxPolyDP(c,0.04*perimeter,True)
       
        if len(approx) == 3:
            shape = "triangle"
        elif len(approx) == 5:
            shape = "pentagon"
        elif len(approx) == 4:
            (x,y,w,h) = cv2.boundingRect(approx)
            aspect_ration =  w/float(h)
            shape = "square" if aspect_ration >= 0.95 and aspect_ration <= 1.05 else "rectangle"
        else:
            shape = "circle"

        return shape

    
    

