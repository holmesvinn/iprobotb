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
    can_position = ot.trackObject(image,can_color)
    my_bot_blue_position = ot.trackObject(image,bot_blue)
    my_bot_green_position = ot.trackObject(image,bot_green)
    print("cans: ",can_position)
    print("my_bot_blue: ",my_bot_blue_position)
    print("my_bot_green: ",my_bot_green_position)
    
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
        
    
    """gray_original = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    final_result = cv2.addWeighted(gray_original,1,mycans,1,0)
    final_result2 = cv2.addWeighted(final_result,1,my_bot_blue,1,0)
    final_result2 = cv2.addWeighted(final_result2,1,my_bot_green,1,0)
    cv2.imshow("final result",final_result)"""
    cv2.imshow("original image",image)
    final_dest = list(zip(destinations,shapes))    
    print(final_dest)
    for i in range(len(final_dest)):
        if final_dest[i][1] == 'circle' and final_dest[i][0][0] !=0 and final_dest[i][0][1] !=0 :
            print(final_dest[i][1], final_dest[i][0])
            print(type(final_dest[i][0]), type(can_position))
            print(can_position)
            shortest_can_position = cd.shortest_can_distance(final_dest[i][0],can_position)
            

        
    k = cv2.waitKey(0)
    
    

    if(k == ord('q')):
        break
cv2.destroyAllWindows()

