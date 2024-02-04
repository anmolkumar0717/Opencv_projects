import cv2 as cv
import numpy as np

#IMAGE RECOGNITION 
img1=cv.imread('blue1.jpg')
dimension=(400,400)
resize=cv.resize(img1,dimension)

hsv=cv.cvtColor(resize,cv.COLOR_BGR2HSV)

lower_yellow=np.array([25, 50, 70])
upper_yellow=np.array([35, 255, 255])


mask=cv.inRange(hsv,lower_yellow,upper_yellow)

cv.imshow("Mask",mask)

res=cv.bitwise_and(resize,resize,mask=mask)

cv.imshow("Orignal",resize)

cv.imshow("resize",res)






cv.waitKey(0)