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
buff = 1024
UDPSock = socket(AF_INET, SOCK_DGRAM)


sd = ShapeDetector()
ot = ObjectTracking()
cd = CoOrdinateDistance()
destinations = []
shapes = []
i = 0
pentagon = []

can_color = "red"
bot_green = "green"
bot_blue = "blue"

#initial = "sta"
#UDPSock.send(initial,addr)



"""def get_destination_point(shape):
    while(i < len(shapes)):
        if shapes[i] == 'circle':
            print("circle position: ",destinations[i])
        
        if shapes[i] == 'pentagon':
            print("pentagon position:", destinations[i])

        if shapes[i] == 'triangle':
            print("triangle position: ", destinations[i])

        i = i+1"""


        




    

cap = cv2.VideoCapture(1)
#cap = cv2.VideoCapture("http://192.168.43.146:8080/video")
while 1:
    
    ret,image = cap.read()
    print(ret)
    #cv2.imshow("",image)

    #image = cv2.imread("quadrac4.png")
    can_position = ot.trackObject(image,can_color)
    print("can_position: ",can_position)
    print("yes")

    my_bot_blue_position = ot.trackObject(image,bot_blue)
    print("blue position: ",my_bot_blue_position)
    my_bot_green_position = ot.trackObject(image,bot_green)
    print("green position: ",my_bot_green_position)
    
    

    #print("\ncans: ",can_position)
    #print("\nmy_bot_blue: ",my_bot_blue_position)
    #print("\nmy_bot_green: ",my_bot_green_position)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cnts = sd.getContour(gray)
    
    for c in cnts:
        points, shape = cd.getCoOrdinate(c,image,True)
        destinations.append(points)

        shapes.append(shape)
        if shape == 'pentagon':
            pentagon.append(points)

    
    first_dist = cd.shortest_can_distance(my_bot_green_position[0],can_position)
    print(first_dist)
    blue_distance = cd.distance_between_points(my_bot_blue_position[0],first_dist[1])
    green_distance = cd.distance_between_points(my_bot_green_position[0],first_dist[1])
    print(first_dist,blue_distance,green_distance)

    
    if blue_distance > green_distance:
        print("blue greater")
        data = "rt"
        UDPSock.sendto(data.encode(),addr)
    
    elif blue_distance < green_distance:
        print("green greater")
        data = "lt"
        UDPSock.sendto(data.encode(),addr)
    else: 
        print("same length")
        data = "fwd"
        while(1):
            UDPSock.sendto(data.encode(),addr)
            (pickdata,addr) = UDPSock.recvfrom(buff) 
            if pickdata == "np":
                break
            if pickdata == "picked":
                while(1):
                    image = cv2.imread("quadrac4.png")


                    my_bot_blue_position = ot.trackObject(image,bot_blue)
                    my_bot_green_position = ot.trackObject(image,bot_green)
                    blue_distance = cd.distance_between_points(my_bot_blue_position[0],pentagon)
                    green_distance = cd.distance_between_points(my_bot_green_position[0],pentagon)

                    if blue_distance > green_distance:
                        print("blue greater")
                        data = "rt"
                        UDPSock.sendto(data.encode(),addr)
                    elif blue_distance < green_distance:
                        print("green greater")
                        data = "lt"
                        UDPSock.sendto(data.encode(),addr)  
                    else :
                        data = "frwd"
                        while(1):
                            UDPSock.sendto(data.encode(),addr)
                            (pickdata,addr) = UDPSock.recvfrom(buff) 
                            blue_dist = ot.trackObject(image,bot_blue)
                            bluee = cd.distance_between_points(pentagon,blue_dist)
                            if bluee < 100:
                                data = "plc"
                                UDPSock.sendto(data.encode(),addr)
                                break
                        break
                           
    cv2.imshow("original image",image)
    final_dest = list(zip(destinations,shapes))
    k = cv2.waitKey(0)
    if(k == ord('q')):
        break
cv2.destroyAllWindows()

