import cv2
import math
import numpy as np
from shapetrack.shapedetector import ShapeDetector
from operator import itemgetter

lengths_list = []
final_sorted_list = []
position_list = []
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
        center = [int(x), int(y)]
        radius = int(radius)
        shape = sd.detect(c)
        if(what):
            return center,shape
        else:
            return center

    def distance_between_points(self,p1,p2):

        dist = math.sqrt(((p2[0]-p1[0])**2)+((p2[1]-p1[1])**2))
        return dist

    def shortest_can_distance(self,center_point,cans):
        i=0
        print(type(center_point))
        print(len(cans))
        while(i<len(cans)):
            short_length = self.distance_between_points(center_point,cans[i])
            print(short_length)
            lengths_list.append(short_length)
            position_list.append(cans[i])
            i =i+1
        finalyy = list(zip(lengths_list,position_list))
        print(type(finalyy), type(finalyy[0]))
        newly = sorted(finalyy,key=lambda x:x[0])
        print("finally: ", newly)
        print()
        return newly[0]
        
