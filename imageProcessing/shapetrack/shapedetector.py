import cv2

class ShapeDetector():
    def __init__(self):
        pass


    def detect(self,c):
        shape = "undefined"
        perimeter = cv2.arcLength(c,True)
        approx = cv2.approxPolyDP(c,0.04*perimeter,True)
        print(len(approx))
        
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

    
    

