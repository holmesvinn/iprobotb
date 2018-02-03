import cv2
import numpy as np
cam = cv2.VideoCapture(1)
while 1:
    ret,frame = cam.read()
    lower = np.array([0, 0, 0])
    upper = np.array([180, 255, 50])
    mask = cv2.inRange(frame,lower,upper)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    cv2.imshow("read image",res)
    k = cv2.waitKey(2)
    if k == ord('q'):
        break
cam.release()

cv2.destroyAllWindows()