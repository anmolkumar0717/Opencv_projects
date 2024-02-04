import cv2 as cv
import numpy as np

capture=cv.VideoCapture(0)



while True:
	istrue,frame=capture.read()
	
	# frame2=cv.GaussianBlur(frame,(7,7),cv.BORDER_DEFAULT)
	# frame1=cv.cvtColor(frame2,cv.COLOR_BGR2RGB)
	# frame=cv.Canny(frame,125,175)

	
	# cv.imshow('Video',frame2)

	hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
	lower_yellow=np.array([25, 50, 70])
	upper_yellow=np.array([35, 255, 255])
	mask=cv.inRange(hsv,lower_yellow,upper_yellow)
	out=cv.bitwise_and(frame,frame,mask=mask)
	cv.imshow('Webcam-Video',out)

	if cv.waitKey(25) == ord('d'):
		break


capture.release()
cv.destroyAllWindows()