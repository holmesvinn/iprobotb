import cv2
from shapetrack.shapedetector import ShapeDetector
from shapetrack.objectTracker import ObjectTracking
from shapetrack.distantdetector import CoOrdinateDistance
import imutils
import numpy as np

sd = ShapeDetector()
ot = ObjectTracking()
cd = CoOrdinateDistance()
destinations = []
shapes = []

can_color = "red"
bot_green = "green"
bot_blue = "blue"
#cap = cv2.VideoCapture(1)
while 1:
    image = cv2.imread("quadrac6.png")
    mycans = ot.trackObject(image,can_color)
    my_bot_blue = ot.trackObject(image,bot_blue)
    my_bot_green = ot.trackObject(image,bot_green)
    
    #resized = imutils.resize(image, width=300)
    #ratio = image.shape[0] / float(resized.shape[0])
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5,5), 0)
    ret, thresh = cv2.threshold(blurred, 240, 255, cv2.THRESH_BINARY)
    print("thresh:",thresh)
    cv2.imshow("threshold",thresh)
    eroded = cv2.erode(thresh,None, iterations=3)
    dilated = cv2.dilate(eroded,None, iterations=3)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]

    for c in cnts:
        points, shape = cd.getCoOrdinate(c,image,True)
        destinations.append(points)
        shapes.append(shape)
    
    gray_original = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    final_result = cv2.addWeighted(gray_original,1,mycans,1,0)
    cv2.imshow("final result",final_result)
    cv2.imshow("original image",image)

    final_dest = list(zip(destinations,shapes))    
    print(final_dest)
    k = cv2.waitKey(0)
    
    

    if(k == ord('q')):
        break
cv2.destroyAllWindows()

