import cv2
from shapetrack.shapedetector import ShapeDetector
from shapetrack.objectTracker import ObjectTracking
import imutils

sd = ShapeDetector()
ot = ObjectTracking()


   

#cap = cv2.VideoCapture(1)
while 1:
    image = cv2.imread("quadrabottrack.png")
    mycans = ot.trackObject(image)
    resized = imutils.resize(image, width=300)
    ratio = image.shape[0] / float(resized.shape[0])
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 240, 255, cv2.THRESH_BINARY)[1]


    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    #print("original: ",image.shape, image.size)
    #print("threshold: ",thresh.shape, thresh.size)
    #print("gray: ",gray.shape, gray.size)


    for c in cnts:
        M = cv2.moments(c)
        if((M["m00"] != 0) & (M["m00"] != 0)):
            cx = int(((M["m10"])/(M["m00"]))*ratio)
            cy = int(((M["m01"])/(M["m00"]))*ratio)
        shape = sd.detect(c)
        c = c.astype("float")
        c *= ratio
        c = c.astype("int") 
        cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
        cv2.putText(image, shape, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
        cv2.imshow("original image",image)
        cv2.imshow("cans in the image",mycans)
        gray_original = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        final_result = cv2.addWeighted(gray_original,1,mycans,1,0)
        cv2.imshow("final result",final_result)
    k = cv2.waitKey(0)
    if(k == ord('q')):
        break
cv2.destroyAllWindows()

