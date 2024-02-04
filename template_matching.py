import cv2 as cv

import numpy as np

img1=cv.imread("family.jpg",0)

img1=cv.resize(img1,(0,0),fx=0.2,fy=0.2)

ball=cv.imread("template.jpg",0)
ball=cv.resize(ball,(0,0),fx=0.2,fy=0.2)



h,w=ball.shape

methods=[cv.TM_CCORR_NORMED, cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]

for method in methods:
	img=img1.copy()
	res=cv.matchTemplate(img,ball,method)
	min_val,max_val,min_loc,max_loc=cv.minMaxLoc(res)
	if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
		location=min_loc
	else:
		location=max_loc

	bottom_right=(location[0]+w,location[1]+h)
	cv.rectangle(img,location,bottom_right,255,3)
	cv.putText(img,"Anmol",(min_loc[0]+20,bottom_right[1]-70),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
	cv.imshow("Template-matching",img)

	cv.waitKey(0)
	cv.destroyAllWindows()



cv.waitKey(0)