import cv2 as cv
import numpy as np

capture=cv.VideoCapture(0)



while True:
	istrue,frame=capture.read()


	hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
	lower_yellow=np.array([110,50,50])
	upper_yellow=np.array([130,255,255])
	mask=cv.inRange(hsv,lower_yellow,upper_yellow)

	
	out=cv.bitwise_and(frame,frame,mask=mask)
	cv.imshow('Webcam-Video',out)

	if cv.waitKey(1) == ord('d'):
		break


capture.release()
cv.destroyAllWindows()