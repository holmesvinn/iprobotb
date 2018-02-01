import cv2
import imutils
import numpy as np
import os
from socket import *
from shapetrack.shapedetector import ShapeDetector
from shapetrack.objectTracker import ObjectTracking
from shapetrack.distantdetector import CoOrdinateDistance


host = "raspberrypi" 
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)


sd = ShapeDetector()
ot = ObjectTracking()
cd = CoOrdinateDistance()
destinations = []
shapes = []
i = 0

can_color = "red"
bot_green = "green"
bot_blue = "blue"



def get_destination_point(shape):
    while(i < len(shapes)):
        if shapes[i] == 'circle':
            print("circle position: ",destinations[i])
        
        if shapes[i] == 'pentagon':
            print("pentagon position:", destinations[i])

        if shapes[i] == 'triangle':
            print("triangle position: ", destinations[i])

        i = i+1

def align_straight(blue,green,dist):

    blue_distance = cd.distance_between_points(blue,dist)
    green_distance = cd.distance_between_points(green,dist)
    while (int(blue_distance) != int(green_distance)):

        if blue_distance > green_distance:
            print("blue greater")
            #move right
        else:
            print("green greater")
            #move left

    return 

    






#def move_front():
#    pass

#cap = cv2.VideoCapture(1)
while 1:
    image = cv2.imread("quadrac6.png")
    can_position = ot.trackObject(image,can_color)
    my_bot_blue_position = ot.trackObject(image,bot_blue)
    my_bot_green_position = ot.trackObject(image,bot_green)

    print("\ncans: ",can_position)
    print("\nmy_bot_blue: ",my_bot_blue_position)
    print("\nmy_bot_green: ",my_bot_green_position)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cnts = sd.getContour(gray)
    
    for c in cnts:
        points, shape = cd.getCoOrdinate(c,image,True)
        destinations.append(points)
        shapes.append(shape)

    
    first_dist = cd.shortest_can_distance(my_bot_green_position[0],can_position)
    aligh_straight(my_bot_blue_position[0],my_bot_green_position[0],first_dist)
    #move Straight
    #isposition = 





    




        

    

    cv2.imshow("original image",image)
    final_dest = list(zip(destinations,shapes))
    print(final_dest)
    k = cv2.waitKey(0)
    if(k == ord('q')):
        break
cv2.destroyAllWindows()

