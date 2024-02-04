import cv2 as cv

def resize1(frame):
	dimension=(400,400)

	return cv.resize(frame,dimension)



img=cv.imread("husky.jpg")
img=resize1(img)

cv.imshow("Husky",img)

#GreyScaling the IMAGE


gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow("Husky_Gray",gray)

# FOR BLURING THE IMAGE

blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)

cv.imshow("Blur",blur)


#EDGE CASCADE

canny=cv.Canny(blur,125,175)

cv.imshow("Edge-of-images",canny)

#DILATING IMAGE

dilated=cv.dilate(canny,(7,7),iterations=5)

cv.imshow("Dilated",dilated)

#ERODEING THE IMAGE

eroded=cv.erode(dilated,(7,7),iterations=5)
cv.imshow("eroded-img",eroded)


cv.waitKey(0)