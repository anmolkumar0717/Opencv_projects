import cv2 as cv
import numpy as np

img1=cv.imread("edge.png")

edge=cv.resize(img1,(0,0),fx=0.3,fy=0.3)

gray=cv.cvtColor(edge,cv.COLOR_BGR2GRAY)

corner=cv.goodFeaturesToTrack(gray,100,0.000001,10)

corner=np.int0(corner)

for i in corner:
	x,y=i.ravel()
	cv.circle(edge,(x,y),4,(255,0,0),-1)

cv.imshow("EDGE-DETECTION",edge)

cv.waitKey(0)
