import cv2
cam = cv2.VideoCapture(1)
ret,frame = cam.read()
cv2.imshow("read image",frame)
cv2.waitKey(0)
cv2.destroyAllWindows()